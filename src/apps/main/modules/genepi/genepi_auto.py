#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PROFIL CoBP/CoHP
ProfileName = globals().get('ProfileName')

# TITRE DE LA PRESENTATION
TitrePres = globals().get('TitrePres', "GENEPI AUTO")

# -------------------------------------------------------------------------------------------------------------------
# AFFICHAGE OU NON DE LA LEGENDE
AfficherLegende = globals().get('AfficherLegende', 1)

# -------------------------------------------------------------------------------------------------------------------
# CHOIX DES EXPORT DE LA PRESENTATION
ExportPDF = globals().get('ExportPDF', True)
ExportExcel = globals().get('ExportExcel', False)
ExportPPT = globals().get('ExportPPT', False)

# -------------------------------------------------------------------------------------------------------------------
# CHOIX DES POST-TRAITEMENTS A EFFECTUER

Trace_InfosCas = globals().get('Trace_InfosCas', 1)
Trace_InfosPlanUtilisateur = globals().get('Trace_InfosPlanUtilisateur', 1)
# --------------
Trace_QualiteMaillage = globals().get('Trace_QualiteMaillage', 0)
Trace_VisuQualiteMaillage = globals().get('Trace_VisuQualiteMaillage', 0)
# --------------
Trace_ConvDebit = globals().get('Trace_ConvDebit', 0)
Trace_ConvResidus = globals().get('Trace_ConvResidus', 0)
# --------------
Trace_ParVariable = globals().get('Trace_ParVariable', 1)
Trace_GradientMoyAdim = globals().get('Trace_GradientMoyAdim', 0)

# --------------
Trace_LoisGeom = globals().get('Trace_LoisGeom', 0)
Trace_Perfos0D = globals().get('Trace_Perfos0D', 1)
Trace_ProfilsRadiaux = globals().get('Trace_ProfilsRadiaux', 1)
Trace_ProfilVsCorde = globals().get('Trace_ProfilVsCorde', 1)
Trace_ProfilsRadiauxAngle = globals().get('Trace_ProfilsRadiauxAngle', 0)
Trace_ProfilAzimuthaux = globals().get('Trace_ProfilAzimuthaux', 0)
Trace_Polaire = globals().get('Trace_Polaire', 0)
# --------------
Trace_ProfilsRadiaux_CL = globals().get('Trace_ProfilsRadiaux_CL', 0)
Trace_EvolutionParois = globals().get('Trace_EvolutionParois', 0)
Trace_EvolutionAxiale = globals().get('Trace_EvolutionAxiale', 0)
Trace_EvolutionMeridienne = globals().get('Trace_EvolutionMeridienne', 0)
# --------------
Trace_VisuEnsight = globals().get('Trace_VisuEnsight', 0)

# --------------
PlanCFD_AmontPerfo = globals().get('PlanCFD_AmontPerfo', '(BA)')
PlanCFD_AvalPerfo = globals().get('PlanCFD_AvalPerfo', '(BF)')
PlanCFD_ProcheBA = globals().get('PlanCFD_ProcheBA', '(BA)')
PlanCFD_ProcheBF = globals().get('PlanCFD_ProcheBF', '(BF)')
PlanCFD_LoinBA = globals().get('PlanCFD_LoinBA', '(BA-1)')
PlanCFD_LoinBF = globals().get('PlanCFD_LoinBF', '(BF+1)')
PlanBSAM_AmontPerfo = globals().get('PlanBSAM_AmontPerfo', '(BA-1)')
PlanBSAM_AvalPerfo = globals().get('PlanBSAM_AvalPerfo', '(BF+1)')
PlanBSAM_ProcheBA = globals().get('PlanBSAM_ProcheBA', '(BA-1)')
PlanBSAM_ProcheBF = globals().get('PlanBSAM_ProcheBF', '(BF+1)')
PlanBSAM_LoinBA = globals().get('PlanBSAM_LoinBA', '(BA-1)')
PlanBSAM_LoinBF = globals().get('PlanBSAM_LoinBF', '(BF+1)')
PlanGcolter_Amont = globals().get('PlanGcolter_Amont', '(BA)')
PlanGcolter_Aval = globals().get('PlanGcolter_Aval', '(BF)')

# --------------
DicoLabelAube2Trace_defaut = {'Total': [], 'Primaire': [], 'Secondaire': []}
DicoLabelAube2Trace = globals().get('DicoLabelAube2Trace',
                                    DicoLabelAube2Trace_defaut)

if len(DicoLabelAube2Trace['Primaire']) > 0 or len(
    DicoLabelAube2Trace['Secondaire']) > 0:
    IsBiFlux = True
else:
    IsBiFlux = False

if IsBiFlux:
    DicoFluxAube_defaut = {'Total': ['MF'],
                           'Primaire': ['RDE', 'RM1', 'RD1', 'RM2', 'RD2',
                                        'RM3', 'RD3', 'RM4', 'RD4', 'RM5',
                                        'RD5', 'RM6', 'RD6', 'RM7', 'RD7',
                                        'RM8', 'RD8', 'RM9', 'RD9', 'RM10',
                                        'RD10'],
                           'Secondaire': ['OGV'],
                           }
else:
    DicoFluxAube_defaut = {
        'Total': ['RDE', 'RM1', 'RD1', 'RM2', 'RD2', 'RM3', 'RD3', 'RM4', 'RD4',
                  'RM5', 'RD5', 'RM6', 'RD6', 'RM7', 'RD7', 'RM8', 'RD8', 'RM9',
                  'RD9', 'RM10', 'RD10'],
        'Primaire': [],
        'Secondaire': [],
        }

DicoFluxAube = globals().get('DicoLabelAube2Trace', DicoFluxAube_defaut)

# --------------
DicoXYVarLoisGeom_defaut = {'HauteurListe': [''],
                            # Pour tracer toutes les coupes [''] sinon [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] ou [10, 20, 30, 40, 50, 60, 70, 80, 90]
                            'HauteurCoupeDessins': True,
                            # Pour tracer toutes les coupes de dessins si celles-ci sont definies dans le cas CARMA.
                            'HauteurCoupeParCoupe': True,
                            # Pour tracer toutes les coupes une a une

                            #  Activation des traces
                            'LoisGeomVisuMeridenne_2trace': True,
                            # Permet d'activer le tracé des visualisations de la geometrie en vue meridienne
                            'LoisGeomVsHauteur_2trace': True,
                            # Permet d'activer le tracé des lois suivant la hauteur
                            'LoisGeomVsCorde_2trace': True,
                            # Permet d'activer le tracé des lois suivant la corde
                            'LoisGeomVsCorde_Hauteur_2trace': True,
                            # Permet d'activer le tracé des lois suivant la corde et la hauteur
                            'LoisGeomCol3D_2trace': True,
                            # Permet d'activer le tracé des lois de section
                            'LoisGeomCoupe_2trace': True,
                            # Permet d'activer le tracé des coupes
                            'LoisGeomVisuAube_2trace': False,
                            # Permet d'activer le tracé des aubages
                            'LoisGeomVisuBABF_2trace': True,
                            # Permet d'activer le tracé des Zooms BA/BF

                            'LoisGeom_XYvar': [
                                ('Comparaison beta1', 'h_H'),
                                # Possibilité de  traiter une unique variable ou plusieurs par le biais d'une liste (Si plusieurs variables alors celles-ci seront supperposées)
                                ('Comparaison beta2', 'h_H'),
                                # (['b1sqT_7.0pct','b1sqT_8.0pct'],'rBA_adim'),
                                # (['b1sqTo','b1sqT_7.5pct'],'rBA_adim'),
                                # (['b2sqT_7.0pct','b2sqT_8.0pct'],'rBF_adim'),
                                # (['b2sqTo','b2sqT_7.5pct'],'rBF_adim'),
                                ('Calage', 'rBF_adim'),
                                ('Cambrure', 'rMoyen_adim'),
                                ('Cambrure_FromCD_8.0pct', 'rMoyen_adim'),
                                ('Cambrure_8.0pct', 'rMoyen_adim'),
                                ('Corde', 'rBF_adim'),
                                ('CordeAxi', 'rBF_adim'),
                                (['EBA_0.30mm', 'EBA_1.00mm', 'EBA_3.00mm'],
                                 'rBA_adim'),
                                (['EBF_5.00mm', 'EBF_3.00mm', 'EBF_1.00mm'],
                                 'rBF_adim'),
                                # ('EBA_0.30mm','rMoyen_adim'),
                                # ('EBA_1.00mm','rMoyen_adim'),
                                # ('EBA_3.00mm','rMoyen_adim'),
                                # ('EBA_5.00mm','rMoyen_adim'),
                                # ('EBA_0.75pct','rMoyen_adim'),
                                # ('EBA_1.0pct','rMoyen_adim'),
                                # ('EBA_1.5pct','rMoyen_adim'),
                                # ('EBA_2.5pct','rMoyen_adim'),
                                # ('EBA_4.0pct','rMoyen_adim'),
                                # ('EBF_1.00mm','rMoyen_adim'),
                                ('Emax', 'rBF_adim'),
                                ('EmaxsC', 'rBF_adim'),
                                ('XEmax', 'rBF_adim'),
                                ('XEmaxsC', 'rBF_adim'),
                                # ('EpBA_Emax_FromCD_8.0pct','rMoyen_adim'),
                                # ('EpBF_Emax_FromCD_8.0pct','rMoyen_adim'),
                                ('ssc', 'rBF_adim'),
                                ('s', 'rBF_adim'),
                                ('XgCale', 'rBF_adim'),
                                ('YgCale', 'rBF_adim'),
                                ('xBa', 'rBA_adim'),
                                ('xBf', 'rBA_adim'),
                                # ('PenteTraceBA','rBA_adim'),
                                # ('PenteTraceBF','rBF_adim'),
                                ('yBa', 'rBA_adim'),
                                ('yBf', 'rBF_adim'),
                                ('sweep_BA', 'rBA_adim'),
                                ('sweep_BF', 'rBF_adim'),
                                ('dihedral_BA', 'rBA_adim'),
                                ('dihedral_BF', 'rBF_adim'),
                                ('INCD', 'rBA_adim'),
                                ('EFP', 'rBF_adim'),
                                ('DLI', 'h_H'),
                                ('PSIA', 'h_H'),
                                ('Marge', 'h_H'),
                                ('ACol/S', 'h_H'),
                                ('ACol/AEntree', 'h_H'),
                                ('ASortie/ACol', 'h_H'),
                                ('SCol/SX', 'h_H'),
                                ('XCol/CX', 'h_H'),
                                ('Mach Entree', 'h_H'),
                                ('Mach Sortie', 'h_H'),
                                ('DiedreBA_8.0pct', 'rMoyen_adim'),
                            ],

                            'LoisGeomVsCorde_XYvar': [
                                (['BSQ', 'BSQ_EXT', 'BSQ_INT'], ['cordeRed']),
                                (['BSQ', 'BSQ_cor_8.0pct'],
                                 ['cordeRed', 'cordeRed_BSQ_adim_8.0pct']),
                                (['BSQ_adim_8.0pct'],
                                 'cordeRed_BSQ_adim_8.0pct'),
                                (['BSQ_EXT', 'BSQ_EXT_cor_8.0pct'],
                                 ['cordeRed', 'cordeRed_BSQ_EXT_adim_8.0pct']),
                                (['BSQ_EXT_adim_8.0pct'],
                                 'cordeRed_BSQ_EXT_adim_8.0pct'),
                                (['EPAIS', 'EPAIS_cor_8.0pct'],
                                 ['cordeRed', 'cordeRed_EPAIS_adim_8.0pct']),
                                (['EPAIS_adim_8.0pct'],
                                 'cordeRed_EPAIS_adim_8.0pct'),
                                ('RayonCourbure',
                                 'cordeRed_BA_BF_BA_RayCourbure'),
                                ('Courbure', 'corde_Courbure'),
                            ],

                            'LoisGeomVsCorde_VarMinMax': {
                                # Mettre None si on veut une valeur automatique ou enlever la variable du dictionnaire
                                # 'PENTE_EXTRA'   : {'Min' : 0.0, 'Max' : None},
                                # 'PENTE_INTRA'   : {'Min' : 10.0, 'Max' : None},

                                # 'BSQ'       : {'Min' : 0.0, 'Max' : 100},
                                'BSQ_adim_8.0pct': {'Min': 0.0, 'Max': 1.0},

                                # 'BSQ_EXT'   : {'Min' : 0.0, 'Max' : 100},
                                'BSQ_EXT_adim_8.0pct': {'Min': 0.0, 'Max': 1.0},

                                # 'EPAIS'     : {'Min' : 0.0, 'Max' : 10},
                                'EPAIS_adim_8.0pct': {'Min': 0.0, 'Max': 1.0},

                                'RayonCourbure': {'Min': 1.45, 'Max': 1.65},
                                'Courbure': {'Min': -0.03, 'Max': 0.03},

                                'cordeReduite': {'Min': 0.0, 'Max': 1.0},
                                'cordeRed': {'Min': 0.0, 'Max': 1.0},
                                'cordeRed_BSQ_adim_8.0pct': {'Min': 0.0,
                                                             'Max': 1.0},
                                'cordeRed_BSQ_EXT_adim_8.0pct': {'Min': 0.0,
                                                                 'Max': 1.0},
                                'cordeRed_EPAIS_adim_8.0pct': {'Min': 0.0,
                                                               'Max': 1.0},
                                'cordeRed_BA_BF_BA_RayCourbure': {'Min': 0.0,
                                                                  'Max': 2.0},
                                # 'corde_Courbure'      : {'Min' : 0.0, 'Max' : 2.0},
                            },

                            'LoisGeomVsCorde_Hauteur_XYvar': [('BSQ', '_h_H'),
                                                              ('PENTE_EXTRA',
                                                               '_h_H'),
                                                              ('PENTE_INTRA',
                                                               '_h_H'),
                                                              ('EPAIS', '_h_H'),
                                                              ],

                            }

# DICTIONNAIRE RELATIF Aux CLEFS : Trace_Perfos0D
DicoXYVarPerfos0D2Trace_defaut = {'Perfos0D_XYvar': {
    'ROTOR': [['Qcorr_ref_KD_ref', 'Pi'], ['etapol', 'Pi'],
              ['Qcorr_ref_KD_ref', 'etapol'], ['etapol', 'PisD']],
    'STATOR': [['Qcorr_ref_KD_ref', 'Pi'], ['cd_fftro', 'Pi'],
               ['Qcorr_ref_KD_ref', 'cd_fftro'], ['cd_fftro', 'PisD']],
    },
                                  'Perfos0D_Plan': [
                                      ['AmontPerfo', 'AvalPerfo']],

                                  'Perfos0D_Tableau': True,
                                  'Perfos0D_TableauXYvar': {
                                      'ROTOR': ['Référence', 'Qcorr_ref',
                                                'Qcorr_ref_KD_ref', 'Pi',
                                                'etapol', 'deltapctQcorr_ref',
                                                'deltapctQcorr_ref_KD_ref',
                                                'deltapctPi', 'deltaetapol'],
                                      # 'R\xe9f\xe9rence'
                                      'STATOR': ['Référence', 'Qcorr_ref',
                                                 'Qcorr_ref_KD_ref', 'Pi',
                                                 'cd_fftro',
                                                 'deltapctQcorr_ref',
                                                 'deltapctQcorr_ref_KD_ref',
                                                 'deltapctPi',
                                                 'deltapctcd_fftro'],
                                      },
                                  }

# Parametrisation dans le cas ou on est en mode champs
DicoXYVarPerfos0D2Trace_Champs_defaut = {'Perfos0D_XYvar': {
    'ROTOR': [['Qcorr_ref', 'Pi'], ['etapol', 'Pi'], ['Qcorr_ref', 'etapol'],
              ['etapol', 'PisD'], ['Qcorr_ref', 'Dev'],
              ['Qcorr_ref', 'W2_W1_RAL'], ['Qcorr_ref', 'XNR_'],
              ['XNR_', 'Pi']],
    'STATOR': [['Qcorr_ref', 'Pi'], ['cd_fftro', 'Pi'],
               ['Qcorr_ref', 'cd_fftro'], ['cd_fftro', 'PisD']],
    },
                                         'Perfos0D_Plan': [['(BA)', '(BF)']],

                                         'Perfos0D_Tableau': False,
                                         'Perfos0D_TableauXYvar': {
                                             'ROTOR': ['Référence', 'Qcorr_ref',
                                                       'Pi', 'etapol',
                                                       'deltapctQcorr_ref',
                                                       'deltapctPi',
                                                       'deltaetapol'],
                                             # 'R\xe9f\xe9rence'
                                             'STATOR': ['Référence',
                                                        'Qcorr_ref', 'Pi',
                                                        'cd_fftro',
                                                        'deltapctQcorr_ref',
                                                        'deltapctPi',
                                                        'deltapctcd_fftro'],
                                             },
                                         }

# DICTIONNAIRE RELATIF AU CLEFS : Trace_ProfilsRadiaux
DicoXYVarProfilsRadiaux2Trace_defaut = {'VisuGeom_2trace': True,
                                        'GradPlanUnique_XVar': ['Ps', 'Pta',
                                                                'Ts', 'Tta',
                                                                'Vm', 'Vx',
                                                                'Ma', 'Mx',
                                                                'alpha', 'beta',
                                                                'phi', 'INCD',
                                                                'EFP'],
                                        'GradPlanUnique_Yvar': 'h_H_norm',
                                        # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                        'GradPlanUnique_Plan': ["LoinBA",
                                                                "ProcheBA",
                                                                "ProcheBF",
                                                                "LoinBF"],
                                        'GradPlanUnique_Plan_INCD_EFP': [
                                            "ProcheBA", "ProcheBF"],

                                        'GradPlanVsPlanRef_XVar': ['Pi',
                                                                   'etapol',
                                                                   'cd_fftro',
                                                                   'Dev',
                                                                   'V2_V1_RAL',
                                                                   'W2_W1_RAL',
                                                                   'PSIA',
                                                                   'DLI', 'Tau',
                                                                   'Marge'],
                                        'GradPlanVsPlanRef_Yvar': 'h_H_norm',
                                        # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                        'GradPlanVsPlanRef_InterpDir': 'q_Q',
                                        # h_H / q_Q
                                        'GradPlanVsPlanRef_Plan': [
                                            ["AmontPerfo", "AvalPerfo"]],

                                        'Grad_DeltaXVar': ['INCD', 'EFP', 'Pi',
                                                           'etapol', 'cd_fftro',
                                                           'Marge'],

                                        'Grad_XVar_NePasTracerPourStator': [
                                            'etapol'],
                                        'Grad_XVar_NePasTracerPourRotor': [
                                            'V2_V1_RAL'],
                                        }

# Parametrisation dans le cas ou on se compare a MISES
DicoXYVarProfilsRadiaux2Trace_Mises_defaut = {'VisuGeom_2trace': True,
                                              'GradPlanUnique_XVar': ['Ps',
                                                                      'Pta',
                                                                      'Ptr',
                                                                      'Ts',
                                                                      'Tta',
                                                                      'Ttr',
                                                                      'W', 'Vm',
                                                                      'Wt',
                                                                      'Ma',
                                                                      'Mm',
                                                                      'beta'],
                                              'GradPlanUnique_Yvar': 'h_H',
                                              # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                              'GradPlanUnique_Plan': ["(BA)",
                                                                      "(BF)"],
                                              'GradPlanUnique_Plan_INCD_EFP': [
                                                  "(BA)", "(BF)"],

                                              'GradPlanVsPlanRef_XVar': ['Pi',
                                                                         'etapol',
                                                                         'cd_fftro',
                                                                         'Cd_MISES',
                                                                         'Cd_shock_MISES',
                                                                         'Cd_visc_MISES',
                                                                         'Dev',
                                                                         'W2_W1_RAL',
                                                                         'Tau'],
                                              'GradPlanVsPlanRef_Yvar': 'h_H',
                                              # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                              'GradPlanVsPlanRef_InterpDir': 'q_Q',
                                              # h_H / q_Q
                                              'GradPlanVsPlanRef_Plan': [
                                                  ["(BA)", "(BF)"]],

                                              'Grad_DeltaXVar': ['INCD', 'EFP',
                                                                 'Pi', 'etapol',
                                                                 'cd_fftro',
                                                                 'Marge'],

                                              'Grad_XVar_NePasTracerPourStator': [
                                                  'etapol'],
                                              'Grad_XVar_NePasTracerPourRotor': [
                                                  'V2_V1_RAL'],
                                              }

# Parametrisation dans le cas ou on est en mode champs
DicoXYVarProfilsRadiaux2Trace_Champs_defaut = {'VisuGeom_2trace': True,
                                               'GradPlanUnique_XVar': ['alpha',
                                                                       'beta',
                                                                       'Ps',
                                                                       'Pta',
                                                                       'Tta',
                                                                       'Vm',
                                                                       'Mr',
                                                                       'RhoVm'],
                                               # Manque INCD/INCD_GX/ PS/PT2 / ROVZ1 / XRVU / DEQ / CDPRO / CDCHO / CDBLO / CDCOR / CDSEC / MARGE / SCOL/PAS/ KD
                                               'GradPlanUnique_Yvar': 'h_H_norm',
                                               # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                               'GradPlanUnique_Plan': ["(BA)",
                                                                       "(BF)"],
                                               'GradPlanUnique_Plan_INCD_EFP': [
                                                   "(BA)", "(BF)"],

                                               'GradPlanVsPlanRef_XVar': ['Pi',
                                                                          'etapol',
                                                                          'cd_fftro',
                                                                          'Dev',
                                                                          'W2_W1_RAL',
                                                                          'PSIA',
                                                                          'DLI',
                                                                          'Tau',
                                                                          'Marge'],
                                               # 'RhoVm2_RhoVm1','R2_R1'
                                               'GradPlanVsPlanRef_Yvar': 'h_H_norm',
                                               # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                               'GradPlanVsPlanRef_InterpDir': 'q_Q',
                                               # h_H / q_Q
                                               'GradPlanVsPlanRef_Plan': [
                                                   ["(BA)", "(BF)"]],

                                               'Grad_DeltaXVar': ['INCD', 'EFP',
                                                                  'Pi',
                                                                  'etapol',
                                                                  'cd_fftro',
                                                                  'Marge'],

                                               'Grad_XVar_NePasTracerPourStator': [
                                                   'etapol'],
                                               'Grad_XVar_NePasTracerPourRotor': [
                                                   'V2_V1_RAL'],
                                               }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilsRadiauxAngle
'''
Variables disponibles: 
        'Q%BSAM','b1sq','b2sq','beta_BA','beta_BF','Calage','corde','deltasq','dli_empilage','dli_rBA','dli_rBF','dli_rmoy','efp','h_H_BA','h_H_BF','h_H_moy','incd','Mr_BA','Mr_BF',
        'Ptr_BA','Ptr_BF','R_BA','R_BF','R_moy','r_R_BA','r_R_BF','r_R_moy','ssc_empilage','ssc_rmoy','Ttr_BA','Ttr_BF','Vt_BA','Vt_BF','W_BA','W_BF','X_BA','X_BF',
        'zweifel_empilage','zweifel_rBA','zweifel_rBF','zweifel_rmoy','plan_amont','plan_aval
'''
DicoXYVarProfilsRadiauxAngle2Trace_defaut = {'VisuGeom_2trace': True,
                                             'GradPlanUnique_XYvar': [
                                                 ('b1sq', 'h_H_BA'),
                                                 ('b2sq', 'h_H_BF'),
                                                 ('incd', 'h_H_BA'),
                                                 ('efp', 'h_H_BF'),
                                                 ('dli_empilage', 'h_H_moy'),
                                                 (
                                                 'zweifel_empilage', 'h_H_moy'),
                                                 ],
                                             }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilVsCorde
DicoXYVarProfilVsCorde2Trace_defaut = {'HauteurType': ['QBSAM', 'QNS3D', 'h_H'],
                                       # 'QBSAM' / 'QNS3D' / 'h_H'
                                       'HauteurListe': [],
                                       # Pour tracer toutes les coupes [''] sinon [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] ou [10, 20, 30, 40, 50, 60, 70, 80, 90]

                                       'CourbeProfil_UnGrapheParPage': False,
                                       # Permet de tracer un graphe par page
                                       'CourbeProfil_UnGrapheParPage_Yvar': [
                                           'mis3'],
                                       # Liste des variables pour lesquelles on va tracer un graphe par page

                                       'CourbeProfil_XYvar': [
                                           ('mis3', 'Corde_BA_BF'),
                                           ('WallCellSize', 'Corde_BA_BF'),
                                           ('delta_cell_count', 'Corde_BA_BF'),
                                           ],

                                       'CourbeProfil_Yvar': {'ROTOR': {
                                           # 'mis3' : {'Min' : , 'Max' : 1.5},    # Mettre None si on veut une valeur automatique ou enlever la variable du dictionnaire
                                           # 'hi'   : {'Min' : 0.0, 'Max' : 5},
                                       },
                                           'STATOR': {
                                               # 'mis3' : {'Min' : 0.2, 'Max' : 1.2},
                                               # 'hi'   : {'Min' : 0.0, 'Max' : 5},
                                           },
                                       },

                                       'CourbeProfilRadiaux': False,
                                       'CourbeProfilRadiaux_XYvar': [
                                           ('h_H', 'mis3_max'),
                                           ('h_H', 'd_D_aero_max(mis3)_ref'),
                                           ('h_H', 'mis3_max/M2'),
                                           ],
                                       }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilAzimuthaux
DicoXYVarProfilAzimuthaux2Trace_defaut = {'VisuGeom_2trace': True,
                                          'ProfilAzimuthaux_Plan': ['(BF+1)'],
                                          'ProfilAzimuthaux_HauteurType': 'h_H',
                                          # 'h_H'
                                          'ProfilAzimuthaux_HauteurListe': [''],
                                          # # Pour tracer toutes les coupes [''] sinon  [10, 30, 50, 70, 80, 90]
                                          'ProfilAzimuthaux_XVar': "azimuth",
                                          'ProfilAzimuthaux_YVar': ['Ps', 'Pta',
                                                                    'Ts', 'Tta',
                                                                    'beta'],
                                          'ProfilAzimuthaux_DeltaYVar': [],
                                          'ProfilAzimuthaux_CalculDisto': 0,
                                          'ProfilAzimuthaux_SuperpositionCas': 0,
                                          'ProfilAzimuthaux_SuperpositionPlan': 0,
                                          'ProfilAzimuthaux_SuperpositionHauteur': 0,
                                          }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_Polaire
DicoXYVarPolaire2Trace_defaut = {'VisuGeom_2trace': True,
                                 'Polaire_XYvar': [
                                     [('absbeta1', 'BA'), ('Mr', 'Inlet')],
                                     [('absbeta1', 'BA'),
                                      ('cd_fftro', ['Inlet', 'Outlet'])],
                                     [('absbeta1', 'BA'), ('absbeta2', 'BF')],
                                     [('Vx', 'BA'), ('Vx', 'BF')],
                                     ],
                                 'Polaire_Hauteur': '0.5',
                                 }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionParois
DicoXYVarEvolParois2Trace_defaut = {
    'EvolutionParois_Var': ['Ps', 'Ts', 'Tta', 'Vx', 'Ma'],
    'EvolutionParois_Hauteur': ["Moyeu", "Carter"],  # "Moyeu", "Carter"
    'EvolutionParois_Groupe': ["CFD", "BSAM"],
    }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionAxiale
DicoXYVarEvolAxiale2Trace_defaut = {
    'EvolutionAxiale_YVar': ['Ps', 'Ts', 'Tta', 'Vx', 'Ma', 'alpha', 'beta',
                             'beta1', 'absbeta1', 'beta2', 'absbeta2', 'phi',
                             'Vm', 'Pi', 'cd_fftro', 'Dev', 'PSIA', 'DLI',
                             'Tau', 'Mr2_Mr1_RAL', 'Ma2_Ma1_RAL '],
    'EvolutionAxiale_XVar': 'X',
    'EvolutionAxiale_PlanAmont': 'AmontPerfo',
    'EvolutionAxiale_PlanAval': 'AvalPerfo',
    'EvolutionAxiale_Hauteur': [0.2, 0.5, 0.8, ],
    'EvolutionAxiale_InterDir': 'q_Q'  # q_Q ou h_H
    }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionMeridienne
DicoXYVarEvolMeridienne2Trace_defaut = {
    'EvolutionMeridienne_YVar': ['Ps', 'Ts', 'Tta', 'Vx', 'Ma', 'alpha', 'beta',
                                 'beta1', 'absbeta1', 'beta2', 'absbeta2',
                                 'phi', 'Vm', 'Pi', 'cd_fftro', 'Dev', 'PSIA',
                                 'DLI', 'Tau', 'Mr2_Mr1_RAL', 'Ma2_Ma1_RAL '],
    'EvolutionMeridienne_XVar': 'X',
    'EvolutionMeridienne_PlanAmont': 'Inlet',
    'EvolutionMeridienne_PlanAval': '*',
    # Si '*' alors tous les plans en aval de la grille sont utlisé
    'EvolutionMeridienne_Hauteur': ["mean"],  # "mean" , 0.5
    }

# DICTIONNAIRES RELATIF A LA CLEF : Trace_ProfilsRadiaux_CL
DicoXYVarProfilsRadiauxInlet_defaut = {'VisuGeom_2trace': True,
                                       'GradPlanUnique_Plan': ['Inlet'],
                                       'GradPlanUnique_XVar': ['Pta', 'Tta',
                                                               'Vx', 'Vt',
                                                               'alpha', 'phi',
                                                               'TurbulentDissipation',
                                                               'TurbulentEnergyKinetic',
                                                               'Viscosity_EddyMolecularRatio'],
                                       'GradPlanUnique_Yvar': 'h_H',
                                       # h_H / Q_q / R
                                       }

DicoXYVarProfilsRadiauxOutlet_defaut = {'VisuGeom_2trace': True,
                                        'GradPlanUnique_Plan': ['Outlet'],
                                        'GradPlanUnique_XVar': ['Ps'],
                                        'GradPlanUnique_Yvar': 'h_H',
                                        # h_H / Q_q / R
                                        }

# -------------------------------------------------------------------------------------------------------------------
# PREFERENCE AFFICHAGE GRAPHE
DicoPrefGraphe_defaut = {"LegendSize": 15, "TailleTitreX": 16,
                         "TailleTicksX": 10, "TailleTitreY": 16,
                         "TailleTicksY": 10, "ShowCaseName": 0,
                         "ShowSecondGrid": 1, "ShowAverage": 0, "ShowLegend": 0,
                         "ShowFlux": 0}

# -------------------------------------------------------------------------------------------------------------------
# PREFERENCE NBRE GRAPHE PAR PAGE
DicoNbreGraphe_defaut = {'VisuGeomMeridienne': {'Nrow': 1, 'Ncol': 1},
                         'VisuGeomCoupe': {'Nrow': 1, 'Ncol': 1},
                         'VisuGeomAubage': {'Nrow': 1, 'Ncol': 1},
                         'VisuGeomBABF': {'Nrow': 2, 'Ncol': 3},
                         'VisuGeomCol3D': {'Nrow': 2, 'Ncol': 3},
                         'LoisGeom': {'Nrow': 1, 'Ncol': 2},
                         'LoisGeomVsCorde': {'Nrow': 1, 'Ncol': 1},
                         'LoisGeomVsCorde_Hauteur': {'Nrow': 1, 'Ncol': 1},
                         'Convergence': {'Nrow': 1, 'Ncol': 1},
                         'VisuPlanPost': {'Nrow': 1, 'Ncol': 1},
                         'Perfos0D': {'Nrow': 2, 'Ncol': 2},
                         'Perfos0DChamps': {'Nrow': 4, 'Ncol': 2},
                         'Polaire': {'Nrow': 1, 'Ncol': 2},
                         'GradPlanInlet': {'Nrow': 2, 'Ncol': 3},
                         'GradPlanOutlet': {'Nrow': 1, 'Ncol': 2},
                         'GradPlanUnique': {'Nrow': 1, 'Ncol': 3},
                         'GradPlanVsPlanRef': {'Nrow': 1, 'Ncol': 2},
                         'ProfilAzimuthaux': {'Nrow': 1, 'Ncol': 2},
                         'ProfilAzimuthauxSum': {'Nrow': 2, 'Ncol': 3},
                         'ProfilVsCorde': {'Nrow': 1, 'Ncol': 1},
                         'ProfilVsCordeSum': {'Nrow': 2, 'Ncol': 3},
                         'EvolutionParois': {'Nrow': 1, 'Ncol': 1},
                         'EvolutionAxiale': {'Nrow': 1, 'Ncol': 1},
                         'VisuCFD': {'Nrow': 1, 'Ncol': 1},
                         'VisuMESH': {'Nrow': 2, 'Ncol': 1},
                         }

# -------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DE CORRESPONDANCE DES LABELS ISSUENT DU BSAM
DicoCorrLabel_defaut = {'HDE': 'RDE',
                        'IGV': 'RDE',
                        'R': 'RM',
                        'S': 'RD',
                        'HR': 'RM',
                        'HS': 'RD',
                        'OGV': 'OGV',
                        }

# -------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DES FORMULES UTILISATEURS
DicoUserFormula_defaut = {
    'absbeta1': {'Var': 'beta1', 'Equation': 'abs(beta1)'},
    'absbeta2': {'Var': 'beta2', 'Equation': 'abs(beta2)'},
    'PisQcorr_ref_KD_ref': {'Var': 'Pi,Qcorr_ref_KD_ref',
                            'Equation': 'Pi/Qcorr_ref_KD_ref'},
    'Cambrure': {'Var': 'b2sqTo,b1sqTo', 'Equation': '-(b2sqTo-b1sqTo)'},
    }

