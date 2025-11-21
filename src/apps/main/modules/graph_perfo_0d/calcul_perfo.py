import math
from bsamreader import ThroughFlow
from bsamreader.average import RadialEntropicAverage
import pandas as pd
import numpy as np

from apps.main.models import Cas, RowPair
from apps.main.modules.graph_perfo_0d.gestion_data import \
    get_row_from_bsam, get_row_from_antares_card, load_bdd_data, add_cas_info, \
    set_inlet_outlet_row_obj, set_type_of_rowpair, load_hdf_data, get_value_from_df_hdf, \
    get_sheet_name_from_rowpair
from apps.main.modules.graph_perfo_0d.get_config_from_row import define_config_list

pd.set_option("display.max_columns", None)

def apply_recalage_kd(case_obj, perfos_data):

    kd = case_obj.iso_vitesse.recalage_kd
    if kd is not None:
        if perfos_data.get('Qcorr') is not None:
            perfos_data['Qcorr'] = kd * perfos_data['Qcorr']
        if perfos_data.get('Qcorr_ref') is not None:
            perfos_data['Qcorr_ref'] = kd * perfos_data['Qcorr_ref']
        if perfos_data.get('PisQcorr_ref') is not None:
            perfos_data['PisQcorr_ref'] = perfos_data['PisQcorr_ref'] / kd
    else:
        # TODO: Prendre le KD de la première roue (exemple)
        # kd_bsam = get_bsam_kd(case_obj)  # À implémenter
        # perfos_data['Qcorr'] = kd_bsam * perfos_data['Qcorr']
        # perfos_data['Qcorr_ref'] = kd_bsam * perfos_data['Qcorr_ref']
        pass
    return perfos_data

def set_rowpair_val(rowpair_obj, data):
    rowpair_obj.Qcorr_ref = data.get("Qcorr_ref")
    rowpair_obj.Qcorr = data.get("Qcorr")
    rowpair_obj.Pi = data.get("Pi")
    rowpair_obj.Etapol = data.get("Etapol")
    rowpair_obj.Cd = data.get("Cd")
    rowpair_obj.Tau = data.get("Tau")
    rowpair_obj.PisQcorr_ref = data.get("PisQcorr_ref")
    rowpair_obj.save()

def calculer_qcorr(Q, Tta, Pta):
    return Q * (math.sqrt(Tta / 288.15) / (Pta / 101325))

def calculer_pi(Pta1, Pta2):
    return Pta2 / Pta1

def calculer_tau(tta1, tta2):
    return tta2 / tta1

def calculer_cd_fftro(ps1, tta1, tta2, pta1, pta2, ptr1, ptr2, gamma1, gamma2, r_gas):
    """
    Compute losses with the same formulation as FFTRO (GENEPI/ANNA)

    :param tta1: inlet total temperature in the absolute frame
    :type tta1: float
    :param tta2: outlet total temperature in the absolute frame
    :type tta2: float
    :param pta1: inlet total pressure in the absolute frame
    :type pta1: float
    :param pta2: outlet total pressure in the absolute frame
    :type pta2: float
    :param gamma1: inlet heat capacity ratio
    :type gamma1: float
    :param gamma2: outlet heat capacity ratio
    :type gamma2: float
    :param r_gas: Gas constant
    :type r_gas: float
    :return: losses  = cd_fftro
    :rtype: float
    """

    cpsr1 = gamma1 / (gamma1 - 1)
    cpsr2 = gamma2 / (gamma2 - 1)

    if abs(cpsr2 - cpsr1) > 0.0005:
        polynomial = compute_polynomial(0.0, 0.0)
        fi1 = compute_phit(polynomial, tta1) / r_gas
        fi2 = compute_phit(polynomial, tta2) / r_gas
    else:
        fi1 = cpsr2 * np.log(tta1)
        fi2 = cpsr2 * np.log(tta2)

    ds = r_gas * (fi2 - fi1 - np.log(pta2 / pta1))
    cd_fftro = ptr2 * (np.exp(ds / r_gas) - 1.0) / (ptr1 - ps1)

    return cd_fftro

