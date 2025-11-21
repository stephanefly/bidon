#!/usr/bin/env python
# -*- coding: utf-8 -*-

DicoXYVarLoisGeom = {'HauteurListe'   : [''],  # Pour tracer toutes les coupes [''] sinon [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] ou [10, 20, 30, 40, 50, 60, 70, 80, 90]
                     'HauteurCoupeDessins'   : True,  # Pour tracer toutes les coupes de dessins si celles-ci sont definies dans le cas CARMA.
                     'HauteurCoupeParCoupe'  : True,  # Pour tracer toutes les coupes une a une
                     
                     #  Activation des traces
                     'LoisGeomVisuMeridenne_2trace' : True,     # Permet d'activer le tracé des visualisations de la geometrie en vue meridienne
                     'LoisGeomVsHauteur_2trace' : True,          # Permet d'activer le tracé des lois suivant la hauteur
                     'LoisGeomVsCorde_2trace' : True,            # Permet d'activer le tracé des lois suivant la corde
                     'LoisGeomVsCorde_Hauteur_2trace' : True,   # Permet d'activer le tracé des lois suivant la corde et la hauteur
                     'LoisGeomCol3D_2trace' : True,             # Permet d'activer le tracé des lois de section
                     'LoisGeomCoupe_2trace' : True,             # Permet d'activer le tracé des coupes
                     'LoisGeomVisuAube_2trace' : False,          # Permet d'activer le tracé des aubages
                     'LoisGeomVisuBABF_2trace' : True,          # Permet d'activer le tracé des Zooms BA/BF
                     
                     'LoisGeom_XYvar' : [
                                        ('Comparaison beta1', 'h_H'),   # Possibilité de  traiter une unique variable ou plusieurs par le biais d'une liste (Si plusieurs variables alors celles-ci seront supperposées)
                                        ('Comparaison beta2', 'h_H'),
                                        # (['b1sqT_5.0pct','b1sqT_8.0pct'],'rBA_adim'),
                                        # (['b2sqT_5.0pct','b2sqT_8.0pct'],'rBF_adim'),
                                        ('Calage','rBF_adim'),
                                        # ('Cambrure','rMoyen_adim'),
                                        ('Cambrure_FromCD_8.0pct','rMoyen_adim'),
                                        # ('Cambrure_8.0pct','rMoyen_adim'),
                                        ('Corde','rBF_adim'),
                                        ('CordeAxi','rBF_adim'),
                                        (['EBA_0.30mm','EBA_1.00mm','EBA_3.00mm'],'rBA_adim'),
                                        (['EBF_0.30mm','EBF_1.00mm','EBF_3.00mm'],'rBF_adim'),
                                        # (['EpBA_FromCD_5.0pct', 'EpBA_FromCD_8.0pct'],'rMoyen_adim'),
                                        # (['EpBF_FromCD_5.0pct', 'EpBF_FromCD_8.0pct'],'rMoyen_adim'),
                                        ('EpBA_Emax_FromCD_8.0pct','rMoyen_adim'),
                                        ('EpBF_Emax_FromCD_8.0pct','rMoyen_adim'),
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
                                        ('Emax','rBF_adim'),
                                        ('EmaxsC','rBF_adim'),
                                        ('XEmax','rBF_adim'),
                                        ('XEmaxsC','rBF_adim'),
                                        ('ssc','rBF_adim'),
                                        ('s','rBF_adim'),
                                        ('XgCale','rBF_adim'),
                                        ('YgCale','rBF_adim'),
                                        ('xBa','rBA_adim'),
                                        ('xBf','rBA_adim'),
                                        # ('PenteTraceBA','rBA_adim'),
                                        # ('PenteTraceBF','rBF_adim'),
                                        ('yBa','rBA_adim'),
                                        ('yBf','rBF_adim'),
                                        ('sweep_BA','rBA_adim'),
                                        ('sweep_BF','rBF_adim'),
                                        ('dihedral_BA','rBA_adim'),
                                        ('dihedral_BF','rBF_adim'),
                                        ('INCD','h_H_BA'),
                                        ('EFP','h_H_BF'),
                                        ('DLI','h_H_BF'),
                                        ('PSIA','h_H_BF'),
                                        ('Marge','h_H'),
                                        ('ACol/S','h_H'),
                                        ('ACol/AEntree','h_H'),
                                        ('ASortie/ACol','h_H'),
                                        ('SCol/SX','h_H'),
                                        ('XCol/CX','h_H'),
                                        ('Mach Entree','h_H'),
                                        ('Mach Sortie','h_H'),
                                        ('DiedreBA_8.0pct','rMoyen_adim'),
                                        ],
                    
                     'LoisGeomVsCorde_XYvar' : [
                                                (['BSQ','BSQ_EXT','BSQ_INT'] ,['cordeRed','cordeRed','cordeRed']),
                                                # (['BSQ_cor_8.0pct','BSQ_EXT_cor_8.0pct','BSQ_INT_cor_8.0pct'] ,['cordeRed_BSQ_adim_8.0pct','cordeRed_BSQ_EXT_adim_8.0pct','cordeRed_BSQ_INT_adim_8.0pct']),
                                                # (['BSQ','BSQ_cor_8.0pct'] ,['cordeRed','cordeRed_BSQ_adim_8.0pct']),
                                                ('BSQ' ,'cordeRed'),
                                                # (['BSQ','BSQ'],['cordeRed','m_Adim']),
                                                (['BSQ_adim_8.0pct'] ,'cordeRed_BSQ_adim_8.0pct'),
                                                # (['BSQ_EXT','BSQ_EXT_cor_8.0pct'] ,['cordeRed','cordeRed_BSQ_EXT_adim_8.0pct']),
                                                (['BSQ_EXT'] ,['cordeRed']),
                                                (['BSQ_EXT_adim_8.0pct'] ,'cordeRed_BSQ_EXT_adim_8.0pct'),
                                                # (['EPAIS','EPAIS_cor_8.0pct'],['cordeRed','cordeRed_EPAIS_adim_8.0pct']),
                                                ('EPAIS','cordeRed'),
                                                # (['EPAIS','EPAIS'],['cordeRed','m_Adim']),
                                                ('EPAIS_adim_8.0pct','cordeRed_EPAIS_adim_8.0pct'),
                                                # ('RayonCourbure','cordeRed_BA_BF_BA_RayCourbure'),
                                                ('RayonCourbure_Ext','cordeRed_RayCourbure_Ext'),
                                                ('RayonCourbure_Int','cordeRed_RayCourbure_Int'),
                                                # ('Courbure','corde_Courbure'),
                                                ('Courbure','corde_Courbure_adim'),
                                               ],
                    
                     'LoisGeomVsCorde_VarMinMax' : {   # Mettre None si on veut une valeur automatique ou enlever la variable du dictionnaire
                                                   # 'PENTE_EXTRA'   : {'Min' : 0.0, 'Max' : None},
                                                   # 'PENTE_INTRA'   : {'Min' : 10.0, 'Max' : None},
                                                    
                                                   # 'BSQ'       : {'Min' : 0.0, 'Max' : 100},
                                                   'BSQ_adim_8.0pct'      : {'Min' : 0.0, 'Max' : 1.0},
                                                   
                                                   # 'BSQ_EXT'   : {'Min' : 0.0, 'Max' : 100},
                                                   'BSQ_EXT_adim_8.0pct'  : {'Min' : 0.0, 'Max' : 1.0},
                                                   
                                                   # 'EPAIS'     : {'Min' : 0.0, 'Max' : 10},
                                                   'EPAIS_adim_8.0pct'    : {'Min' : 0.0, 'Max' : 1.0},
                                                   
                                                   # 'RayonCourbure'     : {'Min' : 1.45,  'Max' : 1.65},
                                                   # 'RayonCourbure_Ext' : {'Min' : 1.45,  'Max' : 1.65},
                                                   # 'RayonCourbure_Int' : {'Min' : 1.45,  'Max' : 1.65},
                                                   # 'Courbure'          : {'Min' : -0.03, 'Max' : 0.03},
                                                   
                                                   'cordeReduite'                : {'Min' : 0.0, 'Max' : 1.0},
                                                   'cordeRed'                    : {'Min' : 0.0, 'Max' : 1.0},
                                                   'cordeRed_BSQ_adim_8.0pct'    : {'Min' : 0.0, 'Max' : 1.0},
                                                   'cordeRed_BSQ_EXT_adim_8.0pct': {'Min' : 0.0, 'Max' : 1.0},
                                                   'cordeRed_EPAIS_adim_8.0pct'  : {'Min' : 0.0, 'Max' : 1.0},
                                                   'cordeRed_BA_BF_BA_RayCourbure'   : {'Min' : 0.0, 'Max' : 2.0},
                                                   # 'corde_Courbure'      : {'Min' : 0.0, 'Max' : 2.0},
                                                    },
                     
                     'LoisGeomVsCorde_Hauteur_XYvar' : [('BSQ','_h_H'),
                                                        ('BSQ_EXT','_h_H'),
                                                        ('BSQ_INT','_h_H'),
                                                        # ('EPAIS','_h_H'),
                                                        # ('BSQ_adim_8.0pct','_h_H'),
                                                        # ('EPAIS_adim_8.0pct','_h_H'),
                                                        ],
                                              
                     }