# -------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DES COURBES UTILISATEURS
DicoUserCurves_defaut = {
    'Delta': {'X': [0, 0], 'Y': [0, 1], 'Couleur': 'Pink', 'Ligne': 'SolidLine',
              'Symbole': None, 'Epaisseur': 2},
    'DLI': {'X': [0.55, 0.55], 'Y': [0, 1], 'Couleur': 'Pink',
            'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'PSIA': {'X': [1.0, 1.0], 'Y': [0, 1], 'Couleur': 'Pink',
             'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'INCD': {'X': [0.0, 0.0], 'Y': [0, 1], 'Couleur': 'Pink',
             'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'EFP': {'X': [0.0, 0.0], 'Y': [0, 1], 'Couleur': 'Pink',
            'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'V2_V1_RAL': {'X': [0.7, 0.7], 'Y': [0, 1], 'Couleur': 'Pink',
                  'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'W2_W1_RAL': {'X': [0.65, 0.65], 'Y': [0, 1], 'Couleur': 'Pink',
                  'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    # 'mis3'      : {'X': [0.0,0.1]   , 'Y': [2.5,2.5] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
    'Marge': {'X': [3, 3], 'Y': [0, 1], 'Couleur': 'Pink', 'Ligne': 'SolidLine',
              'Symbole': None, 'Epaisseur': 2},
    }

# -------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE POUR LA MISE EN FORMES DES VARIABLES
DicoVariables_defaut = {
    'h_H': {'Nom': 'Hauteur Adimensionne', 'Unite': '[%]', 'NbreCS': 1,
            'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
            'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'h_H_norm': {'Nom': 'Hauteur Adimensionne', 'Unite': '[%]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
                 'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    '_h_H': {'Nom': 'Hauteur Adimensionne', 'Unite': '[%]', 'NbreCS': 1,
             'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
             'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'h_H_BA': {'Nom': 'Hauteur Adimensionne BA', 'Unite': '[%]', 'NbreCS': 1,
               'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
               'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'h_H_BF': {'Nom': 'Hauteur Adimensionne BF', 'Unite': '[%]', 'NbreCS': 1,
               'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
               'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'rBA_adim': {'Nom': 'Hauteur Adimensionne BA', 'Unite': '[%]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
                 'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'rBF_adim': {'Nom': 'Hauteur Adimensionne BF', 'Unite': '[%]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
                 'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'rMoyen_adim': {'Nom': 'Hauteur Adimensionne', 'Unite': '[%]', 'NbreCS': 1,
                    'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
                    'PGMax': 0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Numadim': {'Nom': 'Numero des grilles', 'Unite': '[-]', 'NbreCS': 1,
                'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.01,
                'PGMax': 0.99, 'limiteur': 5.0, 'Min': -0.05, 'Max': 1.05},
    'R': {'Nom': 'Rayon', 'Unite': '[m]', 'NbreCS': 1, 'FactMulti': 1,
          'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.01, 'PGMax': 0.99,
          'limiteur': 5.0, 'Min': 0.1, 'Max': 0.18},

    'b1sqTo': {'Nom': 'b1sqTo', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'b2sqTo': {'Nom': 'b2sqTo', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Calage': {'Nom': 'Calage', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Cambrure': {'Nom': 'Cambrure', 'Unite': '[Deg]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'Corde': {'Nom': 'Corde', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
              'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
              'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'CordeAxi': {'Nom': 'Corde Axiale', 'Unite': '[mm]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'ssc': {'Nom': 'Pas Relatif (S/C)', 'Unite': '[-]', 'NbreCS': 2,
            'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
            'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    's': {'Nom': 'Pas inter Aube (S)', 'Unite': '[mm]', 'NbreCS': 0,
          'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
          'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Emax': {'Nom': 'Emax', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'EmaxsC': {'Nom': 'Emax/C', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'XEmaxsC': {'Nom': 'XEmax/C', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
                'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'FmaxsC': {'Nom': 'Flechemax/C', 'Unite': '[-]', 'NbreCS': 2,
               'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
               'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
               'Max': 1.0},
    'XFmaxsC': {'Nom': 'XFlechemax/C', 'Unite': '[-]', 'NbreCS': 2,
                'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                'Max': 1.0},
    'XgCale': {'Nom': 'Xg', 'Unite': '[mm]', 'NbreCS': 1, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'YgCale': {'Nom': 'Yg', 'Unite': '[mm]', 'NbreCS': 1, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'xBa': {'Nom': 'X BA', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'xBf': {'Nom': 'X BA', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'yBa': {'Nom': 'Y BA', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'yBF': {'Nom': 'Y BF', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'sweep_BA': {'Nom': 'Sweep Meca - BA', 'Unite': '[Deg]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'sweep_BF': {'Nom': 'Sweep Meca - BF', 'Unite': '[Deg]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'dihedral_BA': {'Nom': 'Diedre Meca - BA', 'Unite': '[Deg]', 'NbreCS': 0,
                    'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                    'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                    'Max': 1.0},
    'dihedral_BF': {'Nom': 'Diedre Meca - BF', 'Unite': '[Deg]', 'NbreCS': 0,
                    'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                    'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                    'Max': 1.0},
    'ACol/S': {'Nom': 'ACol/S', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'ACol/AEntree': {'Nom': 'ACol/AEntree', 'Unite': '[-]', 'NbreCS': 3,
                     'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                     'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                     'Max': 1.0},
    'ASortie/ACol': {'Nom': 'ASortie/ACol', 'Unite': '[-]', 'NbreCS': 2,
                     'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                     'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                     'Max': 1.0},
    'SCol/SX': {'Nom': 'SCol/SX', 'Unite': '[-]', 'NbreCS': 1, 'FactMulti': 1,
                'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'XCol/CX': {'Nom': 'XCol/CX', 'Unite': '[-]', 'NbreCS': 0, 'FactMulti': 1,
                'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Mach Entree': {'Nom': 'Mach Entree', 'Unite': '[-]', 'NbreCS': 2,
                    'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                    'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                    'Max': 1.0},
    'Mach Sortie': {'Nom': 'Mach Sortie', 'Unite': '[-]', 'NbreCS': 2,
                    'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                    'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                    'Max': 1.0},

    'Qcorr': {'Nom': 'Debit reduit', 'Unite': '[-]', 'NbreCS': 2,
              'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.10,
              'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0, 'Max': 100.},
    'Qcorr_ref': {'Nom': 'Debit reduit Amont', 'Unite': '[-]', 'NbreCS': 2,
                  'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                  'PGMin': 0.10, 'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0,
                  'Max': 100.},
    'deltapctQcorr_ref': {'Nom': 'Delta Relatif Debit reduit Amont [%]',
                          'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
                          'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.10,
                          'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0,
                          'Max': 100.},
    'Qcorr_ref_KD': {'Nom': 'Debit reduit Amont*Kd', 'Unite': '[-]',
                     'NbreCS': 2, 'FactMulti': 1,
                     'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.10,
                     'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0, 'Max': 100.},
    'Qcorr_ref_KD_ref': {'Nom': 'Debit reduit Amont*Kd Amont', 'Unite': '[-]',
                         'NbreCS': 2, 'FactMulti': 1,
                         'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.10,
                         'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0,
                         'Max': 100.},
    'deltapctQcorr_ref_KD_ref': {
        'Nom': 'Delta Relatif Debit reduit Amont*Kd Amont [%]', 'Unite': '[-]',
        'NbreCS': 2, 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
        'PGMin': 0.10, 'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.0, 'Max': 100.},

    'etapol': {'Nom': 'Rendement', 'Unite': '[Point]', 'NbreCS': 3,
               'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
               'PGMin': 0.10, 'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.9,
               'Max': 1.0},
    'deltaetapol': {'Nom': 'Delta Absolu Rendement [Pt]', 'Unite': '[Point]',
                    'NbreCS': 3, 'FactMulti': 100,
                    'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.10,
                    'PGMax': 0.90, 'limiteur': 5.0, 'Min': 0.9, 'Max': 1.0},
    'cd_fftro': {'Nom': 'Cd fftro', 'Unite': '[-]', 'NbreCS': 3, 'FactMulti': 1,
                 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.05,
                 'PGMax': 0.95, 'limiteur': 5.0, 'Min': 0.0, 'Max': 0.20},
    'deltapctcd_fftro': {'Nom': 'Delta Relatif Cd [%]', 'Unite': '[-]',
                         'NbreCS': 2, 'FactMulti': 1,
                         'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.05,
                         'PGMax': 0.95, 'limiteur': 5.0, 'Min': 0.0,
                         'Max': 1.0},
    'Cd_MISES': {'Nom': 'Cd MISES', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
                 'autoScaleMode': 'Manuel', 'PGMin': 0.05, 'PGMax': 0.95,
                 'limiteur': 5.0, 'Min': 0.0, 'Max': 0.20},
    'Cd_shock_MISES': {'Nom': 'Cd Choc MISES', 'Unite': '[-]', 'NbreCS': 2,
                       'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.05,
                       'PGMax': 0.95, 'limiteur': 5.0, 'Min': 0.0, 'Max': 0.20},
    'Cd_visc_MISES': {'Nom': 'Cd Visq MISES', 'Unite': '[-]', 'NbreCS': 2,
                      'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.05,
                      'PGMax': 0.95, 'limiteur': 5.0, 'Min': 0.0, 'Max': 0.20},
    'Pi': {'Nom': 'Pi', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'deltapctPi': {'Nom': 'Delta Relatif Pi [%]', 'Unite': '[-]', 'NbreCS': 2,
                   'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                   'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                   'Max': 1.0},
    'PisD': {'Nom': 'Pi/D', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Dev': {'Nom': 'Deviation', 'Unite': '[Deg]', 'NbreCS': 1, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'W2_W1_RAL': {'Nom': 'Ralentisement relatif', 'Unite': '[-]', 'NbreCS': 1,
                  'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                  'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                  'Max': 1.0},
    'V2_V1_RAL': {'Nom': 'Ralentisement absolu', 'Unite': '[-]', 'NbreCS': 1,
                  'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                  'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                  'Max': 1.0},
    'RAL': {'Nom': 'Ralentisement absolu', 'Unite': '[m/s]', 'NbreCS': 1,
            'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
            'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'PSIA': {'Nom': 'PSIA', 'Unite': '[-]', 'NbreCS': 1, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'DLI': {'Nom': 'DLI', 'Unite': '[-]', 'NbreCS': 1, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Marge': {'Nom': 'Marge au blocage', 'Unite': '[%]', 'NbreCS': 1,
              'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
              'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},

    'Ps': {'Nom': 'Pression statique', 'Unite': '[Bar]', 'NbreCS': 1,
           'FactMulti': 0.00001, 'autoScaleMode': 'Mode P. Ginibre',
           'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
           'Max': 1.0},
    'Pta': {'Nom': 'Pression totale absolu', 'Unite': '[Bar]', 'NbreCS': 1,
            'FactMulti': 0.00001, 'autoScaleMode': 'Mode P. Ginibre',
            'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
            'Max': 1.0},
    'Ptr': {'Nom': 'Pression totale relative', 'Unite': '[Bar]', 'NbreCS': 1,
            'FactMulti': 0.00001, 'autoScaleMode': 'Mode P. Ginibre',
            'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
            'Max': 1.0},

    'Ts': {'Nom': 'Temperature statique', 'Unite': '[K]', 'NbreCS': 1,
           'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
           'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Tta': {'Nom': 'Temperature totale absolue', 'Unite': '[K]', 'NbreCS': 1,
            'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
            'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Ttr': {'Nom': 'Temperature totale relative', 'Unite': '[K]', 'NbreCS': 1,
            'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
            'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},

    'Vx': {'Nom': 'Vx', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Vy': {'Nom': 'Vy', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Vz': {'Nom': 'Vz', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Vm': {'Nom': 'Vm', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Vr': {'Nom': 'Vr', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Vt': {'Nom': 'Vt', 'Unite': '[m/s]', 'NbreCS': 0, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},

    'Mx': {'Nom': 'Mx', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Ma': {'Nom': 'Ma', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Mr': {'Nom': 'Mr', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},

    'alpha': {'Nom': 'Alpha', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
              'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
              'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'beta': {'Nom': 'Beta', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'phi': {'Nom': 'Phi', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
            'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'alpha1': {'Nom': 'Alpha1', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'alpha2': {'Nom': 'Alpha2', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
               'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
               'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'beta1': {'Nom': 'Beta1', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
              'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
              'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'beta2': {'Nom': 'Beta2', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
              'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
              'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'absbeta1': {'Nom': 'ABS(beta1)', 'Unite': '[Deg]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'absbeta2': {'Nom': 'ABS(beta2)', 'Unite': '[Deg]', 'NbreCS': 0,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'bsq1': {'Nom': 'BetaTo1', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'bsq2': {'Nom': 'BetaTo2', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'incd': {'Nom': 'INCD', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': -10.0, 'Max': 10.0},
    'INCD': {'Nom': 'INCD', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': -10.0, 'Max': 10.0},
    'efp': {'Nom': 'EFP', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
            'limiteur': 5.0, 'Min': -5.0, 'Max': 15.0},
    'EFP': {'Nom': 'EFP', 'Unite': '[Deg]', 'NbreCS': 0, 'FactMulti': 1,
            'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
            'limiteur': 5.0, 'Min': -5.0, 'Max': 15.0},

    'Viscosity_EddyMolecularRatio': {'Nom': 'Mut/Mu', 'Unite': '[-]',
                                     'NbreCS': 0, 'FactMulti': 1,
                                     'autoScaleMode': 'Mode P. Ginibre',
                                     'PGMin': 0.02, 'PGMax': 0.98,
                                     'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'TurbulentEnergyKinetic': {'Nom': 'Energie cinetique Turbulente',
                               'Unite': '[-]', 'NbreCS': 0, 'FactMulti': 1,
                               'autoScaleMode': 'Mode P. Ginibre',
                               'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0,
                               'Min': 0.0, 'Max': 1.0},
    'TurbulentDissipation': {'Nom': 'Dissipation Turbulente',
                             'Unite': '[*10^5]', 'NbreCS': 1,
                             'FactMulti': 0.00001,
                             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
                             'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                             'Max': 1.0},

    'BSQ': {'Nom': 'Pente squelette', 'Unite': '[Deg]', 'NbreCS': 0,
            'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
            'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'BSQS': {'Nom': 'Pente squelette simplifiee', 'Unite': '[Deg]', 'NbreCS': 0,
             'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
             'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'BSQ_adim': {'Nom': 'Pente squelette adim', 'Unite': '[-]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': None,
                 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'BSQS_adim': {'Nom': 'Pente squelette simplifiee adim', 'Unite': '[-]',
                  'NbreCS': 1, 'FactMulti': 1, 'autoScaleMode': 'Manuel',
                  'PGMin': None, 'PGMax': None, 'limiteur': 5.0, 'Min': 0.0,
                  'Max': 1.0},
    'PENTE_EXTRA': {'Nom': 'Pente squelette Extrados', 'Unite': '[Deg]',
                    'NbreCS': 0, 'FactMulti': 1,
                    'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                    'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'PENTE_INTRA': {'Nom': 'Pente squelette Intrados', 'Unite': '[Deg]',
                    'NbreCS': 0, 'FactMulti': 1,
                    'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                    'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'EPAI': {'Nom': 'Epaisseur', 'Unite': '[mm]', 'NbreCS': 0, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'EPAI_adim': {'Nom': 'Epaisseur adim', 'Unite': '[-]', 'NbreCS': 1,
                  'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': None,
                  'PGMax': None, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},

    'cordeRed_BA_BF_BA_RayCourbure': {'Nom': 'cordeRed_BA_BF_BA',
                                      'Unite': '[-]', 'NbreCS': 1,
                                      'FactMulti': 1, 'autoScaleMode': 'Manuel',
                                      'PGMin': None, 'PGMax': None,
                                      'limiteur': 5.0, 'Min': 0.0, 'Max': 2.0},
    'corde_Courbure': {'Nom': 'Corde', 'Unite': '[-]', 'NbreCS': 1,
                       'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                       'PGMin': None, 'PGMax': None, 'limiteur': 5.0,
                       'Min': 0.0, 'Max': 2.0},
    'RayonCourbure': {'Nom': 'Rayon de courbure', 'Unite': '[?]', 'NbreCS': 2,
                      'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': None,
                      'PGMax': None, 'limiteur': 5.0, 'Min': 1.4, 'Max': 1.6},
    'Courbure': {'Nom': 'Courbure', 'Unite': '[?]', 'NbreCS': 2, 'FactMulti': 1,
                 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None,
                 'PGMax': None, 'limiteur': 5.0, 'Min': 1.4, 'Max': 1.6},

    'X': {'Nom': 'X', 'Unite': '[m]', 'NbreCS': 1, 'FactMulti': 1,
          'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
          'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Y': {'Nom': 'Y', 'Unite': '[m]', 'NbreCS': 1, 'FactMulti': 1,
          'autoScaleMode': 'Mode P. Ginibre', 'PGMin': None, 'PGMax': None,
          'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'cordeRed': {'Nom': 'Corde BA->BF', 'Unite': '[-]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.02,
                 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Corde BA->BF': {'Nom': 'Corde BA->BF', 'Unite': '[-]', 'NbreCS': 1,
                     'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.02,
                     'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'Corde_BA_BF': {'Nom': 'Corde BA->BF', 'Unite': '[-]', 'NbreCS': 1,
                    'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.02,
                    'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'd_D': {'Nom': 'Abscisse Curviligne Adimensionne', 'Unite': '[-]',
            'NbreCS': 1, 'FactMulti': 1, 'autoScaleMode': 'Manuel',
            'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
            'Max': 1.0},
    'hi': {'Nom': 'Facteur de Forme', 'Unite': '[-]', 'NbreCS': 1,
           'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
           'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'mis3': {'Nom': 'MachIs', 'Unite': '[-]', 'NbreCS': 1, 'FactMulti': 1,
             'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02, 'PGMax': 0.98,
             'limiteur': 5.0, 'Min': 0.0, 'Max': 1.0},
    'mis3_max': {'Nom': 'MachIs_Max', 'Unite': '[-]', 'NbreCS': 1,
                 'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                 'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                 'Max': 1.0},
    'd_D_aero_max(mis3)': {'Nom': 'X_MachIs_Max', 'Unite': '[-]', 'NbreCS': 1,
                           'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                           'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0,
                           'Min': 0.0, 'Max': 1.0},
    'mis3_max/M2': {'Nom': 'MachIs_Max/MachIs_BF', 'Unite': '[-]', 'NbreCS': 1,
                    'FactMulti': 1, 'autoScaleMode': 'Mode P. Ginibre',
                    'PGMin': 0.02, 'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                    'Max': 1.0},

    'KD': {'Nom': 'KD', 'Unite': '[-]', 'NbreCS': 2, 'FactMulti': 1,
           'autoScaleMode': 'Manuel', 'PGMin': 0.02, 'PGMax': 0.98,
           'limiteur': 5.0, 'Min': 0.8, 'Max': 1.0},
    'KD_Meridien': {'Nom': 'KD_Meridien', 'Unite': '[-]', 'NbreCS': 2,
                    'FactMulti': 1, 'autoScaleMode': 'Manuel', 'PGMin': 0.02,
                    'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.8, 'Max': 1.0},

    'XNR': {'Nom': 'Regime reduit', 'Unite': '[-]', 'NbreCS': 0,
            'FactMulti': -1, 'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
            'PGMax': 0.98, 'limiteur': 5.0, 'Min': 200, 'Max': 1500},
    }

ModeMises = globals().get('ModeMises', False)
ModeChamps = globals().get('ModeChamps', False)
DicoXYVarLoisGeom = globals().get('DicoXYVarLoisGeom', DicoXYVarLoisGeom_defaut)
if ModeChamps:
    DicoXYVarPerfos0D2Trace = globals().get('DicoXYVarPerfos0D2Trace_Champs',
                                            DicoXYVarPerfos0D2Trace_Champs_defaut)
else:
    DicoXYVarPerfos0D2Trace = globals().get('DicoXYVarPerfos0D2Trace',
                                            DicoXYVarPerfos0D2Trace_defaut)
if ModeMises:
    DicoXYVarProfilsRadiaux2Trace = globals().get(
        'DicoXYVarProfilsRadiaux2Trace_Mises',
        DicoXYVarProfilsRadiaux2Trace_Mises_defaut)
elif ModeChamps:
    DicoXYVarProfilsRadiaux2Trace = globals().get(
        'DicoXYVarProfilsRadiaux2Trace_Champs',
        DicoXYVarProfilsRadiaux2Trace_Champs_defaut)
else:
    DicoXYVarProfilsRadiaux2Trace = globals().get(
        'DicoXYVarProfilsRadiaux2Trace', DicoXYVarProfilsRadiaux2Trace_defaut)
DicoXYVarProfilsRadiauxAngle2Trace = globals().get(
    'DicoXYVarProfilsRadiauxAngle2Trace',
    DicoXYVarProfilsRadiauxAngle2Trace_defaut)
DicoXYVarProfilVsCorde2Trace = globals().get('DicoXYVarProfilVsCorde2Trace',
                                             DicoXYVarProfilVsCorde2Trace_defaut)
DicoXYVarProfilAzimuthaux2Trace = globals().get(
    'DicoXYVarProfilAzimuthaux2Trace', DicoXYVarProfilAzimuthaux2Trace_defaut)
DicoXYVarPolaire2Trace = globals().get('DicoXYVarPolaire2Trace',
                                       DicoXYVarPolaire2Trace_defaut)
DicoXYVarEvolParois2Trace = globals().get('DicoXYVarEvolParois2Trace',
                                          DicoXYVarEvolParois2Trace_defaut)
DicoXYVarEvolAxiale2Trace = globals().get('DicoXYVarEvolAxiale2Trace',
                                          DicoXYVarEvolAxiale2Trace_defaut)
DicoXYVarEvolMeridienne2Trace = globals().get('DicoXYVarEvolMeridienne2Trace',
                                              DicoXYVarEvolMeridienne2Trace_defaut)
DicoXYVarProfilsRadiauxInlet = globals().get('DicoXYVarProfilsRadiauxInlet',
                                             DicoXYVarProfilsRadiauxInlet_defaut)
DicoXYVarProfilsRadiauxOutlet = globals().get('DicoXYVarProfilsRadiauxOutlet',
                                              DicoXYVarProfilsRadiauxOutlet_defaut)
DicoPrefGraphe = globals().get('DicoPrefGraphe', DicoPrefGraphe_defaut)
DicoNbreGraphe = globals().get('DicoNbreGraphe', DicoNbreGraphe_defaut)
DicoCorrLabel = globals().get('DicoCorrLabel', DicoCorrLabel_defaut)
DicoUserFormula = globals().get('DicoUserFormula', DicoUserFormula_defaut)
DicoUserCurves = globals().get('DicoUserCurves', DicoUserCurves_defaut)
DicoVariables = globals().get('DicoVariables', DicoVariables_defaut)
VarForOnlyCFDCase = ['TurbulentDissipation', 'TurbulentEnergyKinetic',
                     'Viscosity_EddyMolecularRatio']

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
#                                                   SCRIPT
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

'''
A FAIRE/CORRIGER
    - Probleme recurrent avec le calcul de la Marge --> Redmine a faire
        --> Faire une demande d'evolution pour voir si on peut calculer la marge directement dans le fichier Angle.
    - Retouner aube GCOLTER --> Detection automatique des aubes extrados vers le bas (quid des cas multi-aubages)
    - Tracer la meme variable mais sur des plans differents dans un meme graphe
    - Corriger le probleme du Nom de grille lors de l'import CARMA (Nom de l'utilisateur = nom grille BSAM)
            Le label des grilles est recupere automatiquement par la fonction suivante : DataManager.py : gridBSAM,dic = caseParametersCase.getBlades()
            Le meridien qui est utlisé est soit celui contenu dans le rertoire Geom/GOUX ou sinon celui defini pour le KD si il y en a un.
    - Ajouter une fonction d'import CasBSAM --> disponible a partir de la version V94 de GenepiAuto
    - Attention a la correspondance des coupes quand on combine des aubes n'ayant par le meme nombre de coupes. (#89305)
            --> Possibilité de passer par les coupes de dessin, mais cela n'est pas tres intuitif
    - ImportCARMAAuto ne fonctionne pas dans le cas Post Antares Co --> Redmine fait (#96150) --> Fait en CoDev
    - rajouter un garde fou sur le type de ligne (clef "Ligne") pour les tracés car si ligne = None alors pas de trace de gradient ou de Machis
    - pour le tracé des perfos, il faut rajouter la position des plans utlisé dans la legende
    - Trace_InfosPlanUtilisateur : faire un redmine pour ne pas afficher tous les cas de l'iso
    - PB avec l'echelle automatique (Mode P.Ginibre) dans les graphes de comparaison (delta)
    - PB avec l'organisation des tableaux (correspondance plan utlisateur et perfos0D) par page. limitation a 2 tableau max --> Redmine a faire
    - Rajouter une fonction pour detecter si on a acces au reseau SAE --> Fait a partir de la V107
    - Rajouter la possibilité de sauvegarder le carma.trac dans le cas cannelle afin d'eviter de relancer l'execution a chaque fois (#96435)
    - PB avec l'export du graphique Col3D pour la partie geometrique CARMA --> fait a partir de la V99
    - La detection du cas le plus proche BSAM, n'est pas fonctionnelle avec le graphique de type AngleBABF --> (#96705) --> Fait en CoDev
    - Graphe "Vue aubage" & "ZoomBABF" : probleme avec le filtre pour les grilles a tracer
    - Graphe "LoiGeometrique" : le renommage des axes ne s'effectue pas correctement
    - PB avec le nom des onglets du fichier Excel : C:\Appl\GENEPI\TEST\V2.95\GENEPI\modules\PySNPresentation\API_openpyxl\API_openpyxl.py  (def writeSheet(self, workbook, graph):)
    - Perfos0D: Ajout de la methode du point de comparaison (Auto/isoDstd1/isoDstd2/isoPiD) --> Disponible uniquement avec la version TEST de GENEPI --> disponible a partir de la version V94 de GenepiAuto
    - Mettre a jour les script CARMA Gcolter pour la prise en compte des fichiers XML.
    - Rajouter une correction dans le fichier "C:\Appl\GENEPI\DEV\GENEPI\src\DataManager\Common\Col3D.py" pour le traitement des resultats de type -1#NQB
    - PB avec la variable h_H_norm lorsqu'on veut tracer la variable Marge
    - Pouvoir definir un renommage des plan propre a chaque cas --> fait a partir de la V99
    - Pouvoir lister automatiquement les coupes disponibles dans un cas MISES --> fait a partir de la V107
    - Detecter automatiquement les aubes contenues dans les cas CFD --> fait a partir de la V109
    - Tracer le profil radial de MachIs Max
'''

# ===============================================================================
#   DICTIONNAIRES
# ===============================================================================

RenommagePlan_CFD = {"AmontPerfo": [PlanCFD_AmontPerfo],
                     "AvalPerfo": [PlanCFD_AvalPerfo],
                     "LoinBA": [PlanCFD_LoinBA],
                     "LoinBF": [PlanCFD_LoinBF],
                     "ProcheBA": [PlanCFD_ProcheBA],
                     "ProcheBF": [PlanCFD_ProcheBF]}

RenommagePlan_BSAM = {"AmontPerfo": [PlanBSAM_AmontPerfo],
                      "AvalPerfo": [PlanBSAM_AvalPerfo],
                      "LoinBA": [PlanBSAM_LoinBA],
                      "LoinBF": [PlanBSAM_LoinBF],
                      "ProcheBA": [PlanBSAM_ProcheBA],
                      "ProcheBF": [PlanBSAM_ProcheBF]}


# ===============================================================================
#   CLASSES
# ===============================================================================

class bsam:
    def __init__(self):
        self.NPL = [0, 0,
                    0]  # NPL  (1, 2 ET 3) : NOMBRE DE PLANS DES TOTAL, PRIMAIRE ET SECONDAIRE
        self.NLG = [0, 0,
                    0]  # NLG  (1, 2 ET 3) : NOMBRE DE LIGNES DE COURANT DANS LE TOTAL, DANS LE PRIMAIRE ET DANS LE SECONDAIRE
        self.NGRID = [0, 0, 0,
                      0]  # NGRID(1, 2 ET 3) : NOMBRE DE GRILLES DES TOTAL, PRIMAIRE ET SECONDAIRE, NOMBRE DE GRILLES
        self.noms_grille = []
        self.BIFLUX = False
        self.NFLUX = 1
        self.LAMBDA = 0.0
        self.QDEB = []


class grille:
    def __init__(self):
        self.label = ""
        self.zaube = 0
        self.omeg = 0.0


# ===============================================================================
#   FONCTIONS
# ===============================================================================

def ConvertSecondToTime(N):
    return time.strftime("%Hh:%Mm:%Ss", time.gmtime(N))


def ConnexionStatus():
    from env.config import get_env
    try:
        if get_env() == 'SAB':
            data_dir = "DATA"
        else:
            data_dir = "data"

        ftpclient.fileconfigure(
            os.path.abspath(os.environ["ConfigIniCannelle"]),
            {"HOME": r".\GENEPI\modules\ftpclient", "DATA_DIR": data_dir})
        ftpclient.connect()
        Connexion_status = True
        print("connexion OK FTP")
    except:
        Connexion_status = False
        print("connexion au FTP de cannelle impossible !")
    return Connexion_status


def RenameLabel2GENEPI(ListLabel=[],
                       DicoCorrLabel={'IGV': 'RDE', 'R': 'RM', 'S': 'RD',
                                      'HR': 'RM', 'HS': 'RD'}, iPrint=False):
    # Fonction qui permet de renommer les labels de facon a avoir des labels coherents entre tous les CAS CFD & BSAM
    # En sortie on obtient une liste de la forme [ 'RDE','RM1','RD1','RM2','RD2','.....,'OGV']

    ListLabel_Genepi = []
    for Label in ListLabel:
        if Label != None:
            Letters = Label.rstrip(string.digits)
            Digits = Label.strip(string.ascii_letters)
            Digits = Digits.rstrip(string.ascii_letters)
            if Label in DicoCorrLabel.keys():
                ListLabel_Genepi.append(DicoCorrLabel[Label])
            elif Letters in DicoCorrLabel.keys():
                if Digits != '':
                    ListLabel_Genepi.append(
                        "%s%s" % (DicoCorrLabel[Letters], int(Digits)))
                else:
                    ListLabel_Genepi.append("%s" % (DicoCorrLabel[Letters]))
            else:
                if Digits != '':
                    ListLabel_Genepi.append("%s%s" % (Letters, int(Digits)))
                else:
                    ListLabel_Genepi.append("%s" % (Letters))

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : RenameLabel2GENEPI")
        print("                           * ENTREE : %s" % ListLabel)
        print("                           * SORTIE : %s" % ListLabel_Genepi)
        print(
            " --------------------------------------------------------------- \n")

    return ListLabel_Genepi


def CreateListLabelRenommage(DicoLabelCFD={}, ListLabelBSAM=[],
                             DataType="Gradients_Complets", iPrint=False):
    # Fonction qui permet a partir des labels recuperé dans chaque cas de generer les listes au bon format pour les donner a la fonction renommage de GENEPI.
    # Renommage CFD : [("1.01","RM1"),("1.02","RD1")]
    # Renommage BSAM : [("IGV","RDE"),("R1","RM1"),.....]

    # LISTE LABEL CFD
    ListFlux = ['Total', 'Primaire', 'Secondaire']
    RenommageLabel_CFD = []
    ListLabelCFDGENEPI = []
    if DicoLabelCFD != {}:
        for Flux in ListFlux:
            LabelFlux = DicoLabelCFD.get(Flux, [])
            if LabelFlux != []:
                print(f"LabelFlux = {LabelFlux}")
                ListLabelCFDGENEPI = RenameLabel2GENEPI(LabelFlux,
                                                        DicoCorrLabel)
                for NumRoue in range(0, len(ListLabelCFDGENEPI)):
                    if Flux == "Total": RenommageLabel_CFD.append(("1.%.2d" % (
                                NumRoue + 1), "%s" % ListLabelCFDGENEPI[
                                                                       NumRoue]))
                    if Flux == "Primaire": RenommageLabel_CFD.append((
                                                                     "3.%.2d" % (
                                                                                 NumRoue + 1),
                                                                     "%s" %
                                                                     ListLabelCFDGENEPI[
                                                                         NumRoue]))
                    if Flux == "Secondaire": RenommageLabel_CFD.append((
                                                                       "2.%.2d" % (
                                                                                   NumRoue + 1),
                                                                       "%s" %
                                                                       ListLabelCFDGENEPI[
                                                                           NumRoue]))

    # LISTE LABEL BSAM
    ListLabelBSAMGENEPI = RenameLabel2GENEPI(ListLabelBSAM, DicoCorrLabel)
    RenommageLabel_BSAM = []
    for NumRoue in range(0, len(ListLabelBSAM)):
        RenommageLabel_BSAM.append(("%s" % ListLabelBSAM[NumRoue],
                                    "%s" % ListLabelBSAMGENEPI[NumRoue]))

    RenomListConvert_CFD = [[], [], [], []]
    for Tuple in RenommageLabel_CFD:
        RenomListConvert_CFD[0].append(Tuple[0])
        RenomListConvert_CFD[1].append(Tuple[1])
        if len(Tuple) >= 3:
            RenomListConvert_CFD[2].append(Tuple[2])
        else:
            RenomListConvert_CFD[2].append("")
        if len(Tuple) >= 4:
            RenomListConvert_CFD[3].append(Tuple[3])
        else:
            RenomListConvert_CFD[3].append("")

    RenomListConvert_BSAM = [[], [], [], []]
    for Tuple in RenommageLabel_BSAM:
        RenomListConvert_BSAM[0].append(Tuple[0])
        RenomListConvert_BSAM[1].append(Tuple[1])
        if len(Tuple) >= 3:
            RenomListConvert_BSAM[2].append(Tuple[2])
        else:
            RenomListConvert_BSAM[2].append("")
        if len(Tuple) >= 4:
            RenomListConvert_BSAM[3].append(Tuple[3])
        else:
            RenomListConvert_BSAM[3].append("")

    # if DataType == "Post Antares Co":
    # RenomListConvert_CFD = RenomListConvert_BSAM

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateListLabelRenommage")
        print("                           * LabelCFD : %s" % DicoLabelCFD)
        print(
            "                           * LabelCFD_Genepi : %s" % ListLabelCFDGENEPI)
        print(
            "                           * RenommageLabel_CFD : %s" % RenomListConvert_CFD)
        print("                           * LabelBSAM : %s" % ListLabelBSAM)
        print(
            "                           * LabelBSAM_Genepi : %s" % ListLabelBSAMGENEPI)
        print(
            "                           * RenommageLabel_BSAM : %s" % RenomListConvert_BSAM)
        print(
            " --------------------------------------------------------------- \n")

    return RenomListConvert_CFD, RenomListConvert_BSAM


def SetPageProperties(Page, Orientation="paysage", Nrow=2, Ncol=3,
                      ShowLegend=AfficherLegende, iPrint=False):
    Page.orientation = Orientation
    Page.nrow = Nrow
    Page.ncol = Ncol
    Page.showEntete = 0
    Page.pageLegend = ShowLegend

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : SetPageProperties ")
        print("                           * Orientation : %s" % Orientation)
        print("                           * Nrow : %s" % Nrow)
        print("                           * Ncol : %s" % Ncol)
        print("                           * ShowLegend : %s" % ShowLegend)
        print(
            " --------------------------------------------------------------- \n")


def IsRotorOrStator(Label, ListLabelStator=[], iPrint=False):
    if Label in ListLabelStator:
        LabelType = 'STATOR'
    else:
        LabelType = 'ROTOR'

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : IsRotorOrStator")
        print("                           * LabelType : %s" % LabelType)
        print(
            " --------------------------------------------------------------- \n")

    return LabelType


def IsVarInDicoVariables(Var, Dico={}, iPrint=False):
    if not Var in Dico.keys():
        Dico.update({Var: {'Nom': Var, 'Unite': '', 'NbreCS': 1, 'FactMulti': 1,
                           'autoScaleMode': 'Mode P. Ginibre', 'PGMin': 0.02,
                           'PGMax': 0.98, 'limiteur': 5.0, 'Min': 0.0,
                           'Max': 1.0}})

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : IsVarInDicoVariables")
        print("                           * Dico : %s" % Dico)
        print(
            " --------------------------------------------------------------- \n")

    return Dico


def SortGridComp(ListGrid, DicoGrid, iPrint=False):
    '''
    # D:\codes\GENEPI\CURRENT\GENEPI\src\DataManager\nS3DCase\Case.py
    # def sortGridTurbine(self):
    '''

    ListGridSorted = []
    pos = []

    for Index in range(len(ListGrid)):
        AubeName = ListGrid[Index]
        AubeEmp = DicoGrid[Index][0][5]

        insert = False
        for index, posloc in enumerate(pos):
            if posloc > AubeEmp:
                pos.insert(index, AubeEmp)
                ListGridSorted.insert(index, AubeName)
                insert = True
                break
        if not insert:
            pos.append(AubeEmp)
            ListGridSorted.append(AubeName)

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : SortGridComp")
        print("                           * ENTREE : %s" % ListGrid)
        print("                           * SORTIE : %s" % ListGridSorted)
        print(
            " --------------------------------------------------------------- \n")

    return ListGridSorted


def ReadGoux(bsamFile, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : ReadGoux")

    # Ouverture du fichier Bsam
    #
    file = open(bsamFile, 'r')
    gouxLines = file.readlines()
    file.close()

    res_goux = bsam()
    col = 13
    indiceLigne = 0
    #
    # LECTURE DES VARIABLES GENERALES DU CALCUL
    #
    # nbre plans meridien
    indiceLigne = indiceLigne + 1
    res_goux.NPL[0] = int(gouxLines[indiceLigne].strip().split()[0])
    res_goux.NPL[1] = int(gouxLines[indiceLigne].strip().split()[1])
    res_goux.NPL[2] = int(gouxLines[indiceLigne].strip().split()[2])
    # nbre lignes de courants
    indiceLigne = indiceLigne + 1
    res_goux.NLG[0] = int(gouxLines[indiceLigne].strip().split()[0])
    res_goux.NLG[1] = int(gouxLines[indiceLigne].strip().split()[1]) - 1
    if (res_goux.NLG[1] < 0): res_goux.NLG[1] = 0
    res_goux.NLG[2] = res_goux.NLG[0] - res_goux.NLG[1]
    # nbre grilles
    indiceLigne = indiceLigne + 1
    res_goux.NGRID[0] = int(gouxLines[indiceLigne].strip().split()[0])
    res_goux.NGRID[1] = int(gouxLines[indiceLigne].strip().split()[1])
    res_goux.NGRID[2] = int(gouxLines[indiceLigne].strip().split()[2])
    res_goux.NGRID[3] = res_goux.NGRID[0] + res_goux.NGRID[1] + res_goux.NGRID[
        2]
    # nbre de flux
    indiceLigne = indiceLigne + 1
    res_goux.NFLUX = 3
    if res_goux.LAMBDA <= 0.0:
        res_goux.NFLUX = 1
    if res_goux.NFLUX > 1:
        res_goux.BIFLUX = True
    if not (res_goux.BIFLUX):
        res_goux.NLG[2] = 0

    # QDEB les valeurs sont ecrites sur plusieurs lignes mais 6 valeurs par ligne
    nbLignes = int(res_goux.NLG[0] / 6)
    if nbLignes * 6 < res_goux.NLG[0]:
        nbLignes = nbLignes + 1
    for iligne in range(nbLignes):
        indiceLigne = indiceLigne + 1
        for val in gouxLines[indiceLigne].strip().split():
            res_goux.QDEB.append(float(val))

    for indGrille in range(res_goux.NGRID[3]):
        indiceLigne = indiceLigne + 1
        res_goux.noms_grille.append(grille())
        res_goux.noms_grille[indGrille].label = str(
            gouxLines[indiceLigne].strip().split()[0])
        indiceLigne = indiceLigne + 1
        res_goux.noms_grille[indGrille].zaube = float(
            gouxLines[indiceLigne][0 * col:1 * col].strip())
        res_goux.noms_grille[indGrille].omeg = float(
            gouxLines[indiceLigne][1 * col:2 * col].strip())
        indiceLigne = indiceLigne + 8

    return res_goux


def ConvertDicoToList(dico, iPrint=False):
    list = []
    for key in dico.keys():
        for elem in dico[key]:
            list.append(elem)
    return list


def isMisesCase(case_path):
    if os.path.exists(case_path):
        case_info_file = glob.glob(case_path.replace('\\', '/') + '/case_info*')
        if len(case_info_file) != 0:
            return True
        else:
            return False


def GetDicoInfoAube(CaseName="", iPrint=False):
    listCaseName = ftpclient.getListCalc(CaseName)
    # listCaseName = ftpclient.listall(CaseName)

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : GetDicoInfoAube")
        print("                     * CaseName : %s " % (CaseName))
        print("                     * listCaseName : %s " % (listCaseName))

    DicoInfoAube = {}
    for cas in listCaseName:
        caseParametersCase = caseParameters()
        caseParametersCase.case = cas
        caseParametersCase.initTablesID(
            os.path.abspath(os.environ["ConfigIniCannelle"]))
        AllGridCFD, DicoAllGridCFD = caseParametersCase.getBlades()
        ListAllGridCFDSorted = SortGridComp(AllGridCFD, DicoAllGridCFD)
        ListAllGridCFDSortedGENEPI = RenameLabel2GENEPI(ListAllGridCFDSorted,
                                                        DicoCorrLabel)
        DicoInfoAube = {}
        for index, gridName in enumerate(ListAllGridCFDSortedGENEPI):
            Aube = DicoAllGridCFD[index][0]
            if gridName not in DicoInfoAube.keys():
                DicoInfoAube[gridName] = {}
                DicoInfoAube[gridName]["Projet"] = Aube[0]
                DicoInfoAube[gridName]["Aube"] = Aube[2]
                DicoInfoAube[gridName]["TypeCoupe"] = Aube[3]
                DicoInfoAube[gridName]["Emp"] = Aube[5]
                DicoInfoAube[gridName]["Version"] = Aube[1]
                DicoInfoAube[gridName]["InverserY"] = Aube[4]
                DicoInfoAube[gridName]["Calage"] = Aube[6]
                DicoInfoAube[gridName]["NbAube"] = Aube[7]

    if iPrint:
        for Key in DicoInfoAube.keys():
            print("                           * %s : %s " % (
            Key, DicoInfoAube[Key]))
        print(
            " ------------------------------------------------------------- \n")

    return DicoInfoAube


def AddFormula(Dico={}, iPrint=False):
    for Key in Dico.keys():
        VarList = []
        VarList.append(Dico[Key]['Var'])
        UserFormula().addFormula(Key, VarList, Dico[Key]['Equation'])

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : AddFormula")


def AddUserCurves(Dico={}, iPrint=False):
    for Key in Dico.keys():
        App.UserCurvesDefinition.AddCurve(Key, Dico[Key]['X'], Dico[Key]['Y'])
        Curve = App.UserCurvesDefinition.getCurveByName(Key)
        Curve.setCurvePropertieBatch(Dico[Key])

    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : AddUserCurves")


def AddCFDCase(CFDCase="", SetIso=1, TrierIso=1, Dico={},
               DataType="Gradients_Complets", RecalageKDVar=0, iPrint=False):
    CFDCase = CFDCase.replace('\\', '/')

    PostAntaresDir = 'postAntares'
    PostAnNADir = 'postAnNA'

    if "\\" in CFDCase or "/" in CFDCase:
        IsCFDCasePath = True
    else:
        IsCFDCasePath = False

    # On detecte si c'est un cas MISES
    IsMisesCase = isMisesCase(CFDCase)

    MisesDetectionCoupeAuto = Dico.get("MisesDetectionCoupeAuto", 0)

    # On doit recuperer de la variable CFDCase le chemin et le nom du cas
    CFDCasePath = CFDCase
    CFDCaseName = CFDCase
    DicoInfoAube = {}
    listBSAM = []
    if ConnexionStatus and not IsMisesCase:
        if IsCFDCasePath:
            # On connait le chemin donc on recherche le nom du cas pour ensuite recuper les infos dans le BDD cannelle
            if 'case_' in CFDCase and 'post' in CFDCase:
                casename = ''
                i = 0
                while 'case_' not in casename and i <= len(
                        CFDCase.split('/')) - 1:
                    casename = CFDCase.split('/')[i]
                    i += 1
                CFDCase = casename
                CFDCaseName = casename

        # On recupere le nom des aubes
        DicoInfoAube = GetDicoInfoAube(CFDCaseName)

        # On recupere le nom du BSAM si il n'est pas definie dans la mise en donnee
        listBSAM_BDD = [""]

        listCFDCase = ftpclient.getListCalc(CFDCaseName)
        # listCFDCase = ftpclient.listall(CFDCaseName)

        for index, cas in enumerate(listCFDCase):
            # ~\GENEPI\modules\CaseReport\CaseReport.py
            if index == 0:
                # On recupere le chemin du cas cannelle, on va jusqu'au repertoire amont du dossier post
                CFDCasePath = ftpclient.getCasePath(cas)
                # Path = ftpclient.ftp._get_case_path(cas)
                # CasePath = os.path.join('//data/', Path, cas, 'post')
                if os.path.basename(CFDCasePath) == 'post':
                    CFDCasePath = os.path.dirname(CFDCasePath)

                # On recupere le chemin vers le bsam du cas cannelle
                caseParametersCase = caseParameters()
                caseParametersCase.case = cas
                caseParametersCase.initTablesID(
                    os.path.abspath(os.environ["ConfigIniCannelle"]))
                caseParametersCase.getFluidModel(["bsamfile"])
                if caseParametersCase.fluidModel["bsamfile"]:
                    if caseParametersCase.fluidModel["bsamfile"][
                        0] not in listBSAM_BDD:
                        listBSAM_BDD.append(
                            caseParametersCase.fluidModel["bsamfile"][0])

                # On reucpere le label des aubes contenues dans le cas cannelle
                AllGridCFD, DicoAllGridCFD = caseParametersCase.getBlades()
                DefinitionImportCarmaBatch = []
                for index, gridName in enumerate(AllGridCFD):
                    Aube = DicoAllGridCFD[index][0]
                    DicoInfo = {}
                    DicoInfo["Projet"] = Aube[0]
                    DicoInfo["Aube"] = Aube[2]
                    DicoInfo["TypeCoupe"] = Aube[3]
                    DicoInfo["nom"] = gridName
                    DicoInfo["Emp"] = Aube[5]
                    DicoInfo["Version"] = Aube[1]
                    DicoInfo["InverserY"] = Aube[4]
                    DicoInfo["Calage"] = Aube[6]
                    DicoInfo["NbAube"] = Aube[7]
                    DefinitionImportCarmaBatch.append(DicoInfo)

                # On deifnit le liaison vers le cas carma importé en batch
                Dico['LiaisonCasCarma'] = Dico.get("TitreCas",
                                                   "TitreCas") + "_" + Aube[
                                              0] + "_" + Aube[1] + "_" + Aube[2]

                # Si c'est un chemin alors on le conserve, sinon on fait appel au serveur cannelle pour le retrouver
                # if IsCFDCasePath:
                # CasePath = CFDCase
                # else:
                # Path = ftpclient.ftp._get_case_path(cas)
                # CasePath = os.path.join('//data/', Path, cas, 'post')
                break

        listBSAM = [Dico.get("CheminBsam", listBSAM_BDD[0])]
    else:
        # On n'a pas acces a la BDD cannelle ou on traite un cas MISES
        if IsMisesCase or IsCFDCasePath:
            CFDCasePath = CFDCase
        else:
            CFDCasePath = Dico.get("CheminCas", "CAS")

        if IsCFDCasePath:
            if os.path.basename(
                CFDCasePath) == 'post': CFDCasePath = os.path.dirname(
                CFDCasePath)
            listBSAM = [Dico.get("CheminBsam", "")]

    if iPrint:
        print(
            "\n                ---------------------------------------------------------------")
        print("                -> def : AddCFDCase")
        print("                    -  ConnexionStatus = %s" % ConnexionStatus)
        print("                    -  CFDCase = %s" % CFDCase)
        print("                    -  CFDCaseName = %s" % CFDCaseName)
        print("                    -  CFDCasePath = %s" % CFDCasePath)
        print("                    -  IsCFDCasePath = %s" % IsCFDCasePath)
        print(
            "                    -  MisesDetectionCoupeAuto = %s" % MisesDetectionCoupeAuto)
        print("                    -  IsMisesCase = %s" % IsMisesCase)
        print("                    -  listBSAM = %s" % listBSAM)

    if len(listBSAM) == 0 and ConnexionStatus:
        print("\n     --> INFO CAS CFD (%s) : %s   (%s / %s)" % (
        DataType, CFDCase, Dico.get("Couleur", "Black"),
        Dico.get("Ligne", "SolidLine")))
        print(
            "\n               WARNING !!!! LE CAS N'EXISTE PAS --> ON PASSE AU CAS CFD SUIVANT")
        Case2Add = False
    else:
        if len(listBSAM) == 0:
            print("\n     --> INFO CAS CFD (%s) : %s   (%s / %s)" % (
            DataType, CFDCase, Dico.get("Couleur", "Black"),
            Dico.get("Ligne", "SolidLine")))
            print(
                "\n               WARNING !!!! LE CAS N'EXISTE PAS --> ON PASSE AU CAS CFD SUIVANT")
            Case2Add = False
        else:
            bsamPath = listBSAM[0]
            BsamName = os.path.basename(bsamPath)

            if not os.path.isfile(bsamPath):
                if ConnexionStatus:
                    print(
                        "\n               WARNING !!!! LE FICHIER BSAM (%s) N'EXISTE PAS --> ON PREND CELUI CONTENUE DANS LE CAS DE CALCUL" % bsamPath)
                    if os.path.isfile(
                            os.path.join(CFDCasePath, 'init/bc_BSAM')):
                        bsamPath = os.path.join(CFDCasePath,
                                                'init/bc_BSAM')  # Afin de palier au probleme d acces au dossier (tout le monde n'a pas les droits), on lit directement le BSAM aero contenu dans le cas de calcul
                    else:
                        print(
                            "\n               WARNING !!!! LE FICHIER BSAM (%s) N'EXISTE PAS --> IL FAUT METTRE A JOUR LA CLEF 'CheminBsam' DANS VOTRE MISE EN DONNEE !!!" % bsamPath)
                        Case2Add = False
                        sys.exit()
                else:
                    print(
                        "\n               WARNING !!!! LE FICHIER BSAM (%s) N'EXISTE PAS --> IL FAUT METTRE A JOUR LA CLEF 'CheminBsam' DANS VOTRE MISE EN DONNEE !!!" % bsamPath)
                    Case2Add = False
                    sys.exit()

            # ------------------------------------------------------------------------------------------------------------------------
            # TYPE DE POST-TRAITEMENT
            # Par defaut la variable DataType est positionné pour un post-traitement de type PTA
            # Si le cas est post-traite par PTA et par ANTARES, alors c'est le post-traitement ANTARES qui sera pris en compte.
            # Et on met a jour le chemin en focntion du type de post-traitement
            CFDCasePathPost = CFDCasePath
            if "TypePost" in Dico.keys():
                if "PTA" in Dico['TypePost'].upper():
                    DataType = "Gradients_Complets"
                    if not os.path.isfile(os.path.join(CFDCasePath,
                                                       'Gradients_complet.xlsx')):
                        CFDCasePathPost = os.path.join(CFDCasePath, 'post')
                elif "ANTARES" in Dico['TypePost'].upper() or "ANNA" in Dico[
                    'TypePost'].upper():
                    DataType = "Post Antares Co"
                    postDir = ''
                    if not os.path.isfile(os.path.join(CFDCasePath,
                                                       'Gradients_Complets.trac')):
                        if os.path.exists(
                                os.path.join(CFDCasePath, 'post', PostAnNADir)):
                            postDir = PostAnNADir
                        elif os.path.exists(os.path.join(CFDCasePath, 'post',
                                                         PostAntaresDir)):
                            postDir = PostAntaresDir

                        if os.path.isfile(
                                os.path.join(CFDCasePath, 'post', postDir,
                                             'Gradients_Complets.trac')):
                            if postDir not in os.path.basename(CFDCasePath):
                                CFDCasePathPost = os.path.join(CFDCasePath,
                                                               'post', postDir)
            else:
                if IsMisesCase:
                    DataType = "Post Antares Co"
                else:
                    if os.path.isfile(os.path.join(CFDCasePath,
                                                   'Gradients_Complets.trac')):
                        CFDCasePathPost = CFDCasePath
                        DataType = "Post Antares Co"
                    else:
                        for folder in os.listdir(CFDCasePath):
                            if 'post' in folder:
                                CFDCasePathPost = os.path.join(CFDCasePath,
                                                               'post')
                                for sub_folder in os.listdir(CFDCasePathPost):
                                    if sub_folder == PostAnNADir:
                                        postDir = PostAnNADir
                                    elif sub_folder == PostAntaresDir:
                                        postDir = PostAntaresDir

                                    if os.path.isfile(
                                            os.path.join(CFDCasePath, 'post',
                                                         postDir,
                                                         'Gradients_Complets.trac')):
                                        DataType = "Post Antares Co"
                                        CFDCasePathPost = os.path.join(
                                            CFDCasePath, 'post', postDir)

            # ------------------------------------------------------------------------------------------------------------------------
            # TITRE DU CAS
            if IsMisesCase:
                TitreCas = Dico.get("TitreCas", "CAS MISES")
            else:
                TitreCas = Dico.get("TitreCas", "CAS CFD")

            if iPrint:
                print("                    -  DataType = %s" % DataType)
                print("                    -  CFDCasePath = %s" % CFDCasePath)
                print("                    -  TitreCas = %s" % TitreCas)

            if ConnexionStatus and not IsMisesCase:
                CasCFD = caseDef.addNS3DCase(
                    name=TitreCas,
                    dataType=DataType,
                    dataPath=CFDCaseName
                )
            else:
                CasCFD = caseDef.addNS3DCase(
                    name=TitreCas,
                    dataType=DataType,
                    dataPath=CFDCasePathPost
                )

            print("\n     --> INFOS CAS CFD (%s) : %s   (%s / %s)" % (
            DataType, CFDCase, Dico.get("Couleur", "Black"),
            Dico.get("Ligne", "SolidLine")))
            print("          * TITRE DU CAS : %s" % TitreCas)
            print("          * CAS NAME : %s" % CFDCaseName)
            print("          * CAS PATH : %s" % CFDCasePathPost)
            print("          * BSAM PATH : %s" % bsamPath)
            print("          * ACCES BBD CNL : %s" % ConnexionStatus)

            # Recuperation des Labels contenues dans le cas CFD
            if ConnexionStatus and IsCFDCasePath == False:
                AllGridCFD = []
                AllGridCFD, DicoAllGridCFD = caseParametersCase.getBlades()
                # On trie les grilles
                ListAllGridCFDSorted = SortGridComp(AllGridCFD, DicoAllGridCFD)
                DicoAllGridCFDSorted = {'Total': ListAllGridCFDSorted,
                                        'Primaire': [], 'Secondaire': []}
            else:
                DicoAllGridCFDSorted = {'Total': [], 'Primaire': [],
                                        'Secondaire': []}
                DicoCorFlux = {1: 'Total', 2: 'Secondaire', 3: 'Primaire'}
                if DataType == "Post Antares Co":
                    if ConnexionStatus and IsCFDCasePath == False:
                        GradFile = os.path.join(CFDCasePath, 'post', postDir,
                                                'Gradients_Complets.trac')
                    else:
                        if IsMisesCase:
                            GradFile = os.path.join(CFDCasePath,
                                                    'Gradients_Complets.trac')
                            if not os.path.isfile(GradFile):
                                GradFile = os.path.join(CFDCasePath, 'results',
                                                        'Gradients_Complets.trac')
                        else:
                            GradFile = os.path.join(CFDCasePath, 'post',
                                                    postDir,
                                                    'Gradients_Complets.trac')

                    if os.path.isfile(GradFile):
                        Grad_File = h5py.File(GradFile, 'r')
                        for grid in Grad_File:
                            if grid not in ["CGNSLibraryVersion", "DataNozzle"]:
                                iFlux = int(Grad_File[grid]["Flux"][()])
                                FluxName = DicoCorFlux[iFlux]
                                NomGrille = str(
                                    Grad_File[grid]["BSAM_NAME"].asstr()[()])
                                DicoAllGridCFDSorted[FluxName].append(NomGrille)
                    else:
                        DicoAllGridCFDSorted = DicoLabelAube2Trace
                else:
                    if ConnexionStatus and IsCFDCasePath == False:
                        CorresFile = os.path.join(CFDCasePath, 'post',
                                                  'correspondance_roue.csv')
                    else:
                        CorresFile = os.path.join(CFDCasePath, 'post',
                                                  'correspondance_roue.csv')

                    if os.path.isfile(CorresFile):
                        try:
                            Corres_File = open(CorresFile, "r")
                            line = ""
                            while line != [""]:
                                try:
                                    line = Corres_File.readline()
                                    if len(line.split(" ")) == 3:
                                        iFlux = int(line.split(" ")[1][0])
                                        NomGrille = line.split(" ")[0]
                                    else:
                                        iFlux = int(line.split(" ")[2][0])
                                        NomGrille = line.split(" ")[1]
                                    FluxName = DicoCorFlux[iFlux]
                                    if NomGrille not in DicoAllGridCFDSorted[
                                        FluxName]: DicoAllGridCFDSorted[
                                        FluxName].append(NomGrille)
                                except:
                                    break
                        except:
                            pass
                    else:
                        DicoAllGridCFDSorted = DicoLabelAube2Trace

            # Recuperation des infos à partir du BSAM
            print("          * LECTURE DU BSAM : %s" % bsamPath)
            res_goux = ReadGoux(bsamPath)
            Omega = 0.
            OmegaTrMin = True
            ListAllGridBSAM = []
            ListAllGridStator = []
            for indGrille in range(res_goux.NGRID[3]):
                GridBSAM = str(res_goux.noms_grille[indGrille].label)
                ListAllGridBSAM.append(GridBSAM)
                Omega = abs(res_goux.noms_grille[indGrille].omeg)
                if Omega > 1.e-5:
                    if OmegaTrMin:
                        OmegaConfig = Omega * 30. / numpy.pi
                    else:
                        OmegaConfig = -Omega
                else:
                    OmegaConfig = 0.0
                    ListAllGridStator.append(GridBSAM)
            print("              --> OMEGA : %.2f Tr/min" % OmegaConfig)

            # On stocke les labels stators
            ListAllGridStatorGENEPI = RenameLabel2GENEPI(ListAllGridStator,
                                                         DicoCorrLabel)
            for Label in ListAllGridStatorGENEPI:
                if Label not in ListAllGridStatorGlobal:
                    ListAllGridStatorGlobal.append(Label)
            print("          * GRILLE(S) STATOR : %s" % ListAllGridStatorGENEPI)

            RenommageLabel_CFD, RenommageLabel_BSAM = CreateListLabelRenommage(
                DicoAllGridCFDSorted, ListAllGridBSAM, DataType)

            # CHOIX DES FICHIERS A IMPORTER
            CasCFD.importAngles = Trace_ProfilsRadiauxAngle
            CasCFD.importMachis = Trace_ProfilVsCorde
            if Trace_ProfilAzimuthaux:
                CasCFD.lectureLigneAzi = 1
            else:
                CasCFD.lectureLigneAzi = 0
            CasCFD.lectureQualityReport = Trace_QualiteMaillage
            CasCFD.convDebit = Trace_ConvDebit
            CasCFD.convResidus = Trace_ConvResidus
            CasCFD.regenererTrac = 1
            CasCFD.tracerGradients = 1

            # IMPORT CARMA AUTO
            if ConnexionStatus and IsCFDCasePath == False:
                ImportCarmaAuto = False
                if 'ImportCarmaAuto' in Dico.keys():
                    CasCFD.importCarmaAuto = Dico[
                        'ImportCarmaAuto']  # Pour la Carte Carma, le nom de la grille correspond au nom du cas de calcul CFD. Il faut donc que les labels des roue entre cas CFD et BSAM soit coherent
                    if Dico['ImportCarmaAuto'] == 1 or Dico[
                        'ImportCarmaAuto'] == True: ImportCarmaAuto = True

                if 'LiaisonCasCarma' in Dico.keys() and ImportCarmaAuto == False:
                    CasCFD.liaisonCasCarma = Dico.get('LiaisonCasCarma', '')
                    CasCFD.importCarmaAuto = 0
                    print(
                        "          * CAS DE REFERENCE POUR LES AUBAGES : %s" % Dico.get(
                            'LiaisonCasCarma', ''))
                else:
                    CasCFD.importCarmaAuto = Dico.get('ImportCarmaAuto', 1)
                    print("          * IMPORT CARMA AUTO")
            else:
                if ConnexionStatus:
                    CasCFD.importCarmaAuto = Dico.get('ImportCarmaAuto', 1)
                    print("          * IMPORT CARMA AUTO")
                else:
                    CasCFD.liaisonCasCarma = Dico.get('LiaisonCasCarma', '')
                    print(
                        "          * CAS DE REFERENCE POUR LES AUBAGES : %s" % Dico.get(
                            'LiaisonCasCarma', ''))
                    CasCFD.importCarmaAuto = 0

            CasCFD.BABFBSAM = int(Dico.get('BABFBSAM',
                                           1))  # Utilise les plans BA/BF du BSAM et non ceux reinterpreté par PTA

            if IsMisesCase:
                CasCFD.groupeAppartenance = ['MISES']
            else:
                CasCFD.groupeAppartenance = ['CFD']

            if ConnexionStatus:
                CasCFD.DetectionBSAM = int(Dico.get('DetectionCasProcheBSAM',
                                                    0))  # détection automatique du cas le plus proche du BSAM
            else:
                CasCFD.DetectionBSAM = int(Dico.get('DetectionCasProcheBSAM',
                                                    0))  # détection automatique du cas le plus proche du BSAM
            CasCFD.utilisationBsamCalcul = 0

            # RECALAGE KD
            if int(Dico.get('RecalageKD', 0)):
                RecalageKDVar = 1
                if "CheminBsam" in Dico.keys():
                    KDbsamPath = Dico.get('CheminBsam', "")
                    if not os.path.isfile(KDbsamPath):
                        print(
                            "\n               WARNING !!!! LE FICHIER BSAM (%s) N'EXISTE PAS \n                           --> ON NE RECALE PAS PAR LE KD \n" % KDbsamPath)
                        CasCFD.BSAM_KD = ""
                        CasCFD.utilisationBsamCalcul = 1  # On recupere le BSAM aero du calcul
                    else:
                        print(
                            "          * ON PREND LE BSAM SUIVANT POUR LE KD : %s" % KDbsamPath)
                        CasCFD.BSAM_KD = KDbsamPath
                else:
                    print(
                        "          * ON PREND LE BSAM SUIVANT POUR LE KD : %s" % bsamPath)
                    CasCFD.BSAM_KD = bsamPath
            else:
                CasCFD.BSAM_KD = ""
                print(
                    "          * ON NE RECALE PAS LES PERFOS 0D PAR LE KD : %s" % bsamPath)

            # CAS DE REFERENCE
            if Dico['DeltaCasRef'].upper() == "BSAM":
                CasCFD.casReference = "BSAM_%s" % BsamName
                print(
                    "          * CAS DE REFERENCE POUR LES DELTAS : %s" % "BSAM_%s" % BsamName)
                DeltaGraph.append(True)
            elif Dico['DeltaCasRef'].upper() == "":
                print("          * PAS DE CAS DE REFERENCE")
                CasCFD.casReference = Dico['DeltaCasRef']
                DeltaGraph.append(False)
            else:
                CasCFD.casReference = Dico['DeltaCasRef']
                print(
                    "          * CAS DE REFERENCE POUR LES DELTAS : %s" % Dico[
                        'DeltaCasRef'])
                DeltaGraph.append(True)

            CasCFD.setIso(int(SetIso))
            CasCFD.trierIso = int(TrierIso)

            if int(SetIso):
                CasCFD.isoName = Dico.get("TitreIso", "Iso")
            else:
                CasCFD.isoName = ""

            CasCFD.isoMarker = Dico.get("SymboleIso", "o")

            MisesDetectionCoupeAuto = Dico.get('MisesDetectionCoupeAuto', 0)

            if IsMisesCase:
                CasCFD.setCurveProperties(
                    {'curveStyle': Dico.get("Ligne", "SolidLine"),
                     'curveColor': Dico.get("Couleur", "Black"),
                     'curveWidth': Dico.get("Epaisseur", 2),
                     'markerStyle': Dico.get("Symbole", "o"),
                     'markerWidth': 8,
                     })
            else:
                CasCFD.setCurveProperties(
                    {'curveStyle': Dico.get("Ligne", "SolidLine"),
                     'curveColor': Dico.get("Couleur", "Black"),
                     'curveWidth': Dico.get("Epaisseur", 2),
                     'markerStyle': Dico.get("Symbole", None),
                     'markerWidth': 3,
                     })

            # On renomme les aubes CFD selon le formalisme GENEPI
            print(
                "          * GRILLE(S) CONTENUE(S) DANS LE CAS CFD : %s" % DicoAllGridCFDSorted)
            LabelAubeAuto = False
            if LabelAubeAuto:
                print(
                    "          * NOMMAGE AUTOMATIQUE DES AUBES CFD : correspondance_roue.csv")
                CasCFD.utiliserCorrespondanceRoue = 1
            else:
                CasCFD.utiliserCorrespondanceRoue = 0
                print(
                    "          * RENOMMAGE DES AUBES CFD : %s" % RenommageLabel_CFD)
                CasCFD.setUserGridName(RenommageLabel_CFD)

            # On renomme les plans CFD
            ListAllGridCFDSorted = ConvertDicoToList(DicoAllGridCFDSorted)
            ListAllGridCFDSortedGENEPI = RenameLabel2GENEPI(
                ListAllGridCFDSorted, DicoCorrLabel)

            RenommagePlan = Dico.get("RenommagePlan")
            if RenommagePlan != None:
                RenommagePlanCFD = RenommagePlan
            else:
                RenommagePlanCFD = RenommagePlan_CFD

            # for plan in RenommagePlanCFD:
            # RenommagePlanCFD[plan] = RenommagePlanCFD[plan]
            RenomPlanCFD = {}
            if not isinstance(ListAllGridCFDSortedGENEPI, list):
                RenomPlanCFD = {ListAllGridCFDSortedGENEPI: RenommagePlanCFD}
            else:
                for couple in ListAllGridCFDSortedGENEPI:
                    RenomPlanCFD[couple] = RenommagePlanCFD

            CasCFD.renommagePlans = RenomPlanCFD
            print("          * RENOMMAGE DES PLANS CFD : %s" % RenomPlanCFD)

            # Marge au blocage
            if 'Marge' in DicoXYVarProfilsRadiaux2Trace[
                'GradPlanVsPlanRef_XVar']:
                CasCFD.calculerGcolter = 1
            else:
                CasCFD.calculerGcolter = 0

            DicoGcolterRetournerAube = Dico.get("GcolterRetournerAube",
                                                {"STATOR": 0, "ROTOR": 1})
            GcolterRetournerAubeSTATOR = DicoGcolterRetournerAube.get("STATOR",
                                                                      0)
            GcolterRetournerAubeROTOR = DicoGcolterRetournerAube.get("ROTOR", 0)

            DicoAubeGcolter = {}
            for Aube in ListAllGridCFDSortedGENEPI:
                if Aube in ListAllGridStatorGlobal:
                    DicoAubeGcolter[Aube] = GcolterRetournerAubeSTATOR
                else:
                    DicoAubeGcolter[Aube] = GcolterRetournerAubeROTOR

            CasCFD.retournerAubageGcolterDict = DicoAubeGcolter

            RetournerAubeGcolter = Dico.get("RetournerAubeGcolter", 0)
            CasCFD.retournerAubageGcolter = RetournerAubeGcolter

            CasCFD.BAGcolter = PlanGcolter_Amont
            CasCFD.BFGcolter = PlanGcolter_Aval

            TraceBSAM = Dico.get("TraceBSAM", 1)
            if TraceBSAM:
                # ===============================================================================
                #   AJOUT DU BSAM ASSOCIE AU CAS CFD
                print("          * BSAM ASSOCIE AU CAS CFD : %s (%s / %s)" % (
                bsamPath, Dico.get("Couleur", "Black"),
                Dico.get("Ligne", "SolidLine")))

                AddBSAMCase(BsamName, bsamPath, Dico, "CFD", 1)

            Case2Add = True

    return Case2Add, DataType, CFDCasePath, RecalageKDVar, DicoInfoAube


def AddBSAMCase(CaseName="", bsamPath="", Dico={}, Linked2="", SetIso=0,
                iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : AddBSAMCase")

    # Recuperation des Labels contenues dans le BSAM
    if not os.path.isfile(bsamPath):
        print(
            "\n               WARNING !!!! LE FICHIER BSAM (%s) N'EXISTE PAS --> CAS PAS AJOUTE" % bsamPath)
        # sys.exit()
    else:
        if Linked2 == "BSAM": print(
            "          * LECTURE DU BSAM : %s" % bsamPath)
        res_goux = ReadGoux(bsamPath)
        BsamName = os.path.basename(bsamPath)
        if Linked2 == "BSAM": print(
            "          * BSAM ASSOCIE AU CAS : %s (%s / %s)" % (
            BsamName, Dico.get("Couleur", "Black"),
            Dico.get("Ligne", "SolidLine")))

        Omega = 0.
        OmegaTrMin = True
        ListAllGridBSAM = []
        ListAllGridStator = []
        for indGrille in range(res_goux.NGRID[3]):
            GridBSAM = res_goux.noms_grille[indGrille].label
            ListAllGridBSAM.append(GridBSAM)
            Omega = abs(res_goux.noms_grille[indGrille].omeg)
            if Omega > 1.e-5:
                if OmegaTrMin:
                    OmegaConfig = Omega * 30. / numpy.pi
                else:
                    OmegaConfig = -Omega
                print("              --> %s - OMEGA : %.2f Tr/min" % (
                GridBSAM, OmegaConfig))
            else:
                ListAllGridStator.append(GridBSAM)

        ListAllGridBSAMGENEPI = RenameLabel2GENEPI(ListAllGridBSAM,
                                                   DicoCorrLabel)
        print(
            "              --> GRILLE(S) CONTENUE(S) DANS LE CAS BSAM : %s" % ListAllGridBSAMGENEPI)

        # On cree les listes pour renommer les labels au format GENEPI
        RenommageLabel_CFD, RenommageLabel_BSAM = CreateListLabelRenommage({},
                                                                           ListAllGridBSAM,
                                                                           "BSAM")

        ListAllGridStatorGENEPI = RenameLabel2GENEPI(ListAllGridStator,
                                                     DicoCorrLabel)
        print(
            "              --> GRILLE(S) STATOR : %s" % ListAllGridStatorGENEPI)

        for Label in ListAllGridStatorGENEPI:
            if Label not in ListAllGridStatorGlobal:
                ListAllGridStatorGlobal.append(Label)

        casBSAM = caseDef.ajouterCasBSAM("BSAM", bsamPath)
        # if Linked2 != "CARMA":
        casBSAM.setUserGridName(RenommageLabel_BSAM)

        if Linked2 == "BSAM":
            casBSAM.setName(Dico["TitreCas"])
            casBSAM.isoName = Dico.get("TitreIso", "")
        else:
            if CaseName != '':
                casBSAM.setName("BSAM_%s" % CaseName)
                casBSAM.isoName = "BSAM_%s" % CaseName
            else:
                casBSAM.setName(BsamName)
                casBSAM.isoName = BsamName

        casBSAM.setIso(SetIso)

        if 'InverserBsam' in Dico.keys():  # La clef est inversée dans GENEPI.
            if Dico['InverserBsam'] == 1:
                casBSAM.InverserBsam = 0
            else:
                casBSAM.InverserBsam = 1
        else:
            casBSAM.InverserBsam = 0

        if Linked2 == "CFD":
            casBSAM.liaisonCasCarma = Dico.get('LiaisonCasCarma', '')
        elif Linked2 == "BSAM":
            casBSAM.liaisonCasCarma = Dico.get('LiaisonCasCarma', '')
        elif Linked2 == "CARMA":
            casBSAM.liaisonCasCarma = CaseName
        else:
            casBSAM.liaisonCasCarma = Dico.get('LiaisonCasCarma', '')

        if 'Marge' in DicoXYVarProfilsRadiaux2Trace['GradPlanVsPlanRef_XVar']:
            casBSAM.calculerGcolter = Dico.get('Gcolter', 1)
        else:
            casBSAM.calculerGcolter = 0

        if Linked2 == "CARMA": casBSAM.calculerGcolter = 0

        casBSAM.groupeAppartenance = ['BSAM']

        if Linked2.upper() == "CFD":
            casBSAM.setCurveProperties(
                {'curveStyle': Dico.get("LigneBsam", "NoPen"),
                 'curveColor': Dico.get("CouleurBsam",
                                        Dico.get("Couleur", "Black")),
                 'curveWidth': Dico.get("EpaisseurBsam",
                                        Dico.get("Epaisseur", 2)),
                 'markerStyle': Dico.get("SymboleBsam", "t"),
                 'markerWidth': Dico.get("SymboleEpaisseurBsam", 5),
                 # 'markerColor': 'blue',
                 })

        elif Linked2.upper() == "CARMA":
            casBSAM.setCurveProperties(
                {'curveStyle': Dico.get("LigneBsam", "DashLine"),
                 'curveColor': Dico.get("CouleurBsam",
                                        Dico.get("Couleur", "Black")),
                 'curveWidth': Dico.get("EpaisseurBsam",
                                        Dico.get("Epaisseur", 2)),
                 'markerStyle': Dico.get("SymboleBsam", "t"),
                 'markerWidth': Dico.get("SymboleEpaisseurBsam", 5),
                 # 'markerColor': 'blue',
                 })
        else:
            casBSAM.setCurveProperties(
                {'curveStyle': Dico.get('Ligne', "SolidLine"),
                 'curveColor': Dico.get("Couleur", "Black"),
                 'curveWidth': Dico.get("Epaisseur", 2),
                 'markerStyle': Dico.get("Symbole", "o"),
                 'markerWidth': Dico.get("SymboleEpaisseur", 5),
                 # 'markerColor': 'blue',
                 })

        LabelAubeAuto = False
        if LabelAubeAuto:
            print(
                "              --> NOMMAGE AUTOMATIQUE DES AUBES : labels contenus dans le bsam")
            RenommageLabel_BSAM = [[], [], [], []]
        else:
            print(
                "              --> RENOMMAGE DES AUBES BSAM : %s" % RenommageLabel_BSAM)

        RenommagePlan = Dico.get("RenommagePlan")
        if RenommagePlan != None:
            RenommagePlanBSAM = RenommagePlan
        else:
            RenommagePlanBSAM = RenommagePlan_BSAM

        RenomPlanBSAM = {}
        if not isinstance(ListAllGridBSAMGENEPI, list):
            RenomPlanBSAM = {ListAllGridBSAMGENEPI: RenommagePlanBSAM}
        else:
            RenomPlanBSAM = {}
            for couple in ListAllGridBSAMGENEPI:
                RenomPlanBSAM[couple] = RenommagePlanBSAM
        casBSAM.renommagePlans = RenomPlanBSAM


def AddCARMACase(Dico={}, DataType="CarmaBatch", iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : AddCARMACase")

    if "TitreCas" in DicoCase.keys():
        TitreCas = DicoCase['TitreCas']
    else:
        if isinstance(Dico["Aube"], list):
            TitreCas = "%s_%s" % (DicoCase["Projet"], DicoCase["Version"])
        else:
            TitreCas = "%s_%s_%s" % (
            DicoCase["Projet"], DicoCase["Version"], DicoCase["Aube"])

    CasCARMA = caseDef.addCarmaCase(
        name=TitreCas,
        dataType=DataType,
        dataPath="",
    )

    CasCARMA.RedecouperAube = Dico.get("RedecouperAube", 1)
    CasCARMA.reference = 0
    CasCARMA.BSAMhauteur = Dico.get("HauteurBSAM", 1)
    CasCARMA.sweep_dihedre = Dico.get("SweepDiedre", 0)
    CasCARMA.calculerGcolter = Dico.get("Gcolter", 1)
    CasCARMA.GrilleBSAM = Dico.get("CheminBsam", "")
    CasCARMA.coupesDessin = Dico["CoupesDessin"]
    CasCARMA.Groupes = ["CARMA"]
    CasCARMA.setCurveProperties({'curveStyle': Dico.get("Ligne", "SolidLine"),
                                 'curveColor': Dico.get("Couleur", "Black"),
                                 'curveWidth': Dico.get("Epaisseur", 2),
                                 'markerStyle': Dico.get("Symbole", "o"),
                                 'markerWidth': 5,
                                 })

    if not isinstance(Dico["Aube"], list):
        Dico["Aube"] = [Dico["Aube"]]

    DicoKeyCor = {"Grille": "nom",
                  "Xemp": "Emp",
                  "RetournerAube": "InverserY",
                  "lienXML": "lienXML",
                  "RetournerAubeGcolter": "RetournerGcolter",
                  }

    DefImportCarmaBatch = []
    for Index in range(0, len(Dico["Aube"])):
        DicoInfoAube = {}
        if isinstance(Dico["TypeCoupe"], list):
            if isinstance(Dico["TypeCoupe"][Index], list):
                for Index2 in range(0, len(Dico["TypeCoupe"][Index])):
                    DicoInfoAube["TypeCoupe"] = Dico["TypeCoupe"][Index][Index2]
                    for Key in ["Grille", "Projet", "Version", "Aube", "Xemp",
                                "RetournerAube", "Calage", "NbAube",
                                "RetournerAubeGcolter", "lienXML"]:
                        if Key in Dico.keys():
                            if Key in DicoKeyCor.keys():
                                KeyGenepi = DicoKeyCor[Key]
                            else:
                                KeyGenepi = Key

                            if isinstance(Dico[Key], list):
                                DicoInfoAube[KeyGenepi] = Dico[Key][Index]
                            else:
                                DicoInfoAube[KeyGenepi] = Dico[Key]

                            if Key == "lienXML" and Key in Dico.keys():
                                if isinstance(Dico[Key], list):
                                    LienXML = Dico[Key][Index]
                                    if os.path.isfile(LienXML):
                                        DicoInfoAube[KeyGenepi] = LienXML
                                    else:
                                        print(
                                            "             /!\ LE LIEN XML N'EXISTE PAS !!!!")
                                else:
                                    DicoInfoAube[KeyGenepi] = Dico[Key]
            else:
                DicoInfoAube["TypeCoupe"] = Dico["TypeCoupe"][Index]
                for Key in ["Grille", "Projet", "Version", "Aube", "Xemp",
                            "RetournerAube", "Calage", "NbAube",
                            "RetournerAubeGcolter", "lienXML"]:
                    if Key in Dico.keys():
                        if Key in DicoKeyCor.keys():
                            KeyGenepi = DicoKeyCor[Key]
                        else:
                            KeyGenepi = Key

                        if isinstance(Dico[Key], list):
                            DicoInfoAube[KeyGenepi] = Dico[Key][Index]
                        else:
                            DicoInfoAube[KeyGenepi] = Dico[Key]

                        if Key == "lienXML" and Key in Dico.keys():
                            if isinstance(Dico[Key], list):
                                LienXML = Dico[Key][Index]
                                if os.path.isfile(LienXML):
                                    DicoInfoAube[KeyGenepi] = LienXML
                                else:
                                    print(
                                        "             /!\ LE LIEN XML n'EXISTE PAS !!!!")
                            else:
                                DicoInfoAube[KeyGenepi] = Dico[Key]
        else:
            DicoInfoAube["TypeCoupe"] = Dico["TypeCoupe"]

            for Key in ["Grille", "Projet", "Version", "Aube", "Xemp",
                        "RetournerAube", "Calage", "NbAube",
                        "RetournerAubeGcolter", "lienXML"]:
                if Key in Dico.keys():
                    if Key in DicoKeyCor.keys():
                        KeyGenepi = DicoKeyCor[Key]
                    else:
                        KeyGenepi = Key

                    if isinstance(Dico[Key], list):
                        DicoInfoAube[KeyGenepi] = Dico[Key][Index]
                    else:
                        DicoInfoAube[KeyGenepi] = Dico[Key]

                    if Key == "lienXML" and Key in Dico.keys():
                        if isinstance(Dico[Key], list):
                            LienXML = Dico[Key][Index]
                            if os.path.isfile(LienXML):
                                DicoInfoAube[KeyGenepi] = LienXML
                            else:
                                print(
                                    "             /!\ LE LIEN XML N'EXISTE PAS !!!!")
                        else:
                            DicoInfoAube[KeyGenepi] = Dico[Key]

        DefImportCarmaBatch.append(DicoInfoAube)

    CasCARMA.DefinitionImportCarmaBatch = DefImportCarmaBatch

    # Fonction de renommage du label de la grille (disponible uniquement en batch)
    if not isinstance(DicoInfoAube["nom"], list):
        ListAllGridCARMA = [DicoInfoAube["nom"]]
    else:
        ListAllGridCARMA = DicoInfoAube["nom"]

    RenommageLabel_CFD, RenommageLabel_CARMA = CreateListLabelRenommage({},
                                                                        ListAllGridCARMA,
                                                                        "CARMA")
    CasCARMA.setUserGridName(RenommageLabel_CARMA)
    TraceBSAM = Dico.get("TraceBSAM", 1)
    if TraceBSAM:
        # ===============================================================================
        #   AJOUT DU BSAM ASSOCIE AU CAS CARMA
        CheminBsam = Dico.get("CheminBsam")
        if CheminBsam != None:
            BsamName = os.path.basename(CheminBsam)
            print("          * BSAM ASSOCIE AU CAS CARMA : %s (%s / %s)" % (
            BsamName, Dico.get("Couleur", "Black"),
            Dico.get("Ligne", "SolidLine")))

            AddBSAMCase(TitreCas, Dico["CheminBsam"], Dico, "CARMA", 0)


def CreateGraphLoiGeom(PageName, Aube, XVar, YVar, TypeCoupes, DicoVariables={},
                       SuperpositionVar=0, SuperpositionPlan=0,
                       SuperpositionCase=1, SuperpositionBlade=0,
                       Groupe=['CARMA'], DicoPrefGraphe={}, DicoUserCurves={},
                       iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphLoiGeom")

    graph = page.addGraph("LoiGeometrique",
                          name="%s - %s | %s" % (Aube, XVar, YVar))

    # graph.PlaneDefinition = []
    if not isinstance(TypeCoupes, list):
        TypeCoupes = [TypeCoupes]

    for TypeCoupe in TypeCoupes:
        planeDefinition = {}
        planeDefinition["StreamTubeType"] = TypeCoupe
        planeDefinition["bladeName"] = "MainBlade"
        planeDefinition["gridName"] = Aube
        graph.addPlaneDefinition(planeDefinition)

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    graph.superpositionVariables = SuperpositionVar
    graph.PLaneSuperposition = SuperpositionPlan
    graph.superpositionCase = SuperpositionCase
    graph.SuperpositionBlade = SuperpositionBlade

    graph.sortByPlane = 0
    graph.sortByVar = 0
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
    graph.showFlux = DicoPrefGraphe["ShowFlux"]
    if XVar == 'ssc' or XVar == 's':
        graph.afficherZaube = 1
        graph.showLegend = 1
    else:
        graph.afficherZaube = 0

    graph.Grid = 1
    graph.groupeAppartenance = Groupe

    graph.userCurves = []
    ListCourbes = []
    if isinstance(XVar, list):
        for Var in XVar:
            if Var in DicoUserCurves.keys():
                ListCourbes.append(Var)
            if "EBA" in Var and "Spec EpBA" in DicoUserCurves.keys():
                ListCourbes.append("Spec EpBA")
            if "EBF" in Var and "Spec EpBF" in DicoUserCurves.keys():
                ListCourbes.append("Spec EpBF")
        graph.courbesUtilisateurGlobales = ListCourbes
    else:
        if XVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [XVar]
        if "EBA" in XVar and "Spec EpBA" in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = ["Spec EpBA"]
        if "EBF" in XVar and "Spec EpBF" in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = ["Spec EpBF"]

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphCol3D(PageName, Aube, DicoXYVar2Trace, DicoVariables={},
                     Groupe=['CARMA'], DicoPrefGraphe={}, DicoUserCurves={},
                     iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphCol3D")

    graph = page.addGraph("Col3D", name="%s" % (Aube))

    HauteurFormatOKList = []
    for Hauteur in DicoXYVar2Trace['HauteurListe']:
        if Hauteur != '':
            HauteurFormatOK = 'CQ%02d' % Hauteur
            HauteurFormatOKList.append(HauteurFormatOK)
        else:
            HauteurFormatOKList = ['']

    planeDefinition = {}
    planeDefinition["StreamTubeList"] = HauteurFormatOKList
    planeDefinition["bladeName"] = "MainBlade"
    planeDefinition["gridName"] = Aube
    graph.addPlaneDefinition(planeDefinition)

    graph.orthonorme = 0
    graph.caseList = []
    graph.tracerCoupes = 1
    graph.tracerSection = 1
    graph.NombreColonnepage = 3
    graph.superpositionCas = 1

    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
    graph.showFlux = DicoPrefGraphe["ShowFlux"]

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphVisuAubage(PageName, Aube, ShowAubage, ShowCoupeCarma, ZoomBABF,
                          SuperpositionCase, DicoPrefGraphe={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphVisuAubage")

    graph = page.addGraph("Vue Aubage", name="%s" % (Aube))

    graph.afficherAubages = ShowAubage
    graph.superposerLesCas = SuperpositionCase

    graph.afficherCoupeCarma = ShowCoupeCarma

    graph.zoomBABF = ZoomBABF
    graph.listeGrilles = [Aube]
    graph.tailleMarker = 0
    graph.retournerAubage = 0

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphVisuBABF(PageName, Aube, DicoXYVar, ShowAubage, ShowCoupeCarma,
                        ZoomBABF, MarquerBABF, RecalerBABF, SuperpositionCase,
                        DicoPrefGraphe={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphVisuBABF")

    graph = page.addGraph("ZoomBABF", name="%s" % (Aube))

    graph.afficherAubages = ShowAubage
    graph.superposerLesCas = SuperpositionCase

    graph.afficherCoupeCarma = ShowCoupeCarma

    graph.zoomBABF = ZoomBABF
    graph.listeGrilles = [Aube]
    # graph.listeCoupes = DicoXYVar['HauteurListe']   # PROBLEME AVEC CETTE VARIABLE
    graph.listeCoupes = []
    graph.retournerAubage = 0
    graph.NombreColonnepage = 3
    graph.tailleMarker = 0
    graph.marquerBABF = MarquerBABF
    graph.recalageBABF = RecalerBABF

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphGradient(PageName, Aube, Flux, XVar, YVar, XVarDelta, PlanRef,
                        Plan, Groupe=['MISES', 'CFD', 'BSAM', 'CARMA'],
                        DicoVariables={}, DicoPrefGraphe={}, DicoUserCurves={},
                        InterpDir='q_Q', MoyAdim=0, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphGradient")

    if XVarDelta:
        graph = page.addGraph("Gradients",
                              name="%s - %s | %s - DELTA" % (Aube, XVar, YVar))
    else:
        graph = page.addGraph("Gradients",
                              name="%s - %s | %s" % (Aube, XVar, YVar))

    graph.showAverage = DicoPrefGraphe["ShowAverage"]
    graph.groupeAppartenance = Groupe

    if graph.showAverage:
        graph.showLegend = 1
    else:
        graph.showLegend = 0

    graph.adimensionnementMoyenne = MoyAdim
    graph.comparaisonReferenceAdim = 0

    if XVarDelta:
        if iPrint:
            print(
                "         * VARIABLE DELTA: { X: %s   , Y: %s}" % (XVar, YVar))
        graph.comparaisonSimple = 0
        graph.comparaisonReference = 1
        graph.courbesUtilisateurGlobales = ['Delta']
    else:
        graph.comparaisonSimple = 1
        graph.comparaisonReference = 0
        if XVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [XVar]

    if PlanRef == Plan and not XVar in ["INCD", "EFP"]:
        graph.ajouterPlan(gridName="%s" % Aube,
                          planeName="%s" % Plan,
                          flux=Flux)
    else:
        graph.ajouterPlan(gridName_ref="%s" % Aube,
                          gridName="%s" % Aube,
                          planeName="%s" % Plan,
                          planeName_ref="%s" % PlanRef,
                          flux=Flux)

    graph.interpDir = InterpDir

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphGradientAngle(PageName, Aube, Flux, XVar, YVar, XVarDelta,
                             Groupe=['CFD', 'BSAM', 'CARMA'], DicoVariables={},
                             DicoPrefGraphe={}, DicoUserCurves={},
                             iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphGradientAngle")

    if XVarDelta:
        graph = page.addGraph("AnglesBABF",
                              name="%s - %s | %s - DELTA" % (Aube, XVar, YVar))
    else:
        graph = page.addGraph("AnglesBABF",
                              name="%s - %s | %s" % (Aube, XVar, YVar))

    graph.showAverage = DicoPrefGraphe["ShowAverage"]
    graph.groupeAppartenance = Groupe

    if graph.showAverage:
        graph.showLegend = 1
    else:
        graph.showLegend = 0

    if XVarDelta:
        if iPrint:
            print(
                "         * VARIABLE DELTA: { X: %s   , Y: %s}" % (XVar, YVar))
        graph.comparaisonSimple = 0
        graph.comparaisonReference = 1
        graph.courbesUtilisateurGlobales = ['Delta']
    else:
        graph.comparaisonSimple = 1
        graph.comparaisonReference = 0
        if XVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [XVar]

    planeDefinition = {}
    planeDefinition["bladeName"] = "MainBlade"
    planeDefinition["gridName"] = Aube
    graph.addPlaneDefinition(planeDefinition)

    # GraphAddXYVar(graph, XVar, YVar, DicoVariables) --> Fonction non disponible pour ce type de graphique.

    DicoVariables = IsVarInDicoVariables(XVar, DicoVariables)
    graph.XVars = [XVar]
    graph.XVarsUnit = ['%s' % DicoVariables[XVar]['Unite']]
    graph.XVarsCS = ['%s' % DicoVariables[XVar]['NbreCS']]

    DicoVariables = IsVarInDicoVariables(YVar, DicoVariables)
    graph.YVar = [YVar]
    graph.YVarUnit = ['%s' % DicoVariables[YVar]['Unite']]
    graph.YVarCS = ['%s' % DicoVariables[YVar]['NbreCS']]

    # On force les min/max
    graph.minY = 0
    graph.maxY = 1
    graph.pasY = 0.1

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphMarge(PageName, Aube, XVar, YVar, XVarDelta, TypeCoupes,
                     DicoVariables, DicoPrefGraphe, DicoUserCurves,
                     iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphMarge")

    if XVarDelta:
        graph = page.addGraph("Marge",
                              name="%s - %s | %s - DELTA" % (Aube, XVar, YVar))
    else:
        graph = page.addGraph("Marge", name="%s - %s | %s" % (Aube, XVar, YVar))

    graph.showLegend = DicoPrefGraphe["ShowLegend"]

    if XVarDelta:
        graph.comparaisonSimple = 0
        graph.comparaisonReference = 1
        graph.courbesUtilisateurGlobales = ['Delta']
    else:
        graph.comparaisonSimple = 1
        graph.comparaisonReference = 0
        if XVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [XVar]

    if not isinstance(TypeCoupes, list):
        TypeCoupes = [TypeCoupes]

    for TypeCoupe in TypeCoupes:
        planeDefinition = {}
        planeDefinition["StreamTubeType"] = TypeCoupe
        planeDefinition["bladeName"] = "MainBlade"
        planeDefinition["gridName"] = Aube
        graph.addPlaneDefinition(planeDefinition)

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphChamps(PageName, Aube, Flux, XVar, YVar, XVarPlanAmont,
                      XVarPlanAval, YVarPlanAmont, YVarPlanAval, Hauteur,
                      DissocierPlans, SortByVar, SortByPlane, SuperpositionPlan,
                      AfficherVannage, AfficherIsoPi_D, DicoVariables,
                      DicoPrefGraphe, DicoUserCurves, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphChamps")

    graph = page.addGraph("Champs", name="%s - %s (%s/%s) | %s (%s/%s)" % (
    Aube, XVar, XVarPlanAmont, XVarPlanAval, YVar, YVarPlanAmont, YVarPlanAval))

    graph.ajouterPlan(gridName_ref="%s" % Aube,
                      gridName="%s" % Aube,
                      planeName=YVarPlanAval,
                      planeName_ref=YVarPlanAmont,
                      flux=Flux,
                      name="",
                      hauteur=Hauteur)

    graph.ajouterPlanbis(gridName_ref="%s" % Aube,
                         gridName="%s" % Aube,
                         planeName=XVarPlanAval,
                         planeName_ref=XVarPlanAmont,
                         flux=Flux,
                         name="",
                         hauteur=Hauteur)

    graph.VarSuperposition = False
    graph.PLaneSuperposition = SuperpositionPlan
    graph.dissocierPlansAbscisseOrdonnee = DissocierPlans
    graph.sortByVar = SortByVar
    graph.sortByPlane = SortByPlane
    graph.showAverage = DicoPrefGraphe["ShowAverage"]
    graph.showFlux = DicoPrefGraphe["ShowFlux"]
    graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.modeMatriciel = 0
    graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
    graph.groupesATracer = []
    graph.isoATracer = []
    graph.afficherVannage = AfficherVannage
    graph.AfficherIsoPi_D = AfficherIsoPi_D
    if XVar in DicoUserCurves.keys():
        graph.courbesUtilisateurGlobales = [
            XVar]  # liste des courbes globales à afficher
    graph.afficherTitreIso = 0
    graph.tailleMarker = 10

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphEvolutionParois(PageName, Aube, YVar,
                               Hauteurs=["Moyeu", "Carter"],
                               SuperpositionCase=0, Groupe=['CFD'],
                               DicoVariables={}, DicoPrefGraphe={},
                               DicoUserCurves={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphEvolutionParois")

    # D:\codes\GENEPI\SIMU\CURRENT\GENEPI\src\presentationConstruction\graphiques\machParoisConstruction.py
    DicoVariables = IsVarInDicoVariables(YVar, DicoVariables)

    graph = page.addGraph("Evolution parois", name="%s - %s" % (Aube, YVar))
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.Variable = YVar
    graph.Unite = DicoVariables[YVar]['Unite'].replace('[', '').replace(']', '')
    graph.MultY = DicoVariables[YVar]['FactMulti']
    graph.hauteurs = Hauteurs

    graph.autoScaleModeY = 'Mode P. Ginibre'
    graph.autoScaleYPG_minX = 0.02
    graph.autoScaleYPG_maxX = 0.98
    graph.autoScaleYPG_limiteur = 10.0

    graph.autoScaleModeX = 'Mode P. Ginibre'
    graph.autoScaleXPG_minY = DicoVariables[YVar]['PGMin']
    graph.autoScaleXPG_maxY = DicoVariables[YVar]['PGMax']
    graph.autoScaleXPG_limiteur = DicoVariables[YVar]['limiteur']

    graph.comparaisonSimple = 1
    graph.comparaisonReference = 0
    graph.SuperpositionCase = SuperpositionCase
    graph.groupeAppartenance = Groupe
    # if XVar in DicoUserCurves.keys():
    # graph.courbesUtilisateurGlobales = [XVar]

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphEvolutionAxiale(PageName, Aubes, Flux, XVar, YVar,
                               Hauteurs=[0.2, 0.5, 0.7], InterpDir='q_Q',
                               SuperpositionCase=0, PlanRef='AmontPerfo',
                               Plan='AvalPerfo', Groupe=['CFD'],
                               DicoVariables={}, DicoPrefGraphe={},
                               DicoUserCurves={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphEvolutionAxiale")

    # D:\codes\GENEPI\SIMU\CURRENT\GENEPI\src\presentationConstruction\graphiques\evolutionParGrille.py
    DicoVariables = IsVarInDicoVariables(XVar, DicoVariables)
    DicoVariables = IsVarInDicoVariables(YVar, DicoVariables)

    graph = page.addGraph("Evolution par Grille",
                          name="%s - %s | %s" % (Aubes, XVar, YVar))
    graph.showAverage = DicoPrefGraphe["ShowAverage"]
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.Variable = YVar
    graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
    graph.interpDir = InterpDir  # direction d'interpolation
    graph.MoyAzi = "5"  # choix du type de moyenne pour l'azimutale
    graph.comparaisonSimple = 1
    graph.comparaisonReference = 0
    graph.SuperpositionCase = SuperpositionCase
    # if XVar in DicoUserCurves.keys():
    # graph.courbesUtilisateurGlobales = [XVar]

    if YVar in ['Pi', 'etapol', 'cd_fftro', 'Dev', 'W2_W1_RAL', 'PSIA', 'DLI',
                'Tau', 'Marge', 'AVDR']:
        PlanRef = 'AmontPerfo'
        Plan = 'AvalPerfo'

    if YVar in ['REYc', 'Ra_HL',
                'ssc', 'Corde', 'CordeAxi', 'Emax', 'EmaxsC', 'Fmax', 'FmaxsC',
                'XEmax', 'XEmaxsC', 'XFmax', 'XFmaxsC',
                "H_C", "H_CAX", "jeuax"]:
        PlanRef = '(BA)'
        Plan = '(BA)'

    for Hauteur in Hauteurs:
        planeDefinition = {}
        planeDefinition["gridName"] = Aubes
        planeDefinition["planeName_ref"] = PlanRef
        planeDefinition["planeName"] = Plan
        planeDefinition["Name"] = Hauteur
        planeDefinition["hauteur"] = "%s" % Hauteur
        planeDefinition["flux"] = Flux
        graph.addPlaneDefinition(planeDefinition)

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphEvolutionMeridienne(PageName, Aube, XVar, YVar,
                                   Hauteurs=["mean"], SuperpositionCase=0,
                                   PlanRef='AmontPerfo', Plan='*',
                                   Groupe=['CFD'], DicoVariables={},
                                   DicoPrefGraphe={}, DicoUserCurves={},
                                   iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphEvolutionMeridienne")

    # D:\codes\GENEPI\SIMU\CURRENT\GENEPI\src\presentationConstruction\graphiques\evolutionParGrille.py
    DicoVariables = IsVarInDicoVariables(XVar, DicoVariables)
    DicoVariables = IsVarInDicoVariables(YVar, DicoVariables)

    AubeListe = []
    if isinstance(Aube, list):
        for Tuple in Aube:
            AubeListe.append(Tuple[0])
    else:
        AubeListe = [Aube]

    graph = page.addGraph("Meridian",
                          name="%s - %s | %s" % (AubeListe, XVar, YVar))
    graph.showAverage = DicoPrefGraphe["ShowAverage"]
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.Variable = YVar
    graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
    graph.MoyAzi = "5"  # choix du type de moyenne pour l'azimutale
    graph.sortByVar = False
    graph.sortByHeight = True
    graph.moyProf = True
    graph.CaseSuperposition = SuperpositionCase
    graph.VarSuperposition = False
    graph.HeightSuperposition = False
    graph.comparaisonSimple = 1
    graph.comparaisonReference = 0
    # if XVar in DicoUserCurves.keys():
    # graph.courbesUtilisateurGlobales = [XVar]

    for aube in AubeListe:
        for plan in [PlanRef, '*', Plan]:
            planeDefinition = {}
            planeDefinition["gridName_ref"] = aube
            planeDefinition["gridName"] = aube
            planeDefinition["planeName_ref"] = PlanRef
            planeDefinition["planeName"] = plan
            planeDefinition["flux"] = "Total"
            graph.addPlaneDefinition(planeDefinition)

    for Hauteur in Hauteurs:
        HeightDefinition = {}
        HeightDefinition["Height"] = Hauteur
        HeightDefinition["variable"] = YVar
        graph.addHeightDefinition(HeightDefinition)

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphProfilAzimuthaux(PageName, Aube, XVar, YVar, Plan='AvalPerfo',
                                HauteurType='h_H',
                                Hauteurs=[10, 30, 50, 70, 80, 90],
                                CalculDistortion=1, SuperpositionCas=False,
                                SuperpositionPlan=False,
                                SuperpositionHauteur=False, Groupe=['CFD'],
                                DicoVariables={}, DicoPrefGraphe={},
                                DicoUserCurves={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphProfilAzimuthaux")

    # D:\codes\GENEPI\SIMU\CURRENT\GENEPI\src\presentationConstruction\graphiques\ligneAzimutaleConstruction.py
    DicoVariables = IsVarInDicoVariables(XVar, DicoVariables)
    DicoVariables = IsVarInDicoVariables(YVar, DicoVariables)

    graph = page.addGraph("LigneAzimutale",
                          name="%s - %s | %s" % (Aube, XVar, YVar))
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.Variable = YVar
    graph.calculDistortion = 0
    graph.VarSuperposition = SuperpositionCas
    graph.PLaneSuperposition = SuperpositionPlan
    graph.hauteurSuperposition = SuperpositionHauteur
    # graph.comparaisonSimple = 1
    # graph.comparaisonReference = 0
    # if XVar in DicoUserCurves.keys():
    # graph.courbesUtilisateurGlobales = [XVar]
    graph.SuperpositionCase = SuperpositionCas

    if HauteurType == 'QNS3D':
        HauteurType = 'q_Q'
        Hauteurs = [0.1, 0.3, 0.5, 0.7, 0.9]
    elif HauteurType == 'h_H':
        # On repasse les valeurs entre 0 et 1
        if Hauteurs != ['']:
            ListHauteurAdim = []
            for Hauteur in Hauteurs:
                # HauteurAdim = float(Hauteur)/100
                ListHauteurAdim.append("%.2f" % float(Hauteur))
            Hauteurs = ListHauteurAdim
        elif Hauteurs == ['']:
            Hauteurs = ['*']
    else:
        graph.variable = 'q_Q'
        Hauteurs = [0.1, 0.3, 0.5, 0.7, 0.9]

    planeDefinition = {}
    planeDefinition["gridName"] = Aube
    planeDefinition["planeName"] = Plan
    planeDefinition["Name"] = "Hauteurs"
    planeDefinition["hauteur"] = "%s" % Hauteurs
    planeDefinition[
        "VariableHauteur"] = HauteurType  # Depend des extraction Antares (actuellement seulement en Rpct ou R)
    graph.addPlaneDefinition(planeDefinition)

    GraphAddXYVar(graph, XVar, YVar, DicoVariables)

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphVisu(GraphName, DicoImageList, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphVisu")

    # D:\codes\GENEPI\SIMU\CURRENT\GENEPI\src\presentationConstruction\graphiques\ImagesConstruction.py
    graph = page.addGraph("Images", name="%s" % (GraphName))
    graph.DefinitionImages = DicoImageList
    graph.afficher_legende = 1


def CreateGraphVisuGeom(PageName, Aube, Plan, CoupesCarma, TailleMarqueur,
                        DicoPrefGraphe, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphVisuGeom")

    graph = page.addGraph("Geometry", name="%s" % (Aube))
    graph.superpositionCas = 1
    graph.afficherInterfaces = 0  # Permet d'afficher les plans de melange
    graph.afficherBABF = 1
    graph.afficherPlansUtilisateurs = 0
    graph.afficherAubages = 1
    graph.superposerLesCas = 1
    graph.afficherTousLesPlansBSAM = 0
    if Plan != "":
        graph.ajouterPlan(Aube, Plan)
    if isinstance(Aube, list):
        graph.listeGrilles = Aube
    else:
        graph.listeGrilles = [Aube]
    graph.recalagePiedFan = 0
    graph.recalageDiametreFan = 0
    graph.afficherSeparation = 0
    graph.afficherCoupeCarma = CoupesCarma
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.tailleMarker = TailleMarqueur

    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphVisuProfilVsCorde(PageName, Aube, DicoXYVar2Trace,
                                 Groupe=['CFD', 'BSAM'], DicoVariables={},
                                 DicoPrefGraphe={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphVisuProfilVsCorde")

    graph = page.addGraph("StreamLines", name="%s" % (Aube))
    graph.superpositionCas = 1
    graph.groupeAppartenance = Groupe
    graph.listeGrilles = [Aube]
    if DicoXYVar2Trace['HauteurType'] == 'QNS3D':
        graph.variable = 'q_Q'
        graph.hauteurs = DicoXYVar2Trace['HauteurListe']
    elif DicoXYVar2Trace['HauteurType'] == 'h_H':
        graph.variable = 'h_H'
        # On repasse les valeurs entre 0 et 1
        ListNappeAdim = []
        for Nappe in DicoXYVar2Trace['HauteurListe']:
            NappeAdim = float(Nappe) / 100
            ListNappeAdim.append("%.2f" % NappeAdim)
        graph.hauteurs = ListNappeAdim
    elif DicoXYVar2Trace['HauteurType'] == 'QBSAM':
        graph.variable = 'q_Q'
        graph.hauteurs = [0.1, 0.3, 0.5, 0.7,
                          0.9]  # Actuellement on ne peut tracer que les heuteurs en h_H et q_Q. Donc on force le depouillement en q_Q
    else:
        graph.variable = 'q_Q'
        graph.hauteurs = [0.1, 0.3, 0.5, 0.7,
                          0.9]  # Actuellement on ne peut tracer que les heuteurs en h_H et q_Q. Donc on force le depouillement en q_Q

    graph._zoomAuto = 1
    GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube, AubeType,
                             DicoXYVar2Trace, SuperpositionNappe,
                             SuperpositionVar, SuperpositionPlan,
                             SuperpositionCase, ShowDecel, Orthonorme,
                             DicoVariables={}, DicoPrefGraphe={},
                             DicoUserCurves={}, EvolRadiale=False,
                             GarderCouleurCas=1, CouleurFiltre=0,
                             Bornes=(0.0, 1.0), Localisation=['Extrados'],
                             iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphProfilVsCorde")

    HauteurFormatOKList = []
    if not EvolRadiale:
        if 'HauteurCoupeDessins' in DicoXYVar2Trace.keys():
            if DicoXYVar2Trace['HauteurCoupeDessins']:
                HauteurFormatOKList = ['CoupesDessins']
        else:
            for Hauteur in DicoXYVar2Trace['HauteurListe']:
                if Hauteur != '':
                    HauteurFormatOK = '%01d' % Hauteur
                    HauteurFormatOKList.append(HauteurFormatOK)
                else:
                    HauteurFormatOKList = ['']

    CDVarList = ['BSQ', 'BSQ_EXT', 'BSQ_INT', 'Courbure', 'BSQ_adim_8.0pct',
                 'BSQ_EXT_adim_8.0pct', 'EPAIS']

    TypeCoupe = DicoXYVar2Trace.get('HauteurType', "CQ")
    if isinstance(YVar, list):
        for var in YVar:
            if var in CDVarList:
                TypeCoupe = "CD"
    else:
        if YVar in CDVarList:
            TypeCoupe = "CD"

    if EvolRadiale:
        loc = [Localisation]
    else:
        loc = ['tout']

    ListGraph = []
    if isinstance(TypeCoupe, list):
        for Type in TypeCoupe:
            if SuperpositionNappe == 0:
                GraphName = "%s - %s - %s | %s - SUPERPOSE" % (
                Aube, Type, YVar, XVar)
            else:
                GraphName = "%s - %s - %s | %s" % (Aube, Type, YVar, XVar)
            graph = page.addGraph("Machis", name=GraphName)
            graph.ajouterCoupes(gridName=Aube,
                                bladeName='MainBlade',
                                StreamTubeType=Type,
                                StreamTubeList=HauteurFormatOKList,
                                localisation=loc,
                                radialEvolution=EvolRadiale)
            ListGraph.append(graph)
    else:
        if SuperpositionNappe == 0:
            GraphName = "%s - %s - %s | %s - SUPERPOSE" % (
            Aube, TypeCoupe, YVar, XVar)
        else:
            GraphName = "%s - %s - %s | %s" % (Aube, TypeCoupe, YVar, XVar)
        graph = page.addGraph("Machis", name=GraphName)
        graph.ajouterCoupes(gridName=Aube,
                            bladeName='MainBlade',
                            StreamTubeType=TypeCoupe,
                            StreamTubeList=HauteurFormatOKList,
                            localisation=loc,
                            radialEvolution=EvolRadiale)
        ListGraph.append(graph)

    for graph in ListGraph:
        GraphAddXYVar(graph, XVar, YVar, DicoVariables)

        # On force les min/max
        graph.minX = 0
        graph.maxX = 1
        graph.pasX = 0.1

        if isinstance(XVar, list):
            XVar = XVar[0]
        if isinstance(YVar, list):
            YVar = YVar[0]

        # Cas CFD
        try:
            for key in DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType].keys():
                if key in XVar:
                    if DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                        'Min'] != None and \
                            DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                                'Max'] != None:
                        graph.autoScaleModeX = 'Manuel'
                        Xmin = \
                        DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                            'Min']
                        Xmax = \
                        DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                            'Max']
                        graph.minX = Xmin
                        graph.maxX = Xmax
                        graph.pasX = (Xmax - Xmin) / 10
        except:
            pass
        try:
            for key in DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType].keys():
                if key in YVar:
                    if DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                        'Min'] != None and \
                            DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                                'Max'] != None:
                        graph.autoScaleModeY = 'Manuel'
                        Ymin = \
                        DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                            'Min']
                        Ymax = \
                        DicoXYVar2Trace['CourbeProfil_Yvar'][AubeType][key][
                            'Max']
                        graph.minY = Ymin
                        graph.maxY = Ymax
                        graph.pasY = (Ymax - Ymin) / 10
        except:
            pass

        # Cas CARMA
        try:
            for key in DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'].keys():
                if key == XVar:
                    if DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key][
                        'Min'] != None and \
                            DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key][
                                'Max'] != None:
                        graph.autoScaleModeX = 'Manuel'
                        Xmin = \
                        DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key]['Min']
                        Xmax = \
                        DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key]['Max']
                        graph.minX = Xmin
                        graph.maxX = Xmax
                        graph.pasX = (Xmax - Xmin) / 10
        except:
            pass
        try:
            for key in DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'].keys():
                if key == YVar:
                    if DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key][
                        'Min'] != None and \
                            DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key][
                                'Max'] != None:
                        graph.autoScaleModeY = 'Manuel'
                        Ymin = \
                        DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key]['Min']
                        Ymax = \
                        DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][key]['Max']
                        graph.minY = Ymin
                        graph.maxY = Ymax
                        # graph.pasY = (Ymax - Ymin)/10
        except:
            pass

        graph.VarSuperposition = SuperpositionVar
        graph.PLaneSuperposition = SuperpositionPlan
        graph.superpositionCase = SuperpositionCase
        graph.SuperpositionNappe = SuperpositionNappe  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
        graph.sortByPlane = 0
        graph.sortByVar = 0
        # graph.showLegend = DicoPrefGraphe["ShowLegend"]
        if SuperpositionNappe == 0:
            graph.showLegend = 1  # On affiche la legende dans le cas ou on supperpose les coupes
        else:
            graph.showLegend = 0

        if SuperpositionNappe == 0:
            graph.showCaseName = 1
        else:
            graph.showCaseName = DicoPrefGraphe["ShowCaseName"]

        graph.showFlux = DicoPrefGraphe["ShowFlux"]
        graph.showAverage = DicoPrefGraphe["ShowAverage"]
        if ShowDecel and YVar in ['mis3', 'Ue/a0']:
            graph.ShowDecel = ShowDecel
            graph.showLegend = 1
        else:
            graph.ShowDecel = 0
        graph.orthonorme = Orthonorme
        graph.Grid = 1
        graph.borneInfDecel = Bornes[0]
        graph.borneSupDecel = Bornes[1]
        graph.affichageTypeCoupe = 1
        graph.afficherHauteurCoupe = 1
        graph.afficherNomVariableLegende = 1
        graph.separationCouleurIntraExtra = 0
        graph.garderCouleurCas = GarderCouleurCas
        graph.couleurFiltre = CouleurFiltre
        if EvolRadiale:
            graph.tailleMarker = 5
        else:
            graph.tailleMarker = 0
        graph.userCurves = []
        if YVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [
                YVar]  # Non disponible dans ce type de graphique. En revanche, possibilité de rajouter des courbes utilisateurs locales.
        elif XVar in DicoUserCurves.keys():
            graph.courbesUtilisateurGlobales = [XVar]

        GraphPrefAffichage(graph, DicoPrefGraphe)


def CreateGraphGeomVsCorde_Hauteur(PageName, XVar, YVar, Aube, DicoXYVar2Trace,
                                   SuperpositionVar, SuperpositionPlan,
                                   SuperpositionCas, SuperpositionNappe,
                                   SuperpositionBlade, DicoVariables={},
                                   DicoPrefGraphe={}, DicoUserCurves={},
                                   iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : CreateGraphGeomVsCorde_Hauteur")

    graph = page.addGraph(u"Contrôle Lois",
                          name="%s - %s | %s" % (Aube, YVar, XVar))

    if 'HauteurType' not in DicoXYVar2Trace.keys():
        TypeCoupe = "CQ"  # Dans la cas d'import CARMA, les coupes sont automatiquement nommees CQ
    else:
        TypeCoupe = DicoXYVar2Trace['HauteurType']

    # Hauteur = DicoXYVar2Trace['HauteurListe']

    # Localisation = ['Extrados'] # ['tout','Extrados']
    Localisation = ['tout']  # ['tout','Extrados']

    graph.addPlaneDefinition({"gridName": Aube,
                              "bladeName": "MainBlade",
                              "StreamTubeType": TypeCoupe,
                              "StreamTubeList": [''],
                              "localisation": Localisation})

    # GraphAddXYVar(graph, XVar, YVar, DicoVariables) --> Fonction non disponible pour ce type de graphique.

    graph.XVars = [XVar]
    # graph.XVarsUnit = DicoVariables[XVar]['Unite']
    # graph.XVarsCS = [DicoVariables[XVar]['NbreCS']]
    graph.YVar = [YVar]
    # graph.YVarUnit = DicoVariables[YVar]['Unite']
    # graph.YVarCS = DicoVariables[YVar]['NbreCS']

    try:
        if XVar in DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'].keys():
            if DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][XVar][
                'Min'] != None and \
                    DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][XVar][
                        'Max'] != None:
                graph.autoScaleModeX = 'Manuel'
                Xmin = DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][XVar]['Min']
                Xmax = DicoXYVar2Trace['LoisGeomVsCorde_VarMinMax'][XVar]['Max']
                graph.minX = Xmin
                graph.maxX = Xmax
                graph.pasX = (Xmax - Xmin) / 10
    except:
        pass
    # On force les min/max
    graph.minY = 0
    graph.maxY = 1
    graph.pasY = 0.1

    graph.VarSuperposition = SuperpositionVar
    graph.PLaneSuperposition = SuperpositionPlan
    graph.superpositionCase = SuperpositionCas
    graph.SuperpositionNappe = SuperpositionNappe  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
    graph.SuperpositionBlade = SuperpositionBlade

    graph.sortByPlane = 0
    graph.sortByVar = 0
    graph.showLegend = DicoPrefGraphe["ShowLegend"]
    graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
    graph.showFlux = DicoPrefGraphe["ShowFlux"]

    graph.userCurves = []

    graph.Grid = 1
    graph.showAverage = 0
    graph.ShowDecel = 0

    graph.afficherHauteurCoupe = 0
    graph.affichageTypeCoupe = 1

    graph.intervalles = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    graph.variableInterp = "cordeRed"
    graph.VariablesPossibles_variableInterp = ["cordeRed", "absCurvRedExt",
                                               "absCurvRedInt", "squelRed",
                                               "xRedInt", "xRedExt"]

    graph.orthonorme = 0
    graph.separationCouleurIntraExtra = 0

    # cette variable permet de ne tracer que certains groupes
    graph.groupeAppartenance = []

    graph.couleurFiltre = 0
    graph.garderCouleurCas = 1

    GraphPrefAffichage(graph, DicoPrefGraphe)


def GraphAddXYVar(graph, XVar, YVar, DicoVariables={}, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : GraphAddXYVar")

    if isinstance(XVar, list):
        XVarList = XVar
    else:
        XVarList = [XVar]

    for XVar in XVarList:
        DicoVariables = IsVarInDicoVariables(XVar, DicoVariables)

        graph.addVariableX(XVar,
                           unite=DicoVariables[XVar]['Unite'],
                           chiffresSign=int(DicoVariables[XVar]['NbreCS']),
                           renommage=DicoVariables[XVar]['Nom'],
                           mult=DicoVariables[XVar]['FactMulti'],
                           )  # D:\codes\GENEPI\CURRENT\GENEPI\src\presentationConstruction\graphiques\generic2DConstruction.py

        graph.autoScaleModeX = DicoVariables[XVar]['autoScaleMode']
        if DicoVariables[XVar]['autoScaleMode'] == 'Manuel':
            graph.minX = DicoVariables[XVar]['Min']
            graph.maxX = DicoVariables[XVar]['Max']
            # graph.pasX = ""
        else:
            if DicoVariables[XVar]['PGMin'] == None:
                graph.autoScaleXPG_minY = ''
                graph.autoScaleXPG_maxY = ''
            else:
                graph.autoScaleXPG_minY = DicoVariables[XVar]['PGMin']
                graph.autoScaleXPG_maxY = DicoVariables[XVar]['PGMax']
            graph.autoScaleXPG_limiteur = DicoVariables[XVar]['limiteur']

    if isinstance(YVar, list):
        YVarList = YVar
    else:
        YVarList = [YVar]

    for Yvar in YVarList:
        DicoVariables = IsVarInDicoVariables(Yvar, DicoVariables)

        graph.addVariableY(Yvar,
                           unite=DicoVariables[Yvar]['Unite'],
                           chiffresSign=int(DicoVariables[Yvar]['NbreCS']),
                           renommage=str(DicoVariables[Yvar]['Nom']),
                           mult=DicoVariables[Yvar]['FactMulti'])

        graph.autoScaleModeY = DicoVariables[Yvar]['autoScaleMode']
        if DicoVariables[Yvar]['autoScaleMode'] == 'Manuel':
            graph.minY = DicoVariables[Yvar]['Min']
            graph.maxY = DicoVariables[Yvar]['Max']
            graph.pasY = 0.1
        else:
            if DicoVariables[Yvar]['PGMin'] == None:
                graph.autoScaleYPG_minX = ''
                graph.autoScaleYPG_maxX = ''
            else:
                graph.autoScaleYPG_minX = DicoVariables[Yvar]['PGMin']
                graph.autoScaleYPG_maxX = DicoVariables[Yvar]['PGMax']
            graph.autoScaleYPG_limiteur = DicoVariables[Yvar]['limiteur']


def GraphPrefAffichage(graph, DicoPrefGraphe, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : GraphPrefAffichage")

    graph.tailleTitreX = DicoPrefGraphe['TailleTitreX']
    graph.tailleTitreY = DicoPrefGraphe['TailleTitreY']
    graph.tailleTicksX = DicoPrefGraphe['TailleTicksX']
    graph.tailleTicksY = DicoPrefGraphe['TailleTicksY']
    graph.secondGrid = DicoPrefGraphe['ShowSecondGrid']
    graph.legendSize = DicoPrefGraphe['LegendSize']


def GetNcolNRow(NbreAube, Delta, iPrint=False):
    if iPrint:
        print(
            "\n ---------------------------------------------------------------")
        print("                -> def : GetNcolNRow")

    if NbreAube == 1:
        Orientation = "paysage"
        NrowByVar = 1
        NcolByVar = 2
    else:
        Orientation = "paysage"
        if NbreAube <= 4:
            NrowByVar = 1
            NcolByVar = NbreAube
        if NbreAube > 4:
            NrowByVar = 2
            NcolByVar = 4

    return Orientation, NrowByVar, NcolByVar


def TracePerfos0D(NumChap, ListLabelAube, RecalageKDVar=1, AfficherIsoPi_D=1,
                  ModeChamps=0, DicoXYVar2Trace={}, DicoVariables={},
                  DicoPrefGraphe={}, DicoUserCurves={}, iPrint=False):
    # LISTE LABELS GLOBAL/PSEUDO/ETAGE/ROUE
    DicoPerfos0D = {'GLOBAL': [], 'PSEUDO': [], 'ETAGE': [], 'ROUE': []}
    DicoPerfos0DModeComparaison = {'GLOBAL': 'isoPiD', 'PSEUDO': 'isoPiD',
                                   'ETAGE': 'isoPiD',
                                   'ROUE': {'ROTOR': 'isoPiD',
                                            'STATOR': 'isoDstd2'}}
    TypeConfList = ['GLOBAL', 'PSEUDO', 'ETAGE', 'ROUE']
    AubeList = []

    for Flux in DicoFluxAube.keys():
        if DicoFluxAube[Flux] != []:
            if Flux != 'Total':
                if DicoFluxAube['Total'][0] != DicoFluxAube[Flux][-1]:
                    DicoPerfos0D['GLOBAL'].append(([DicoFluxAube['Total'][0],
                                                    DicoFluxAube[Flux][-1]],
                                                   Flux))
                else:
                    DicoPerfos0D['GLOBAL'].append(
                        ([DicoFluxAube[Flux][0], DicoFluxAube[Flux][-1]], Flux))
            else:
                DicoPerfos0D['GLOBAL'].append(
                    ([DicoFluxAube[Flux][0], DicoFluxAube[Flux][-1]], Flux))

            if len(DicoFluxAube[Flux]) > 1:
                for i in range(len(DicoFluxAube[Flux]) - 1):
                    if (i % 2) == 0:
                        if DicoFluxAube[Flux][0] in ListAllGridStatorGlobal:
                            DicoPerfos0D['PSEUDO'].append(([DicoFluxAube[Flux][
                                                                i],
                                                            DicoFluxAube[Flux][
                                                                i + 1]], Flux))
                            if (i + 2) < len(DicoFluxAube[Flux]):
                                DicoPerfos0D['ETAGE'].append(([DicoFluxAube[
                                                                   Flux][i + 1],
                                                               DicoFluxAube[
                                                                   Flux][
                                                                   i + 2]],
                                                              Flux))
                        else:
                            DicoPerfos0D['ETAGE'].append((
                                                         [DicoFluxAube[Flux][i],
                                                          DicoFluxAube[Flux][
                                                              i + 1]], Flux))
                            if (i + 2) < len(DicoFluxAube[Flux]):
                                DicoPerfos0D['PSEUDO'].append(([DicoFluxAube[
                                                                    Flux][
                                                                    i + 1],
                                                                DicoFluxAube[
                                                                    Flux][
                                                                    i + 2]],
                                                               Flux))

            if len(DicoFluxAube[Flux]) >= 1:
                for i in range(len(DicoFluxAube[Flux])):
                    DicoPerfos0D['ROUE'].append((DicoFluxAube[Flux][i], Flux))
                    AubeList.append(DicoFluxAube[Flux][i])

    for Type in TypeConfList:
        print("     --> Perfos0D %s : %s" % (Type, DicoPerfos0D[Type]))

    # PAGE CHAPITRE PERFOS 0D
    PageName = "PERFOS 0D"
    page = pres.addPage(type="Chapitre",
                        name="---- CHAPITRE %s ----" % (PageName))
    page.numeroChapitre = "%i" % (NumChap)
    page.titre = PageName
    NumChap += 1

    if DicoXYVar2Trace['Perfos0D_Tableau']:
        # PAGE TABLEAU INFO KD
        PageName = "PERFOS 0D - TABLEAU KD"
        print("   - %s" % PageName)
        page = pres.addPage(type="Standard", name="%s" % (PageName))

        SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)

        ListAubeTemp = []
        j = 0
        if len(AubeList) <= Treshold:
            graph = page.addGraph("Verif KD", name="%s" % (AubeList))
            # graph.title = "KD"
            graph.UtiliserCouleurCas = 1
            graph.listeAubage = AubeList
        else:
            for i in range(0, len(AubeList)):
                print(
                    " i : %s , j : %s ListAubeTemp : %s" % (i, j, ListAubeTemp))
                if j <= Treshold:
                    ListAubeTemp.append(AubeList[i])
                    j += 1
                else:
                    j = 0
                    graph = page.addGraph("Verif KD",
                                          name="%s" % (ListAubeTemp))
                    # graph.title = "KD"
                    graph.UtiliserCouleurCas = 1
                    graph.listeAubage = ListAubeTemp
                    ListAubeTemp = []

        # PAGE TABLEAU PERFOS 0D
        if not ModeChamps:
            for PlanVsPlanRef in DicoXYVar2Trace['Perfos0D_Plan']:

                for TypeConf in TypeConfList:

                    for Tuple in DicoPerfos0D[TypeConf]:

                        PageName = "PERFOS 0D - TABLEAU  - %s (%s|%s) - %s" % (
                        TypeConf, PlanVsPlanRef[0], PlanVsPlanRef[1], Tuple)
                        print("   - %s" % PageName)
                        page = pres.addPage(type="Standard",
                                            name="%s" % (PageName))
                        SetPageProperties(page, Orientation="paysage", Nrow=1,
                                          Ncol=1)

                        Aube = Tuple[0]
                        Flux = Tuple[1]
                        if isinstance(Aube, list):
                            AubeAmont = Aube[0]
                            AubeAval = Aube[1]
                        else:
                            AubeAmont = Aube
                            AubeAval = Aube

                        if TypeConf == 'ROUE' and Aube in ListAllGridStatorGlobal:
                            XYVarPerfosList = \
                            DicoXYVar2Trace['Perfos0D_TableauXYvar']['STATOR']
                        else:
                            XYVarPerfosList = \
                            DicoXYVar2Trace['Perfos0D_TableauXYvar']['ROTOR']

                        graph = page.addGraph("Table Perfo0D",
                                              name="%s - %s" % (
                                              AubeAmont, AubeAval))
                        for Var in XYVarPerfosList:
                            if True in RecalageKDVarList:
                                if "Qcorr" in Var:
                                    Var = "%s_KD" % Var
                            print("         * VARIABLE: %s" % (Var))
                            GraphAddXYVar(graph, Var, Var, DicoVariables)

                        graph.PlaneDefinition = [
                            {"gridName_ref": "%s" % AubeAmont,
                             "gridName": "%s" % AubeAval,
                             "planeName_ref": "%s" % PlanVsPlanRef[0],
                             "planeName": "%s" % PlanVsPlanRef[1],
                             "flux": Flux,
                             "Name": ""}]

                        graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
                        graph.showFlux = DicoPrefGraphe["ShowFlux"]
                        graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
                        graph.UtiliserCouleurCas = 1

                        GraphPrefAffichage(graph, DicoPrefGraphe)

    # PAGE PERFOS 0D - CHAMPS
    if Trace_ParVariable:
        for PlanVsPlanRef in DicoXYVar2Trace['Perfos0D_Plan']:
            PageName = "PERFOS 0D - CHAMPS (%s|%s)" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            print("   - %s" % PageName)
            XYVarPerfosList = DicoXYVar2Trace['Perfos0D_XYvar']['ROTOR']

            for TypeConf in TypeConfList:
                AddPage = True

                for XYVarPerfos in XYVarPerfosList:

                    for Tuple in DicoPerfos0D[TypeConf]:
                        Aube = Tuple[0]
                        Flux = Tuple[1]
                        if isinstance(Aube, list):
                            AubeAmont = Aube[0]
                            AubeAval = Aube[1]
                        else:
                            AubeAmont = Aube
                            AubeAval = Aube

                        if AddPage:
                            page = pres.addPage(type="Standard",
                                                name="%s - %s" % (
                                                PageName, TypeConf))
                            if ModeChamps:
                                if TypeConf == 'GLOBAL':
                                    SetPageProperties(page,
                                                      Orientation="paysage",
                                                      Nrow=1, Ncol=1)
                                else:
                                    SetPageProperties(page,
                                                      Orientation="portrait",
                                                      Nrow=DicoNbreGraphe[
                                                          'Perfos0DChamps'][
                                                          'Nrow'], Ncol=
                                                      DicoNbreGraphe[
                                                          'Perfos0DChamps'][
                                                          'Ncol'])
                            else:
                                SetPageProperties(page, Orientation="paysage",
                                                  Nrow=
                                                  DicoNbreGraphe['Perfos0D'][
                                                      'Nrow'], Ncol=
                                                  DicoNbreGraphe['Perfos0D'][
                                                      'Ncol'])
                            AddPage = False

                        graph = page.addGraph("Champs", name="%s - %s" % (
                        Aube, XYVarPerfos))
                        if TypeConf == 'ROUE':
                            if Aube in ListAllGridStatorGlobal:
                                ModeComparaison = \
                                DicoPerfos0DModeComparaison[TypeConf]['STATOR']
                            else:
                                ModeComparaison = \
                                DicoPerfos0DModeComparaison[TypeConf]['ROTOR']
                        else:
                            ModeComparaison = DicoPerfos0DModeComparaison[
                                TypeConf]
                        graph.methode_comparaison = ModeComparaison
                        # print("         * MODE DE COMPARAISON: %s"%(ModeComparaison))

                        XVar = XYVarPerfos[0]
                        YVar = XYVarPerfos[1]

                        AddGraph = True
                        if XVar in ['XNR', 'W2_W1_RAL'] or YVar in ['XNR',
                                                                    'W2_W1_RAL']:
                            if AubeAmont in ListAllGridStatorGlobal or AubeAval in ListAllGridStatorGlobal:
                                AddGraph = False
                        if XVar in ['Dev'] or YVar in ['Dev']:
                            if TypeConf != 'ROUE':
                                AddGraph = False

                        if AddGraph:
                            if Aube in ListAllGridStatorGlobal:
                                if XVar == 'etapol': XVar = 'cd_fftro'
                                if YVar == 'etapol': YVar = 'cd_fftro'

                            # print("         * VARIABLE: { X: %s   , Y: %s}"%(XVar,YVar))
                            # GraphAddXYVar(graph, XVar, YVar, DicoVariables)

                            if True in RecalageKDVarList:
                                if "Qcorr" in XVar: XVar = "%s_KD" % XVar
                                if "Qcorr" in YVar: YVar = "%s_KD" % YVar
                            print("         * VARIABLE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                            GraphAddXYVar(graph, XVar, YVar, DicoVariables)

                            graph.ajouterPlan(gridName_ref="%s" % AubeAmont,
                                              gridName="%s" % AubeAval,
                                              planeName_ref="%s" %
                                                            PlanVsPlanRef[0],
                                              planeName="%s" % PlanVsPlanRef[1],
                                              flux=Flux,
                                              name="",
                                              hauteur="")

                            graph.ajouterPlanbis(gridName_ref="%s" % AubeAmont,
                                                 gridName="%s" % AubeAval,
                                                 planeName_ref="%s" %
                                                               PlanVsPlanRef[0],
                                                 planeName="%s" % PlanVsPlanRef[
                                                     1],
                                                 flux=Flux,
                                                 name="",
                                                 hauteur="")

                            graph.VarSuperposition = False
                            graph.PLaneSuperposition = 0
                            graph.sortByVar = False
                            graph.sortByPlane = False
                            graph.showAverage = DicoPrefGraphe["ShowAverage"]
                            graph.showFlux = DicoPrefGraphe["ShowFlux"]
                            graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
                            graph.showLegend = DicoPrefGraphe["ShowLegend"]
                            graph.modeMatriciel = 0
                            graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
                            graph.groupesATracer = []
                            graph.isoATracer = []
                            graph.afficherVannage = 0
                            graph.AfficherIsoPi_D = AfficherIsoPi_D
                            if XVar in DicoUserCurves.keys():
                                graph.courbesUtilisateurGlobales = [
                                    XVar]  # liste des courbes globales à afficher
                            graph.afficherTitreIso = 0  # permet d'afficher le titre de l'iso sur le graphique
                            # graph.tailleMarker = 10
                            GraphPrefAffichage(graph, DicoPrefGraphe)
    else:
        for PlanVsPlanRef in DicoXYVar2Trace['Perfos0D_Plan']:
            PageName = "PERFOS 0D - CHAMPS (%s|%s)" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            print("   - %s" % PageName)
            for TypeConf in TypeConfList:
                for Tuple in DicoPerfos0D[TypeConf]:
                    Aube = Tuple[0]
                    Flux = Tuple[1]

                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    if ModeChamps:
                        if TypeConf == 'GLOBAL':
                            SetPageProperties(page, Orientation="paysage",
                                              Nrow=1, Ncol=1)
                        else:
                            SetPageProperties(page, Orientation="portrait",
                                              Nrow=
                                              DicoNbreGraphe['Perfos0DChamps'][
                                                  'Nrow'], Ncol=
                                              DicoNbreGraphe['Perfos0DChamps'][
                                                  'Ncol'])
                    else:
                        SetPageProperties(page, Orientation="paysage",
                                          Nrow=DicoNbreGraphe['Perfos0D'][
                                              'Nrow'],
                                          Ncol=DicoNbreGraphe['Perfos0D'][
                                              'Ncol'])

                    if isinstance(Aube, list):
                        AubeAmont = Aube[0]
                        AubeAval = Aube[1]
                    else:
                        AubeAmont = Aube
                        AubeAval = Aube

                    graph = page.addGraph("Champs", name="%s" % (Aube))

                    if TypeConf == 'ROUE':
                        if Aube in ListAllGridStatorGlobal:
                            ModeComparaison = \
                            DicoPerfos0DModeComparaison[TypeConf]['STATOR']
                        else:
                            ModeComparaison = \
                            DicoPerfos0DModeComparaison[TypeConf]['ROTOR']
                    else:
                        ModeComparaison = DicoPerfos0DModeComparaison[TypeConf]
                    graph.methode_comparaison = ModeComparaison
                    # print("         * MODE DE COMPARAISON: %s"%(ModeComparaison))

                    if TypeConf == 'ROUE' and Aube in ListAllGridStatorGlobal:
                        XYVarPerfosList = DicoXYVar2Trace['Perfos0D_XYvar'][
                            'STATOR']
                    else:
                        XYVarPerfosList = DicoXYVar2Trace['Perfos0D_XYvar'][
                            'ROTOR']

                    for XYVarPerfos in XYVarPerfosList:
                        XVar = XYVarPerfos[0]
                        YVar = XYVarPerfos[1]

                        AddGraph = True
                        if 'XNR' in XVar or 'XNR' in YVar:
                            if AubeAmont in ListAllGridStatorGlobal or AubeAval in ListAllGridStatorGlobal:
                                AddGraph = False

                        if AddGraph:
                            if True in RecalageKDVarList:
                                if "Qcorr" in XVar: XVar = "%s_KD" % XVar
                                if "Qcorr" in YVar: YVar = "%s_KD" % YVar
                            print("         * VARIABLE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                            GraphAddXYVar(graph, XVar, YVar, DicoVariables)

                    graph.ajouterPlan(gridName_ref="%s" % AubeAmont,
                                      gridName="%s" % AubeAval,
                                      planeName_ref="%s" % PlanVsPlanRef[0],
                                      planeName="%s" % PlanVsPlanRef[1],
                                      flux=Flux,
                                      name="",
                                      hauteur="")

                    graph.ajouterPlanbis(gridName_ref="%s" % AubeAmont,
                                         gridName="%s" % AubeAval,
                                         planeName_ref="%s" % PlanVsPlanRef[0],
                                         planeName="%s" % PlanVsPlanRef[1],
                                         flux=Flux,
                                         name="",
                                         hauteur="")

                    graph.VarSuperposition = False
                    graph.PLaneSuperposition = 0
                    graph.sortByVar = False
                    graph.sortByPlane = False
                    graph.showAverage = DicoPrefGraphe["ShowAverage"]
                    graph.showFlux = DicoPrefGraphe["ShowFlux"]
                    graph.showCaseName = DicoPrefGraphe["ShowCaseName"]
                    graph.showLegend = DicoPrefGraphe["ShowLegend"]
                    graph.modeMatriciel = 0
                    graph.typeMoyOD = ProfileManager().getSelectedProfile().getMoyenne0DDefaut()
                    graph.groupesATracer = []
                    graph.isoATracer = []
                    graph.afficherVannage = 0
                    graph.AfficherIsoPi_D = AfficherIsoPi_D
                    if XVar in DicoUserCurves.keys():
                        graph.courbesUtilisateurGlobales = [
                            XVar]  # liste des courbes globales à afficher
                    graph.afficherTitreIso = 0  # permet d'afficher le titre de l'iso sur le graphique
                    # graph.tailleMarker = 10

                    GraphPrefAffichage(graph, DicoPrefGraphe)


# ------------------------------------------------------------------------------------------------
import os, sys, numpy, xlrd, string, time, glob, datetime

sys.path.insert(0, r"./modules")
os.environ["ModeGENEPI"] = "batch"
import ftpclient
import h5py
from src.chaining.MainApp import MainApp
from src.core.ProfileManager import ProfileManager
from src.customization.Customization import Customization
from modules.CaseReport.CaseReport import caseParameters
from src.chaining.CasesDefinition import CasesDefinition
from src.chaining.UserFormula import UserFormula
from src.chaining.UserCurveDefinition import UserCurvesDefinition
from src.presentationConstruction.userCurve import userCurve

ExportPath = os.path.abspath(os.path.split(__file__)[0])
ScriptName, fileExtension = os.path.splitext(os.path.split(__file__)[-1])

ConnexionStatus = ConnexionStatus()

print(
    "\n--------------------------------------------------------------------------------------")
print(
    "------------------                EXECUTION SCRIPT                --------------------")
print(
    "--------------------------------------------------------------------------------------\n")
print(
    " ====================       ACCES A LA BASE CANNELLE : %s       ====================\n" % ConnexionStatus)
print(" * LISTE DU(DES) AUBE(S) A TRACER : ")

NbreAube = 0
ListFlux = ['Total', 'Primaire', 'Secondaire']
ListTupleLabelAube2Trace = []
ListLabelAube2TraceAll = []
for Flux in ListFlux:
    if DicoLabelAube2Trace[Flux] != []:
        NbreAube = NbreAube + len(DicoLabelAube2Trace[Flux])
        print("       - Flux %s : %s (%s Aube(s))" % (
        Flux, DicoLabelAube2Trace[Flux], len(DicoLabelAube2Trace[Flux])))
        for Label in DicoLabelAube2Trace[Flux]:
            ListTupleLabelAube2Trace.append((Label, Flux))
            ListLabelAube2TraceAll.append(Label)

# ON RECUPERE LA LISTE DES CAS A TRAITER
CFDCaseList = []
BSAMCaseList = []
CARMACaseList = []
for key in sorted(locals().keys()):
    if key.upper().startswith('INFOCASCFD'):
        InfoCase = locals().get(key)
        CFDCaseList.append(InfoCase)
    if key.upper().startswith('INFOCASBSAM'):
        InfoCase = locals().get(key)
        BSAMCaseList.append(InfoCase)
    if key.upper().startswith('INFOCASCARMA'):
        InfoCase = locals().get(key)
        CARMACaseList.append(InfoCase)

print("\n * NOMBRE CAS CFD A TRAITER : %s" % len(CFDCaseList))
for iCase in range(len(CFDCaseList)):
    print("       - (%s/%s) : %s" % (
    iCase + 1, len(CFDCaseList), CFDCaseList[iCase]))

print("\n * NOMBRE CAS BSAM A TRAITER : %s" % len(BSAMCaseList))
for iCase in range(len(BSAMCaseList)):
    print("       - (%s/%s) : %s" % (
    iCase + 1, len(BSAMCaseList), BSAMCaseList[iCase]))

print("\n * NOMBRE CAS CARMA A TRAITER : %s" % len(CARMACaseList))
for iCase in range(len(CARMACaseList)):
    print("       - (%s/%s) : %s" % (
    iCase + 1, len(CARMACaseList), CARMACaseList[iCase]))

print(
    "--------------------------------------------------------------------------------------\n")

if ProfileName == None:
    if IsBiFlux:
        ProfileManager().setSelectedProfileTitle("Compresseur BP")
    else:
        ProfileManager().setSelectedProfileTitle("Compresseur HP")

# ~\GENEPI\src\chaining\MainApp.py
App = MainApp()
App.resetAll()
App.resetListIso()

TIME = str(time.strftime('%y%m%d_%Hh%M', time.localtime()))
USER = os.environ.get('USER', os.environ.get('USERNAME', '?'))
PresName = '%s_%s_%s' % (ScriptName, USER, TIME)

# On initialise les variables.
ListAllGridStatorGlobal = []
DeltaGraph = []  # Permet de savoir si l'utilisateur a demandé une comparaison a un cas de réference
Treshold = 4  # Nombre de d'aube maximum traité pour le tableau des perfos 0D afin que le tableau reste lisible
RecalageKDVar = 0
RecalageKDVarList = []  # indique si on doit tracer Qcorr_ref et/ou Qcorr_ref_KD

print("\n-----------------------------------------------------------")

# ===============================================================================
#   AJOUT GROUPE
print("  * ON AJOUTE LES GROUPES")
App.ajouterGroupe(['MISES', 'CFD', 'BSAM', 'CARMA'])
print("-----------------------------------------------------------")

# ===============================================================================
#   AJOUT FORMULE
if DicoUserFormula != {}:
    print("  * ON AJOUTE LES FORMULES UTILISATEURS")
    AddFormula(DicoUserFormula)
    for Key in DicoUserFormula.keys():
        print("         * %s : %s = %s" % (
        Key, DicoUserFormula[Key]['Var'], DicoUserFormula[Key]['Equation']))
print("-----------------------------------------------------------")

# ===============================================================================
#   AJOUT COURBES UTILISATEURS
if DicoUserCurves != {}:
    print("  * ON AJOUTE LES COURBES UTILISATEURS")
    AddUserCurves(DicoUserCurves)
    for Key in DicoUserCurves.keys():
        print("         * %s : %s = %s" % (
        Key, DicoUserCurves[Key]['X'], DicoUserCurves[Key]['Y']))
print("-----------------------------------------------------------")

# ===============================================================================
#   CASE DEFINITION
caseDef = App.getCaseDefinition()

# ===============================================================================
#   AJOUT CAS CFD
DicoInfoAubeCFD = {}
DataTypeList = []
if CFDCaseList != []:
    print("  * ON AJOUTE LES CAS CFD")
    SetIso = 1
    for index, DicoCase in enumerate(CFDCaseList):
        TrierIso = DicoCase.get('TrierIso', 0)
        MisesDetectionCoupeAuto = DicoCase.get('MisesDetectionCoupeAuto', 0)
        CheminCas = DicoCase.get('CheminCas', '')
        TitreCas = DicoCase.get('TitreCas', '')
        DicoCase['TitreIso'] = TitreCas

        if MisesDetectionCoupeAuto:
            print(
                "          * DETECTION AUTOMATIQUE DES COUPES CONTENUE DANS LE CAS MISES")
            CheminCasParent = CheminCas
            print("                  --> %s" % CheminCasParent)
            if os.path.exists(CheminCasParent):
                Folders = os.listdir(CheminCasParent)
                CheminCas = []  # On initialise la liste
                for folder in Folders:
                    FolderPath = os.path.join(CheminCasParent, folder)
                    if os.path.isdir(FolderPath):
                        CheminCas.append(FolderPath)
                if not CheminCas:
                    print(
                        "             --> AUCUN DOSSIER DE TYPE 'CQ' TROUVE A CET EMPLACEMENT : %s" % CheminCasParent)
            else:
                print(
                    "             --> CHEMIN INEXISTANT : %s" % CheminCasParent)
                CheminCas = ''

        if CheminCas != '':
            Case2Add = False
            if isinstance(CheminCas, list):
                CFDCasePath = CheminCas
                for Cas in CheminCas:
                    print(
                        "     --> ON TENTE D'AJOUTER LE CAS CFD SUIVANT : %s" % (
                            Cas))

                    if "\\" in Cas or "/" in Cas:
                        IsCasPath = True
                    else:
                        IsCasPath = False
                    # print("            --> IsCasPath : %s"%(IsCasPath))

                    if MisesDetectionCoupeAuto:
                        Coupe = os.path.basename(Cas)
                        DicoCase['TitreCas'] = "%s - %s" % (TitreCas, Coupe)
                    else:
                        if len(CheminCas) > 1:
                            if IsCasPath:
                                if os.path.basename(Cas) == 'post':
                                    DicoCase['TitreCas'] = os.path.basename(
                                        os.path.dirname(Cas)).replace("case_",
                                                                      "")
                                else:
                                    DicoCase['TitreCas'] = os.path.basename(
                                        Cas).replace("case_", "")
                            else:
                                DicoCase['TitreCas'] = Cas.replace("case_", "")

                    # print("            --> TitreCas : %s"%(DicoCase['TitreCas']))
                    Case2Add, DataType, CFDCasePath, RecalageKDVar, DicoInfoAube = AddCFDCase(
                        Cas, SetIso, TrierIso, DicoCase)

            else:
                print("     --> ON TENTE D'AJOUTER LE CAS CFD SUIVANT : %s" % (
                    CheminCas))
                # print("            --> TitreCas : %s"%(DicoCase['TitreCas']))
                Case2Add, DataType, CFDCasePath, RecalageKDVar, DicoInfoAube = AddCFDCase(
                    CheminCas, SetIso, TrierIso, DicoCase)

            if Case2Add:
                print(
                    "\n          --> CAS CFD AJOUTE (YOUHOU !!!) : %s (%s / %s)\n" % (
                    CFDCasePath, DicoCase.get("Couleur", "Black"),
                    DicoCase.get("Ligne", "SolidLine")))
                DataTypeList.append(DataType)
                DicoInfoAubeCFD.update(DicoInfoAube)
                RecalageKDVarList.append(RecalageKDVar)

            CFDCaseList[index]['CFDCasePath'] = CFDCasePath

    print("-----------------------------------------------------------")

# ===============================================================================
#   AJOUT CAS BSAM
if BSAMCaseList != []:
    print("  * ON AJOUTE LES CAS BSAM")

    for DicoCase in BSAMCaseList:
        print("     --> CAS BSAM : %s (%s / %s)\n" % (
        DicoCase['CheminBsam'], DicoCase.get("Couleur", "Black"),
        DicoCase.get("Ligne", "SolidLine")))
        TitreCas = DicoCase.get('TitreCas', '')
        DicoCase['TitreIso'] = TitreCas
        DicoCase['TitreCas'] = TitreCas
        if isinstance(DicoCase["CheminBsam"], list):
            for CheminBsam in DicoCase["CheminBsam"]:
                DicoCase['TitreCas'] = os.path.basename(CheminBsam)
                AddBSAMCase(DicoCase['TitreCas'], CheminBsam, DicoCase, 'BSAM',
                            1)
        else:
            AddBSAMCase(DicoCase['TitreCas'], DicoCase["CheminBsam"], DicoCase,
                        'BSAM', 1)
        print("-----------------------------------------------------------")

# ===============================================================================
#   AJOUT CAS CARMA
DicoInfoAubeCARMA = {"Grilles": [], "TypeCoupes": []}
if CARMACaseList != []:
    print("  * ON AJOUTE LES CAS CARMA")

    for DicoCase in CARMACaseList:
        PVA = "%s_%s_%s" % (
        DicoCase["Projet"], DicoCase["Version"], DicoCase["Aube"])
        if isinstance(DicoCase["Grille"], list):
            for Grille in DicoCase["Grille"]:
                DicoInfoAubeCARMA["Grilles"].append(Grille)
        else:
            DicoInfoAubeCARMA["Grilles"].append(DicoCase["Grille"])

        DicoCase["TypeCoupe"] = DicoCase.get("TypeCoupe",
                                             len(DicoCase["Aube"]) * ["CQ"])
        for TypeCoupe in DicoCase["TypeCoupe"]:
            if TypeCoupe not in DicoInfoAubeCARMA["TypeCoupes"]:
                DicoInfoAubeCARMA["TypeCoupes"].append(TypeCoupe)
        print("     --> CAS CARMA : %s (%s | %s)\n" % (
        PVA, DicoCase.get("Couleur", "Black"),
        DicoCase.get("Ligne", "SolidLine")))
        AddCARMACase(DicoCase)
    print("-----------------------------------------------------------")

if CFDCaseList == []:
    AfficherIsoPi_D = 0
else:
    AfficherIsoPi_D = 1
# ===============================================================================
# ECRITURE DE LA PRESENTATION
NumChapRoue = 1

print("  * ON ECRIT LA PRESENTATION")
pres = App.addNewPresentation(PresName)

# PAGE DE GARDE
page = pres.addPage(type="Page de garde", name="PAGE DE GARDE")
page.titre = TitrePres

# PAGE SOMMAIRE
page = pres.addPage(type="Sommaire",
                    name="SOMMAIRE ")  # Non fonctionnel --> Sommaire avec lien dynamique afin de pouvoir se deplacer dans la presentation

# PAGE INFORMATION CAS
if Trace_InfosCas:
    # PAGE CHAPITRE INFORMATION CAS
    PageName = "INFOS CAS"
    page = pres.addPage(type="Chapitre",
                        name="---- CHAPITRE %s ----" % (PageName))
    page.numeroChapitre = "%i" % (NumChapRoue)
    page.titre = PageName
    NumChapRoue += 1

    # PAGE LISTE CAS CFD / BSAM / CARMA
    PageName = "LISTE CAS"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)
    graph = page.addGraph("ListeCas", name="%s" % (PageName))
    graph.UtiliserCouleurCas = 1
    graph.groupeAppartenance = ['CFD', 'BSAM', 'CARMA']

# PAGE TABLEAU INFO PLANS UTILISATEURS
if Trace_InfosPlanUtilisateur:
    PageName = "VISU GEOM"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)
    ListLabelAube = []
    for Tuple in ListTupleLabelAube2Trace:
        Aube = Tuple[0]
        Flux = Tuple[1]
        ListLabelAube.append(Aube)
    CreateGraphVisuGeom(PageName, ListLabelAube, "", 0, 1, DicoPrefGraphe)

    PageName = "TABLEAU PLAN UTILISATEUR"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)

    ListAubeTemp = []
    j = 0
    if len(ListLabelAube2TraceAll) == 1:
        graph = page.addGraph("Controle Plans Utilisateur",
                              name="%s" % (ListLabelAube2TraceAll[0]))
        graph.listeAubage = ListLabelAube2TraceAll
        graph.groupeAppartenance = ['CFD', 'BSAM']
        GraphPrefAffichage(graph, DicoPrefGraphe)
    else:
        for i in range(0, len(ListLabelAube2TraceAll)):
            # print(" i : %s , j : %s"%(i,j))
            if j <= 1:
                ListAubeTemp.append(ListLabelAube2TraceAll[i])
                j += 1
            else:
                graph = page.addGraph("Controle Plans Utilisateur",
                                      name="%s" % (ListAubeTemp))
                graph.listeAubage = ListAubeTemp
                graph.groupeAppartenance = ['CFD', 'BSAM']
                GraphPrefAffichage(graph, DicoPrefGraphe)
                j = 0
                ListAubeTemp = []

# PAGE VERIFICATION MAILLAGE
if Trace_QualiteMaillage and CFDCaseList != []:
    PageName = "TABLEAU QUALITE MAILLAGE"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)
    graph = page.addGraph("Check Maillage", name="%s" % (PageName))
    graph.UtiliserCouleurCas = 1

# PAGE VISUALISATION MAILLAGE
if Trace_VisuQualiteMaillage and CFDCaseList != []:
    PageName = "VISU MAILLAGE"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="portrait",
                      Nrow=DicoNbreGraphe['VisuMESH']['Nrow'],
                      Ncol=DicoNbreGraphe['VisuMESH']['Ncol'])

    ListVisuTuple = [('Meridien', 'FullView'), ('Meridien', 'ZoomShroud'),
                     ('Meridien', 'ZoomHub'), ('B2B', 'FullView'),
                     ('B2B', 'ZoomBA'), ('B2B', 'ZoomBF'),
                     ('Meridien', 'ZoomMixingPlane')]

    for CFDCase in CFDCaseList:
        CFDCasePath = CFDCase.get('CFDCasePath', '')
        if os.path.exists(CFDCasePath):
            GraphName = os.path.basename(os.path.basename(CFDCasePath))
            for Tuple in ListVisuTuple:
                DicoImageList = []
                for File in glob.glob(
                        os.path.join(CFDCasePath, 'mesh', 'Visu', '*')):
                    print(File)
                    if Tuple[0] in File and Tuple[1] in File:
                        FileName = os.path.basename(File)
                        DicoImage = {'name': FileName, 'chemin': File}
                        DicoImageList.append(DicoImage)
                if len(DicoImageList) != 0:
                    CreateGraphVisu(
                        "%s - %s %s" % (GraphName, Tuple[0], Tuple[1]),
                        DicoImageList, False)

# PAGE CONVERGENCE DEBIT
if Trace_ConvDebit and CFDCaseList != []:
    PageName = "CONV DEBIT"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage",
                      Nrow=DicoNbreGraphe['Convergence']['Nrow'],
                      Ncol=DicoNbreGraphe['Convergence']['Ncol'])

    graph = page.addGraph("analyseConvergenceelsA", name="%s" % (PageName))
    graph.afficherCasSansGradients = 0
    graph.listeGrilles = ['In_Out']
    graph.afficherDebit = 1
    graph.afficherDelta = 0
    graph.afficherPgenTgen = 0
    graph.ConserverCouleurCas = 1
    graph.superposerLesCas = 0
    GraphPrefAffichage(graph, DicoPrefGraphe)

    graph = page.addGraph("analyseConvergenceelsA",
                          name="%s - Delta" % (PageName))
    graph.afficherCasSansGradients = 0
    graph.listeGrilles = ['In_Out']
    graph.afficherDebit = 0
    graph.afficherDelta = 1
    graph.afficherPgenTgen = 1
    graph.ConserverCouleurCas = 1
    graph.superposerLesCas = 0
    graph.minY = -2
    graph.maxY = 2
    graph.pasY = 0.5

    GraphPrefAffichage(graph, DicoPrefGraphe)

# PAGE CONVERGENCE RESIDUS
if Trace_ConvResidus and CFDCaseList != []:
    PageName = "CONV RESIDUS"
    page = pres.addPage(type="Standard", name="%s" % (PageName))
    SetPageProperties(page, Orientation="paysage",
                      Nrow=DicoNbreGraphe['Convergence']['Nrow'],
                      Ncol=DicoNbreGraphe['Convergence']['Ncol'])
    graph = page.addGraph("analyseConvergenceelsA", name="%s" % (PageName))

    GraphPrefAffichage(graph, DicoPrefGraphe)

# PAGE PERFOS 0D
if Trace_Perfos0D:
    if ModeChamps:
        TracePerfos0D(NumChapRoue, ListLabelAube2TraceAll, RecalageKDVar,
                      AfficherIsoPi_D, ModeChamps,
                      DicoXYVarPerfos0D2Trace_Champs, DicoVariables,
                      DicoPrefGraphe, DicoUserCurves)
    else:
        TracePerfos0D(NumChapRoue, ListLabelAube2TraceAll, RecalageKDVar,
                      AfficherIsoPi_D, ModeChamps, DicoXYVarPerfos0D2Trace,
                      DicoVariables, DicoPrefGraphe, DicoUserCurves)

if Trace_ParVariable:

    # PAGE GEOMETRIE
    if Trace_LoisGeom and CARMACaseList != []:
        # PAGE CHAPITRE GEOMETRIE
        PageName = "GEOMETRIE"
        page = pres.addPage(type="Chapitre",
                            name="---- CHAPITRE %s ----" % (PageName))
        page.numeroChapitre = "%i" % (NumChapRoue)
        page.titre = PageName
        NumChapRoue += 1

        # PAGE VUE MERIDIENNE
        if DicoXYVarLoisGeom['LoisGeomVisuMeridenne_2trace']:
            PageName = "VISU GEOM MERIDIENNE"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage", Nrow=NrowByVar,
                              Ncol=NcolByVar)
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphVisuGeom(PageName, Aube, [], 1, 0, DicoPrefGraphe)

        # PAGE LOIS GEOMETRIQUES
        if DicoXYVarLoisGeom['LoisGeomVsHauteur_2trace']:
            PageName = "LOIS GEOM"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage", Nrow=NrowByVar,
                              Ncol=NcolByVar)
            # TypeCoupes = DicoInfoAubeCARMA["TypeCoupes"]
            TypeCoupes = "CQ"  # On force le tracé des lois sur les coupes CQ
            PlanAmont = "BA"
            PlanAval = "BF"
            for Tuple in DicoXYVarLoisGeom['LoisGeom_XYvar']:
                XVar = Tuple[0]
                YVar = Tuple[1]
                print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    if XVar in ["Comparaison beta1", "Comparaison beta2",
                                "INCD", "EFP", "DLI", "PSIA"]:
                        CreateGraphGradient(PageName, Aube, Flux, XVar, YVar,
                                            False, PlanAmont, PlanAval,
                                            ['CARMA', 'BSAM'], DicoVariables,
                                            DicoPrefGraphe, DicoUserCurves,
                                            InterpDir='h_H')
                        # if Trace_GradientMoyAdim: CreateGraphGradient(PageName, Aube, Flux, XVar ,YVar, False, PlanAmont, PlanAval, ['CARMA', 'BSAM'], DicoVariables, DicoPrefGraphe, {}, InterpDir = 'h_H', MoyAdim = 1)

                    elif XVar in ["Marge", "ACol/S", "ACol/AEntree",
                                  "ASortie/ACol", "SCol/SX", "XCol/CX",
                                  "Mach Entree", "Mach Sortie"]:
                        CreateGraphMarge(PageName, Aube, XVar, YVar, False,
                                         TypeCoupes[0], DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)
                    else:
                        SuperpositionPlan = 0
                        SuperpositionCase = 1
                        SuperpositionBlade = 0
                        if isinstance(XVar, list):
                            SuperpositionVar = 1
                        else:
                            SuperpositionVar = 0
                        CreateGraphLoiGeom(PageName, Aube, XVar, YVar,
                                           TypeCoupes, DicoVariables,
                                           SuperpositionVar, SuperpositionPlan,
                                           SuperpositionCase,
                                           SuperpositionBlade,
                                           ['CARMA', 'BSAM'], DicoPrefGraphe,
                                           DicoUserCurves)

        # PAGE LOIS Vs CORDE
        if DicoXYVarLoisGeom['LoisGeomVsCorde_2trace']:
            PageName = "LOIS GEOM Vs CORDE"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage", Nrow=NrowByVar,
                              Ncol=NcolByVar)

            for Tuple in DicoXYVarLoisGeom['LoisGeomVsCorde_XYvar']:
                XVar = Tuple[1]
                YVar = Tuple[0]
                print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
                SuperpositionCase = 1
                SuperpositionPlan = 1
                if isinstance(YVar, list):
                    SuperpositionVar = 1
                else:
                    SuperpositionVar = 0
                ShowDecel = 0
                Orthonorme = 0
                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    if Aube in ListAllGridStatorGlobal:
                        AubeType = 'STATOR'
                    else:
                        AubeType = 'ROTOR'
                    if DicoXYVarLoisGeom['HauteurCoupeDessins']:
                        SuperpositionNappe = 0  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                        if isinstance(YVar, list):
                            if len(YVar) == 1:  # On trace la supperposition des coupes que si il n'y a qu'une seule variable a tracer
                                CreateGraphProfilVsCorde(PageName, XVar, YVar,
                                                         Aube, AubeType,
                                                         DicoXYVarLoisGeom,
                                                         SuperpositionNappe,
                                                         SuperpositionVar,
                                                         SuperpositionPlan,
                                                         SuperpositionCase,
                                                         ShowDecel, Orthonorme,
                                                         DicoVariables,
                                                         DicoPrefGraphe,
                                                         DicoUserCurves, False,
                                                         0, 1)
                        else:
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves, False, 0,
                                                     1)

                        # DicoXYVarLoisGeom['HauteurCoupeDessins'] = False # On desactive la clef pour ensuite tracer les variables coupes par coupes
                        if DicoXYVarLoisGeom['HauteurCoupeParCoupe']:
                            SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)
                        # DicoXYVarLoisGeom['HauteurCoupeDessins'] = True # On réactive la clef pour les autres variables
                    else:
                        SuperpositionNappe = 0  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                        CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                 AubeType, DicoXYVarLoisGeom,
                                                 SuperpositionNappe,
                                                 SuperpositionVar,
                                                 SuperpositionPlan,
                                                 SuperpositionCase, ShowDecel,
                                                 Orthonorme, DicoVariables,
                                                 DicoPrefGraphe, DicoUserCurves,
                                                 False, 0, 1)
                        if DicoXYVarLoisGeom['HauteurCoupeParCoupe']:
                            SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)

        # PAGE PENTE SQL RADIALE
        if DicoXYVarLoisGeom['LoisGeomVsCorde_Hauteur_2trace']:
            PageName = "LOIS GEOM Vs HAUTEUR"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage", Nrow=NrowByVar,
                              Ncol=NcolByVar)

            for Tuple in DicoXYVarLoisGeom['LoisGeomVsCorde_Hauteur_XYvar']:
                XVar = Tuple[0]
                YVar = Tuple[1]
                print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    CreateGraphGeomVsCorde_Hauteur(PageName, XVar, YVar, Aube,
                                                   DicoXYVarLoisGeom, 0, False,
                                                   1, 0, 0, DicoVariables,
                                                   DicoPrefGraphe,
                                                   DicoUserCurves)

        # PAGE COL3D
        if DicoXYVarLoisGeom['LoisGeomCol3D_2trace']:
            PageName = "VISU COL3D"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['VisuGeomCol3D']['Nrow'],
                              Ncol=DicoNbreGraphe['VisuGeomCol3D']['Ncol'])
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphCol3D(PageName, Aube, DicoXYVarLoisGeom,
                                 DicoVariables, ['CARMA'], DicoPrefGraphe,
                                 DicoUserCurves)

        # PAGE VISUALISATION COUPE
        if DicoXYVarLoisGeom['LoisGeomCoupe_2trace']:
            PageName = "VISU COUPES"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['VisuGeomCoupe']['Nrow'],
                              Ncol=DicoNbreGraphe['VisuGeomCoupe']['Ncol'])
            if DicoXYVarLoisGeom['HauteurCoupeDessins']:
                SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                GarderCouleurCas = 1
                CouleurFiltre = 0
            else:
                SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                GarderCouleurCas = 1
                CouleurFiltre = 0
            SuperpositionVar = 0
            SuperpositionPlan = 0
            SuperpositionCase = 1
            ShowDecel = 0
            Orthonorme = 1
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                if Aube in ListAllGridStatorGlobal:
                    AubeType = 'STATOR'
                else:
                    AubeType = 'ROTOR'
                CreateGraphProfilVsCorde(PageName, "X", "Y", Aube, AubeType,
                                         DicoXYVarLoisGeom, SuperpositionNappe,
                                         SuperpositionVar, SuperpositionPlan,
                                         SuperpositionCase, ShowDecel,
                                         Orthonorme, DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves,
                                         EvolRadiale, GarderCouleurCas,
                                         CouleurFiltre)

        # PAGE VISUALISATION AUBAGE
        if DicoXYVarLoisGeom['LoisGeomVisuAube_2trace']:
            PageName = "VISU AUBAGE"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage", Nrow=NrowByVar,
                              Ncol=NcolByVar)
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphVisuAubage(PageName, Aube, 1, 1, 0, 1,
                                      DicoPrefGraphe)

        # PAGE VISUALISATION BA/BF
        if DicoXYVarLoisGeom['LoisGeomVisuBABF_2trace']:
            PageName = "VISU BA-BF"
            print("   - TRACE GEOMETRIQUE - %s" % PageName)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['VisuGeomBABF']['Nrow'],
                              Ncol=DicoNbreGraphe['VisuGeomBABF']['Ncol'])
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphVisuBABF(PageName, Aube, DicoXYVarLoisGeom, 1, 1, 1,
                                    1, 1, 1, DicoPrefGraphe)

    # PAGE POLAIRE
    if Trace_Polaire:
        # PAGE CHAPITRE POLAIRES
        PageName = "POLAIRE"
        page = pres.addPage(type="Chapitre",
                            name="---- CHAPITRE %s ----" % (PageName))
        page.numeroChapitre = "%i" % (NumChapRoue)
        page.titre = PageName
        NumChapRoue += 1

        # PAGE TABLEAU POLAIRES
        PageName = "POLAIRE - TABLEAU"
        # page = pres.addPage(type = "Standard", name = "%s"%(PageName))    # A developpper
        # SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)

        # PAGE POLAIRE - CHAMPS
        PageName = 'POLAIRE - CHAMPS'
        print("   - %s" % PageName)
        page = pres.addPage(type="Standard", name="%s" % (PageName))
        Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
        SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                          Ncol=NcolByVar)

        for XYVarPolaire in DicoXYVarPolaire2Trace['Polaire_XYvar']:
            XVar = XYVarPolaire[0][0]
            XVarPlan = XYVarPolaire[0][1]
            YVar = XYVarPolaire[1][0]
            YVarPlan = XYVarPolaire[1][1]

            Hauteur = DicoXYVarPolaire2Trace['Polaire_Hauteur']

            if isinstance(XVarPlan, list) and len(XVarPlan) == 2:
                XVarPlanAmont = XVarPlan[0]
                XVarPlanAval = XVarPlan[1]
            else:
                XVarPlanAmont = XVarPlan
                XVarPlanAval = XVarPlan

            if isinstance(YVarPlan, list) and len(YVarPlan) == 2:
                YVarPlanAmont = YVarPlan[0]
                YVarPlanAval = YVarPlan[1]
            else:
                YVarPlanAmont = YVarPlan
                YVarPlanAval = YVarPlan

            print("         * VARIABLE: { X : %s (%s/%s) , Y : %s (%s/%s)}" % (
            XVar, XVarPlanAmont, XVarPlanAval, YVar, YVarPlanAmont,
            YVarPlanAval))
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphChamps(PageName, Aube, Flux, XVar, YVar,
                                  XVarPlanAmont, XVarPlanAval, YVarPlanAmont,
                                  YVarPlanAval, Hauteur, 1, False, True, 1, 0,
                                  0, DicoVariables, DicoPrefGraphe,
                                  DicoUserCurves)

    # PAGE PROFILS RADIAUX
    if Trace_ProfilsRadiaux:

        for PlanUnique in DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Plan']:

            # PAGE CHAPITRE PROFILS RADIAUX PLAN UTILISATEURS
            PageName = "GRADIENTS (%s)" % PlanUnique
            page = pres.addPage(type="Chapitre",
                                name="---- CHAPITRE %s ----" % (PageName))
            page.numeroChapitre = "%i" % (NumChapRoue)
            page.titre = PageName
            NumChapRoue += 1

            # PAGE PROFILS RADIAUX PLAN UTILISATEURS
            print("   - GRADIENTS PLAN UNIQUE")
            print("       - PLAN UNIQUE: %s" % (PlanUnique))

            # PAGE VISUALISATION PLAN
            if DicoXYVarProfilsRadiaux2Trace[
                'VisuGeom_2trace'] and not ModeMises:
                Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
                PageName = 'GRADIENTS (%s) - VISU GEOM' % PlanUnique
                page = pres.addPage(type="Standard", name="%s" % (PageName))
                SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                                  Ncol=NcolByVar)

                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    CreateGraphVisuGeom("%s - %s" % (Aube, PlanUnique), Aube,
                                        PlanUnique, 0, 1, DicoPrefGraphe)

            if NbreAube == 1:
                PageName = 'GRADIENTS (%s) - VARIABLES' % (PlanUnique)
                page = pres.addPage(type="Standard", name="%s" % (PageName))
                SetPageProperties(page, Orientation='paysage', Nrow=2, Ncol=3)

            YVar = DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Yvar']
            for XVar in DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_XVar']:
                if XVar in DicoXYVarProfilsRadiaux2Trace[
                    'Grad_DeltaXVar'] and True in DeltaGraph:
                    Delta = True
                else:
                    Delta = False

                if "BA" in PlanUnique and XVar == 'EFP':
                    print(
                        "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                        PlanUnique, XVar))
                elif "BF" in PlanUnique and XVar == 'INCD':
                    print(
                        "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                        PlanUnique, XVar))
                else:
                    # PAGE PROFILS RADIAUX PLAN UTILISATEURS
                    if NbreAube != 1:
                        PageName = 'GRADIENTS (%s)' % PlanUnique
                        Orientation, NrowByVar, NcolByVar = GetNcolNRow(
                            NbreAube, Delta)
                        page = pres.addPage(type="Standard",
                                            name="%s - %s" % (PageName, XVar))
                        SetPageProperties(page, Orientation=Orientation,
                                          Nrow=NrowByVar, Ncol=NcolByVar)

                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))
                    if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                        print(
                            "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                    else:
                        for Tuple in ListTupleLabelAube2Trace:
                            Aube = Tuple[0]
                            Flux = Tuple[1]
                            if Aube in ListAllGridStatorGlobal:
                                if XVar not in DicoXYVarProfilsRadiaux2Trace[
                                    'Grad_XVar_NePasTracerPourStator']:
                                    CreateGraphGradient(PageName, Aube, Flux,
                                                        XVar, YVar, False,
                                                        PlanUnique, PlanUnique,
                                                        ['MISES', 'CFD',
                                                         'BSAM'], DicoVariables,
                                                        DicoPrefGraphe,
                                                        DicoUserCurves)
                                    if Trace_GradientMoyAdim: CreateGraphGradient(
                                        PageName, Aube, Flux, XVar, YVar, False,
                                        PlanUnique, PlanUnique,
                                        ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                        DicoPrefGraphe, {}, MoyAdim=1)

                            else:
                                if XVar not in DicoXYVarProfilsRadiaux2Trace[
                                    'Grad_XVar_NePasTracerPourRotor']:
                                    CreateGraphGradient(PageName, Aube, Flux,
                                                        XVar, YVar, False,
                                                        PlanUnique, PlanUnique,
                                                        ['MISES', 'CFD',
                                                         'BSAM'], DicoVariables,
                                                        DicoPrefGraphe,
                                                        DicoUserCurves)
                                    if Trace_GradientMoyAdim: CreateGraphGradient(
                                        PageName, Aube, Flux, XVar, YVar, False,
                                        PlanUnique, PlanUnique,
                                        ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                        DicoPrefGraphe, {}, MoyAdim=1)

                        if Delta:
                            print(
                                "         * VARIABLE DELTA: { X: %s   , Y: %s}" % (
                                XVar, YVar))
                            Orientation, NrowByVar, NcolByVar = GetNcolNRow(
                                NbreAube, Delta)
                            page = pres.addPage(type="Standard",
                                                name="%s - %s - DELTA" % (
                                                PageName, XVar))
                            SetPageProperties(page, Orientation=Orientation,
                                              Nrow=NrowByVar, Ncol=NcolByVar)
                            for Tuple in ListTupleLabelAube2Trace:
                                Aube = Tuple[0]
                                Flux = Tuple[1]
                                if Aube in ListAllGridStatorGlobal:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourStator']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            True, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            True, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)
                                else:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourRotor']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            True, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            True, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)

        for PlanVsPlanRef in DicoXYVarProfilsRadiaux2Trace[
            'GradPlanVsPlanRef_Plan']:

            # PAGE CHAPITRE PROFILS RADIAUX PLAN UTILISATEURS
            PageName = "GRADIENTS (%s|%s)" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            page = pres.addPage(type="Chapitre",
                                name="---- CHAPITRE %s ----" % (PageName))
            page.numeroChapitre = "%i" % (NumChapRoue)
            page.titre = PageName
            NumChapRoue += 1

            # PAGE PROFILS RADIAUX PLAN PERFOS
            print("   - GRADIENTS PLAN Vs PLANREF")
            print("       - PLAN PERFOS: %s | %s" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1]))

            # PAGE VISUALISATION PLAN
            if DicoXYVarProfilsRadiaux2Trace[
                'VisuGeom_2trace'] and not ModeMises:
                Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
                PageName = 'GRADIENTS (%s|%s) - VISU GEOM' % (
                PlanVsPlanRef[0], PlanVsPlanRef[1])
                page = pres.addPage(type="Standard", name="%s" % (PageName))
                SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                                  Ncol=NcolByVar)

                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    CreateGraphVisuGeom("%s - %s | %s" % (
                    Aube, PlanVsPlanRef[0], PlanVsPlanRef[1]), Aube,
                                        PlanVsPlanRef, 0, 1, DicoPrefGraphe)

            if NbreAube == 1:
                PageName = 'GRADIENTS (%s|%s) - VARIABLES' % (
                PlanVsPlanRef[0], PlanVsPlanRef[1])
                page = pres.addPage(type="Standard", name="%s" % (PageName))
                SetPageProperties(page, Orientation='paysage', Nrow=2, Ncol=3)

            InterpDir = DicoXYVarProfilsRadiaux2Trace[
                'GradPlanVsPlanRef_InterpDir']
            YVar = DicoXYVarProfilsRadiaux2Trace['GradPlanVsPlanRef_Yvar']
            for XVar in DicoXYVarProfilsRadiaux2Trace['GradPlanVsPlanRef_XVar']:
                # PAGE PROFILS RADIAUX PLAN PERFOS
                if XVar in DicoXYVarProfilsRadiaux2Trace[
                    'Grad_DeltaXVar'] and True in DeltaGraph:
                    Delta = True
                else:
                    Delta = False

                if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                    print(
                        "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                        XVar, YVar))
                else:
                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))

                    if NbreAube != 1:
                        PageName = 'GRADIENTS'
                        Orientation, NrowByVar, NcolByVar = GetNcolNRow(
                            NbreAube, Delta)
                        page = pres.addPage(type="Standard",
                                            name="%s - %s" % (PageName, XVar))
                        SetPageProperties(page, Orientation=Orientation,
                                          Nrow=NrowByVar, Ncol=NcolByVar)

                    for Tuple in ListTupleLabelAube2Trace:
                        Aube = Tuple[0]
                        Flux = Tuple[1]

                        if XVar == 'Marge':
                            try:
                                TypeCoupe = DicoInfoAubeCFD[Aube]['TypeCoupe']
                                YVar = 'h_H'  # si on est en h_H_norm alors la variable n'est pas tracé.
                                CreateGraphMarge(PageName, Aube, XVar, YVar,
                                                 False, TypeCoupe,
                                                 DicoVariables, DicoPrefGraphe,
                                                 DicoUserCurves)
                            except:
                                print(
                                    "         * VARIABLE NON TRACE: { X: %s , Y: %s}" % (
                                    XVar, YVar))
                        else:
                            if Aube in ListAllGridStatorGlobal:
                                if XVar not in DicoXYVarProfilsRadiaux2Trace[
                                    'Grad_XVar_NePasTracerPourStator']:
                                    CreateGraphGradient(PageName, Aube, Flux,
                                                        XVar, YVar, False,
                                                        PlanVsPlanRef[0],
                                                        PlanVsPlanRef[1],
                                                        ['MISES', 'CFD',
                                                         'BSAM'], DicoVariables,
                                                        DicoPrefGraphe,
                                                        DicoUserCurves,
                                                        InterpDir)
                                    if Trace_GradientMoyAdim: CreateGraphGradient(
                                        PageName, Aube, Flux, XVar, YVar, False,
                                        PlanVsPlanRef[0], PlanVsPlanRef[1],
                                        ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                        DicoPrefGraphe, {}, InterpDir,
                                        MoyAdim=1)
                            else:
                                if XVar not in DicoXYVarProfilsRadiaux2Trace[
                                    'Grad_XVar_NePasTracerPourRotor']:
                                    CreateGraphGradient(PageName, Aube, Flux,
                                                        XVar, YVar, False,
                                                        PlanVsPlanRef[0],
                                                        PlanVsPlanRef[1],
                                                        ['MISES', 'CFD',
                                                         'BSAM'], DicoVariables,
                                                        DicoPrefGraphe,
                                                        DicoUserCurves,
                                                        InterpDir)
                                    if Trace_GradientMoyAdim: CreateGraphGradient(
                                        PageName, Aube, Flux, XVar, YVar, False,
                                        PlanVsPlanRef[0], PlanVsPlanRef[1],
                                        ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                        DicoPrefGraphe, {}, InterpDir,
                                        MoyAdim=1)
                    if Delta:
                        print("         * VARIABLE DELTA: { X: %s , Y: %s}" % (
                        XVar, YVar))
                        for Tuple in ListTupleLabelAube2Trace:
                            Aube = Tuple[0]
                            Flux = Tuple[1]
                            if XVar == 'Marge':
                                try:
                                    TypeCoupe = DicoInfoAubeCFD[Aube][
                                        'TypeCoupe']
                                    YVar = 'h_H'  # si on est en h_H_norm alors la variable n'est pas tracé.
                                    CreateGraphMarge(PageName, Aube, XVar, YVar,
                                                     True, TypeCoupe,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)
                                except:
                                    print(
                                        "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                        XVar, YVar))
                            else:
                                if Aube in ListAllGridStatorGlobal:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourStator']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            True,
                                                            PlanVsPlanRef[0],
                                                            PlanVsPlanRef[1],
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            True, PlanVsPlanRef[0],
                                            PlanVsPlanRef[1],
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)
                                else:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourRotor']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            True,
                                                            PlanVsPlanRef[0],
                                                            PlanVsPlanRef[1],
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            True, PlanVsPlanRef[0],
                                            PlanVsPlanRef[1],
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)

    # PAGE PROFILS RADIAUX ANGLE
    if Trace_ProfilsRadiauxAngle and CFDCaseList != []:

        PlanVsPlanRef = ['BA', 'BF']

        # PAGE CHAPITRE PROFILS RADIAUX PLAN UTILISATEURS
        PageName = "GRADIENTS (ANGLES) (%s | %s)" % (
        PlanVsPlanRef[0], PlanVsPlanRef[1])
        page = pres.addPage(type="Chapitre",
                            name="---- CHAPITRE %s ----" % (PageName))
        page.numeroChapitre = "%i" % (NumChapRoue)
        page.titre = PageName
        NumChapRoue += 1

        # PAGE PROFILS RADIAUX PLAN PERFOS
        print("   - GRADIENTS ANGLE")
        print("       - PLANS: %s | %s" % (PlanVsPlanRef[0], PlanVsPlanRef[1]))

        # PAGE VISUALISATION PLAN
        if DicoXYVarProfilsRadiauxAngle2Trace[
            'VisuGeom_2trace'] and not ModeMises:
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            PageName = "GRADIENTS (ANGLES) (%s|%s) - VISU GEOM" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            page = pres.addPage(type="Standard", name="%s " % (PageName))
            SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                              Ncol=NcolByVar)

            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphVisuGeom(
                    "%s - %s | %s" % (Aube, PlanVsPlanRef[0], PlanVsPlanRef[1]),
                    Aube, PlanVsPlanRef, 0, 1, DicoPrefGraphe)

        if NbreAube == 1:
            PageName = "GRADIENTS (ANGLES) (%s|%s) - VARIABLES" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
            page = pres.addPage(type="Standard", name="%s" % (PageName))
            SetPageProperties(page, Orientation=Orientation, Nrow=2, Ncol=3)

        # PAGE PROFILS RADIAUX ANGLE
        for Tuple in DicoXYVarProfilsRadiauxAngle2Trace['GradPlanUnique_XYvar']:
            XVar = Tuple[0]
            YVar = Tuple[1]
            print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))

            if NbreAube != 1:
                Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (PageName, XVar))
                SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                                  Ncol=NcolByVar)

            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                CreateGraphGradientAngle(PageName, Aube, Flux, XVar, YVar,
                                         False, ['CFD', 'BSAM'], DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)

    # PAGE PROFILS LE LONG DE LA CORDE
    if Trace_ProfilVsCorde and CFDCaseList != []:

        # PAGE CHAPITRE PROFILS LE LONG DE LA CORDE
        PageName = "PROFILS Vs CORDE"
        page = pres.addPage(type="Chapitre",
                            name="---- CHAPITRE %s ----" % (PageName))
        page.numeroChapitre = "%i" % (NumChapRoue)
        page.titre = PageName
        NumChapRoue += 1

        # PAGE PROFILS LE LONG DE LA CORDE
        print("   - PROFILS LE LONG DE LA CORDE (GoupeParVariable)")

        # PAGE VISUALISATION LIGNES DE COURANT
        PageName = "LIGNE DE COURANT"
        # if NbreAube != 1:
        Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
        page = pres.addPage(type="Standard", name="%s - VISU GEOM" % (PageName))
        SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                          Ncol=NcolByVar)

        for Tuple in ListTupleLabelAube2Trace:
            Aube = Tuple[0]
            Flux = Tuple[1]
            CreateGraphVisuProfilVsCorde(PageName, Aube,
                                         DicoXYVarProfilVsCorde2Trace,
                                         ['CFD', 'BSAM'], DicoVariables,
                                         DicoPrefGraphe)

        # PAGE PROFIL VS CORDE
        for Tuple in DicoXYVarProfilVsCorde2Trace['CourbeProfil_XYvar']:
            XVar = Tuple[1]
            YVar = Tuple[0]
            print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
            for Tuple in ListTupleLabelAube2Trace:
                Aube = Tuple[0]
                Flux = Tuple[1]
                page = pres.addPage(type="Standard",
                                    name="%s - %s - %s - ParVariable" % (
                                    PageName, YVar, Aube))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['ProfilVsCordeSum'][
                                      'Nrow'],
                                  Ncol=DicoNbreGraphe['ProfilVsCordeSum'][
                                      'Ncol'])
                if Aube in ListAllGridStatorGlobal:
                    AubeType = 'STATOR'
                else:
                    AubeType = 'ROTOR'
                SuperpositionNappe = 1
                SuperpositionVar = 0
                SuperpositionPlan = 0
                SuperpositionCase = 1
                ShowDecel = 0
                Orthonorme = 0
                CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube, AubeType,
                                         DicoXYVarProfilVsCorde2Trace,
                                         SuperpositionNappe, SuperpositionVar,
                                         SuperpositionPlan, SuperpositionCase,
                                         ShowDecel, Orthonorme, DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)

            # PAGE COUPE PAR COUPE
            if DicoXYVarProfilVsCorde2Trace[
                'CourbeProfil_UnGrapheParPage'] and YVar in \
                    DicoXYVarProfilVsCorde2Trace[
                        'CourbeProfil_UnGrapheParPage_Yvar']:
                print("   - PROFILS LE LONG DE LA CORDE : COUPE PAR COUPE")
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['ProfilVsCorde']['Nrow'],
                                  Ncol=DicoNbreGraphe['ProfilVsCorde']['Ncol'])
                print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
                SuperpositionNappe = 1
                SuperpositionVar = 0
                SuperpositionPlan = 0
                SuperpositionCase = 1
                ShowDecel = 1
                Orthonorme = 0
                # DicoXYVarProfilVsCorde2Trace['HauteurListe'] = ['']
                CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube, AubeType,
                                         DicoXYVarProfilVsCorde2Trace,
                                         SuperpositionNappe, SuperpositionVar,
                                         SuperpositionPlan, SuperpositionCase,
                                         ShowDecel, Orthonorme, DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)

        # PAGE PROFILS RADIAUX MIN/MAX
        EvolRad = DicoXYVarProfilVsCorde2Trace.get('CourbeProfilRadiaux', False)

        if EvolRad:
            for dico in DicoXYVarProfilVsCorde2Trace[
                'CourbeProfilRadiaux_XYvar']:
                localisation = dico.get('loc', ['Extrados'])
                for loc in localisation:
                    XVar = dico.get('Xvar')
                    YVar = dico.get('Yvar')
                    BornesDecel = dico.get('Bornes', (0.0, 1.0))

                    print(
                        "         * VARIABLE: { X: %s   , Y: %s} - Localisation = %s" % (
                        XVar, YVar, loc))
                    for Tuple in ListTupleLabelAube2Trace:
                        Aube = Tuple[0]
                        Flux = Tuple[1]
                        page = pres.addPage(type="Standard",
                                            name="%s - EVOL RADIALE %s - %s - ParVariable" % (
                                            PageName, XVar, Aube))
                        SetPageProperties(page, Orientation="paysage", Nrow=1,
                                          Ncol=2)
                        if Aube in ListAllGridStatorGlobal:
                            AubeType = 'STATOR'
                        else:
                            AubeType = 'ROTOR'
                        SuperpositionNappe = 1
                        SuperpositionVar = 0
                        SuperpositionPlan = 0
                        SuperpositionCase = 1
                        ShowDecel = 0
                        Orthonorme = 0
                        CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                 AubeType,
                                                 DicoXYVarProfilVsCorde2Trace,
                                                 SuperpositionNappe,
                                                 SuperpositionVar,
                                                 SuperpositionPlan,
                                                 SuperpositionCase, ShowDecel,
                                                 Orthonorme, DicoVariables,
                                                 DicoPrefGraphe, DicoUserCurves,
                                                 True, Bornes=BornesDecel,
                                                 Localisation=loc)

    # PAGE PROFILS AZIMUTHAUX
    if Trace_ProfilAzimuthaux and "Post Antares Co" in DataTypeList:

        for PlanUnique in DicoXYVarProfilAzimuthaux2Trace[
            'ProfilAzimuthaux_Plan']:

            # PAGE CHAPITRE PROFILS AZIMUTHAUX PLAN UTILISATEURS
            PageName = "PROFILS AZIMUTHAUX (%s)" % PlanUnique
            page = pres.addPage(type="Chapitre",
                                name="---- CHAPITRE %s ----" % (PageName))
            page.numeroChapitre = "%i" % (NumChapRoue)
            page.titre = PageName
            NumChapRoue += 1

            # PAGE PROFILS AZIMUTHAUX PLAN UTILISATEURS
            print("   - PROFILS AZIMUTHAUX PLAN UNIQUE")
            print("       - PLAN UNIQUE: %s" % (PlanUnique))

            # PAGE VISUALISATION PLAN
            if DicoXYVarProfilAzimuthaux2Trace[
                'VisuGeom_2trace'] and not ModeMises:
                Orientation, NrowByVar, NcolByVar = GetNcolNRow(NbreAube, False)
                PageName = "PROFILS AZIMUTHAUX (%s) - VISU GEOM" % (PlanUnique)
                page = pres.addPage(type="Standard", name="%s" % (PageName))
                SetPageProperties(page, Orientation=Orientation, Nrow=NrowByVar,
                                  Ncol=NcolByVar)

                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    CreateGraphVisuGeom("%s - %s" % (Aube, PlanUnique), Aube,
                                        PlanUnique, 0, 1, DicoPrefGraphe)

            XVar = DicoXYVarProfilAzimuthaux2Trace['ProfilAzimuthaux_XVar']
            Hauteurs = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_HauteurListe']
            HauteursType = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_HauteurType']
            CalculDistortion = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_CalculDisto']
            SuperpositionCas = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_SuperpositionCas']
            SuperpositionPlan = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_SuperpositionPlan']
            SuperpositionHauteur = DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_SuperpositionHauteur']

            for YVar in DicoXYVarProfilAzimuthaux2Trace[
                'ProfilAzimuthaux_YVar']:
                if YVar in DicoXYVarProfilAzimuthaux2Trace[
                    'ProfilAzimuthaux_DeltaYVar'] and True in DeltaGraph:
                    Delta = True
                else:
                    Delta = False

                # PAGE PROFILS RADIAUX PLAN UTILISATEURS
                PageName = "PROFILS AZIMUTHAUX"
                page = pres.addPage(type="Standard",
                                    name="%s - %s - ParVariable" % (
                                    PageName, YVar))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['ProfilAzimuthauxSum'][
                                      'Nrow'],
                                  Ncol=DicoNbreGraphe['ProfilAzimuthauxSum'][
                                      'Ncol'])
                for Tuple in ListTupleLabelAube2Trace:
                    Aube = Tuple[0]
                    Flux = Tuple[1]
                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))
                    CreateGraphProfilAzimuthaux(PageName, Aube, XVar, YVar,
                                                PlanUnique, HauteursType,
                                                Hauteurs, CalculDistortion,
                                                SuperpositionCas,
                                                SuperpositionPlan,
                                                SuperpositionHauteur, ['CFD'],
                                                DicoVariables, DicoPrefGraphe,
                                                DicoUserCurves)

    # PAGE VISUALISATION ENSIGHT
    if Trace_VisuEnsight and CFDCaseList != []:
        print("   - VISUALISATION CHAMPS 3D (GoupeParVariable)")
        # PAGE CHAPITRE VISUALISATION ENSIGHT
        PageName = "VISU CHAMPS 3D"
        page = pres.addPage(type="Chapitre",
                            name="---- CHAPITRE %s ----" % (PageName))
        page.numeroChapitre = "%i" % (NumChapRoue)
        page.titre = PageName
        NumChapRoue += 1

        for Tuple in ListTupleLabelAube2Trace:
            Aube = Tuple[0]
            Flux = Tuple[1]
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['VisuCFD']['Nrow'],
                              Ncol=DicoNbreGraphe['VisuCFD']['Ncol'])

            DicoImageList = []
            for File in glob.glob(
                    os.path.join(CasePath, 'post', 'VisuCFD', '*')):
                FileName = os.path.basename(File)
                DicoImage = {'name': FileName, 'chemin': File}
                DicoImageList.append(DicoImage)

            CreateGraphVisu(PageName, Aube, DicoImageList, False)
else:
    for Tuple in ListTupleLabelAube2Trace:

        Aube = Tuple[0]
        Flux = Tuple[1]

        if Aube in ListAllGridStatorGlobal:
            AubeType = 'STATOR'
        else:
            AubeType = 'ROTOR'

        if Trace_LoisGeom or Trace_Polaire or Trace_ProfilsRadiaux_CL or Trace_ProfilsRadiaux or Trace_ProfilAzimuthaux or Trace_ProfilVsCorde or Trace_EvolutionParois or Trace_EvolutionAxiale or Trace_EvolutionMeridienne or Trace_VisuEnsight:
            print("\n ********* AUBE: %s (%s) **********\n" % (Aube, AubeType))

            NumChap = 1
            PageName = Aube
            page = pres.addPage(type="Chapitre",
                                name="%s ----------------------" % (PageName))
            page.numeroChapitre = "%i" % (NumChapRoue)
            page.titre = "%s" % PageName

        if Trace_LoisGeom and CARMACaseList != []:
            # PAGE CHAPITRE GEOMETRIE
            PageName = "GEOMETRIE"
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s ----" % (
                                Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            page.titre = PageName
            NumChap += 1

            # PAGE VUE MERIDIENNE
            if DicoXYVarLoisGeom['LoisGeomVisuMeridenne_2trace']:
                PageName = "VISU GEOM"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['VisuGeomMeridienne'][
                                      'Nrow'],
                                  Ncol=DicoNbreGraphe['VisuGeomMeridienne'][
                                      'Ncol'])
                CreateGraphVisuGeom(PageName, Aube, [], 1, 0, DicoPrefGraphe)

            # PAGE LOIS GEOMETRIQUES
            if DicoXYVarLoisGeom['LoisGeomVsHauteur_2trace']:
                PageName = "LOIS GEOM"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['LoisGeom']['Nrow'],
                                  Ncol=DicoNbreGraphe['LoisGeom']['Ncol'])
                # TypeCoupes = DicoInfoAubeCARMA["TypeCoupes"]
                TypeCoupes = "CQ"  # On force le tracé des lois sur les coupes CQ
                PlanAmont = "BA"
                PlanAval = "BF"
                for Tuple in DicoXYVarLoisGeom['LoisGeom_XYvar']:
                    XVar = Tuple[0]
                    YVar = Tuple[1]
                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))

                    if XVar in ["Comparaison beta1", "Comparaison beta2",
                                "INCD", "EFP", "DLI", "PSIA"]:
                        CreateGraphGradient(PageName, Aube, Flux, XVar, YVar,
                                            False, PlanAmont, PlanAval,
                                            ['CARMA', 'BSAM'], DicoVariables,
                                            DicoPrefGraphe, DicoUserCurves,
                                            InterpDir='h_H')
                    elif XVar in ["Marge", "ACol/S", "ACol/AEntree",
                                  "ASortie/ACol", "SCol/SX", "XCol/CX",
                                  "Mach Entree", "Mach Sortie"]:
                        CreateGraphMarge(PageName, Aube, XVar, YVar, False,
                                         TypeCoupes[0], DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)
                    else:
                        SuperpositionPlan = 0
                        SuperpositionCase = 1
                        SuperpositionBlade = 0
                        if isinstance(XVar, list):
                            SuperpositionVar = 1
                        else:
                            SuperpositionVar = 0
                        CreateGraphLoiGeom(PageName, Aube, XVar, YVar,
                                           TypeCoupes, DicoVariables,
                                           SuperpositionVar, SuperpositionPlan,
                                           SuperpositionCase,
                                           SuperpositionBlade,
                                           ['CARMA', 'BSAM'], DicoPrefGraphe,
                                           DicoUserCurves)

            # PAGE LOIS Vs CORDE
            if DicoXYVarLoisGeom['LoisGeomVsCorde_2trace']:
                PageName = "LOIS GEOM Vs CORDE"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['LoisGeomVsCorde'][
                                      'Nrow'],
                                  Ncol=DicoNbreGraphe['LoisGeomVsCorde'][
                                      'Ncol'])

                for Tuple in DicoXYVarLoisGeom['LoisGeomVsCorde_XYvar']:
                    XVar = Tuple[1]
                    YVar = Tuple[0]
                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))
                    SuperpositionCase = 1
                    SuperpositionPlan = 1
                    if isinstance(YVar, list):
                        SuperpositionVar = 1
                    else:
                        SuperpositionVar = 0
                    ShowDecel = 0
                    Orthonorme = 0
                    if DicoXYVarLoisGeom['HauteurCoupeDessins']:
                        SuperpositionNappe = 0  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                        if isinstance(YVar, list):
                            if len(YVar) == 1:  # On ne trace le supperposition des coupes que si il n'y a qu'une seul variable a tracer
                                CreateGraphProfilVsCorde(PageName, XVar, YVar,
                                                         Aube, AubeType,
                                                         DicoXYVarLoisGeom,
                                                         SuperpositionNappe,
                                                         SuperpositionVar,
                                                         SuperpositionPlan,
                                                         SuperpositionCase,
                                                         ShowDecel, Orthonorme,
                                                         DicoVariables,
                                                         DicoPrefGraphe,
                                                         DicoUserCurves, False,
                                                         0, 1)
                        else:
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves, False, 0,
                                                     1)

                        # DicoXYVarLoisGeom['HauteurCoupeDessins'] = False # On desactive la clef pour ensuite tracer les variables coupes par coupes
                        if DicoXYVarLoisGeom['HauteurCoupeParCoupe']:
                            SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)
                        # DicoXYVarLoisGeom['HauteurCoupeDessins'] = True # On réactive la clef pour les autres variables
                    else:
                        SuperpositionNappe = 0  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                        CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                 AubeType, DicoXYVarLoisGeom,
                                                 SuperpositionNappe,
                                                 SuperpositionVar,
                                                 SuperpositionPlan,
                                                 SuperpositionCase, ShowDecel,
                                                 Orthonorme, DicoVariables,
                                                 DicoPrefGraphe, DicoUserCurves,
                                                 False, 0, 1)
                        if DicoXYVarLoisGeom['HauteurCoupeParCoupe']:
                            SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                            CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                     AubeType,
                                                     DicoXYVarLoisGeom,
                                                     SuperpositionNappe,
                                                     SuperpositionVar,
                                                     SuperpositionPlan,
                                                     SuperpositionCase,
                                                     ShowDecel, Orthonorme,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)

            # PAGE PENTE SQL RADIALE
            if DicoXYVarLoisGeom['LoisGeomVsCorde_Hauteur_2trace']:
                PageName = "LOIS GEOM Vs HAUTEUR"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage", Nrow=
                DicoNbreGraphe['LoisGeomVsCorde_Hauteur']['Nrow'], Ncol=
                                  DicoNbreGraphe['LoisGeomVsCorde_Hauteur'][
                                      'Ncol'])

                for Tuple in DicoXYVarLoisGeom['LoisGeomVsCorde_Hauteur_XYvar']:
                    XVar = Tuple[0]
                    YVar = Tuple[1]
                    print("         * VARIABLE: { X: %s   , Y: %s}" % (
                    XVar, YVar))
                    CreateGraphGeomVsCorde_Hauteur(PageName, XVar, YVar, Aube,
                                                   DicoXYVarLoisGeom, 0, False,
                                                   1, 0, 0, DicoVariables,
                                                   DicoPrefGraphe,
                                                   DicoUserCurves)

            # PAGE COL3D
            if DicoXYVarLoisGeom['LoisGeomCol3D_2trace']:
                PageName = "VISU COL3D"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['VisuGeomCol3D']['Nrow'],
                                  Ncol=DicoNbreGraphe['VisuGeomCol3D']['Ncol'])
                CreateGraphCol3D(PageName, Aube, DicoXYVarLoisGeom,
                                 DicoVariables, ['CARMA'], DicoPrefGraphe,
                                 DicoUserCurves)

            # PAGE VISUALISATION COUPE
            if DicoXYVarLoisGeom['LoisGeomCoupe_2trace']:
                PageName = "VISU COUPES"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['VisuGeomCoupe']['Nrow'],
                                  Ncol=DicoNbreGraphe['VisuGeomCoupe']['Ncol'])
                if DicoXYVarLoisGeom['HauteurCoupeDessins']:
                    SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                    GarderCouleurCas = 1
                    CouleurFiltre = 0
                else:
                    SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                    GarderCouleurCas = 1
                    CouleurFiltre = 0
                SuperpositionVar = 0
                SuperpositionPlan = 0
                SuperpositionCase = 1
                ShowDecel = 0
                Orthonorme = 1
                EvolRadiale = False

                CreateGraphProfilVsCorde(PageName, "X", "Y", Aube, AubeType,
                                         DicoXYVarLoisGeom, SuperpositionNappe,
                                         SuperpositionVar, SuperpositionPlan,
                                         SuperpositionCase, ShowDecel,
                                         Orthonorme, DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves,
                                         EvolRadiale, GarderCouleurCas,
                                         CouleurFiltre)

            # PAGE VISUALISATION AUBAGE
            if DicoXYVarLoisGeom['LoisGeomVisuAube_2trace']:
                PageName = "VISU AUBAGE"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['VisuGeomAubage']['Nrow'],
                                  Ncol=DicoNbreGraphe['VisuGeomAubage']['Ncol'])
                CreateGraphVisuAubage(PageName, Aube, 1, 1, 0, 1,
                                      DicoPrefGraphe)

            # PAGE VISUALISATION BA/BF
            if DicoXYVarLoisGeom['LoisGeomVisuBABF_2trace']:
                PageName = "VISU BA-BF"
                print("   - TRACE GEOMETRIQUE - %s" % PageName)
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['VisuGeomBABF']['Nrow'],
                                  Ncol=DicoNbreGraphe['VisuGeomBABF']['Ncol'])
                CreateGraphVisuBABF(PageName, Aube, DicoXYVarLoisGeom, 1, 1, 1,
                                    1, 1, 1, DicoPrefGraphe)

        if Trace_Polaire and Aube in DicoInfoAubeCFD.keys():
            # PAGE CHAPITRE POLAIRES
            PageName = "POLAIRE"
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s ----" % (
                                Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            page.titre = PageName
            NumChap += 1

            # PAGE TABLEAU POLAIRES
            # page = pres.addPage(type = "Standard", name = "%s - TABLEAU %s"%(Aube,PageName))    # A developpper
            # SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)

            # PAGE CHAMPS POLAIRES
            print("   - CHAMPS POLAIRES")
            PageName = "POLAIRE - CHAMPS"
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['Polaire']['Nrow'],
                              Ncol=DicoNbreGraphe['Polaire']['Ncol'])

            for XYVarPolaire in DicoXYVarPolaire2Trace['Polaire_XYvar']:
                XVar = XYVarPolaire[0][0]
                XVarPlan = XYVarPolaire[0][1]
                YVar = XYVarPolaire[1][0]
                YVarPlan = XYVarPolaire[1][1]

                Hauteur = DicoXYVarPolaire2Trace['Polaire_Hauteur']

                if isinstance(XVarPlan, list) and len(XVarPlan) == 2:
                    XVarPlanAmont = XVarPlan[0]
                    XVarPlanAval = XVarPlan[1]
                else:
                    XVarPlanAmont = XVarPlan
                    XVarPlanAval = XVarPlan

                if isinstance(YVarPlan, list) and len(YVarPlan) == 2:
                    YVarPlanAmont = YVarPlan[0]
                    YVarPlanAval = YVarPlan[1]
                else:
                    YVarPlanAmont = YVarPlan
                    YVarPlanAval = YVarPlan

                print(
                    "         * VARIABLE: { X : %s (%s/%s) , Y : %s (%s/%s)}" % (
                    XVar, XVarPlanAmont, XVarPlanAval, YVar, YVarPlanAmont,
                    YVarPlanAval))

                CreateGraphChamps(PageName, Aube, Flux, XVar, YVar,
                                  XVarPlanAmont, XVarPlanAval, YVarPlanAmont,
                                  YVarPlanAval, Hauteur, 1, False, True, 1, 0,
                                  0, DicoVariables, DicoPrefGraphe,
                                  DicoUserCurves)

        if Trace_ProfilsRadiaux_CL and Aube in DicoInfoAubeCFD.keys():

            if DicoXYVarProfilsRadiauxInlet['GradPlanUnique_Plan'] != []:
                # PAGE CHAPITRE PROFILS RADIAUX INLET
                PageName = "GRADIENTS INLET"
                page = pres.addPage(type="Chapitre",
                                    name="%s ---- CHAPITRE %s ----" % (
                                    Aube, PageName))
                page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
                page.titre = PageName
                NumChap += 1

                # PAGE PROFILS RADIAUX INLET
                print("   - GRADIENTS INLET")
                for PlanUnique in DicoXYVarProfilsRadiauxInlet[
                    'GradPlanUnique_Plan']:
                    print("        - PLAN UNIQUE: %s" % (PlanUnique))

                    # PAGE PROFILS RADIAUX INLET
                    PageName = "GRADIENTS INLET"
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage",
                                      Nrow=DicoNbreGraphe['GradPlanInlet'][
                                          'Nrow'],
                                      Ncol=DicoNbreGraphe['GradPlanInlet'][
                                          'Ncol'])
                    YVar = DicoXYVarProfilsRadiauxInlet['GradPlanUnique_Yvar']
                    for XVar in DicoXYVarProfilsRadiauxInlet[
                        'GradPlanUnique_XVar']:
                        if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                            print(
                                "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                XVar, YVar))
                        else:
                            print("         * VARIABLE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                            CreateGraphGradient(PageName, Aube, Flux, XVar,
                                                YVar, False, PlanUnique,
                                                PlanUnique,
                                                ['MISES', 'CFD', 'BSAM'],
                                                DicoVariables, DicoPrefGraphe,
                                                DicoUserCurves)
                            if Trace_GradientMoyAdim: CreateGraphGradient(
                                PageName, Aube, Flux, XVar, YVar, False,
                                PlanUnique, PlanUnique,
                                ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                DicoPrefGraphe, {}, MoyAdim=1)

            if DicoXYVarProfilsRadiauxOutlet['GradPlanUnique_Plan'] != []:
                # PAGE CHAPITRE PROFILS RADIAUX OUTLET
                PageName = "GRADIENTS OUTLET"
                page = pres.addPage(type="Chapitre",
                                    name="%s ---- CHAPITRE %s ----" % (
                                    Aube, PageName))
                page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
                page.titre = PageName
                NumChap += 1

                # PAGE PROFILS RADIAUX OUTLET
                print("   - GRADIENTS OUTLET")
                for PlanUnique in DicoXYVarProfilsRadiauxOutlet[
                    'GradPlanUnique_Plan']:
                    print("        - PLAN UNIQUE: %s" % (PlanUnique))

                    # PAGE VISUALISATION PLAN
                    if DicoXYVarProfilsRadiauxOutlet[
                        'VisuGeom_2trace'] and not ModeMises:
                        PageName = "GRADIENTS OUTLET (%s) - VISU GEOM" % (
                            PlanUnique)
                        page = pres.addPage(type="Standard",
                                            name="%s - %s" % (Aube, PageName))
                        SetPageProperties(page, Orientation="paysage", Nrow=1,
                                          Ncol=1)

                        CreateGraphVisuGeom("%s - %s" % (Aube, PlanUnique),
                                            Aube, PlanUnique, 0, 1,
                                            DicoPrefGraphe)

                    # PAGE PROFILS RADIAUX OUTLET
                    PageName = "GRADIENTS OUTLET"
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage",
                                      Nrow=DicoNbreGraphe['GradPlanOutlet'][
                                          'Nrow'],
                                      Ncol=DicoNbreGraphe['GradPlanOutlet'][
                                          'Ncol'])
                    YVar = DicoXYVarProfilsRadiauxOutlet['GradPlanUnique_Yvar']
                    for XVar in DicoXYVarProfilsRadiauxOutlet[
                        'GradPlanUnique_XVar']:
                        if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                            print(
                                "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                XVar, YVar))
                        else:
                            print("         * VARIABLE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                            CreateGraphGradient(PageName, Aube, Flux, XVar,
                                                YVar, False, PlanUnique,
                                                PlanUnique,
                                                ['MISES', 'CFD', 'BSAM'],
                                                DicoVariables, DicoPrefGraphe,
                                                DicoUserCurves)
                            if Trace_GradientMoyAdim: CreateGraphGradient(
                                PageName, Aube, Flux, XVar, YVar, False,
                                PlanUnique, PlanUnique,
                                ['MISES', 'CFD', 'BSAM'], DicoVariables,
                                DicoPrefGraphe, {}, MoyAdim=1)

        if Trace_ProfilsRadiaux:
            # PAGE CHAPITRE PROFILS RADIAUX PLAN UTILISATEURS
            PageName = "GRADIENTS PLAN UNIQUE"
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            page.titre = PageName
            NumChap += 1

            # PAGE PROFILS RADIAUX PLAN UTILISATEURS
            print("   - GRADIENTS PLAN UNIQUE")

            if DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Plan'] != []:
                for PlanUnique in DicoXYVarProfilsRadiaux2Trace[
                    'GradPlanUnique_Plan']:
                    print("        - PLAN UNIQUE: %s" % (PlanUnique))

                    # PAGE VISUALISATION PLAN
                    if DicoXYVarProfilsRadiaux2Trace[
                        'VisuGeom_2trace'] and not ModeMises:
                        PageName = "GRADIENTS (%s) - VISU GEOM" % (PlanUnique)
                        page = pres.addPage(type="Standard",
                                            name="%s - %s" % (Aube, PageName))
                        SetPageProperties(page, Orientation="paysage", Nrow=1,
                                          Ncol=1)
                        CreateGraphVisuGeom("%s - %s" % (Aube, PlanUnique),
                                            Aube, PlanUnique, 0, 1,
                                            DicoPrefGraphe)

                    # PAGE PROFILS RADIAUX PLAN UTILISATEURS
                    PageName = "GRADIENTS (%s)" % (PlanUnique)
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage",
                                      Nrow=DicoNbreGraphe['GradPlanUnique'][
                                          'Nrow'],
                                      Ncol=DicoNbreGraphe['GradPlanUnique'][
                                          'Ncol'])

                    YVar = DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Yvar']

                    for XVar in DicoXYVarProfilsRadiaux2Trace[
                        'GradPlanUnique_XVar']:
                        if "BA" in PlanUnique and XVar == 'EFP':
                            print(
                                "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                PlanUnique, XVar))
                        elif "BF" in PlanUnique and XVar == 'INCD':
                            print(
                                "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                PlanUnique, XVar))
                        else:
                            if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                                print(
                                    "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                    XVar, YVar))
                            else:
                                if Aube in ListAllGridStatorGlobal:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourStator']:
                                        print(
                                            "         * VARIABLE: { X: %s   , Y: %s}" % (
                                            XVar, YVar))
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            False, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)

                                else:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourRotor']:
                                        print(
                                            "         * VARIABLE: { X: %s   , Y: %s}" % (
                                            XVar, YVar))
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            False, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)

                    if len(DicoXYVarProfilsRadiaux2Trace[
                               'Grad_DeltaXVar']) != 0:
                        page = pres.addPage(type="Standard",
                                            name="%s - %s - DELTA" % (
                                            Aube, PageName))
                        SetPageProperties(page, Orientation="paysage",
                                          Nrow=DicoNbreGraphe['GradPlanUnique'][
                                              'Nrow'],
                                          Ncol=DicoNbreGraphe['GradPlanUnique'][
                                              'Ncol'])
                        for XVar in DicoXYVarProfilsRadiaux2Trace[
                            'Grad_DeltaXVar']:
                            if "BA" in PlanUnique and XVar == 'EFP':
                                print(
                                    "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                    PlanUnique, XVar))
                            elif "BF" in PlanUnique and XVar == 'INCD':
                                print(
                                    "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                    PlanUnique, XVar))
                            else:
                                if XVar in DicoXYVarProfilsRadiaux2Trace[
                                    'GradPlanUnique_XVar']:
                                    if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                                        print(
                                            "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                            XVar, YVar))
                                    else:
                                        if Aube in ListAllGridStatorGlobal:
                                            if XVar not in \
                                                    DicoXYVarProfilsRadiaux2Trace[
                                                        'Grad_XVar_NePasTracerPourStator']:
                                                print(
                                                    "         * VARIABLE DELTA: { X: %s   , Y: %s}" % (
                                                    XVar, YVar))
                                                CreateGraphGradient(PageName,
                                                                    Aube, Flux,
                                                                    XVar, YVar,
                                                                    True,
                                                                    PlanUnique,
                                                                    PlanUnique,
                                                                    ['MISES',
                                                                     'CFD',
                                                                     'BSAM'],
                                                                    DicoVariables,
                                                                    DicoPrefGraphe,
                                                                    DicoUserCurves)
                                                if Trace_GradientMoyAdim: CreateGraphGradient(
                                                    PageName, Aube, Flux, XVar,
                                                    YVar, True, PlanUnique,
                                                    PlanUnique,
                                                    ['MISES', 'CFD', 'BSAM'],
                                                    DicoVariables,
                                                    DicoPrefGraphe, {},
                                                    MoyAdim=1)
                                        else:
                                            if XVar not in \
                                                    DicoXYVarProfilsRadiaux2Trace[
                                                        'Grad_XVar_NePasTracerPourRotor']:
                                                print(
                                                    "         * VARIABLE DELTA: { X: %s   , Y: %s}" % (
                                                    XVar, YVar))
                                                CreateGraphGradient(PageName,
                                                                    Aube, Flux,
                                                                    XVar, YVar,
                                                                    True,
                                                                    PlanUnique,
                                                                    PlanUnique,
                                                                    ['MISES',
                                                                     'CFD',
                                                                     'BSAM'],
                                                                    DicoVariables,
                                                                    DicoPrefGraphe,
                                                                    DicoUserCurves)
                                                if Trace_GradientMoyAdim: CreateGraphGradient(
                                                    PageName, Aube, Flux, XVar,
                                                    YVar, True, PlanUnique,
                                                    PlanUnique,
                                                    ['MISES', 'CFD', 'BSAM'],
                                                    DicoVariables,
                                                    DicoPrefGraphe, {},
                                                    MoyAdim=1)

            # PAGE INCD EFP
            PageName = "GRADIENTS PLAN UNIQUE (INCD/EFP)"
            print("   - %s" % PageName)
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=2)

            if DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Plan'] != []:
                for PlanUnique in DicoXYVarProfilsRadiaux2Trace[
                    'GradPlanUnique_Plan_INCD_EFP']:
                    print("        - PLAN UNIQUE: %s" % (PlanUnique))

                    YVar = DicoXYVarProfilsRadiaux2Trace['GradPlanUnique_Yvar']

                    for XVar in ['INCD', 'EFP']:
                        if "BA" in PlanUnique and XVar == 'EFP':
                            print(
                                "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                PlanUnique, XVar))
                        elif "BF" in PlanUnique and XVar == 'INCD':
                            print(
                                "         * VARIABLE NON TRACE: { Plan : %s --> X: %s}" % (
                                PlanUnique, XVar))
                        else:
                            if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                                print(
                                    "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                    XVar, YVar))
                            else:
                                if Aube in ListAllGridStatorGlobal:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourStator']:
                                        print(
                                            "         * VARIABLE: { X: %s   , Y: %s}" % (
                                            XVar, YVar))
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            False, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)
                                else:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourRotor']:
                                        print(
                                            "         * VARIABLE: { X: %s   , Y: %s}" % (
                                            XVar, YVar))
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False, PlanUnique,
                                                            PlanUnique,
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            False, PlanUnique, PlanUnique,
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            MoyAdim=1)

            # PAGE CHAPITRE PROFILS RADIAUX PLAN PERFOS
            PageName = "GRADIENTS PLAN Vs PLANREF"
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            page.titre = PageName
            NumChap += 1

            # PAGE PROFILS RADIAUX PLAN PERFOS
            print("   - %s" % PageName)
            if DicoXYVarProfilsRadiaux2Trace['GradPlanVsPlanRef_Plan'] != []:
                for PlanVsPlanRef in DicoXYVarProfilsRadiaux2Trace[
                    'GradPlanVsPlanRef_Plan']:
                    print("        - PLAN Vs PLANREF: (%s|%s)" % (
                    PlanVsPlanRef[0], PlanVsPlanRef[1]))

                    # PAGE VISUALISATION PLAN
                    if DicoXYVarProfilsRadiaux2Trace[
                        'VisuGeom_2trace'] and not ModeMises:
                        PageName = "GRADIENTS  (%s|%s) - VISU GEOM" % (
                        PlanVsPlanRef[0], PlanVsPlanRef[1])
                        page = pres.addPage(type="Standard",
                                            name="%s - %s" % (Aube, PageName))
                        SetPageProperties(page, Orientation="paysage", Nrow=1,
                                          Ncol=1)
                        CreateGraphVisuGeom("%s - %s | %s" % (
                        Aube, PlanVsPlanRef[0], PlanVsPlanRef[1]), Aube,
                                            PlanVsPlanRef, 0, 1, DicoPrefGraphe)

                    # PAGE PROFILS RADIAUX PLAN PERFOS
                    PageName = "GRADIENTS  (%s|%s)" % (
                    PlanVsPlanRef[0], PlanVsPlanRef[1])
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage",
                                      Nrow=DicoNbreGraphe['GradPlanVsPlanRef'][
                                          'Nrow'],
                                      Ncol=DicoNbreGraphe['GradPlanVsPlanRef'][
                                          'Ncol'])

                    YVar = DicoXYVarProfilsRadiaux2Trace[
                        'GradPlanVsPlanRef_Yvar']
                    InterpDir = DicoXYVarProfilsRadiaux2Trace[
                        'GradPlanVsPlanRef_InterpDir']
                    for XVar in DicoXYVarProfilsRadiaux2Trace[
                        'GradPlanVsPlanRef_XVar']:
                        if CFDCaseList == [] and XVar in VarForOnlyCFDCase:
                            print(
                                "         * VARIABLE NON TRACE: { X: %s   , Y: %s}" % (
                                XVar, YVar))
                        else:
                            print("         * VARIABLE: { X: %s   , Y: %s}" % (
                            XVar, YVar))
                            if XVar == 'Marge':
                                try:
                                    TypeCoupe = DicoInfoAubeCFD[Aube][
                                        'TypeCoupe']
                                    YVar = 'h_H'  # si on est en h_H_norm alors la variable n'est pas tracé.
                                    CreateGraphMarge(PageName, Aube, XVar, YVar,
                                                     False, TypeCoupe,
                                                     DicoVariables,
                                                     DicoPrefGraphe,
                                                     DicoUserCurves)
                                    if XVar in DicoXYVarProfilsRadiaux2Trace[
                                        'Grad_DeltaXVar']:
                                        CreateGraphMarge(PageName, Aube, XVar,
                                                         YVar, True, TypeCoupe,
                                                         DicoVariables,
                                                         DicoPrefGraphe,
                                                         DicoUserCurves)
                                except:
                                    pass
                            else:
                                if Aube in ListAllGridStatorGlobal:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourStator']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False,
                                                            PlanVsPlanRef[0],
                                                            PlanVsPlanRef[1],
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves,
                                                            InterpDir)
                                        if XVar in \
                                                DicoXYVarProfilsRadiaux2Trace[
                                                    'Grad_DeltaXVar']:
                                            CreateGraphGradient(PageName, Aube,
                                                                Flux, XVar,
                                                                YVar, True,
                                                                PlanVsPlanRef[
                                                                    0],
                                                                PlanVsPlanRef[
                                                                    1],
                                                                ['MISES', 'CFD',
                                                                 'BSAM'],
                                                                DicoVariables,
                                                                DicoPrefGraphe,
                                                                DicoUserCurves,
                                                                InterpDir)
                                            if Trace_GradientMoyAdim: CreateGraphGradient(
                                                PageName, Aube, Flux, XVar,
                                                YVar, True, PlanVsPlanRef[0],
                                                PlanVsPlanRef[1],
                                                ['MISES', 'CFD', 'BSAM'],
                                                DicoVariables, DicoPrefGraphe,
                                                {}, InterpDir, MoyAdim=1)
                                else:
                                    if XVar not in \
                                            DicoXYVarProfilsRadiaux2Trace[
                                                'Grad_XVar_NePasTracerPourRotor']:
                                        CreateGraphGradient(PageName, Aube,
                                                            Flux, XVar, YVar,
                                                            False,
                                                            PlanVsPlanRef[0],
                                                            PlanVsPlanRef[1],
                                                            ['MISES', 'CFD',
                                                             'BSAM'],
                                                            DicoVariables,
                                                            DicoPrefGraphe,
                                                            DicoUserCurves,
                                                            InterpDir)
                                        if Trace_GradientMoyAdim: CreateGraphGradient(
                                            PageName, Aube, Flux, XVar, YVar,
                                            False, PlanVsPlanRef[0],
                                            PlanVsPlanRef[1],
                                            ['MISES', 'CFD', 'BSAM'],
                                            DicoVariables, DicoPrefGraphe, {},
                                            InterpDir, MoyAdim=1)

                                        if XVar in \
                                                DicoXYVarProfilsRadiaux2Trace[
                                                    'Grad_DeltaXVar']:
                                            CreateGraphGradient(PageName, Aube,
                                                                Flux, XVar,
                                                                YVar, True,
                                                                PlanVsPlanRef[
                                                                    0],
                                                                PlanVsPlanRef[
                                                                    1],
                                                                ['MISES', 'CFD',
                                                                 'BSAM'],
                                                                DicoVariables,
                                                                DicoPrefGraphe,
                                                                DicoUserCurves,
                                                                InterpDir)
                                            if Trace_GradientMoyAdim: CreateGraphGradient(
                                                PageName, Aube, Flux, XVar,
                                                YVar, True, PlanVsPlanRef[0],
                                                PlanVsPlanRef[1],
                                                ['MISES', 'CFD', 'BSAM'],
                                                DicoVariables, DicoPrefGraphe,
                                                {}, InterpDir, MoyAdim=1)

        if Trace_ProfilsRadiauxAngle and CFDCaseList != []:

            PlanVsPlanRef = ['BA', 'BF']

            # PAGE CHAPITRE PROFILS RADIAUX ANGLE PLAN UTILISATEURS
            PageName = "GRADIENTS (ANGLES) (%s|%s)" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            page.titre = PageName
            NumChap += 1

            # PAGE VISUALISATION PLAN
            PageName = "GRADIENTS (ANGLES) (%s|%s) - VISU GEOM" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            page = pres.addPage(type="Standard",
                                name="%s - %s " % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)
            CreateGraphVisuGeom(
                "%s - %s | %s" % (Aube, PlanVsPlanRef[0], PlanVsPlanRef[1]),
                Aube, PlanVsPlanRef, 0, 1, DicoPrefGraphe)

            # PAGE PROFILS RADIAUX ANGLE
            PageName = "GRADIENTS (ANGLES) (%s|%s)" % (
            PlanVsPlanRef[0], PlanVsPlanRef[1])
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['GradPlanUnique']['Nrow'],
                              Ncol=DicoNbreGraphe['GradPlanUnique']['Ncol'])

            for Tuple in DicoXYVarProfilsRadiauxAngle2Trace[
                'GradPlanUnique_XYvar']:
                XVar = Tuple[0]
                YVar = Tuple[1]

                CreateGraphGradientAngle(PageName, Aube, Flux, XVar, YVar,
                                         False, ['CFD', 'BSAM'], DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)

        if Trace_ProfilVsCorde and CFDCaseList != []:
            # PAGE CHAPITRE PROFILS LE LONG DE LA CORDE
            PageName = "PROFILS Vs CORDE"
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            NumChap += 1
            page.titre = PageName

            # PAGE VISUALISATION LIGNES DE COURANT
            PageName = "VISU LIGNE DE COURANT"
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=1)

            CreateGraphVisuProfilVsCorde(PageName, Aube,
                                         DicoXYVarProfilVsCorde2Trace,
                                         ['CFD', 'BSAM'], DicoVariables,
                                         DicoPrefGraphe)

            # PAGE PROFILS LE LONG DE LA CORDE
            print("   - PROFILS LE LONG DE LA CORDE")

            for Tuple in DicoXYVarProfilVsCorde2Trace['CourbeProfil_XYvar']:
                XVar = Tuple[1]
                YVar = Tuple[0]
                print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
                PageName = "PROFILS Vs CORDE"
                page = pres.addPage(type="Standard",
                                    name="%s - %s - %s - ParVariable" % (
                                    Aube, PageName, YVar))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['ProfilVsCordeSum'][
                                      'Nrow'],
                                  Ncol=DicoNbreGraphe['ProfilVsCordeSum'][
                                      'Ncol'])
                SuperpositionNappe = 1  # /!\ Attention variable inversé : Si 1 alors desactivé et 0 activé
                SuperpositionVar = 0
                SuperpositionPlan = 0
                SuperpositionCase = 1
                ShowDecel = 0
                Orthonorme = 0
                CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube, AubeType,
                                         DicoXYVarProfilVsCorde2Trace,
                                         SuperpositionNappe, SuperpositionVar,
                                         SuperpositionPlan, SuperpositionCase,
                                         ShowDecel, Orthonorme, DicoVariables,
                                         DicoPrefGraphe, DicoUserCurves)

            # PAGE COUPE PAR COUPE
            if DicoXYVarProfilVsCorde2Trace['CourbeProfil_UnGrapheParPage']:
                print("   - PROFILS LE LONG DE LA CORDE : COUPE PAR COUPE")
                page = pres.addPage(type="Standard",
                                    name="%s - %s" % (Aube, PageName))
                SetPageProperties(page, Orientation="paysage",
                                  Nrow=DicoNbreGraphe['ProfilVsCorde']['Nrow'],
                                  Ncol=DicoNbreGraphe['ProfilVsCorde']['Ncol'])
                for Tuple in DicoXYVarProfilVsCorde2Trace['CourbeProfil_XYvar']:
                    XVar = Tuple[1]
                    YVar = Tuple[0]
                    if YVar in DicoXYVarProfilVsCorde2Trace[
                        'CourbeProfil_UnGrapheParPage_Yvar']:
                        print("         * VARIABLE: { X: %s   , Y: %s}" % (
                        XVar, YVar))
                        SuperpositionNappe = 1
                        SuperpositionVar = 0
                        SuperpositionPlan = 0
                        SuperpositionCase = 1
                        ShowDecel = 1
                        Orthonorme = 0
                        # DicoXYVarProfilVsCorde2Trace['HauteurListe'] = ['']
                        CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                 AubeType,
                                                 DicoXYVarProfilVsCorde2Trace,
                                                 SuperpositionNappe,
                                                 SuperpositionVar,
                                                 SuperpositionPlan,
                                                 SuperpositionCase, ShowDecel,
                                                 Orthonorme, DicoVariables,
                                                 DicoPrefGraphe, DicoUserCurves)

            # PAGE PROFILS RADIAUX MIN/MAX
            print("   - PROFILS LE LONG DE LA CORDE : EVOLUTION RADIALE")
            page = pres.addPage(type="Standard",
                                name="%s - %s - EVOL RADIALE" % (
                                Aube, PageName))
            SetPageProperties(page, Orientation="paysage", Nrow=1, Ncol=2)
            EvolRad = DicoXYVarProfilVsCorde2Trace.get('CourbeProfilRadiaux',
                                                       False)

            if EvolRad:
                for dico in DicoXYVarProfilVsCorde2Trace[
                    'CourbeProfilRadiaux_XYvar']:
                    localisation = dico.get('loc', ['Extrados'])
                    for loc in localisation:
                        XVar = dico.get('Xvar')
                        YVar = dico.get('Yvar')
                        BornesDecel = dico.get('Bornes', (0.0, 1.0))

                        print(
                            "         * VARIABLE: { X: %s   , Y: %s} - Localisation = %s" % (
                            XVar, YVar, loc))

                        SuperpositionNappe = 1
                        SuperpositionVar = 0
                        SuperpositionPlan = 0
                        SuperpositionCase = 1
                        ShowDecel = 0
                        Orthonorme = 0
                        CreateGraphProfilVsCorde(PageName, XVar, YVar, Aube,
                                                 AubeType,
                                                 DicoXYVarProfilVsCorde2Trace,
                                                 SuperpositionNappe,
                                                 SuperpositionVar,
                                                 SuperpositionPlan,
                                                 SuperpositionCase, ShowDecel,
                                                 Orthonorme, DicoVariables,
                                                 DicoPrefGraphe, DicoUserCurves,
                                                 True, Bornes=BornesDecel,
                                                 Localisation=loc)

        if Trace_ProfilAzimuthaux and "Post Antares Co" in DataTypeList:
            # PAGE CHAPITRE PROFILS AZIMUTHAUX
            PageName = "PROFILS AZIMUTHAUX"
            print("   - %s" % PageName)
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            NumChap += 1
            page.titre = PageName

            if DicoXYVarProfilAzimuthaux2Trace['ProfilAzimuthaux_Plan'] != []:
                for Plan in DicoXYVarProfilAzimuthaux2Trace[
                    'ProfilAzimuthaux_Plan']:
                    print("        - PLAN : %s" % (Plan))

                    # PAGE VISUALISATION PLAN
                    PageName = "PROFILS AZIMUTHAUX (%s) - VISU GEOM" % (Plan)
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage", Nrow=1,
                                      Ncol=1)
                    CreateGraphVisuGeom("%s - %s" % (Aube, Plan), Aube, Plan, 0,
                                        1, DicoPrefGraphe)

                    # PAGE PROFILS AZIMUTHAUX
                    PageName = "PROFILS AZIMUTHAUX (%s)" % (Plan)
                    page = pres.addPage(type="Standard",
                                        name="%s - %s" % (Aube, PageName))
                    SetPageProperties(page, Orientation="paysage",
                                      Nrow=DicoNbreGraphe['ProfilAzimuthaux'][
                                          'Nrow'],
                                      Ncol=DicoNbreGraphe['ProfilAzimuthaux'][
                                          'Ncol'])

                    XVar = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_XVar']
                    Hauteurs = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_HauteurListe']
                    HauteursType = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_HauteurType']
                    CalculDistortion = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_CalculDisto']
                    SuperpositionCas = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_SuperpositionCas']
                    SuperpositionPlan = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_SuperpositionPlan']
                    SuperpositionHauteur = DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_SuperpositionHauteur']
                    for YVar in DicoXYVarProfilAzimuthaux2Trace[
                        'ProfilAzimuthaux_YVar']:
                        print("         * VARIABLE: { X: %s   , Y: %s}" % (
                        XVar, YVar))
                        CreateGraphProfilAzimuthaux(PageName, Aube, XVar, YVar,
                                                    Plan, HauteursType,
                                                    Hauteurs, CalculDistortion,
                                                    SuperpositionCas,
                                                    SuperpositionPlan,
                                                    SuperpositionHauteur,
                                                    ['CFD'], DicoVariables,
                                                    DicoPrefGraphe,
                                                    DicoUserCurves)

        if Trace_VisuEnsight and Aube in DicoInfoAubeCFD.keys():
            # PAGE CHAPITRE VISUALISATION ENSIGHT
            PageName = "VISU CHAMPS 3D"
            print("   - %s" % PageName)
            page = pres.addPage(type="Chapitre",
                                name="%s ---- CHAPITRE %s" % (Aube, PageName))
            page.numeroChapitre = "%i-%i" % (NumChapRoue, NumChap)
            NumChap += 1
            page.titre = PageName

            # PAGE VISUALISATION ENSIGHT
            page = pres.addPage(type="Standard",
                                name="%s - %s" % (Aube, PageName))
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['VisuCFD']['Nrow'],
                              Ncol=DicoNbreGraphe['VisuCFD']['Ncol'])

            DicoImageList = []
            for File in glob.glob(
                    os.path.join(CasePath, 'post', 'VisuCFD', '*')):
                FileName = os.path.basename(File)
                print("     * Imgage: %s" % FileName)
                DicoImage = {'name': FileName, 'chemin': File}
                DicoImageList.append(DicoImage)

            CreateGraphVisu(PageName, Aube, DicoImageList, False)

        NumChapRoue += 1