def calculer_etapol(tta1, tta2, pta1, pta2, gamma1, gamma2, r_gas):
    """
    Compute polytropic Efficiency with the same formulation as FFTRO (GENEPI/ANNA)

    :param tta1: inlet total temperature in the absolute frame
    :type tta1: float
    :param tta2: outlet total temperature in the absolute frame
    :type tta2: float
    :param pta1: inlet total pressure in the absolute frame
    :type pta1: float
    :param pta2: outlet total pressure in the absolute frame
    :type pta2: float
    :param gamma1: inlet heat capacity ratio
    :type gamma1: float
    :param gamma2: outlet heat capacity ratio
    :type gamma2: float
    :param r_gas: Gas constant
    :type r_gas: float
    :return: polytropic efficiency = etapol
    :rtype: float
    """
    if tta2 / tta1 != 1.0:
        cpsr1 = gamma1 / (gamma1 - 1)
        cpsr2 = gamma2 / (gamma2 - 1)

        if abs(cpsr2 - cpsr1) > 0.0005:
            polynomial = compute_polynomial(0.0, 0.0)
            fi1 = compute_phit(polynomial, tta1)
            fi2 = compute_phit(polynomial, tta2)
            etapol = r_gas * np.log(pta2 / pta1) / (fi2 - fi1)
        else:
            fi1 = cpsr2 * np.log(tta1)
            fi2 = cpsr2 * np.log(tta2)
            etapol = np.log(pta2 / pta1) / (fi2 - fi1)
    else:
        return np.sign(pta2 / pta1 - 1.0) * float("inf")

    return etapol

def compute_polynomial(far=0.0, war=0.0):
    """
    compute the coefficients of Heat Capacity (Cp) polynomial
    These coefficients are from the document "Modélisation thermodynamiques Janus YYPV – Avril 2008"
    which used the document 1982 - NASA Technical Paper 1906 - Thermodynamic Transport Combustion Properties of Hydrocarbons With Air
    The validity of these coeffcients is between 200K and 2200K

    :param far: fuel air ratio
    :type far: float
    :param war: water air ratio
    :type war: float
    :return: ideal Gas Heat Capacity polynomial coefficients (Cp)
    :rtype: np.array
    """
    cp_kerosene = np.array(
        [
            1.2850007e03,
            2.3021158e00,
            -5.2739400e-04,
            0.0000000e00,
            0.0000000e00,
            0.0000000e00,
            0.0000000e00,
            0.0000000e00,
        ]
    )
    cp_air = np.array(
        [
            1.0684300e03,
            -5.2174200e-01,
            1.2378500e-03,
            -6.2798400e-07,
            -3.3094000e-10,
            4.7097200e-13,
            -1.7961300e-16,
            2.3582200e-20,
        ]
    )
    cp_water = np.array(
        [
            0.188457e04,
            -0.484304,
            0.173478e-02,
            -0.114179e-05,
            0.334500e-09,
            -0.386134e-13,
            0.0000000e00,
            0.0000000e00,
        ]
    )
    return (cp_air + far * cp_kerosene + war * cp_water) / (1 + far + war)

def compute_phit(polynomial, temperature):
    """
    compute the variable PhiT base on the Cp polynomial coefficient at a given temperature

    :param polynomial: ideal Gas Heat Capacity polynomial coefficients (Cp)
    :type polynomial: np.array
    :param temperature: temperature
    :type temperature: float
    :return: phiT
    :rtype: float
    """
    return (
        polynomial[0] * np.log(temperature)
        + polynomial[1] * temperature
        + polynomial[2] / 2 * temperature**2
        + polynomial[3] / 3 * temperature**3
        + polynomial[4] / 4 * temperature**4
        + polynomial[5] / 5 * temperature**5
        + polynomial[6] / 6 * temperature**6
        + polynomial[7] / 7 * temperature**7
    )

def set_perfo_data_format(cd, etapol, qcorr_ref, qcorr, pi, pisqcorrref, tau):
    return {
        "Cd": round(100 * cd, 2),
        "Etapol": round(etapol, 4),
        "Qcorr_ref": round(qcorr_ref, 4),
        "Qcorr": round(qcorr, 4),
        "Pi": round(pi, 4),
        'PisQcorr_ref': round(pisqcorrref, 4),
        "Tau": round(tau, 4)
    }

def update_perfo_data(perfo_data, stator_only):

    if stator_only:
        perfo_data['Etapol'] = 0
    else:
        perfo_data['Cd'] = 0
    print(f" stator_only = {stator_only} --> {perfo_data['Etapol']}")
    return perfo_data