# DICTIONNAIRE RELATIF Aux CLEFS : Trace_Perfos0D
DicoXYVarPerfos0D2Trace = {'Perfos0D_XYvar' : {'ROTOR'  : [['Qcorr_ref','Pi'],['etapol','Pi'],['Qcorr_ref','etapol'],['etapol','PisD']],
                                               'STATOR' : [['Qcorr_ref','Pi'],['cd_fftro','Pi'],['Qcorr_ref','cd_fftro'],['cd_fftro','PisD']],
                                              },
                           'Perfos0D_Plan' : [['AmontPerfo','AvalPerfo']],
                           
                           'Perfos0D_Tableau' : False,
                           'Perfos0D_TableauXYvar' : {'ROTOR' : ['Référence','Qcorr_ref', 'Pi', 'etapol', 'deltapctQcorr_ref', 'deltapctPi', 'deltaetapol'], #'R\xe9f\xe9rence'
                                                      'STATOR'  : ['Référence','Qcorr_ref', 'Pi', 'cd_fftro', 'deltapctQcorr_ref', 'deltapctPi', 'deltapctcd_fftro'],
                                                     },
                           }

# Parametrisation dans le cas ou on est en mode champs
DicoXYVarPerfos0D2Trace_Champs = {'Perfos0D_XYvar' : {'ROTOR'  : [['Qcorr_ref','Pi'],['etapol','Pi'],['Qcorr_ref','etapol'],['etapol','PisD'],['Qcorr_ref','Dev'],['Qcorr_ref','W2_W1_RAL'],['Qcorr_ref','XNR'],['XNR','Pi']],
                                                      'STATOR' : [['Qcorr_ref','Pi'],['cd_fftro','Pi'],['Qcorr_ref','cd_fftro'],['cd_fftro','PisD']],
                                              },
                           'Perfos0D_Plan' : [['(BA)','(BF)']],
                           
                           'Perfos0D_Tableau' : False,
                           'Perfos0D_TableauXYvar' : {'ROTOR' : ['Référence','Qcorr_ref', 'Pi', 'etapol', 'deltapctQcorr_ref', 'deltapctPi', 'deltaetapol'], #'R\xe9f\xe9rence'
                                                      'STATOR'  : ['Référence','Qcorr_ref', 'Pi', 'cd_fftro', 'deltapctQcorr_ref', 'deltapctPi', 'deltapctcd_fftro'],
                                                     },
                           }
                           
# DICTIONNAIRE RELATIF AU CLEFS : Trace_ProfilsRadiaux
DicoXYVarProfilsRadiaux2Trace = { 'VisuGeom_2trace' : True,
                                 'GradPlanUnique_XVar' : ['Ps','Pta','Ptr', 'Ts','Tta','Ttr', 'V','W','Vm', 'Ma','Mr','Mm', 'Tu_relatif','Tu_absolu','Viscosity_EddyMolecularRatio', 'alpha','beta','phi','Qa','RhoVm','INCD','EFP'], # ,'REYc','Ra_HL'
                                 'GradPlanUnique_Yvar' : 'h_H_norm' ,  # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanUnique_Plan' : ["LoinBA", "ProcheBA", "ProcheBF", "LoinBF"],
                                 'GradPlanUnique_Plan_INCD_EFP' : ["ProcheBA", "ProcheBF"],
                                 
                                 'GradPlanVsPlanRef_XVar' : ['Pi','etapol','cd_fftro','Dev','V2_V1_RAL','W2_W1_RAL','PSIA','DLI','Tau','Marge','AVDR'],
                                 'GradPlanVsPlanRef_Yvar' : 'h_H_norm',   # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanVsPlanRef_InterpDir' : 'q_Q',   # h_H / q_Q 
                                 'GradPlanVsPlanRef_Plan' : [["AmontPerfo","AvalPerfo"]],
                                 
                                 # 'Grad_DeltaXVar' : ['INCD', 'EFP','Pi','etapol','cd_fftro','Marge'],
                                 'Grad_DeltaXVar' : [],
                                 
                                 'Grad_XVar_NePasTracerPourStator' : ['etapol'],
                                 'Grad_XVar_NePasTracerPourRotor' : ['V2_V1_RAL'],
                                }