# PAGE EVOLUTION MERIDIENNE
if Trace_EvolutionMeridienne:
    PageName = "EVOLUTION MERIDIENNE"
    print("   - %s" % PageName)
    page = pres.addPage(type="Chapitre",
                        name="---- CHAPITRE %s ----" % (PageName))
    page.numeroChapitre = "%i" % (NumChapRoue)
    page.titre = PageName
    NumChapRoue += 1

    XVar = DicoXYVarEvolMeridienne2Trace['EvolutionMeridienne_XVar']
    for YVar in DicoXYVarEvolMeridienne2Trace['EvolutionMeridienne_YVar']:
        print("         * VARIABLE: { X: %s   , Y: %s}" % (XVar, YVar))
        page = pres.addPage(type="Standard", name="%s - %s" % (PageName, YVar))
        SetPageProperties(page, Orientation="paysage",
                          Nrow=DicoNbreGraphe['EvolutionAxiale']['Nrow'],
                          Ncol=DicoNbreGraphe['EvolutionAxiale']['Ncol'])
        SuperpositionCase = 1
        PlanRef = DicoXYVarEvolMeridienne2Trace['EvolutionMeridienne_PlanAmont']
        Plan = DicoXYVarEvolMeridienne2Trace['EvolutionMeridienne_PlanAval']
        Hauteurs = DicoXYVarEvolMeridienne2Trace['EvolutionMeridienne_Hauteur']
        CreateGraphEvolutionMeridienne(PageName, ListTupleLabelAube2Trace, XVar,
                                       YVar, Hauteurs, SuperpositionCase,
                                       PlanRef, Plan, [], DicoVariables,
                                       DicoPrefGraphe, DicoUserCurves)

