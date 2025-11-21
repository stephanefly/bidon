import scipy
import numpy as np
from bsamreader import ThroughFlow, RadialEntropicAverage
from scipy import optimize
from numpy.polynomial import Polynomial
from pathlib import Path

bsam_filepath = [r"\\Nas23\yrkc\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\04_Chaining\MidFan_Booster\ShenRON\00_Inputs\GTD_M8.47_H_v6p1_70Nn_TOPB_gradOpFan.bsam",
r"\\Nas23\yrkc\02_Methodes_et_Outils\03_Outils\03_Moyenne_Fidelite_CFD\04_Chaining\MidFan_Booster\ShenRON\00_Inputs\GTD_M8.47_H_v6p1_70Nn_TOPB_gradOpF.bsam"]


yplus_target = 1


def compute_wallcellsize(bsam_filepath, yplus_target=1):

    def func(x, rey, beta=2.51):
        # Colebrook–White equation
        return 1. / np.sqrt(x) + 2. * np.log10(beta / rey / np.sqrt(x))

    def compute_utau_u(x):
        return np.sqrt(x / 8.)

    def compute_cf(utau_u):
        return 2. * np.power(utau_u, 2.)

    def mu(t, tref=273.15, ta=110.4):
        return 1.711 * 1.e-5 * np.power(t / tref, 1.5) * (tref + ta) / (t + ta)

    def rho(t, p, mair=0.0289644, r=8.3144621):
        return p * mair / r / t

    tf = ThroughFlow.from_bsam(bsam_filepath)

    result_text = []

    for zone in tf.zones:

        for row in zone.rows:

            v = row.qdebz

            ldc_middle = min(range(len(v)), key=lambda i: abs(v[i] - 0.5))

            grid_name_bsam = row.name

            coeff_corde = row.c.coef

            aero_data = {}
            for key in ["BA", "BF"]:

                aero_data[key] = {}

                plane = row.inlet if key == "BA" else row.outlet

                aero_data[key]['Ps'] = plane.points.p[ldc_middle]
                aero_data[key]['Ts'] = plane.points.T[ldc_middle]
                aero_data[key]['Vx'] = plane.points.Vx[ldc_middle]
                aero_data[key]['Vr'] = plane.points.Vr[ldc_middle]
                aero_data[key]['Vt'] = plane.points.Vt[ldc_middle]

                # average = RadialEntropicAverage(plane)
                # aero_data[key]['Ps'] = average.p
                # aero_data[key]['Ts'] = average.T
                # aero_data[key]['Vx'] = average.Vx
                # aero_data[key]['Vr'] = average.Vr
                # aero_data[key]['Vt'] = average.Vt

                aero_data[key]['V'] = np.sqrt(np.power(aero_data[key]['Vx'], 2.) + np.power(aero_data[key]['Vr'], 2.) + np.power(aero_data[key]['Vt'], 2.))
                aero_data[key]['X'] = plane.points.x
                aero_data[key]['R'] = plane.points.r

            rbai = aero_data["BA"]['R'][0]
            rbae = aero_data["BA"]['R'][-1]
            rbfi = aero_data["BF"]['R'][0]
            rbfe = aero_data["BF"]['R'][-1]

            rme = (rbae + rbfe) * 0.5
            rmi = (rbai + rbfi) * 0.5
            r1 = (rme + rmi) * 0.5

            chord_mean = (Polynomial(coeff_corde)(rmi) + Polynomial(coeff_corde)(rme) + Polynomial(coeff_corde)(r1) * 4.) / 6.

            velocity_ref = 0.5 * (aero_data['BA']['V'] + aero_data['BF']['V'])

            density = 0.5 * (rho(aero_data['BA']['Ts'], aero_data['BA']['Ps']) + rho(aero_data['BF']['Ts'], aero_data['BF']['Ps']))
            viscosity = 0.5 * (mu(aero_data['BA']['Ts']) + mu(aero_data['BF']['Ts']))
            reynolds = density * velocity_ref * chord_mean / viscosity

            # darcy friction factor
            friction_factor = scipy.optimize.newton(func, x0=0.01, fprime=None, args=(reynolds, 3.6), tol=1.e-8, maxiter=100000, fprime2=None)
            utau_u = compute_utau_u(friction_factor)  # skin friction velocity
            cf = compute_cf(utau_u)

            utau = utau_u * velocity_ref
            wallcellsize = viscosity / density * yplus_target / utau

            line = (
                f"{grid_name_bsam};"
                f"{yplus_target:.2f};"
                f"{wallcellsize * 1e6:.2f};"
                f"{cf:.3e};"
                f"{utau_u * 100:.2f};"
                f"{velocity_ref:.2f};"
                f"{utau:.2f};"
                f"{1000 * chord_mean:.2f};"
                f"{reynolds:.2e}"
            )


            result_text.append(line)


    return result_text


def mise_en_forme(result_text):
    rows = []

    for line in result_text:
        cols = line.split(";")  # <-- split ici
        rows.append(cols)

    return rows