# Parametrisation dans le cas ou on se compare a MISES
DicoXYVarProfilsRadiaux2Trace_Mises = { 'VisuGeom_2trace' : True,
                                 'GradPlanUnique_XVar' : ['Ps','Pta','Ptr', 'Ts','Tta','Ttr', 'V','W','Vm', 'Ma','Mr','Mm', 'alpha','beta','phi', 'Qa','INCD','EFP'],
                                 'GradPlanUnique_Yvar' : 'h_H' ,  # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanUnique_Plan' : ["(BA)", "(BF)"],
                                 'GradPlanUnique_Plan_INCD_EFP' : ["(BA)", "(BF)"],
                                 
                                 'GradPlanVsPlanRef_XVar' : ['Pi','etapol','cd_fftro','Cd_MISES','Cd_shock_MISES','Cd_visc_MISES','Dev','W2_W1_RAL','Tau','Marge'],
                                 'GradPlanVsPlanRef_Yvar' : 'h_H',   # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanVsPlanRef_InterpDir' : 'q_Q',   # h_H / q_Q 
                                 'GradPlanVsPlanRef_Plan' : [["(BA)","(BF)"]],
                                 
                                 # 'Grad_DeltaXVar' : ['INCD', 'EFP','Pi','etapol','cd_fftro','Marge'],
                                 'Grad_DeltaXVar' : [],
                                 
                                 'Grad_XVar_NePasTracerPourStator' : ['etapol'],
                                 'Grad_XVar_NePasTracerPourRotor' : ['V2_V1_RAL'],
                                }

# Parametrisation dans le cas ou on est en mode champs
DicoXYVarProfilsRadiaux2Trace_Champs = { 'VisuGeom_2trace' : True,
                                 'GradPlanUnique_XVar' : ['alpha','beta','Ps','Pta','Tta','Vm','Mr','RhoVm'],  # Manque INCD/INCD_GX/ PS/PT2 / ROVZ1 / XRVU / DEQ / CDPRO / CDCHO / CDBLO / CDCOR / CDSEC / MARGE / SCOL/PAS/ KD
                                 'GradPlanUnique_Yvar' : 'h_H_norm' ,  # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanUnique_Plan' : ["(BA)", "(BF)"],
                                 'GradPlanUnique_Plan_INCD_EFP' : ["(BA)", "(BF)"],
                                 
                                 'GradPlanVsPlanRef_XVar' : ['Pi','etapol','cd_fftro','Dev','W2_W1_RAL','PSIA','DLI','Tau','Marge'],   # 'RhoVm2_RhoVm1','R2_R1'
                                 'GradPlanVsPlanRef_Yvar' : 'h_H_norm',   # h_H / h_H_norm (utile pour les bi-flux) / q_Q / R
                                 'GradPlanVsPlanRef_InterpDir' : 'q_Q',   # h_H / q_Q 
                                 'GradPlanVsPlanRef_Plan' : [["(BA)","(BF)"]],
                                 
                                 'Grad_DeltaXVar' : ['INCD', 'EFP','Pi','etapol','cd_fftro','Marge'],
                                 
                                 'Grad_XVar_NePasTracerPourStator' : ['etapol'],
                                 'Grad_XVar_NePasTracerPourRotor' : ['V2_V1_RAL'],
                                }
                                
# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilsRadiauxAngle
'''
Variables disponibles: 
        'Q%BSAM','b1sq','b2sq','beta_BA','beta_BF','Calage','corde','deltasq','dli_empilage','dli_rBA','dli_rBF','dli_rmoy','efp','h_H_BA','h_H_BF','h_H_moy','incd','Mr_BA','Mr_BF',
        'Ptr_BA','Ptr_BF','R_BA','R_BF','R_moy','r_R_BA','r_R_BF','r_R_moy','ssc_empilage','ssc_rmoy','Ttr_BA','Ttr_BF','Vt_BA','Vt_BF','W_BA','W_BF','X_BA','X_BF',
        'zweifel_empilage','zweifel_rBA','zweifel_rBF','zweifel_rmoy','plan_amont','plan_aval
'''
DicoXYVarProfilsRadiauxAngle2Trace = { 'VisuGeom_2trace' : True,
                                      'GradPlanUnique_XYvar' : [('b1sq','h_H_BA'),
                                                                ('b2sq','h_H_BF'),
                                                                ('incd','h_H_BA'),
                                                                ('efp','h_H_BF'),
                                                                ('dli_empilage','h_H_moy'),
                                                                ('zweifel_empilage','h_H_moy'),
                                                                ],
                                              }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilVsCorde
DicoXYVarProfilVsCorde2Trace = {'HauteurType' : ['QBSAM'] ,     # 'QBSAM' / 'QNS3D' / 'h_H'
                                'HauteurListe'   : [],    # Pour tracer toutes les coupes [''] sinon [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] ou [10, 20, 30, 40, 50, 60, 70, 80, 90]

                                'CourbeProfil_UnGrapheParPage' : True, # Permet de tracer un graphe par page
                                'CourbeProfil_UnGrapheParPage_Yvar' : ['mis3'], # Liste des variables pour lesquelles on va tracer un graphe par page

                                'CourbeProfil_XYvar' : [('mis3','Corde_BA_BF'),
                                                        ('WallCellSize','Corde_BA_BF'),
                                                        ('delta_cell_count','Corde_BA_BF'),
                                                        
                                                        # ('hi','Corde_BA_BF'),
                                                        ('ShapeFactor','Corde_BA_BF'),
                                                        
                                                        # ('delta1','Corde_BA_BF'),
                                                        # ('theta11','Corde_BA_BF'),
                                                        # ('runit','Corde_BA_BF'),
                                                        
                                                        # ('Cf','Corde_BA_BF'),
                                                        ('SkinFrictionMagnitude','Corde_BA_BF'),
                                                        # ('SkinFrictionX','Corde_BA_BF'),
                                                        # ('SkinFrictionY','Corde_BA_BF'),
                                                        # ('SkinFrictionZ','Corde_BA_BF'),

                                                        
                                                      ],
                                
                                'CourbeProfil_Yvar' : {'ROTOR' : { 
                                                                   # 'mis3' : {'Min' : 0.4, 'Max' : 1.5},    # Mettre None si on veut une valeur automatique ou enlever la variable du dictionnaire
                                                                   # 'hi'   : {'Min' : 0.0, 'Max' : 5},
                                                                   },
                                                       'STATOR' : {
                                                                   # 'mis3' : {'Min' : 0.0, 'Max' : 0.8},
                                                                   # 'hi'   : {'Min' : 0.0, 'Max' : 5},
                                                                   },
                                                      },
                                
                                'CourbeProfilRadiaux' : True,
                                'CourbeProfilRadiaux_XYvar' : [{'Xvar': 'mis3_max', 'Yvar': 'h_H', 'loc': ['Extrados']},
                                                               {'Xvar': 'Corde_BA_BF(mis3_max)', 'Yvar': 'h_H', 'loc': ['Extrados']},
                                                               # {'Xvar': 'mis3_ba', 'Yvar': 'h_H', 'loc': ['Intrados', 'Extrados'], 'Bornes': (0.0, 1.0)},
                                                               # {'Xvar': 'mis3_bf', 'Yvar': 'h_H', 'loc': ['Intrados', 'Extrados'], 'Bornes': (0.1, 1.0)},
                                                               {'Xvar': 'mis3_max/mis3_bf', 'Yvar': 'h_H', 'loc': ['Extrados']},
                                                               {'Xvar': 'mis3_max/mis3_bf', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 1.0)},
                                                               # {'Xvar': 'hi_max', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 1.0)},
                                                               # {'Xvar': 'hi_bf', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 1.0)},
                                                               # {'Xvar': 'delta_cell_count_max', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 1.0)},
                                                               {'Xvar': 'SkinFrictionMagnitude_min', 'Yvar': 'h_H', 'loc': ['Extrados']},
                                                               {'Xvar': 'SkinFrictionMagnitude_min', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 0.9)},
                                                               {'Xvar': 'Corde_BA_BF(SkinFrictionMagnitude_min)', 'Yvar': 'h_H', 'loc': ['Extrados'], 'Bornes': (0.1, 0.9)},

                                                               ],
                             }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_ProfilAzimuthaux