# PAGE EVOLUTION PAROIS
if Trace_EvolutionParois:
    print("   - EVOLUTION PAROIS")
    # PAGE CHAPITRE EVOLUTION PAROIS
    PageName = "EVOLUTION PAROIS"
    page = pres.addPage(type="Chapitre",
                        name="---- CHAPITRE %s ----" % (PageName))
    page.numeroChapitre = "%i" % (NumChapRoue)
    page.titre = PageName
    NumChapRoue += 1

    for hauteur in DicoXYVarEvolParois2Trace['EvolutionParois_Hauteur']:
        print("            * HAUTEUR: %s " % (hauteur))
        for YVar in DicoXYVarEvolParois2Trace['EvolutionParois_Var']:
            print("              - VARIABLE: %s " % (YVar))
            page = pres.addPage(type="Standard", name="%s - h_H=%s - %s" % (
            PageName, hauteur, YVar))
            SetPageProperties(page, Orientation="paysage",
                              Nrow=DicoNbreGraphe['EvolutionParois']['Nrow'],
                              Ncol=DicoNbreGraphe['EvolutionParois']['Ncol'])
            SuperpositionCase = 1

            Aube = "COMPLET"
            CreateGraphEvolutionParois(PageName, Aube, YVar, [hauteur],
                                       SuperpositionCase,
                                       DicoXYVarEvolParois2Trace[
                                           'EvolutionParois_Groupe'],
                                       DicoVariables, DicoPrefGraphe,
                                       DicoUserCurves)

