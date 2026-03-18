#!/usr/bin/env python
import os
import re
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def generate_pdf(file_path, figs=None):
    pdf = PdfPages(file_path)
    if figs is None:
        figs = [plt.figure(n) for n in plt.get_fignums()]
    for fig in figs:
        fig.savefig(pdf, format='pdf')

    pdf.close()


def read_input_file(file_path):
    input_dico = {}
    if os.path.exists(file_path):
        exec(open(file_path).read(), None, input_dico)
    return input_dico


def get_flux_aliases(alias, data_type='bsam'):
    if data_type.lower() == 'bsam':
        flux_aliases = {'total': 1, 'secondaire': 3, 'primaire': 2}
    else:
        flux_aliases = {'total': 1, 'secondaire': 2, 'primaire': 3}

    for key, val in flux_aliases.items():
        if alias == key:
            return val
        if alias == val:
            return key


def get_massflow_filepath(dir_path):

    basename_inflow = '_INFLOWMassflow.v3d'
    basename_outflow = '_OUTFLOWMassflow.v3d'
    basename_outflow_bypass = '_OUTFLOW_BYPASSMassflow.v3d'

    inflow_filepath = sorted(list(dir_path.glob(f"*{basename_inflow}")))
    outflow_filepath = sorted(list(dir_path.glob(f"*{basename_outflow}")))
    outflow_bypass_filepath = sorted(list(dir_path.glob(f"*{basename_outflow_bypass}")))

    return inflow_filepath, outflow_filepath, outflow_bypass_filepath


def read_file(file_path):
    fichier = open(file_path, "r")
    lines = fichier.readlines()  # Lit tout le fichier d'un coup
    fichier.close()

    for i in range(0, len(lines)):
        lines[i] = lines[i].replace('-', ' ')
        lines[i] = lines[i].replace('E ', 'E-')  # En cas de nombres < 1
        lines[i] = lines[i].replace('  ', ' ')

    return lines


def extract_data(source):
    """Récupère les données (itérations et débits) d'une liste de lignes, retourne une liste formatée."""

    for idx, line in enumerate(source):
        if 'va iteration' in line:
            idx_ite_begin = idx + 2
        if 'va convflux_ro' in line:
            idx_ite_end = idx - 1
            idx_massflow_begin = idx + 2
        idx_massflow_end = idx

    for idx in [idx_ite_end, idx_massflow_end]:
        if source[idx].strip() == '':
            del source[idx]
            if idx == idx_ite_end:
                idx_ite_end -= 1
                idx_massflow_begin -= 1
                idx_massflow_end -= 1
            else:
                idx_massflow_end -= 1

    def extract_values(start, end):
        """Extrait et nettoie les valeurs d'une plage de lignes"""
        values = []
        for line in source[start:end+1]:
            parts = [x for x in line.split(' ') if x]
            values.extend(float(part.split()[0]) for part in parts)
        return values

    iterations = extract_values(idx_ite_begin, idx_ite_end)
    debits = extract_values(idx_massflow_begin, idx_massflow_end)

    return iterations, debits


def ecart_relatif(df, col_name):
    min_val = df[col_name].min()
    max_val = df[col_name].max()
    if (max_val + min_val) != 0:
        return (max_val - min_val) / (max_val + min_val) * 2 * 100
    else:
        return float('nan')

def extract_parts(s):
    pattern_row = r'var_([^_]+_[^_]+)__'
    m_row = re.search(pattern_row, s)
    row = m_row.group(1) if m_row else None

    pattern_flow = r'OUTFLOW_BYPASS|OUTFLOW|INFLOW'
    m_flow = re.search(pattern_flow, s)
    flow = m_flow.group(0) if m_flow else None

    return row, flow

def convert_row_string(s):
    match = re.match(r'ROW_(\d+)', s)
    if match:
        return f"ROW({match.group(1)})"
    else:
        return s  # ou None si tu veux ignorer les non-match


def get_casename_from_path(case_path):
    match = re.search(r'(case[^\\/]+)', str(case_path))
    return match.group(1) if match else None