DicoXYVarProfilAzimuthaux2Trace = {'VisuGeom_2trace' : True,
                                   'ProfilAzimuthaux_Plan' : ['(BF+1)'],
                                   'ProfilAzimuthaux_HauteurType' : 'h_H' ,     # 'h_H'
                                   'ProfilAzimuthaux_HauteurListe'   : [''],  # # Pour tracer toutes les coupes [''] sinon  [10, 30, 50, 70, 80, 90]
                                   'ProfilAzimuthaux_XVar' : "azimuth" ,
                                   'ProfilAzimuthaux_YVar' : ['Ps','Pta','beta','Vx'],
                                   'ProfilAzimuthaux_DeltaYVar' : [],
                                   'ProfilAzimuthaux_CalculDisto' : 0,
                                   'ProfilAzimuthaux_SuperpositionCas' : 0,
                                   'ProfilAzimuthaux_SuperpositionPlan' : 0,
                                   'ProfilAzimuthaux_SuperpositionHauteur' : 0,
                                    }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_Polaire
DicoXYVarPolaire2Trace = {  'VisuGeom_2trace' : True,
                             'Polaire_XYvar'   : [  [('Qa_ref','BA'),('Pi',['BA','BF'])],
                                                    [('Qa','BF'),('Pi',['BA','BF'])],
                                                    [('etapol',['BA','BF']),('Pi',['BA','BF'])],
                                                    [('Qa_ref','BA'),('Tau',['BA','BF'])],
                                                    [('Qa','BF'),('Tau',['BA','BF'])],
                                                    [('absbeta1','BA'),('cd_fftro',['BA','BF'])],
                                                    [('INCD','BA'),('cd_fftro',['BA','BF'])],
                                                    [('Qa_ref','BA'),('cd_fftro',['BA','BF'])],
                                                    [('Qa','BF'),('cd_fftro',['BA','BF'])],
                                                    [('Qa_ref','BA'),('etapol',['BA','BF'])],
                                                    [('Qa','BF'),('etapol',['BA','BF'])],
                                                    [('absbeta1','BA'),('INCD','BA')],
                                                    [('absbeta1','BA'),('EFP','BF')],
                                                    [('INCD','BA'),('EFP','BF')],
                                                    [('absbeta1','BA'),('absbeta2','BF')],
                                                    [('absbeta1','BA'),('DLI',['BA','BF'])],
                                                    [('absbeta1','BA'),('W2_W1_RAL',['BA','BF'])],
                                                   ],
                              
                             # 'Polaire_XYvar'   : [  [('Qa','(BA-1)'),('cd_fftro',['(BA-1)','(BF+1)'])],
                                                    # [('Qa','(BA-1)'),('Pi',['(BA-1)','(BF+1)'])],
                                                    # [('Qa','(BA-1)'),('INCD','(BA-1)')],
                                                    # [('INCD','(BA-1)'),('cd_fftro',['(BA-1)','(BF+1)'])],
                                                    # [('INCD','(BA-1)'),('Pi',['(BA-1)','(BF+1)'])],
                                                    # [('INCD','(BA-1)'),('DLI',['(BA-1)','(BF+1)'])],
                                                    # [('INCD','(BA-1)'),('PSIA',['(BA-1)','(BF+1)'])],
                                                    # [('Mr','(BA-1)'),('PSIA',['(BA-1)','(BF+1)'])],
                                                    # [('INCD','(BA-1)'),('Mr', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('W', '(BA-1)')],
                                                    # [('Regime','BA'),('Corde', '(BA-1)')],
                                                    # [('Regime','BA'),('Calage', '(BA-1)')],
                                                    # [('Regime','BA'),('Freq1F', '(BA-1)')],
                                                    # [('Regime','BA'),('Freq1T', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('Vr_1F', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('Vr_1T', '(BA-1)')],
                                                    # [('Mr','(BA-1)'),('Vr_1F', '(BA-1)')],
                                                    # [('Mr','(BA-1)'),('Vr_1T', '(BA-1)')],
                                                    # [('Vr_1T','(BA-1)'),('Vr_1F', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('Fr_1F', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('Fr_1T', '(BA-1)')],
                                                    # [('Mr','(BA-1)'),('Fr_1F', '(BA-1)')],
                                                    # [('Mr','(BA-1)'),('Fr_1T', '(BA-1)')],
                                                    # [('Fr_1T','(BA-1)'),('Fr_1F', '(BA-1)')],
                                                    # [('INCD','(BA-1)'),('Allison_criteria', '(BA-1)')],
                                                    # [('Mr','(BA-1)'),('Allison_criteria', '(BA-1)')],
                                                    # [('Regime','(BA-1)'),('Allison_criteria', '(BA-1)')],
                                                   # ], 

                           'Polaire_Hauteur' : ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9'],
                           # 'Polaire_Hauteur' : ['0.25', '0.50', '0.875', '0.98'],
                          }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionParois
DicoXYVarEvolParois2Trace = { 'EvolutionParois_Var'     : ['alpha','beta','Ps','Pta','Tta','Vm','Mr','RhoVm'],
                              'EvolutionParois_Hauteur' : ["Moyeu","Carter"],  # "Moyeu", "Carter"
                              'EvolutionParois_Groupe'  : ["CFD","BSAM"],
                            }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionAxiale
DicoXYVarEvolAxiale2Trace = { 'EvolutionAxiale_YVar'      : ['alpha','beta','Ps','Pta','Tta','Vm','Mr','RhoVm'],
                              'EvolutionAxiale_XVar'      : 'X',
                              'EvolutionAxiale_PlanAmont' : 'Inlet',
                              'EvolutionAxiale_PlanAval'  : '*', # Si '*' alors tous les plans sont trace
                              'EvolutionAxiale_Hauteur'   : [0.2, 0.5, 0.8],
                              'EvolutionAxiale_InterDir'  : 'q_Q'   # q_Q ou h_H
                            }

