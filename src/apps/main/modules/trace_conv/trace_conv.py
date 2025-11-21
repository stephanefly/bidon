#!/usr/bin/env python
# -*- coding: utf-8 -*-

#######################################################################################################
#      DESCRIPTION DU SCRIPT : Critères de convergence
#######################################################################################################

# /*********   Created by Mehmet DEMIRCI    ***************/
# /*********   Creation date : 03/11/2022   ***************/
# /*********   Script version : V4.0        ***************/
# /*********   Update date : 31/10/2023     ***************/

# /*********   News in V3.1                 ***************/
# /*********   o Ajout de la libraire glob
# /*********   o Elargissement de l'intervalle de tolerance a 0.2%

# /*********   News in V4.0                 ***************/
# /*********   o Compatibilité du script avec toutes les configurations :
# /*********     (FAN-OGV, FAN-OGV360, RANS360, uRANS360, Booster, Turbines...)
# /*********   o Ajout de la possibilité de renseigner plusieurs répertoires des cas pour une
# /*********     une meilleure automatisation du script
# /*********   o Affranchissement des fichiers params_case qui sont
# /*********     parfois responsables des bugs du script
# /*********   o Correction des divers bugs
# /*********   o Amélioration de l'interface graphique pour une meilleure lisibilité des figures
# /*********   o Ajout des légendes sur les figures : Limites inf et sup, valeur débit moyen et
# /*********     écart relatif débit min/max

# ======================================================================================================
# Importation des librairies et des fonctions de reference
# ======================================================================================================

import os, logging
import glob
from math import *
from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MaxNLocator
import csv
from collections import defaultdict

###################################################
#             CRITERES DE CONVERGENCE             #
###################################################

# nombre d'iterations pour etude des oscillations
nombre_ite = 2000

# ecart en % entre la valeur max et min
ecart_amp = 0.2

###################################################
#              REPERTOIRE DE SORTIE               #
###################################################
# OutputPath = os.path.dirname(__file__)

###################################################
#                  CAS de CALCULS                 #
###################################################
# Cas_Traces = 0

###################################################
#      CORPS DU SCRIPT : NE PAS TOUCHER !!!       #
###################################################

def Recup_Roues_In_Out(Param_info, ResuDir):
    """Recuperation du nom des aubes de la premiere et derniere grille"""
    numero_aube = 0
    nombre_roues = 0

    debit_in = '_INFLOWMassflow.v3d'
    debit_out = '_OUTFLOWMassflow.v3d'
    debit_out_bypass = '_OUTFLOW_BYPASSMassflow.v3d'

    os.chdir(ResuDir)
    liste_roues = glob.glob("*" + debit_in)
    nombre_roues = len(liste_roues)

    nom_Row_In = [] * nombre_roues
    nom_Row_Out = [] * nombre_roues
    nom_Row_Out_ByPass = [] * nombre_roues

    # Les fichiers de resultats ont deux noms possibles : le nom réel de l'aube ou ROW_X
    # Grâce à la fonction Glob, on récupère le nom de tous les fichiers MASSFLOw*.v3d (sans distinction entre ROW_X et le nom réel de la roue)
    nom_Row_In = liste_roues
    nom_Row_Out = glob.glob("*" + debit_out)
    nom_Row_Out_ByPass_intermediate = glob.glob("*" + debit_out_bypass)

    # Si les roues ne sont pas positionnees dans le bon ordre, on trie dans l'ordre croissant
    is_OrdreRoueCorrect = True
    for i in range(len(nom_Row_In)):
        if (nom_Row_In[i][:9] != nom_Row_Out[i][:9]):
            is_OrdreRoueCorrect = False
            break
    if (is_OrdreRoueCorrect == False):
        nom_Row_In = sorted(nom_Row_In)
        nom_Row_Out = sorted(nom_Row_Out)
        nom_Row_Out_ByPass_intermediate = sorted(
            nom_Row_Out_ByPass_intermediate)

    # On fait une boucle de maniere a ce que toutes les listes nom_Row_* ont la meme longueur pour s'affranchir des bugs dans la suite
    for i in range(len(nom_Row_In)):
        nom_Row_Out_ByPass.append('NULL')
        for j in range(len(nom_Row_Out_ByPass_intermediate)):
            if (nom_Row_Out_ByPass_intermediate[j][:9] == nom_Row_In[i][
                                                          :9]):
                nom_Row_Out_ByPass[i] = nom_Row_Out_ByPass_intermediate[j]

    return nom_Row_In, nom_Row_Out, nom_Row_Out_ByPass