# PAGE EVOLUTION AXIALE
if Trace_EvolutionAxiale:
    print("   - EVOLUTION AXIALE")
    # PAGE CHAPITRE EVOLUTION AXIALE
    PageName = "EVOLUTION AXIALE"
    page = pres.addPage(type="Chapitre",
                        name="---- CHAPITRE %s ----" % (PageName))
    page.numeroChapitre = "%i" % (NumChapRoue)
    page.titre = PageName
    NumChapRoue += 1

    XVar = DicoXYVarEvolAxiale2Trace['EvolutionAxiale_XVar']
    for YVar in DicoXYVarEvolAxiale2Trace['EvolutionAxiale_YVar']:
        print("         * VARIABLE: %s " % (YVar))
        page = pres.addPage(type="Standard",
                            name="%s - %s - ParVariable" % (PageName, YVar))
        SetPageProperties(page, Orientation="paysage",
                          Nrow=DicoNbreGraphe['EvolutionAxiale']['Nrow'],
                          Ncol=DicoNbreGraphe['EvolutionAxiale']['Ncol'])
        SuperpositionCase = 1
        PlanRef = DicoXYVarEvolAxiale2Trace['EvolutionAxiale_PlanAmont']
        Plan = DicoXYVarEvolAxiale2Trace['EvolutionAxiale_PlanAval']
        Hauteurs = DicoXYVarEvolAxiale2Trace['EvolutionAxiale_Hauteur']
        InterpDir = DicoXYVarEvolAxiale2Trace['EvolutionAxiale_InterDir']
        for Flux in DicoFluxAube.keys():
            if DicoFluxAube[Flux]:
                CreateGraphEvolutionAxiale(PageName, DicoFluxAube[Flux], Flux,
                                           XVar, YVar, Hauteurs, InterpDir,
                                           SuperpositionCase, PlanRef, Plan, [],
                                           DicoVariables, DicoPrefGraphe,
                                           DicoUserCurves)

