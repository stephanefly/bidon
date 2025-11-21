from apps.main.models import Cas, IsoVitesse
import shutil

def duplicate_cotenue_etat(new_etat, old_etat):
    # Dupliquer les Cas associés
    for isovitesse in IsoVitesse.objects.filter(etat=old_etat):
        new_iso_vitesse = IsoVitesse.objects.create(
            name=isovitesse.name,
            etat=new_etat,
            color=isovitesse.color,
            row_config=isovitesse.row_config,
            marker=isovitesse.marker,
            recalage_kd=isovitesse.recalage_kd,
            file_type=isovitesse.file_type,
        )
        for cas in Cas.objects.filter(iso_vitesse=isovitesse):
            Cas.objects.create(
                name=cas.name,
                used=cas.used,
                available=cas.available,
                iso_vitesse=new_iso_vitesse,  # Associer à l'iso_vitesse existant
                file_path=cas.file_path,
                select = cas.select,
                bsam_path = cas.bsam_path,
                calculate_perfo=0,
                repertory=cas.repertory,
                obj_type=cas.obj_type,
                row_metadata=cas.row_metadata,
                revue_veine=cas.revue_veine,
            )

    shutil.copytree(old_etat.work_directory, new_etat.work_directory)