def Lecture(file_path):
    """Lecture du contenu d'un fichier en modifiant le formalisme
        - remplacement des tirets par un espace
        - remplacement des doubles espaces par un espace simple
    """
    fichier = open(file_path, "r")
    lines = fichier.readlines()  # Lit tout le fichier d'un coup
    fichier.close()

    for i in range(0, len(lines)):
        lines[i] = lines[i].replace('-', ' ')
        lines[i] = lines[i].replace('E ', 'E-')  # En cas de nombres < 1
        lines[i] = lines[i].replace('  ', ' ')

    return lines


def Concatener(source, isDebit_inlet):
    """recuperation des donnees et sauvegarde dans une variable avec un separateur precis : ; """

    destination = []
    liste_iteration = []
    liste_debits = []

    # ------------------------------------------- FICHIERS DEBIT REF --------------------------------------------------

    # On récupère les lignes du fichier où commencent et se terminent les valeurs des itérations extraites et
    # les lignes du fichier où commencent et se terminent les valeurs du débit extraites aux itérations correspondantes
    ligne_ite_debut = ligne_ite_fin = 0
    ligne_debit_debut = ligne_debit_fin = 0

    for lineno, line in enumerate(source):
        if 'va iteration' in line:
            ligne_ite_debut = lineno + 2
        if 'va convflux_ro' in line:
            ligne_ite_fin = lineno - 1
            ligne_debit_debut = lineno + 2
        ligne_debit_fin = lineno

    # Si le dernier element de la liste liste_ligne_iteration contient un caractère de saut de line (\n), alors on le supprime de la liste --> Evite le bug du script
    if (source[ligne_ite_fin] == '\n' or source[ligne_ite_fin] == ' \n'):
        del source[ligne_ite_fin]
        ligne_ite_fin -= 1
        ligne_debit_debut -= 1
        ligne_debit_fin -= 1

    # Par précaution, si le dernier element de la liste liste_ligne_debit contient un caractère de saut de line (\n), alors on le supprime de la liste
    if (source[ligne_debit_fin] == '\n' or source[
        ligne_debit_fin] == ' \n'):
        del source[ligne_debit_fin]
        ligne_debit_fin -= 1

    for lineno, line in enumerate(source):
        # D'abord on crée un liste contenant les numéros des itérations
        if ligne_ite_debut <= lineno <= ligne_ite_fin:
            liste_ligne_iteration = line.split(' ')
            liste_ligne_iteration[-1] = (liste_ligne_iteration[-1]).split()[
                0]
            liste_ligne_iteration.remove('')
            liste_iteration += liste_ligne_iteration
        # On crée une autre liste de même longueur contenant la valeur du débit correspondant à l'itération
        if ligne_debit_debut <= lineno <= ligne_debit_fin:
            liste_ligne_debit = line.split(' ')
            liste_ligne_debit[-1] = (liste_ligne_debit[-1]).split()[0]
            liste_ligne_debit.remove('')
            liste_debits += liste_ligne_debit

    # ------------------------------------------- ECRITURE FICHIER FINAL ----------------------------------------------

    for a in range(0, len(liste_iteration)):
        if isDebit_inlet == True:
            destination.append([liste_iteration[a], liste_debits[a]])
        else:
            destination.append([liste_debits[a]])

    return destination


