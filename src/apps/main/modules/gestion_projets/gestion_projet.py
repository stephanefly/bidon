
import os
import shutil
from pathlib import Path

from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect

from apps.main.models import IsoVitesse, Cas, Etat, Project, RevueVeine, Aube, RevueAube
from apps.main.modules.gestion_projets.tools import copy_dirs_only
from apps.main.utils.paths import get_user_path


def duplicate_cotenue_etat(request, new_name: str, old_etat: Etat) -> None:
    """
    Duplique un Etat (IsoVitesse + Cas) dans le même Project que old_etat.
    Copie uniquement l'arborescence des dossiers (sans fichiers) après commit DB.

    Hypothèse : Etat.created_by est un CharField (on stocke request.user.username).
    """
    username = request.user.username
    projet = old_etat.projet

    old_dir = Path(old_etat.work_directory)
    new_dir = None

    try:
        # 1) Empêche la duplication si un état de même nom existe déjà dans le projet
        if Etat.objects.filter(name=new_name, projet=projet).exists():
            messages.error(request, "Un état avec ce nom existe déjà dans ce projet !")
            return redirect("info_projet", old_etat.projet.id)

        if Project.objects.filter(name=projet.name, created_by=username).exists():
            user_project = Project.objects.get(name=projet, created_by=username)
        else:
            user_project = Project(
                name=projet.name,
                created_by=username,
            )
            user_project.save()
            user_project.work_directory = os.path.join(get_user_path(user_project),
                                                 "Perfo_0D", projet.name)
            user_project.save()

        with transaction.atomic():
            # 2) Création du nouvel état dans le même projet
            new_etat = Etat.objects.create(
                name=new_name,
                projet=user_project,
                created_by=username,
                work_directory=os.path.join(str(user_project.work_directory), str(new_name)),
                cas_temp_repertory=old_etat.cas_temp_repertory,
            )

            new_dir = Path(new_etat.work_directory)

            # 3) Duplication DB IsoVitesse + Cas
            for old_iso in IsoVitesse.objects.filter(etat=old_etat):
                new_iso = IsoVitesse.objects.create(
                    name=old_iso.name,
                    etat=new_etat,
                    color=old_iso.color,
                    row_config=old_iso.row_config,
                    marker=old_iso.marker,
                    recalage_kd=old_iso.recalage_kd,
                    file_type=old_iso.file_type,
                )

                for old_cas in Cas.objects.filter(iso_vitesse=old_iso):
                    Cas.objects.create(
                        name=old_cas.name,
                        used=old_cas.used,
                        available=old_cas.available,
                        iso_vitesse=new_iso,
                        file_path=old_cas.file_path,
                        select=old_cas.select,
                        bsam_path=old_cas.bsam_path,
                        calculate_perfo=0,
                        repertory=old_cas.repertory,
                        obj_type=old_cas.obj_type,
                        row_metadata=old_cas.row_metadata,
                        revue_veine=old_cas.revue_veine,
                    )

            # 4) Copie uniquement des dossiers après commit DB (pas les fichiers)
            def copy_dirs_after_commit():
                if not old_dir.exists():
                    return

                new_dir.mkdir(parents=True, exist_ok=True)
                copy_dirs_only(old_dir, new_dir)

            transaction.on_commit(copy_dirs_after_commit)

        messages.info(request, "Duplication terminée")

        os.chmod(new_dir, 0o777)
        messages.info(request, f" {new_etat}: Etat crée")
        return new_etat

    except Exception as e:
        # Nettoyage FS si le dossier cible a été créé
        if new_dir is not None and new_dir.exists():
            shutil.rmtree(new_dir, ignore_errors=True)

        messages.error(request, f"Erreur duplication ({e})")
        return redirect("info_projet", old_etat.projet.id)