# DICTIONNAIRE RELATIF A LA CLEF : Trace_EvolutionMeridienne
DicoXYVarEvolMeridienne2Trace = { 'EvolutionMeridienne_YVar'      : ['KD_Meridien','alpha','beta','Ps','Pta','Tta','Vm','Mr','RhoVm'],
                                  'EvolutionMeridienne_XVar'      : 'X',
                                  'EvolutionMeridienne_PlanAmont' : 'Inlet',
                                  'EvolutionMeridienne_PlanAval'  : 'Outlet',    # Si '*' alors tous les plans en aval du plan BA la grille sont utlisé
                                  'EvolutionMeridienne_Hauteur'   : ["mean"],  #"mean"
                                }

# DICTIONNAIRES RELATIF A LA CLEF : Trace_ProfilsRadiaux_CL
DicoXYVarProfilsRadiauxInlet = { 'VisuGeom_2trace' : True,
                                 'GradPlanUnique_Plan' : ['Inlet'],
                                 'GradPlanUnique_XVar' : ['Pta','Tta','Vx','Vt','alpha','phi','TurbulentDissipation','TurbulentEnergyKinetic','Viscosity_EddyMolecularRatio'],
                                 'GradPlanUnique_Yvar' : 'h_H',   # h_H / Q_q / R
                               }

DicoXYVarProfilsRadiauxOutlet = {'VisuGeom_2trace' : True,
                                 'GradPlanUnique_Plan' : ['Outlet'],
                                 'GradPlanUnique_XVar' : ['Ps'],
                                 'GradPlanUnique_Yvar' : 'h_H',   # h_H / Q_q / R
                                }

#-------------------------------------------------------------------------------------------------------------------
# PREFERENCE AFFICHAGE GRAPHE
DicoPrefGraphe = { "LegendSize" : 15, "TailleTitreX" : 16, "TailleTicksX" : 10, "TailleTitreY" : 16,  "TailleTicksY" : 10, "ShowCaseName" : 0, "ShowSecondGrid" : 1, "ShowAverage" : 0, "ShowLegend" : 0, "ShowFlux" : 0}

#-------------------------------------------------------------------------------------------------------------------
# PREFERENCE NBRE GRAPHE PAR PAGE
DicoNbreGraphe = { 'VisuGeomMeridienne'       : {'Nrow': 1, 'Ncol': 1},
                   'VisuGeomCoupe'            : {'Nrow': 1, 'Ncol': 1},
                   'VisuGeomAubage'           : {'Nrow': 1, 'Ncol': 1},
                   'VisuGeomBABF'             : {'Nrow': 2, 'Ncol': 3},
                   'VisuGeomCol3D'            : {'Nrow': 2, 'Ncol': 3},
                   'LoisGeom'                 : {'Nrow': 1, 'Ncol': 2},
                   'LoisGeomVsCorde'          : {'Nrow': 1, 'Ncol': 1},
                   'LoisGeomVsCorde_Hauteur'  : {'Nrow': 1, 'Ncol': 1},
                   'Convergence'              : {'Nrow': 1, 'Ncol': 1},
                   'VisuPlanPost'             : {'Nrow': 1, 'Ncol': 1},
                   'Perfos0D'                 : {'Nrow': 2, 'Ncol': 2},
                   'Perfos0DChamps'           : {'Nrow': 4, 'Ncol': 2},
                   'Polaire'                  : {'Nrow': 1, 'Ncol': 2},
                   'GradPlanInlet'            : {'Nrow': 2, 'Ncol': 3},
                   'GradPlanOutlet'           : {'Nrow': 1, 'Ncol': 2},
                   'GradPlanUnique'           : {'Nrow': 2, 'Ncol': 3},
                   'GradPlanVsPlanRef'        : {'Nrow': 1, 'Ncol': 2},
                   'ProfilAzimuthaux'         : {'Nrow': 1, 'Ncol': 2},
                   'ProfilAzimuthauxSum'      : {'Nrow': 2, 'Ncol': 3},
                   'ProfilVsCorde'            : {'Nrow': 1, 'Ncol': 1},
                   'ProfilVsCordeSum'         : {'Nrow': 2, 'Ncol': 3},
                   'EvolutionParois'          : {'Nrow': 1, 'Ncol': 1},
                   'EvolutionAxiale'          : {'Nrow': 1, 'Ncol': 1},
                   'VisuCFD'                  : {'Nrow': 1, 'Ncol': 1},
                   'VisuMESH'                 : {'Nrow': 2, 'Ncol': 1},
                }

#-------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DES FORMULES UTILISATEURS
DicoUserFormula = { 'absbeta1' : {'Var' : 'beta1' , 'Equation' : 'abs(beta1)'},
                    'absbeta2' : {'Var' : 'beta2' , 'Equation' : 'abs(beta2)'},
                    'PisQcorr_ref_KD_ref' : {'Var' : 'Pi,Qcorr_ref_KD_ref' , 'Equation' : 'Pi/Qcorr_ref_KD_ref'},
                    'Cambrure' : {'Var' : 'b2sqTo,b1sqTo' , 'Equation' : '-(b2sqTo-b1sqTo)'},
                    'H'        : {'Var' : 'delta1,theta11' , 'Equation' : 'delta1/theta11'},
                  }