def Calcul_Convergence(liste, data_out, row_name, blade_number, isByPass,
                       pdf):
    """calcul de la convergence du calcul :
        - amplitude des oscillations sur les dernieres iterations : plage etudiee a definir
    sauvegarde du resultat dans un fichier commun a tous les calculs de l'analyse"""

    Liste_graphe = [[], [], [], []]
    Liste_graphe_out_tot = []

    for line in range(0, len(liste)):
        liste[line][0] = float(liste[line][0])
        liste[line][1] = float(liste[line][1])
        liste[line][2] = float(liste[line][2])

        # Liste composée de n = len(liste) lignes de 5 colonnes que l'on transforme
        # en une liste composée de 5 listes de n = len(liste) nombres
        Liste_graphe[0].append(liste[line][0])
        Liste_graphe[1].append(liste[line][1])
        Liste_graphe[2].append(liste[line][2])

        if isByPass == True:
            liste[line][3] = float(liste[line][3])
            Liste_graphe[3].append(liste[line][3])

    nombre_ite_max = liste[len(liste) - 1][0]

    # --------------------------------------------------------------------------------------------------
    # verification de la convergence par l'amplitude des oscillations sur les X dernières itérations
    # --------------------------------------------------------------------------------------------------

    if len(liste) >> 1:  # si calcul avec 1 seule itération, pas de calcul de convergence possible ...
        # si nombre d'iterations du calcul plus petit que le nombre d'iterations demandé pour étude de la convergence,
        # on regarde toutes les iterations
        if nombre_ite >> len(liste):
            ite_oscill = int(
                len(liste)) * 50  # donnees disponibles toutes les 50 itérations
        else:
            ite_oscill = nombre_ite

        debut_ite_last = liste[len(liste) - 1][
                             0] - ite_oscill  # On souhaite regarder uniquement les dernieres iterations
        i = 0
        while liste[i][0] < debut_ite_last:
            liste.pop(
                i)  # suppression des iterations inferieures a l'iteration seuil

        # initialisation du max et du min sur la premiere valeur
        ampli_max_in = liste[0][1]
        ampli_min_in = liste[0][1]
        ampli_max_out = liste[0][2]
        ampli_min_out = liste[0][2]
        if isByPass == True:
            ampli_min_bypass = liste[0][3]
            ampli_max_bypass = liste[0][3]

        Liste_graphe_zoom = [[], [], [], []]
        Liste_graphe_out_tot_zoom = []

        for line in range(0, len(liste)):
            # On recupere les valeurs dans des listes pour le graphe zoomé
            Liste_graphe_zoom[0].append(liste[line][0])
            Liste_graphe_zoom[1].append(liste[line][1])
            Liste_graphe_zoom[2].append(liste[line][2])
            if isByPass == True:
                Liste_graphe_zoom[3].append(liste[line][3])

            # REF
            # Test sur les valeurs de debit inlet
            if liste[line][
                1] >= ampli_max_in:  # si superieur au max, on remplace la valeur
                ampli_max_in = liste[line][1]
            elif liste[line][
                1] <= ampli_min_in:  # si inferieur au min, on remplace la valeur
                ampli_min_in = liste[line][1]
            # Test sur les valeurs de debit outlet
            if liste[line][2] >= ampli_max_out:
                ampli_max_out = liste[line][2]
            elif liste[line][2] <= ampli_min_out:
                ampli_min_out = liste[line][2]
            # Test sur les valeurs de debit outlet bypass
            if isByPass == True:
                if liste[line][2] >= ampli_max_out:
                    ampli_max_bypass = liste[line][2]
                elif liste[line][2] <= ampli_min_out:
                    ampli_min_bypass = liste[line][2]

        # On calcule la moyenne en débit et taux de compression des dernières valeurs extraites
        moy_fin_in = moy_fin_out = moy_fin_bypass = 0
        for line in range(0, len(liste) - 1):
            moy_fin_in += liste[line][1]
            moy_fin_out += liste[line][2]
            if isByPass == True:
                moy_fin_bypass += liste[line][3]

        # REF
        # Calcul de l'ecart sur le debit d'entree
        moy_fin_in = moy_fin_in / (len(liste) - 1)
        ampli_in = ampli_max_in - ampli_min_in
        delta_in = (ampli_in / moy_fin_in) * 100

        # Calcul de l'ecart sur le debit de sortie
        moy_fin_out = moy_fin_out / (len(liste) - 1)
        ampli_out = ampli_max_out - ampli_min_out
        delta_out = (ampli_out / moy_fin_out) * 100

        # Calcul de l'ecart sur le debit de sortie bypass
        if isByPass == True:
            moy_fin_bypass = moy_fin_bypass / (len(liste) - 1)
            ampli_bypass = ampli_max_bypass - ampli_min_bypass
            delta_bypass = (ampli_bypass / moy_fin_bypass) * 100

        # --------------------------------------------------------------------------------------------------
        # Création des graphiques et exportation en format pdf
        # --------------------------------------------------------------------------------------------------

        # print ("pdf debut")
        # pdf = PdfPages(data_out+os.sep+ nom_calcul + '.pdf')
        # print ("pdf fin")

        # ----------------------------------- DEBIT INLET ------------------------------------------------
        # Affichage du graphique global
        plt.suptitle("DEBIT INLET de la roue " + row_name)
        plt.subplot(211)
        plt.subplots_adjust(hspace=0.25)
        # print ('plt')
        plt.grid(True)
        plt.gca().yaxis.set_major_locator(MaxNLocator(6))
        plt.plot(Liste_graphe[0], Liste_graphe[1], "b", label="inlet_REF")
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel('Itérations', fontsize=9, labelpad=0)
        plt.ylabel('Débit [kg/s]', fontsize=9)
        plt.legend(loc='best')

        # affichage du graphe sur le zoom des dernieres iterations pour calcul des oscillations
        plt.subplot(212)
        plt.grid(True)
        plt.gca().yaxis.set_major_locator(MaxNLocator(6))
        plt.plot(Liste_graphe_zoom[0], Liste_graphe_zoom[1], "b")

        # Affichage des bornes inf et sup
        plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                 [moy_fin_in + moy_fin_in * ecart_amp / 200,
                  moy_fin_in + moy_fin_in * ecart_amp / 200], "r--")
        plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                 [moy_fin_in - moy_fin_in * ecart_amp / 200,
                  moy_fin_in - moy_fin_in * ecart_amp / 200], "r--")

        # Affichage de la valeur de la limite sup
        text1 = plt.text(
            liste[0][0] + (liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
            moy_fin_in + moy_fin_in * ecart_amp / 200 - 0.00022 * (
                        moy_fin_in + moy_fin_in * ecart_amp / 200),
            'Lim sup = ' + str(
                round(moy_fin_in + moy_fin_in * ecart_amp / 200, 3)),
            color="red", fontsize=7)
        text1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        # Affichage de la valeur de la limite inf
        text2 = plt.text(
            liste[0][0] + (liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
            moy_fin_in - moy_fin_in * ecart_amp / 200 + 0.00014 * (
                        moy_fin_in - moy_fin_in * ecart_amp / 200),
            'Lim inf = ' + str(
                round(moy_fin_in - moy_fin_in * ecart_amp / 200, 3)),
            color="red", fontsize=7)
        text2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        # Affichage de la valeur du débit moyen
        text3 = plt.text(liste[0][0], moy_fin_in - 0.0005 * moy_fin_in,
                         'Débit moyen = ' + str(round(moy_fin_in, 3)),
                         color="green", fontsize=7)
        text3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='green'))

        # Affichage de l'écart relatif des débits min/max
        ecart_deb_min_max = (max(Liste_graphe_zoom[1]) - min(
            Liste_graphe_zoom[1])) / (max(Liste_graphe_zoom[1]) + min(
            Liste_graphe_zoom[1])) * 2 * 100
        text4 = plt.text(liste[len(liste) - 1][0] - 300,
                         moy_fin_in + moy_fin_in * ecart_amp / 200 - 0.00036 * (
                                     moy_fin_in + moy_fin_in * ecart_amp / 200),
                         'Ecart débit min/max (%)\n' + str(
                             round(ecart_deb_min_max, 3)), color="black",
                         fontsize=7)
        text4.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel('Dernières itérations', fontsize=9)
        plt.ylabel('Débit [kg/s]', fontsize=9)

        pdf.savefig()
        plt.close()

        # ----------------------------------- DEBIT OUTLET -----------------------------------------------
        # Affichage du graphique global
        plt.suptitle("DEBIT OUTLET de la roue " + row_name)
        plt.subplot(211)
        plt.subplots_adjust(hspace=0.25)
        plt.grid(True)
        plt.gca().yaxis.set_major_locator(MaxNLocator(6))
        plt.plot(Liste_graphe[0], Liste_graphe[2], "b", label="outlet_REF")
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel('Itérations', fontsize=9, labelpad=0)
        plt.ylabel('Débit [kg/s]', fontsize=9)
        plt.legend(loc='best')

        # affichage du graphe sur le zoom des dernieres iterations pour calcul des oscillations
        plt.subplot(212)
        plt.grid(True)
        plt.gca().yaxis.set_major_locator(MaxNLocator(6))
        plt.plot(Liste_graphe_zoom[0], Liste_graphe_zoom[2], "b")
        # Affichage des bornes inf et sup
        plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                 [moy_fin_out + moy_fin_out * ecart_amp / 200,
                  moy_fin_out + moy_fin_out * ecart_amp / 200], "r--")
        plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                 [moy_fin_out - moy_fin_out * ecart_amp / 200,
                  moy_fin_out - moy_fin_out * ecart_amp / 200], "r--")

        # Affichage de la valeur de la limite sup
        text1 = plt.text(
            liste[0][0] + (liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
            moy_fin_out + moy_fin_out * ecart_amp / 200 - 0.00022 * (
                        moy_fin_out + moy_fin_out * ecart_amp / 200),
            'Lim sup = ' + str(
                round(moy_fin_out + moy_fin_out * ecart_amp / 200, 3)),
            color="red", fontsize=7)
        text1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        # Affichage de la valeur de la limite inf
        text2 = plt.text(
            liste[0][0] + (liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
            moy_fin_out - moy_fin_out * ecart_amp / 200 + 0.00014 * (
                        moy_fin_out - moy_fin_out * ecart_amp / 200),
            'Lim inf = ' + str(
                round(moy_fin_out - moy_fin_out * ecart_amp / 200, 3)),
            color="red", fontsize=7)
        text2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        # Affichage de la valeur du débit moyen
        text3 = plt.text(liste[0][0], moy_fin_out - 0.0005 * moy_fin_out,
                         'Débit moyen = ' + str(round(moy_fin_out, 3)),
                         color="green", fontsize=7)
        text3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='green'))

        # Affichage de l'écart relatif des débits min/max
        ecart_deb_min_max = (max(Liste_graphe_zoom[2]) - min(
            Liste_graphe_zoom[2])) / (max(Liste_graphe_zoom[2]) + min(
            Liste_graphe_zoom[2])) * 2 * 100
        text4 = plt.text(liste[len(liste) - 1][0] - 300,
                         moy_fin_out + moy_fin_out * ecart_amp / 200 - 0.00036 * (
                                     moy_fin_out + moy_fin_out * ecart_amp / 200),
                         'Ecart débit min/max (%)\n' + str(
                             round(ecart_deb_min_max, 3)), color="black",
                         fontsize=7)
        text4.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel('Dernières itérations', fontsize=9)
        plt.ylabel('Débit [kg/s]', fontsize=9)

        pdf.savefig()
        plt.close()

        # ----------------------------------- DEBIT OUTLET BYPASS ----------------------------------------
        # Affichage du graphique global
        if isByPass == True:
            plt.suptitle("DEBIT OUTLET BYPASS de la roue " + row_name)
            plt.subplot(211)
            plt.subplots_adjust(hspace=0.25)
            plt.grid(True)
            plt.gca().yaxis.set_major_locator(MaxNLocator(6))
            plt.plot(Liste_graphe[0], Liste_graphe[3], "b",
                     label="outlet_ByPass_REF")
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.xlabel('Itérations', fontsize=9, labelpad=0)
            plt.ylabel('Débit [kg/s]')
            plt.legend(loc='best')

            # affichage du graphe sur le zoom des dernieres iterations pour calcul des oscillations
            plt.subplot(212)
            plt.grid(True)
            plt.gca().yaxis.set_major_locator(MaxNLocator(6))
            plt.plot(Liste_graphe_zoom[0], Liste_graphe_zoom[3], "b")
            # Affichage des bornes inf et sup
            plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                     [moy_fin_bypass + moy_fin_bypass * ecart_amp / 200,
                      moy_fin_bypass + moy_fin_bypass * ecart_amp / 200],
                     "r--")
            plt.plot([liste[0][0], liste[len(liste) - 1][0]],
                     [moy_fin_bypass - moy_fin_bypass * ecart_amp / 200,
                      moy_fin_bypass - moy_fin_bypass * ecart_amp / 200],
                     "r--")

            # Affichage de la valeur de la limite sup
            text1 = plt.text(liste[0][0] + (
                        liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
                             moy_fin_bypass + moy_fin_bypass * ecart_amp / 200 - 0.00022 * (
                                         moy_fin_bypass + moy_fin_bypass * ecart_amp / 200),
                             'Lim sup = ' + str(round(
                                 moy_fin_bypass + moy_fin_bypass * ecart_amp / 200,
                                 3)), color="red", fontsize=7)
            text1.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            # Affichage de la valeur de la limite inf
            text2 = plt.text(liste[0][0] + (
                        liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
                             moy_fin_bypass - moy_fin_bypass * ecart_amp / 200 + 0.00014 * (
                                         moy_fin_bypass - moy_fin_bypass * ecart_amp / 200),
                             'Lim inf = ' + str(round(
                                 moy_fin_bypass - moy_fin_bypass * ecart_amp / 200,
                                 3)), color="red", fontsize=7)
            text2.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            # Affichage de la valeur du débit moyen
            text3 = plt.text(liste[0][0],
                             moy_fin_bypass - 0.0005 * moy_fin_bypass,
                             'Débit moyen = ' + str(
                                 round(moy_fin_bypass, 3)), color="green",
                             fontsize=7)
            text3.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='green'))

            # Affichage de l'écart relatif des débits min/max
            ecart_deb_min_max = (max(Liste_graphe_zoom[3]) - min(
                Liste_graphe_zoom[3])) / (max(Liste_graphe_zoom[3]) + min(
                Liste_graphe_zoom[3])) * 2 * 100
            text4 = plt.text(liste[len(liste) - 1][0] - 300,
                             moy_fin_bypass + moy_fin_bypass * ecart_amp / 200 - 0.00036 * (
                                         moy_fin_bypass + moy_fin_bypass * ecart_amp / 200),
                             'Ecart débit min/max (%)\n' + str(
                                 round(ecart_deb_min_max, 3)),
                             color="black", fontsize=7)
            text4.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.xlabel('Dernières itérations', fontsize=9)
            plt.ylabel('Débit [kg/s]', fontsize=9)

            pdf.savefig()
            plt.close()

        # ----------------------------------- DEBIT TOTAL = OUTLET + OUTLET BYPASS ----------------------------------------
        # Affichage du graphique global
        if isByPass == True:

            # Ajout des deux debits de la roue concernee et stockage dans un tableau specifique pour les traces
            for i in range(len(Liste_graphe[2])):
                Liste_graphe_out_tot.append(
                    Liste_graphe[2][i] + Liste_graphe[3][i])
            for i in range(len(Liste_graphe_zoom[2])):
                Liste_graphe_out_tot_zoom.append(
                    Liste_graphe_zoom[2][i] + Liste_graphe_zoom[3][i])

            plt.suptitle(
                "DEBIT OUTLET TOTAL (PRIMARY FLOW + BYPASS FLOW) - Roue " + row_name)
            plt.subplot(211)
            plt.subplots_adjust(hspace=0.25)
            plt.grid(True)
            plt.gca().yaxis.set_major_locator(MaxNLocator(6))
            plt.plot(Liste_graphe[0], Liste_graphe_out_tot, "b",
                     label="outlet_Total_REF")
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.xlabel('Itérations', fontsize=9, labelpad=0)
            plt.ylabel('Débit [kg/s]', fontsize=9)
            plt.legend(loc='best')

            # affichage du graphe sur le zoom des dernieres iterations pour calcul des oscillations
            plt.subplot(212)
            plt.grid(True)
            plt.gca().yaxis.set_major_locator(MaxNLocator(6))
            plt.plot(Liste_graphe_zoom[0], Liste_graphe_out_tot_zoom, "b")
            # Affichage des bornes inf et sup
            plt.plot([liste[0][0], liste[len(liste) - 1][0]], [
                (moy_fin_out + moy_fin_bypass) + (
                            moy_fin_out + moy_fin_bypass) * ecart_amp / 200,
                (moy_fin_out + moy_fin_bypass) + (
                            moy_fin_out + moy_fin_bypass) * ecart_amp / 200],
                     "r--")
            plt.plot([liste[0][0], liste[len(liste) - 1][0]], [
                (moy_fin_out + moy_fin_bypass) - (
                            moy_fin_out + moy_fin_bypass) * ecart_amp / 200,
                (moy_fin_out + moy_fin_bypass) - (
                            moy_fin_out + moy_fin_bypass) * ecart_amp / 200],
                     "r--")

            # Affichage de la valeur de la limite sup
            text1 = plt.text(liste[0][0] + (
                        liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
                             (moy_fin_out + moy_fin_bypass) + (
                                         moy_fin_out + moy_fin_bypass) * ecart_amp / 200 - 0.00022 * (
                                         (moy_fin_out + moy_fin_bypass) + (
                                             moy_fin_out + moy_fin_bypass) * ecart_amp / 200),
                             'Lim sup = ' + str(round(
                                 (moy_fin_out + moy_fin_bypass) + (
                                             moy_fin_out + moy_fin_bypass) * ecart_amp / 200,
                                 3)), color="red", fontsize=7)
            text1.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            # Affichage de la valeur de la limite inf
            text2 = plt.text(liste[0][0] + (
                        liste[len(liste) - 1][0] - liste[0][0]) / 2 - 50,
                             (moy_fin_out + moy_fin_bypass) - (
                                         moy_fin_out + moy_fin_bypass) * ecart_amp / 200 + 0.00014 * (
                                         (moy_fin_out + moy_fin_bypass) - (
                                             moy_fin_out + moy_fin_bypass) * ecart_amp / 200),
                             'Lim inf = ' + str(round(
                                 (moy_fin_out + moy_fin_bypass) - (
                                             moy_fin_out + moy_fin_bypass) * ecart_amp / 200,
                                 3)), color="red", fontsize=7)
            text2.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            # Affichage de la valeur du débit moyen
            text3 = plt.text(liste[0][0],
                             (moy_fin_out + moy_fin_bypass) - 0.0005 * (
                                         moy_fin_out + moy_fin_bypass),
                             'Débit moyen = ' + str(
                                 round((moy_fin_out + moy_fin_bypass), 3)),
                             color="green", fontsize=7)
            text3.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='green'))

            # Affichage de l'écart relatif des débits min/max
            ecart_deb_min_max = (max(Liste_graphe_out_tot_zoom) - min(
                Liste_graphe_out_tot_zoom)) / (
                                            max(Liste_graphe_out_tot_zoom) + min(
                                        Liste_graphe_out_tot_zoom)) * 2 * 100
            text4 = plt.text(liste[len(liste) - 1][0] - 300,
                             (moy_fin_out + moy_fin_bypass) + (
                                         moy_fin_out + moy_fin_bypass) * ecart_amp / 200 - 0.00036 * (
                                         (moy_fin_out + moy_fin_bypass) + (
                                             moy_fin_out + moy_fin_bypass) * ecart_amp / 200),
                             'Ecart débit min/max (%)\n' + str(
                                 round(ecart_deb_min_max, 3)),
                             color="black", fontsize=7)
            text4.set_bbox(
                dict(facecolor='white', alpha=1, edgecolor='red'))

            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8)
            plt.xlabel('Dernières itérations', fontsize=9)
            plt.ylabel('Débit [kg/s]', fontsize=9)

            pdf.savefig()
            plt.close()