def get_root_case_path(case_path):
    root_path = None
    for i, part in enumerate(case_path.parts):
        if part.startswith('case'):
            root_path = Path(*case_path.parts[:i + 1])
            break
    return root_path


def get_blade_info(config_dico, row_name):
    row_info = config_dico['gridFields'].get(row_name, {})
    blade_name = list(row_info['Blades'].keys())[0]
    return row_info['Blades'][blade_name]


def get_row_flux(config_dico, row_name):
    row_info = config_dico['gridFields'].get(row_name, {})
    return get_flux_aliases(row_info['Flux'], data_type='cfd')


def get_massflow_conv_data(case_path):

    antares_card_path = case_path / 'calculation' / 'carte_antares.py'

    config_dico = read_input_file(antares_card_path)

    res_dir_path = case_path / 'res'

    filepath_inlet, filepath_outlet, filepath_outlet_bypass = get_massflow_filepath(res_dir_path)

    df_global = pd.DataFrame({'iteration': []})

    for index, filepath in enumerate(filepath_inlet + filepath_outlet + filepath_outlet_bypass):
        if not filepath.exists():
            print(f"Fichier {filepath} introuvable pour le cas.")
        else:
            data = read_file(filepath)
            interation, debit = extract_data(data)
            row, flow = extract_parts(filepath.stem)

            row_convert = convert_row_string(row)

            blade_info = get_blade_info(config_dico, row_convert)
            blade_flux = get_row_flux(config_dico, row_convert)
            blade_name = blade_info['Aube']

            df_current = pd.DataFrame({'iteration': interation, f'{blade_flux.upper()}_{row_convert}_{blade_name}_{flow}': debit})

            if not df_current.empty:
                df_global = pd.merge(df_global, df_current, on='iteration', how='outer')

    return df_global


def check_massflow_conv_status(df_global, nbre_ite_analyse, tol_amplitude=0.2):

    case_status = True

    for col in df_global.columns:
        if col != 'iteration':

            yvar_name = col

            ite_zoom_begin = df_global.iteration.max() - nbre_ite_analyse
            df_global_filtered = df_global[df_global.iteration >= ite_zoom_begin]

            yval_filtered_mean = df_global_filtered[yvar_name].mean()
            y_sup = yval_filtered_mean + yval_filtered_mean * 0.5 * tol_amplitude / 100
            y_inf = yval_filtered_mean - yval_filtered_mean * 0.5 * tol_amplitude / 100

            # Récupère les valeurs en dehors des bornes
            df_global_filtered_out_boundary = df_global_filtered[(df_global_filtered[yvar_name] < y_inf) | (df_global_filtered[yvar_name] > y_sup)]
            if not df_global_filtered_out_boundary.empty:
                case_status = False
                break

    return case_status