def compute_perfo(aero_data):
    gamma1 = aero_data.get('gamma1')
    gamma2 = aero_data.get('gamma2')
    r_gas = aero_data.get('r_gas')
    q1_moy = aero_data.get('q1_moy')
    q2_moy = aero_data.get('q2_moy')
    ps1_moy = aero_data.get('ps1_moy')
    tta1_moy = aero_data.get('tta1_moy')
    tta2_moy = aero_data.get('tta2_moy')
    pta1_moy = aero_data.get('pta1_moy')
    pta2_moy = aero_data.get('pta2_moy')
    ptr1_moy = aero_data.get('ptr1_moy')
    ptr2_moy = aero_data.get('ptr2_moy')

    cd = calculer_cd_fftro(ps1_moy, tta1_moy, tta2_moy, pta1_moy, pta2_moy, pta1_moy, pta2_moy, gamma1, gamma2, r_gas)
    etapol = calculer_etapol(tta1_moy, tta2_moy, pta1_moy, pta2_moy, gamma1, gamma2, r_gas)
    qcorr_ref = calculer_qcorr(q1_moy, tta1_moy, pta1_moy)
    qcorr = calculer_qcorr(q2_moy, tta2_moy, pta2_moy)
    pi = calculer_pi(pta1_moy, pta2_moy)
    tau = calculer_tau(tta1_moy, tta2_moy)
    pisqcorrref = pi / qcorr_ref

    perfo_data = set_perfo_data_format(cd, etapol, qcorr_ref, qcorr, pi, pisqcorrref, tau)

    return perfo_data

def compute_perfo_bsam(tf, rowpair_obj):

    debit = tf.debn

    zone_start = tf.get_row_zone(rowpair_obj.entry_row.bsam_name)[0]
    zone_end = tf.get_row_zone(rowpair_obj.exit_row.bsam_name)[0]

    average_inlet = RadialEntropicAverage(zone_start.inlet)
    average_outlet = RadialEntropicAverage(zone_end.outlet)

    aero_data = {
        'gamma1': zone_start.inlet.gamma,
        'gamma2': zone_end.outlet.gamma,
        'r_gas': tf.rgas,
        'q1_moy': debit * zone_start.inlet.qdjz,
        'q2_moy': debit * zone_end.outlet.qdjz,
        'ps1_moy': average_inlet.p,
        'ps2_moy': average_outlet.p,
        'tta1_moy': average_inlet.Tt,
        'tta2_moy': average_outlet.Tt,
        'pta1_moy': average_inlet.pt,
        'pta2_moy': average_outlet.pt,
        'ptr1_moy': average_inlet.ptw(omega=zone_start.omega),
        'ptr2_moy': average_outlet.ptw(omega=zone_end.omega)
        }

    perfo_data = compute_perfo(aero_data)

    perfo_data = update_perfo_data(perfo_data, rowpair_obj.is_only_stator())

    set_rowpair_val(rowpair_obj, perfo_data)

    set_type_of_rowpair(rowpair_obj, "")

    return perfo_data

def compute_perfo_excel(cas, rowpair_obj):

    sheet_name = get_sheet_name_from_rowpair(cas.file_path, rowpair_obj)

    df = pd.read_excel(cas.file_path, sheet_name=sheet_name)
    df["Qcorr"] = df["Qcorr_ref"] * np.sqrt(df["Tau"]) / df["Pi"]

    row = df.iloc[0]

    cd = float(row["Cd"])
    etapol = float(row.get("etapol", 1.0))
    qcorr_ref = float(row["Qcorr_ref"])
    qcorr = float(row["Qcorr"])
    pi = float(row["Pi"])
    pisqcorrref = pi / qcorr_ref
    tau = float(row["Tau"])

    perfo_data = set_perfo_data_format(cd, etapol, qcorr_ref, qcorr, pi, pisqcorrref, tau)

    perfo_data = update_perfo_data(perfo_data, rowpair_obj.is_only_stator())

    set_rowpair_val(rowpair_obj, perfo_data)

    set_type_of_rowpair(rowpair_obj, sheet_name)

    return perfo_data