def convergenceAnalysis(casePath, caseName, outputdir, PDFname):

    print('**************** ', caseName, ' ****************')
    print('')

    logger = logging.getLogger()

    resDir = casePath + os.sep + 'res'
    # fichier contenant le nombre d'aubes et leur nom dans le bon ordre
    paramInfo = casePath + os.sep + 'params_case'

    print(
        "*****-------------------------    VERIFICATION DES DONNEES EN COURS                    -------------------------*****")

    if not os.path.isfile(paramInfo):
        logger.error("Fichier params_case introuvable pour le cas")

    else:
        # Recuperation des noms des grilles In, Out et ByPass
        # (row_in, row_out, row_out_bypass) = (list of 'ROW_x_INFLOW', list of 'ROW_x_OUTFLOW', list of 'ROW_x_OUTFLOW_BYPASS')
        (row_in, row_out, row_out_bypass) = Recup_Roues_In_Out(paramInfo,
                                                               resDir)

        # Recuperation des noms de roue
        row_name = [] * len(row_in)
        for i in range(len(row_in)):
            if (row_in[i][4:7] == 'ROW'):
                row_name.append(row_in[i][4:9])
            else:
                row_name.append(row_in[i][4:8])

        print(
            "*****-------------------------    VERIFICATION DES DONNEES EFFECTUES AVEC SUCCES       -------------------------*****\n")

        inlet_debit = []
        outlet_debit = []
        outlet_bypass_debit = []
        data_inlet = []
        data_outlet = []
        data_outlet_bypass = []
        destination_inlet = []
        destination_outlet = []
        destination_outlet_bypass = []
        desti_intermediate = []
        destination_in_out = []
        destination_all = []
        list_intermediate = []

        print(
            "*****-------------------------    DEBUT DE LA PREPARATION DES DONNEES                  -------------------------*****")

        # **--------------------    GENERATION DE LA LISTE CONTENANT LES VALEURS DU DEBIT INFLOW    -------------------------------**

        for i in range(len(row_in)):
            # inlet_debit.append(resDir + os.sep + 'var_' + row_in[i] + 'Massflow.v3d')
            inlet_debit.append(resDir + os.sep + row_in[i])

            if not os.path.isfile(inlet_debit[
                                      i]):  # On va chercher si les fichiers ROW_x_INFLOWMassflow.v3d existent
                # si absence d'un des fichiers : calcul non revenu
                print(
                    "Fichiers INFLOWMassflow introuvables pour le cas. Etes-vous sur que les calculs sont revenus ?")
            else:
                data_inlet.append(Lecture(inlet_debit[
                                              i]))  # On va lire les fichiers ROW_x_INFLOWMassflow.v3d et y recuperer toutes les informations
                destination_inlet.append(Concatener(data_inlet[i],
                                                    True))  # On va concatener la liste afin d'y recuperer les informations utiles (nombre iterations et debits inlet)

        print(
            "*****-------------------------    >>> Import des debits Inlet OK")

        # **--------------------    GENERATION DE LA LISTE CONTENANT LES VALEURS DU DEBIT OUTFLOW    ------------------------------**

        for i in range(len(row_out)):
            # outlet_debit.append(resDir + os.sep + 'var_' + row_out[i] + 'Massflow.v3d')
            outlet_debit.append(resDir + os.sep + row_out[i])

            if not os.path.isfile(outlet_debit[
                                      i]):  # On va chercher si les fichiers ROW_x_OUTFLOWMassflow.v3d existent
                # si absence d'un des fichiers : calcul non revenu
                print(
                    "Fichier OUTFLOWMassflow introuvables pour le cas. Etes-vous sur que les calculs sont revenus ?")
            else:
                data_outlet.append(Lecture(outlet_debit[
                                               i]))  # On va lire les fichiers ROW_x_OUTFLOWMassflow.v3d et y recuperer toutes les informations
                destination_outlet.append(Concatener(data_outlet[i],
                                                     False))  # On va concatener la liste afin d'y recuperer les informations utiles (nombre iterations et debits inlet)

        print(
            "*****-------------------------    >>> Import des debits Outlet OK")

        # **--------------------    GENERATION DE LA LISTE CONTENANT LES VALEURS DU DEBIT OUTFLOW_BYPASS    ------------------------------**

        for i in range(len(row_out_bypass)):
            # outlet_bypass_debit.append(resDir + os.sep + 'var_' + row_out_bypass[i] + 'Massflow.v3d')
            outlet_bypass_debit.append(resDir + os.sep + row_out_bypass[i])

            if not os.path.isfile(outlet_bypass_debit[
                                      i]):  # On va chercher si les fichiers ROW_x_OUTFLOW_BYPASSMassflow.v3d existent
                # si absence du fichier ROW_x_OUTFLOW_BYPASSMassflow.v3d --> Warning
                print(
                    "*****-------------------------    >>> Fichier OUTFLOW_BYPASSMassflow introuvables pour la roue " +
                    row_name[i])
                if not os.path.isfile(inlet_debit[i]):
                    print(
                        "*****-------------------------        Etes-vous sur que les calculs sont revenus ?")
                else:
                    print(
                        "*****-------------------------        Cette roue n'a pas de débit ByPass.")
                data_outlet_bypass.append(['Null'])
                destination_outlet_bypass.append(['NULL'])
            else:
                data_outlet_bypass.append(Lecture(outlet_bypass_debit[
                                                      i]))  # On va lire les fichiers ROW_x_OUTFLOW_BYPASSMassflow.v3d et y recuperer toutes les informations
                destination_outlet_bypass.append(
                    Concatener(data_outlet_bypass[i],
                               False))  # On va concatener la liste afin d'y recuperer les informations utiles (debits outlet by_pass)
                print(
                    "*****-------------------------    >>> Import des debits Outlet ByPass OK pour la roue " +
                    row_name[i])

        # print('******************************************************************')
        for i in range(len(destination_outlet)):
            for j in range(len(destination_outlet[i])):
                desti_intermediate.append(
                    destination_inlet[i][j] + destination_outlet[i][
                        j])  # On ajoute les valeurs (debits inlet et outlet) correspondant a une iteration donnee dans une même mini-liste j
            destination_in_out.append(
                desti_intermediate)  # On ajoute la liste desti_intermediate (contenant j mini-listes) correspondant a chaque dans la liste destination_in_out
            desti_intermediate = []  # Une fois qu'on fait le tour d'une roue on reinitialise la liste desti_intermediate

        for i in range(len(destination_outlet_bypass)):
            for j in range(len(destination_in_out[i])):
                if destination_outlet_bypass[i] == ['NULL']:
                    desti_intermediate.append(
                        destination_in_out[i][j] + ['NULL'])
                else:
                    desti_intermediate.append(destination_in_out[i][j] +
                                              destination_outlet_bypass[i][
                                                  j])  # On ajoute les valeurs (debits inlet, outlet et outlet by_pass) correspondant a une iteration donnee dans une même mini-liste j
            destination_all.append(
                desti_intermediate)  # On ajoute la liste desti_intermediate (contenant j mini-listes) correspondant a chaque dans la liste destination_all
            desti_intermediate = []  # Une fois qu'on fait le tour d'une roue on reinitialise la liste desti_intermediate

        print(
            "*****-------------------------    PREPARATION DES DONNEES EFFECTUEES AVEC SUCCES       -------------------------*****\n")

        #######-----------------------***-----------------------      ANALYSES DE CONVERGENCE      -----------------------***-----------------------#######
        print(
            "*****-------------------------    ANALYSES DE LA CONVERGENCE EN COURS                  -------------------------*****")
        pdf = PdfPages(
            outputdir + os.sep + PDFname + '.pdf')  # Creation du PDF ou apparaitront toutes les figures relatives aux analyses des convergences

        for i in range(len(destination_all)):
            blade_number = i + 1
            isByPass = True
            if destination_outlet_bypass[i] == [
                'NULL']:  # Si absence des debits by_pass pour la roue concerne, alors on informe a la fonction Calcul_Convergence qu'on ne generera pas de figures relatives aux debits outlet by_pass
                isByPass = False

            # La fonction permet de calculer la convergence et de tracer les figures avec la plage de variation de 0.1% par rapport a la moyenne des valeurs sur les x dernieres iterations (avec x=ite (cf en tete de ce code))
            Calcul_Convergence(destination_all[i], outputdir, row_name[i],
                               blade_number, isByPass, pdf)

        pdf.close()

    print(
        "*****-------------------------    ANALYSES DE LA CONVERGENCE EFFECTUEES AVEC SUCCES    -------------------------*****\n")


###################################################
#                PARTIE A MODIFIER                #
###################################################

def launch_trace_conv(etat, case):

    caseName = case.name
    casePath = os.path.join(etat.cas_temp_repertory, case.name)

    # Definition du nom du PDF
    PDFname = 'Convergence_' + caseName

    print(
        '\n======================= TRACES DES CONVERGENCES DES DEBITS =======================\n')
    print('CAS D' + "'" + 'ETUDE  : ' + caseName)

    output_dir = os.path.join(etat.work_directory, "ConvAuto")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    convergenceAnalysis(casePath, caseName, output_dir, PDFname)

    print('\nTRAVAIL TERMINÉ. CAS TRACÉ = ', caseName)