# ON VERIFIE QUE LE REPERTOIRE EXISTE
if ExportPath:
    if not os.path.isdir(ExportPath):
        try:
            os.makedirs(ExportPath)
        except:
            pass

# ON SAUVEGARDE LE FICHIER XML
XML_ExportPath = os.path.join(ExportPath, "%s.xml" % ScriptName)
print("\n  * ON SAUVEGARDE LE FICHIER XML %s\n" % XML_ExportPath)
App.saveDataXML(XML_ExportPath)

# ON ECRIT LA PRESENTATION
if ExportExcel or ExportPDF or ExportPPT:

    App.loadData()

    if Trace_LoisGeom == True and DicoXYVarLoisGeom['LoisGeomCol3D_2trace']:
        App.loadDataXML(
            XML_ExportPath)  # pour avoir la visu Col3D, il faut recharger le XML. Mais cela provoque un autre bug. La marge NS3D n'est plus tracee.

    maPres = App.writePresentation()
    App.presentationConstruction.presentationList[0].Name = TitrePres

    PrefOuverture = Customization().getPreferencesOuverture()
    PrefOuverture['pdf'] = True  # On force l'ouverture du pdf

    for pres in maPres:
        if ExportPPT:
            t1 = time.time()
            print("\n  * ECRITURE DU PPT EN COURS --> ON PATIENTE !!!!\n")
            pres.exportPresentationPPTAuto(ExportPath,
                                           ouvertureAuto=PrefOuverture["ppt"])
            t2 = time.time()
            print("        --> PPT ECRIT EN %s DANS LE DOSSIER %s" % (
            ConvertSecondToTime(t2 - t1), ExportPath))
        if ExportPDF:
            t1 = time.time()
            print("\n  * ECRITURE DU PDF EN COURS --> ON PATIENTE !!!!\n")
            pres.ExportPresentationPDFAuto(ExportPath,
                                           ouvertureAuto=PrefOuverture["pdf"])
            t2 = time.time()
            print("        --> PDF ECRIT EN %s DANS LE DOSSIER %s" % (
            ConvertSecondToTime(t2 - t1), ExportPath))
        if ExportExcel:
            t1 = time.time()
            print("\n  * ECRITURE DE L'EXCEL EN COURS --> ON PATIENTE !!!!\n")
            pres.exportExcelNomAuto(ExportPath,
                                    ouvertureAuto=PrefOuverture["excel"])
            t2 = time.time()
            print("        --> EXCEL ECRIT EN %s DANS LE DOSSIER %s" % (
            ConvertSecondToTime(t2 - t1), ExportPath))
    # App.clearWorkdir()