def duplicate_contenue_revue_veine(request, new_name: str, old_revue: RevueVeine):
    """
    Duplique une RevueVeine (Cas + IsoVitesse liés) chez l'utilisateur courant.
    Copie uniquement l'arborescence des dossiers (sans fichiers) après commit DB.

    Important:
    - On NE modifie PAS les chemins des Cas (file_path / repertory / bsam_path).
    - On recrée les IsoVitesse nécessaires (uniques), puis les Cas.
    """

    username = request.user.username

    old_dir = Path(old_revue.work_directory) if old_revue.work_directory else None
    new_dir = None

    try:
        # 1) Empêche la duplication si une revue de même nom existe déjà chez l'utilisateur
        if RevueVeine.objects.filter(name=new_name, created_by=username).exists():
            messages.error(request, "Une RevueVeine avec ce nom existe déjà chez vous !")
            return redirect("lst_revue_veine")

        # 2) Prépare le nouveau dossier chez l'utilisateur

        temp_revue = RevueVeine(name=new_name, created_by=username)
        base_user_dir = Path(get_user_path(temp_revue))
        dest_dir = base_user_dir / "RevueVeine" / new_name

        # rend le chemin unique si déjà existant
        if dest_dir.exists():
            messages.error(request, "Un dossier exite déjà ! ")
            return redirect("lst_revue_veine")

        with transaction.atomic():
            # 3) Crée la nouvelle revue
            new_revue = RevueVeine.objects.create(
                name=new_name,
                created_by=username,
                work_directory=str(dest_dir),
            )

            new_dir = Path(new_revue.work_directory)

            # 4) Duplication DB IsoVitesse + Cas (sans recalcul chemins)
            iso_map = {}  # old_iso_id -> new_iso

            old_cas_qs = Cas.objects.select_related("iso_vitesse").filter(revue_veine=old_revue)

            for old_cas in old_cas_qs:
                old_iso = old_cas.iso_vitesse
                new_iso = None

                if old_iso:
                    if old_iso.id not in iso_map:
                        iso_map[old_iso.id] = IsoVitesse.objects.create(
                            name=old_iso.name,
                            etat=old_iso.etat,              # on garde l’état tel quel
                            color=old_iso.color,
                            row_config=old_iso.row_config,
                            marker=old_iso.marker,
                            recalage_kd=old_iso.recalage_kd,
                            file_type=old_iso.file_type,
                        )
                    new_iso = iso_map[old_iso.id]

                Cas.objects.create(
                    name=old_cas.name,
                    used=old_cas.used,
                    available=old_cas.available,
                    iso_vitesse=new_iso,
                    file_path=old_cas.file_path,       # inchangé (pas de recalcul)
                    select=old_cas.select,
                    bsam_path=old_cas.bsam_path,       # inchangé
                    calculate_perfo=0,
                    repertory=old_cas.repertory,       # inchangé
                    obj_type=old_cas.obj_type,
                    row_metadata=old_cas.row_metadata,
                    revue_veine=new_revue,             # IMPORTANT: on rattache à la nouvelle revue
                )

            # 5) Copie uniquement des dossiers après commit DB (pas les fichiers)
            def copy_dirs_after_commit():
                if not old_dir or not old_dir.exists():
                    return
                os.makedirs(new_dir, exist_ok=True)
                copy_dirs_only(old_dir, new_dir)

            transaction.on_commit(copy_dirs_after_commit)

        os.chmod(new_dir, 0o777)
        messages.info(request, f" {new_name}: Revue crée")
        return new_revue

    except Exception as e:
        if new_dir is not None and new_dir.exists():
            shutil.rmtree(new_dir, ignore_errors=True)

        messages.error(request, f"Erreur duplication ({e})")
        return redirect("lst_revue_veine")


def duplicate_contenue_revue_aube(request, new_name: str, old_revue: RevueAube):
    """
    Duplique une RevueAube (Aube liés) chez l'utilisateur courant.
    Copie uniquement l'arborescence des dossiers (sans fichiers) après commit DB.
    """

    username = request.user.username

    old_dir = Path(old_revue.work_directory) if old_revue.work_directory else None
    new_dir = None

    try:
        # 1) Empêche la duplication si une revue de même nom existe déjà chez l'utilisateur
        if RevueAube.objects.filter(name=new_name, created_by=username).exists():
            messages.error(request, "Une RevueAube avec ce nom existe déjà chez vous !")
            return redirect("lst_revue_aube")

        # 2) Prépare le nouveau dossier chez l'utilisateur
        temp_revue = RevueAube(name=new_name, created_by=username)
        base_user_dir = Path(get_user_path(temp_revue))
        dest_dir = base_user_dir / "RevueAube" / new_name

        # Rend le chemin unique si déjà existant
        if dest_dir.exists():
            messages.error(request, "Un dossier exite déjà ! ")
            return redirect("lst_revue_veine")

        with transaction.atomic():
            # 3) Crée la nouvelle revue (on copie dico_genepi_auto)
            new_revue = RevueAube.objects.create(
                name=new_name,
                created_by=username,
                work_directory=str(dest_dir),
                dico_genepi_auto=old_revue.dico_genepi_auto,
            )

            new_dir = Path(new_revue.work_directory)

            # 4) Duplication DB des Aube liés (sans recalcul des chemins)
            old_aubes_qs = Aube.objects.filter(revue_aube=old_revue)

            for old_aube in old_aubes_qs:
                Aube.objects.create(
                    color=old_aube.color,
                    projet=old_aube.projet,
                    version=old_aube.version,
                    aube=old_aube.aube,
                    type_coupe_nbre_ldc=old_aube.type_coupe_nbre_ldc,
                    coupe_dessin=old_aube.coupe_dessin,
                    label_bsam=old_aube.label_bsam,
                    inversion_aube=old_aube.inversion_aube,
                    fichier_bsam=old_aube.fichier_bsam,
                    inversion_bsam=old_aube.inversion_bsam,
                    calage_deg=old_aube.calage_deg,
                    titre_cas=old_aube.titre_cas,
                    lien_xml=old_aube.lien_xml,
                    revue_aube=new_revue,   # rattache à la nouvelle revue
                    used=old_aube.used,
                )

            # 5) Copie uniquement des dossiers après commit DB (pas les fichiers)
            def copy_dirs_after_commit():
                if not old_dir or not old_dir.exists():
                    return
                os.makedirs(new_dir, exist_ok=True)
                copy_dirs_only(old_dir, new_dir)

            transaction.on_commit(copy_dirs_after_commit)

            messages.info(request, f"{new_name}: RevueAube créée")


        os.chmod(new_dir, 0o777)
        messages.info(request, f" {new_name}: Revue crée")
        return new_revue

    except Exception as e:
        if new_dir is not None and new_dir.exists():
            shutil.rmtree(new_dir, ignore_errors=True)

        messages.error(request, f"Erreur duplication ({e})")
        return redirect("lst_revue_aube")