def compute_perfo_hdf(cas, rowpair_obj):

    df = load_hdf_data(cas)

    pair_row_name_split = rowpair_obj.name.split("-")
    if len(pair_row_name_split) == 1:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[0]
    else:
        row_amont, row_aval = pair_row_name_split[0], pair_row_name_split[1]

    aero_data = {
        'gamma1': df[df['BSAM_Name'] == row_amont]['gamma'].unique()[0],
        'gamma2': df[df['BSAM_Name'] == row_aval]['gamma'].unique()[0],
        'r_gas': df[df['BSAM_Name'] == row_amont]['r_gaz'].unique()[0],
        'q1_moy': get_value_from_df_hdf(df, row_amont, 'Inlet', 'Q'),
        'q2_moy': get_value_from_df_hdf(df, row_aval, 'Outlet', 'Q'),
        'ps1_moy': get_value_from_df_hdf(df, row_amont, 'Inlet', 'Ps'),
        'ps2_moy': get_value_from_df_hdf(df, row_aval, 'Outlet', 'Ps'),
        'tta1_moy': get_value_from_df_hdf(df, row_amont, 'Inlet', 'Tta'),
        'tta2_moy': get_value_from_df_hdf(df, row_aval, 'Outlet', 'Tta'),
        'pta1_moy': get_value_from_df_hdf(df, row_amont, 'Inlet', 'Pta'),
        'pta2_moy': get_value_from_df_hdf(df, row_aval, 'Outlet', 'Pta'),
        'ptr1_moy': get_value_from_df_hdf(df, row_amont, 'Inlet', 'Ptr'),
        'ptr2_moy': get_value_from_df_hdf(df, row_aval, 'Outlet', 'Ptr')
        }

    perfo_data = compute_perfo(aero_data)

    perfo_data = update_perfo_data(perfo_data, rowpair_obj.is_only_stator())

    set_rowpair_val(rowpair_obj, perfo_data)

    set_type_of_rowpair(rowpair_obj, "")

    return perfo_data

def process_data(data_cache, iso_vitesse):

    case_obj_list = Cas.objects.filter(iso_vitesse=iso_vitesse, used=True)

    for case_obj in case_obj_list:
        print(f" * On traite le cas suivant --> {case_obj.name}")
        if iso_vitesse.file_type == "excel" or iso_vitesse.file_type == "hdf":
            row_obj_list = get_row_from_antares_card(case_obj)
            iso_vitesse.row_config = define_config_list(row_obj_list)
            iso_vitesse.save()

        elif iso_vitesse.file_type == "bsam":
            row_obj_list = get_row_from_bsam(case_obj)
            iso_vitesse.row_config = define_config_list(row_obj_list)
            iso_vitesse.save()

    for rowpair_label in iso_vitesse.get_lst_row_config():
        data_cache.setdefault(rowpair_label, {})
        print(f"     * On traite le rowpair suivant --> {rowpair_label}")

        for case_obj in case_obj_list:
            if not case_obj.calculate_perfo:
                rowpair_obj, _ = RowPair.objects.get_or_create(
                    name=rowpair_label,
                    cas=case_obj,
                )

                rowpair_obj.type = iso_vitesse.get_type_of_row_with_config(rowpair_obj.name)
                rowpair_obj.cas = case_obj
                rowpair_obj.save()

                set_inlet_outlet_row_obj(case_obj, rowpair_obj)

                if iso_vitesse.file_type == "bsam":
                    tf = ThroughFlow.from_bsam(case_obj.bsam_path)
                    perfos_data = compute_perfo_bsam(tf, rowpair_obj)

                elif iso_vitesse.file_type == "excel":
                    print("Excel")
                    perfos_data = compute_perfo_excel(case_obj, rowpair_obj)

                elif iso_vitesse.file_type == "hdf":
                    perfos_data = compute_perfo_hdf(case_obj, rowpair_obj)

                else:
                    print(f" Type de donnée inconnu --> {iso_vitesse.file_type} !!!")
                    return data_cache

                perfos_data = apply_recalage_kd(case_obj, perfos_data)

                perfos_data["element_color"] = case_obj.iso_vitesse.color
                perfos_data["group"] = case_obj.iso_vitesse.name
                perfos_data["id"] = case_obj.id
                perfos_data["KD"] = case_obj.iso_vitesse.recalage_kd
                perfos_data["name"] = case_obj.name
                perfos_data["marker"] = case_obj.iso_vitesse.marker
                perfos_data["data_type"] = case_obj.iso_vitesse.file_type
                df = pd.DataFrame([perfos_data])

                # print(f"({iso_vitesse.name} calculate_perfo) rowpair_obj.is_only_stator() = {rowpair_obj.is_only_stator()}")
                df['is_only_stator'] = rowpair_obj.is_only_stator()

                data_cache.setdefault(rowpair_obj.name, {})[case_obj.id] = df

            else:

                print(case_obj, rowpair_label)
                data, rowpair_obj = load_bdd_data(case_obj, rowpair_label)

                data = apply_recalage_kd(case_obj, data)
                df = pd.DataFrame([data])
                df = add_cas_info(df, case_obj)
                print(f"({iso_vitesse.name} BDD) rowpair_obj.is_only_stator() = {rowpair_obj.is_only_stator()}")
                df['is_only_stator'] = rowpair_obj.is_only_stator()
                data_cache[rowpair_obj.name][case_obj.id] = df

    for case_obj in case_obj_list:
        if not case_obj.calculate_perfo:
            case_obj.calculate_perfo = True
            case_obj.save()

    return data_cache