def plot_massflow_conv(df_global, case_name, nbre_ite_analyse, tol_amplitude=0.2, show_plot=False):

    xvar_name = 'iteration'

    figs = []
    for col in df_global.columns:
        if col != xvar_name:

            yvar_name = col

            ite_zoom_begin = df_global.iteration.max() - nbre_ite_analyse
            df_global_filtered = df_global[df_global.iteration >= ite_zoom_begin]

            yval_filtered_mean = df_global_filtered[yvar_name].mean()
            y_sup = yval_filtered_mean + yval_filtered_mean * 0.5 * tol_amplitude / 100
            y_inf = yval_filtered_mean - yval_filtered_mean * 0.5 * tol_amplitude / 100

            # Récupère les valeurs en dehors des bornes
            df_global_filtered_out_boundary = df_global_filtered[
                (df_global_filtered[yvar_name] < y_inf) | (df_global_filtered[yvar_name] > y_sup)]

            x0 = df_global_filtered[xvar_name].min()
            x1 = df_global_filtered[xvar_name].max()

            yval_max = df_global[yvar_name].max()
            yval_min = df_global[yvar_name].min()
            yval_mean = df_global[yvar_name].mean()

            fig, axes = plt.subplots(2, 1, figsize=(10, 5))

            fig.suptitle(f"{col} (Tolerance=+/-{tol_amplitude / 2}%)", fontsize=16)
            fig.supxlabel(f"CaseName = {case_name}", fontsize=8)

            axes[0].grid(True)
            axes[0].yaxis.set_major_locator(MaxNLocator(6))
            axes[0].plot(df_global[xvar_name], df_global[yvar_name], ls="-", color='black', label=col)
            axes[0].plot([ite_zoom_begin, ite_zoom_begin], [yval_min, yval_max], ls="--", color='grey')
            axes[0].plot([x1, x1], [yval_min, yval_max], ls="--", color='grey')

            axes[0].text(0.965 * np.mean([ite_zoom_begin, x1]), yval_mean, f'  ZOOM\n{nbre_ite_analyse:.0f} Ite',
                         color="grey", fontsize=10)
            axes[0].set_xlabel(xvar_name, fontsize=9, labelpad=0)
            axes[0].set_ylabel('Debit [Kg/s]', fontsize=9)
            axes[0].tick_params(axis='both', labelsize=8)
            # axes[0].legend(loc='best')

            axes[1].grid(True)
            axes[1].yaxis.set_major_locator(MaxNLocator(6))
            axes[1].plot(df_global_filtered[xvar_name], df_global_filtered[yvar_name],
                         color='black', marker='o', markerfacecolor='green', markeredgecolor='green', label=col)

            if not df_global_filtered_out_boundary.empty:
                axes[1].plot(df_global_filtered_out_boundary[xvar_name], df_global_filtered_out_boundary[yvar_name],
                             color='red', marker="o", linestyle="")

            axes[1].set_xlabel(xvar_name, fontsize=9, labelpad=0)
            axes[1].set_ylabel('Debit [Kg/s]', fontsize=9)
            axes[1].tick_params(axis='both', labelsize=8)

            axes[1].plot([x0, x1], [y_sup, y_sup], "r--")
            axes[1].text(x0, y_sup, f'Lim sup={y_sup:.3f}Kg/s', color="red", fontsize=7,
                         bbox=dict(facecolor='white', alpha=1, edgecolor='red'))

            axes[1].plot([x0, x1], [y_inf, y_inf], "r--")
            axes[1].text(x0, y_inf, f'Lim inf={y_inf:.3f}Kg/s', color="red", fontsize=7,
                         bbox=dict(facecolor='white', alpha=1, edgecolor='red'))
            axes[1].text(x0, yval_filtered_mean, f'Débit moyen={yval_filtered_mean:.3f}Kg/s',
                         color="black", fontsize=7,
                         bbox=dict(facecolor='white', alpha=1, edgecolor='black'))

            yval_ecart_rel = ecart_relatif(df_global_filtered, yvar_name)
            color = "green" if yval_ecart_rel <= tol_amplitude else "red"

            axes[1].text(x1, y_sup, f'Ecart min/max={yval_ecart_rel:.3f}%',
                         color=color, fontsize=7, bbox=dict(facecolor='white', alpha=1, edgecolor=color))

            plt.tight_layout()

            if show_plot:
                plt.show()

            figs.append(fig)

            plt.close(fig)
            del fig

    return figs
    

def launch_trace_conv(etat, case):

    case_name = case.name
    case_path = Path(case.repertory)

    conv_tol_amplitude = 0.2

    df_conv = get_massflow_conv_data(case_path)

    nbre_ite_analyse = 0.1 * (df_conv.iteration.max() - df_conv.iteration.min())
    nbre_ite_analyse = np.clip(nbre_ite_analyse, 300, 2000)

    figs = plot_massflow_conv(df_conv, case_name, nbre_ite_analyse, conv_tol_amplitude, show_plot=False)
    
    output_dir = Path(etat.work_directory) / "ConvAuto"
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(output_dir, 0o777)
    
    pdf_filepath = output_dir / f'ConvAuto_{case_name}.pdf'
    
    generate_pdf(pdf_filepath, figs)
    
    return Path(pdf_filepath).exists()