#-------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DES COURBES UTILISATEURS
DicoUserCurves = {'Delta'            : {'X': [0, 0]       , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'DLI'              : {'X': [0.55, 0.55] , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'PSIA'             : {'X': [1.0, 1.0]   , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'INCD'             : {'X': [0.0, 0.0]   , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'EFP'              : {'X': [0.0, 0.0]   , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'V2_V1_RAL'        : {'X': [0.7, 0.7]   , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'W2_W1_RAL'        : {'X': [0.65, 0.65] , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'Marge'            : {'X': [3, 3]       , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'mis3_max/mis3_bf' : {'X': [2.5, 2.5]   , 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'SkinFrictionMagnitude' : {'X': [0.85, 1.0], 'Y': [0, 0] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'SkinFrictionMagnitude_min' : {'X': [0, 0], 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  'Corde_BA_BF(SkinFrictionMagnitude_min)' : {'X': [0.85, 0.85], 'Y': [0, 1] , 'Couleur': 'Pink' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 2},
                  
                  # 'Vr_1F_criteria_PC203' : {'X': [-10, 10], 'Y': [5.56, 5.56] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  # 'Vr_1F_criteria_PC267' : {'X': [-10, 10], 'Y': [5.50, 5.50] , 'Couleur': 'Green' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1F_criteria_GE' : {'X': [-10, 10], 'Y': [5, 5] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Vr_1F_criteria_PC203_SAE_DEM21_neg' : {'X': [-10.3, -8.0, -5.9], 'Y': [0.00, 0.75, 1.50] , 'Couleur': 'Orange' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Vr_1F_criteria_PC203_GE_DAM_pos' : {'X': [5.5, 5.7, 7.0, 8.0, 10.0, 13.0], 'Y': [5.00, 3.50, 3.00, 2.80, 2.60, 2.42] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Vr_1F_criteria_PC203_GE_GrandeCorde_pos' : {'X': [7.2, 8.0, 10.0, 12.0, 14.0], 'Y': [5.50, 4.60, 3.90, 3.40, 3.00] , 'Couleur': 'Blue' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1F_criteria_PC203_GE_GrandeCorde_neg' : {'X': [-20, -15, -11, -8, -5.7, -4.2], 'Y': [2, 2.65, 3.6, 4.6, 5.6, 7.0] , 'Couleur': 'Blue' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1F_criteria_PC203_GE_TouteAube_pos' : {'X': [5.0, 5.0, 10.5, 14.0], 'Y': [5.30, 3.20, 1.80, 1.80] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},

                  'Vr_1T_criteria_PC203' : {'X': [0, 7.5], 'Y': [1.54, 1.54] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1T_criteria_PC267' : {'X': [0, 7.5], 'Y': [1.60, 1.60] , 'Couleur': 'Green' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1T_criteria_GE' : {'X': [0, 7.5], 'Y': [1.60, 1.60] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},

                  'Vr_1T_criteria_PC203_GE_GrandeCorde_pos' : {'X': [7.45, 7.45, 7.8, 8.2, 9.3, 10, 11, 12, 13], 'Y': [1.80, 1.6, 1.5, 1.4, 1.2, 1.1, 1, 0.95, 0.91] , 'Couleur': 'Blue' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1T_criteria_PC203_SAE_pos' : {'X': [6.50, 6.5, 7, 7.5, 8.5, 10], 'Y': [1.80, 1.6, 1.4, 1.3, 1.2, 1.2] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Vr_1T_criteria_SAE_expe_M53_pos' : {'X': [14.0, 12.6, 11.1, 10.1, 9.3, 8.7, 8.5, 8.6, 8.6, 8.8, 9.0, 9.4], 'Y': [1.01, 1.05, 1.12, 1.18, 1.24, 1.35, 1.43, 1.47, 1.51, 1.55, 1.59, 1.63] , 'Couleur': 'Orange' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  'Vr_1T_criteria_SAE_expe_H6_pos' : {'X': [5.00, 7.8], 'Y': [0.60, 0.2] , 'Couleur': 'Orange' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Fr_1F_criteria_PC350' : {'X': [-5, 10], 'Y': [0.86, 0.86] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  # 'Fr_1F_criteria_GE' : {'X': [-5, 10], 'Y': [0.40, 0.40] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Fr_1T_criteria_PC350' : {'X': [-5, 10], 'Y': [1.37, 1.37] , 'Couleur': 'Green' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  # 'Fr_1T_criteria_GE' : {'X': [-5, 10], 'Y': [1.25, 1.25] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Armstrong_Stevenson_criteria' : {'X': [1.37, 1.37, 1.37, 1.0, 3], 'Y': [2, 0.7, 0.86, 0.86, 0.86] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  'Allison_criteria' : {'X': [1.00013, 1.25379, 1.53325, 1.82131, 1.99759], 'Y': [3.28442, 2.56159, 1.76268, 0.938406, 0.431159] , 'Couleur': 'Red' , 'Ligne': 'SolidLine', 'Symbole': None, 'Epaisseur': 1},
                  'Allison_criteria_SAE_exp' : {'X': [1.0, 1.6], 'Y': [2.4, 0.67] , 'Couleur': 'Orange' , 'Ligne': 'DashLine', 'Symbole': None, 'Epaisseur': 1},
                  
                  }

#-------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE DE CORRESPONDANCE DES LABELS ISSUENT DU BSAM
DicoCorrLabel = { 'HDE' : 'RDE',
                  'BDE' : 'RDE',
                  'IGV' : 'RDE',
                  'R'   : 'RM' ,
                  'S'   : 'RD' ,
                  'HR'  : 'RM' ,
                  'HS'  : 'RD' ,
                  'BR'  : 'RM' ,
                  'BS'  : 'RD' ,
                  'OGV' : 'OGV',
                  }

#-------------------------------------------------------------------------------------------------------------------
# DICTIONNAIRE POUR LA MISE EN FORMES DES VARIABLES
DicoVariables = {   'h_H'         : {'Nom': 'Hauteur Adimensionne'      ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'h_H_norm'    : {'Nom': 'Hauteur Adimensionne'      ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    '_h_H'        : {'Nom': 'Hauteur Adimensionne'      ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'h_H_BA'      : {'Nom': 'Hauteur Adimensionne BA'   ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'h_H_BF'      : {'Nom': 'Hauteur Adimensionne BF'   ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'rBA_adim'    : {'Nom': 'Hauteur Adimensionne BA'   ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'rBF_adim'    : {'Nom': 'Hauteur Adimensionne BF'   ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'rMoyen_adim' : {'Nom': 'Hauteur Adimensionne'      ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.0, 'Max':1.0},
                    'Numadim'     : {'Nom': 'Numero des grilles'        ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': -0.05, 'Max':1.05},
                    'R'           : {'Nom': 'Rayon'                     ,'Unite':'[m]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.01 , 'PGMax':0.99, 'limiteur': 5.0, 'Min': 0.1, 'Max':0.18},
                    
                    'b1sqTo'       : {'Nom': 'b1sqTo'                  ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'b2sqTo'       : {'Nom': 'b2sqTo'                  ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Calage'       : {'Nom': 'Calage'                  ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Cambrure'     : {'Nom': 'Cambrure'                ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Corde'        : {'Nom': 'Corde'                   ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'CordeAxi'     : {'Nom': 'Corde Axiale'            ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'ssc'          : {'Nom': 'Pas Relatif (S/C)'       ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    's'            : {'Nom': 'Pas inter Aube (S)'      ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'H_C'          : {'Nom': 'H_C'                     ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.8, 'Max':2.0},
                    'H_CAX'        : {'Nom': 'H_CAX'                   ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.8, 'Max':2.0},
                    'Emax'         : {'Nom': 'Emax'                    ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'EmaxsC'       : {'Nom': 'Emax/C'                  ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'XEmax'        : {'Nom': 'XEmax'                   ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'XEmaxsC'      : {'Nom': 'XEmax/C'                 ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'FmaxsC'       : {'Nom': 'Flechemax/C'             ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'XFmaxsC'      : {'Nom': 'XFlechemax/C'            ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'XgCale'       : {'Nom': 'Xg'                      ,'Unite':'[mm]'   ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'YgCale'       : {'Nom': 'Yg'                      ,'Unite':'[mm]'   ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'xBa'          : {'Nom': 'X BA'                    ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'xBf'          : {'Nom': 'X BA'                    ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'yBa'          : {'Nom': 'Y BA'                    ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'yBF'          : {'Nom': 'Y BF'                    ,'Unite':'[mm]'   ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'sweep_BA'     : {'Nom': 'Sweep Meca - BA'         ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'sweep_BF'     : {'Nom': 'Sweep Meca - BF'         ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'dihedral_BA'  : {'Nom': 'Diedre Meca - BA'        ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'dihedral_BF'  : {'Nom': 'Diedre Meca - BF'        ,'Unite':'[Deg]'  ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'ACol/S'       : {'Nom': 'ACol/S'                  ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'ACol/AEntree' : {'Nom': 'ACol/AEntree'            ,'Unite':'[-]'    ,'NbreCS': 3,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'ASortie/ACol' : {'Nom': 'ASortie/ACol'            ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'SCol/SX'      : {'Nom': 'SCol/SX'                 ,'Unite':'[-]'    ,'NbreCS': 1,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'XCol/CX'      : {'Nom': 'XCol/CX'                 ,'Unite':'[-]'    ,'NbreCS': 0,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Mach Entree'  : {'Nom': 'Mach Entree'             ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Mach Sortie'  : {'Nom': 'Mach Sortie'             ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    
                    'Qcorr'                    : {'Nom': 'Debit reduit'                                  ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'Qcorr_ref'                : {'Nom': 'Debit reduit Amont'                            ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'deltapctQcorr_ref'        : {'Nom': 'Delta Relatif Debit reduit Amont [%]'          ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'Qcorr_ref_KD'             : {'Nom': 'Debit reduit Amont*Kd'                         ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'Qcorr_ref_KD_ref'         : {'Nom': 'Debit reduit Amont*Kd Amont'                   ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'deltapctQcorr_ref_KD_ref' : {'Nom': 'Delta Relatif Debit reduit Amont*Kd Amont [%]' ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'Qa'                       : {'Nom': 'Qa'                                            ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    'Qa_ref'                   : {'Nom': 'Qa_ref'                                        ,'Unite':'[-]'    ,'NbreCS': 2,  'FactMulti' : 1  , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.0, 'Max':100.},
                    
                    'etapol'           : {'Nom': 'Rendement'                     ,'Unite':'[Point]'   ,'NbreCS': 3,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.9, 'Max':1.0},
                    'deltaetapol'      : {'Nom': 'Delta Absolu Rendement [Pt]'   ,'Unite':'[Point]'   ,'NbreCS': 3,  'FactMulti' : 100     , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':5.0, 'Min': 0.9, 'Max':1.0},
                    'cd_fftro'         : {'Nom': 'Cd fftro'                      ,'Unite':'[-]'       ,'NbreCS': 3,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 0.0, 'Max':0.20},
                    'deltapctcd_fftro' : {'Nom': 'Delta Relatif Cd [%]'          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Cd_MISES'         : {'Nom': 'Cd MISES'                      ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 0.0, 'Max':0.20},
                    'Cd_shock_MISES'   : {'Nom': 'Cd Choc MISES'                 ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 0.0, 'Max':0.20},
                    'Cd_visc_MISES'    : {'Nom': 'Cd Visq MISES'                 ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 0.0, 'Max':0.20},
                    'Tau'              : {'Nom': 'TT2/TT1'                       ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Pi'               : {'Nom': 'Pi'                            ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'deltapctPi'       : {'Nom': 'Delta Relatif Pi [%]'          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'PisD'             : {'Nom': 'Pi/D'                          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Dev'              : {'Nom': 'Deviation'                     ,'Unite':'[Deg]'     ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'W2_W1_RAL'        : {'Nom': 'Ralentisement relatif'         ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'V2_V1_RAL'        : {'Nom': 'Ralentisement absolu'          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'RAL'              : {'Nom': 'Ralentisement absolu'          ,'Unite':'[m/s]'     ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'PSIA'             : {'Nom': 'PSIA'                          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'AVDR'             : {'Nom': 'AVDR'                          ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'DLI'              : {'Nom': 'DLI'                           ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Marge'            : {'Nom': 'Marge au blocage'              ,'Unite':'[%]'       ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    
                    'Ps'            : {'Nom': 'Pression statique'             ,'Unite':'[Bar]'     ,'NbreCS': 1,  'FactMulti' : 0.00001 , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Pta'           : {'Nom': 'Pression totale absolu'        ,'Unite':'[Bar]'     ,'NbreCS': 1,  'FactMulti' : 0.00001 , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Ptr'           : {'Nom': 'Pression totale relative'      ,'Unite':'[Bar]'     ,'NbreCS': 1,  'FactMulti' : 0.00001 , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    
                    'Ts'            : {'Nom': 'Temperature statique'          ,'Unite':'[K]'       ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Tta'           : {'Nom': 'Temperature totale absolue'    ,'Unite':'[K]'       ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Ttr'           : {'Nom': 'Temperature totale relative'   ,'Unite':'[K]'       ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    
                    'Vx'            : {'Nom': 'Vx'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Vy'            : {'Nom': 'Vy'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Vz'            : {'Nom': 'Vz'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Vm'            : {'Nom': 'Vm'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Vr'            : {'Nom': 'Vr'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Vt'            : {'Nom': 'Vt'                            ,'Unite':'[m/s]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                                    
                    'Mx'            : {'Nom': 'Mx'                            ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Ma'            : {'Nom': 'Ma'                            ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Mr'            : {'Nom': 'Mr'                            ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Mm'            : {'Nom': 'Mm'                            ,'Unite':'[-]'       ,'NbreCS': 2,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                                    
                    'alpha'         : {'Nom': 'Alpha'                         ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'beta'          : {'Nom': 'Beta'                          ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'phi'           : {'Nom': 'Phi'                           ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'alpha1'        : {'Nom': 'Alpha1'                        ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'alpha2'        : {'Nom': 'Alpha2'                        ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'beta1'         : {'Nom': 'Beta1'                         ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'beta2'         : {'Nom': 'Beta2'                         ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'absbeta1'      : {'Nom': 'ABS(beta1)'                    ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'absbeta2'      : {'Nom': 'ABS(beta2)'                    ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'bsq1'          : {'Nom': 'BetaTo1'                       ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'bsq2'          : {'Nom': 'BetaTo2'                       ,'Unite':'[Deg]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'incd'          : {'Nom': 'INCD'                          ,'Unite':'[Deg]'     ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': -10.0, 'Max':10.0},
                    'INCD'          : {'Nom': 'INCD'                          ,'Unite':'[Deg]'     ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': -10.0, 'Max':10.0},
                    'efp'           : {'Nom': 'EFP'                           ,'Unite':'[Deg]'     ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': -5.0, 'Max':15.0},
                    'EFP'           : {'Nom': 'EFP'                           ,'Unite':'[Deg]'     ,'NbreCS': 1,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': -5.0, 'Max':15.0},
                    
                    'Viscosity_EddyMolecularRatio'  : {'Nom': 'Mut/Mu'                         ,'Unite':'[-]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'TurbulentEnergyKinetic'        : {'Nom': 'Energie cinetique Turbulente'   ,'Unite':'[-]'     ,'NbreCS': 0,  'FactMulti' : 1       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'TurbulentDissipation'          : {'Nom': 'Dissipation Turbulente'         ,'Unite':'[*10^5]' ,'NbreCS': 1,  'FactMulti' : 0.00001       , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    
                    'BSQ'           : {'Nom': 'Pente squelette'                 ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':20.0, 'Min': 0.0, 'Max':1.0},
                    'BSQS'          : {'Nom': 'Pente squelette simplifiee'      ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':20.0, 'Min': 0.0, 'Max':1.0},
                    'BSQ_EXT'       : {'Nom': 'Pente Extrados'                  ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':20.0, 'Min': 0.0, 'Max':1.0},
                    'BSQ_INT'       : {'Nom': 'Pente Intrados'                  ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.10, 'PGMax':0.90, 'limiteur':20.0, 'Min': 0.0, 'Max':1.0},
                    'BSQ_adim'      : {'Nom': 'Pente squelette adim'            ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'BSQS_adim'     : {'Nom': 'Pente squelette simplifiee adim' ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'PENTE_EXTRA'   : {'Nom': 'Pente squelette Extrados'        ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.1,  'PGMax':0.9,  'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'PENTE_INTRA'   : {'Nom': 'Pente squelette Intrados'        ,'Unite':'[Deg]'   ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.1,  'PGMax':0.9,  'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'EPAIS'          : {'Nom': 'Epaisseur'                       ,'Unite':'[mm]'    ,'NbreCS': 0,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05,  'PGMax':0.95,  'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'EPAIS_adim'     : {'Nom': 'Epaisseur adim'                  ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    
                    'cordeRed_BA_BF_BA_RayCourbure': {'Nom': 'cordeRed_BA_BF_BA'             ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 0.0, 'Max':2.0},
                    'cordeRed_RayCourbure_Ext'     : {'Nom': 'cordeRed'                      ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 0.0, 'Max':2.0},
                    'cordeRed_RayCourbure_Int'     : {'Nom': 'cordeRed'                      ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 0.0, 'Max':2.0},
                    'corde_Courbure'               : {'Nom': 'Corde'                         ,'Unite':'[mm]'    ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 0.0, 'Max':2.0},
                    'corde_Courbure_adim'          : {'Nom': 'CordeRed'                      ,'Unite':'[-]'     ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'RayonCourbure'                : {'Nom': 'Rayon de courbure'             ,'Unite':'[mm]'    ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': None, 'PGMax':None, 'limiteur':5.0, 'Min': 1.4, 'Max':1.6},
                    'RayonCourbure_Ext'            : {'Nom': 'Rayon de courbure Extrados'    ,'Unite':'[mm]'    ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':10.0, 'Min': 1.4, 'Max':1.6},
                    'RayonCourbure_Int'            : {'Nom': 'Rayon de courbure Intrados'    ,'Unite':'[mm]'    ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':10.0, 'Min': 1.4, 'Max':1.6},
                    'Courbure'                     : {'Nom': 'Courbure'                      ,'Unite':'[1/mm]'  ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':5.0, 'Min': 1.4, 'Max':1.6},
                    
                    'X'           : {'Nom': 'X'                                ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Y'           : {'Nom': 'Y'                                ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': None, 'PGMax': None, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'cordeRed'    : {'Nom': 'Corde BA->BF'                     ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'm_Adim'      : {'Nom': 'm_adim'                           ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Corde BA->BF': {'Nom': 'Corde BA->BF'                     ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'Corde_BA_BF' : {'Nom': 'Corde BA->BF'                     ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'd_D'         : {'Nom': 'Abscisse Curviligne Adimensionne' ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.0, 'Max':1.0},
                    'hi'          : {'Nom': 'Facteur de Forme incompressible'  ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'H'           : {'Nom': 'Facteur de Forme compresible'     ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'ShapeFactor' : {'Nom': 'Facteur de Forme compresible'     ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.95, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'SkinFrictionMagnitude' : {'Nom': 'Frottement au parois'   ,'Unite':'[Pa]'  ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.1, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'delta'       : {'Nom': 'Epaisseur de couche limite'       ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'delta1'      : {'Nom': 'Epaisseur dplt longitudinal'      ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'delta2'      : {'Nom': 'Epaisseur dplt transverse'        ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'theta'       : {'Nom': 'Epaisseur qdm longitudinal'       ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'theta11'     : {'Nom': 'Epaisseur qdm longitudinal'       ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'theta12'     : {'Nom': 'Epaisseur qdm transverse'         ,'Unite':'[m]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.05, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'mis3'        : {'Nom': 'MachIs'                           ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.04, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':None},
                    'mis3_max'    : {'Nom': 'MachIs_Max'                       ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'mis3_BF'     : {'Nom': 'MachIs_BF'                        ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    # 'Corde_BA_BF(mis3)' : {'Nom': 'X_MachIs_Max'             ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    # 'd_D_aero_max(mis3)' : {'Nom': 'X_MachIs_Max'            ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    'mis3_max/mis3_bf' : {'Nom': 'MachIs_Max/MachIs_BF'        ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'Corde_BA_BF(SkinFrictionMagnitude_min)' : {'Nom': 'X_SkinFrictionMagnitude_min'        ,'Unite':'[-]'   ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'  , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0.0, 'Max':1.0},
                    
                    'KD'          : {'Nom': 'KD'                               ,'Unite':'[-]'   ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.8, 'Max':1.0},
                    'KD_Meridien' : {'Nom': 'KD_Meridien'                      ,'Unite':'[-]'   ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 0.8, 'Max':1.0},
                    
                    'XNR'         : {'Nom': 'Regime reduit'                    ,'Unite':'[-]'   ,'NbreCS': 0,  'FactMulti' : -1   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 200, 'Max':1500},
                    
                    'REYc'        : {'Nom': 'Reynolds_corde'                   ,'Unite':'[Millions]'   ,'NbreCS': 2,  'FactMulti' : 0.000001   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 200, 'Max':1500},
                    'Ra_HL'       : {'Nom': 'Rugosite lisse'                   ,'Unite':'[Microns]' ,'NbreCS': 2,  'FactMulti' : 1000000   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':5.0, 'Min': 200, 'Max':1500},
                    
                    'Vr_1F' : {'Nom': 'Vitesse Reduite_1F'                     ,'Unite':'[-]' ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'Vr_1T' : {'Nom': 'Vitesse Reduite_1T'                     ,'Unite':'[-]' ,'NbreCS': 1,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'Fr_1F' : {'Nom': 'Freq Reduite_1F'                        ,'Unite':'[-]' ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'Fr_1T' : {'Nom': 'Freq Reduite_1T'                        ,'Unite':'[-]' ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Mode P. Ginibre'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': None, 'Max':1.0},
                    'Allison_criteria'     : {'Nom': 'Allison'                 ,'Unite':'[-]' ,'NbreCS': 2,  'FactMulti' : 1   , 'autoScaleMode': 'Manuel'           , 'PGMin': 0.02, 'PGMax':0.98, 'limiteur':10.0, 'Min': 0, 'Max':10.0},
                    
                    }