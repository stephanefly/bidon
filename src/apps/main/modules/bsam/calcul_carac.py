from typing import Union
from bsamreader.average import RadialEntropicAverage
from bsamreader.core import intersect, degree
from scipy.interpolate import interp1d, make_interp_spline, lagrange
import numpy as np
from numpy.polynomial import Polynomial
import math


def P3(polynome, valeurs):
    return polynome[0] + polynome[1] * valeurs + polynome[2] * valeurs ** 2 + polynome[3] * valeurs ** 3

def __find_intersections(A, B):
    # min, max and all for arrays
    amin = lambda x1, x2: np.where(x1 < x2, x1, x2)
    amax = lambda x1, x2: np.where(x1 > x2, x1, x2)
    aall = lambda abools: np.dstack(abools).all(axis=2)
    slope = lambda line: (lambda d: d[:, 1] / d[:, 0])(np.diff(line, axis=0))

    x11, x21 = np.meshgrid(A[:-1, 0], B[:-1, 0])
    x12, x22 = np.meshgrid(A[1:, 0], B[1:, 0])
    y11, y21 = np.meshgrid(A[:-1, 1], B[:-1, 1])
    y12, y22 = np.meshgrid(A[1:, 1], B[1:, 1])

    m1, m2 = np.meshgrid(slope(A), slope(B))
    if (m1 == 0).any() or (m2 == 0).any():
        return None

    m1inv, m2inv = 1 / m1, 1 / m2

    yi = (m1 * (x21 - x11 - m2inv * y21) + y11) / (1 - m1 * m2inv)
    xi = (yi - y21) * m2inv + x21

    xconds = (amin(x11, x12) < xi, xi <= amax(x11, x12),
              amin(x21, x22) < xi, xi <= amax(x21, x22))
    yconds = (amin(y11, y12) < yi, yi <= amax(y11, y12),
              amin(y21, y22) < yi, yi <= amax(y21, y22))

    if len(xi[aall(xconds)]) == 0 or len(yi[aall(yconds)]) == 0:
        return None
    else:
        return xi[aall(xconds)], yi[aall(yconds)]

def __perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def __seg_intersect(a1, a2, b1, b2):
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = __perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)

    x3 = ((num / denom.astype(float)) * db + b1)[0]
    y3 = ((num / denom.astype(float)) * db + b1)[1]

    dtest = np.array([x3, y3]) - a1
    dtest2 = np.array([x3, y3]) - b1

    if 0 < np.dot(dtest, da) <= np.dot(da, da) and 0 < np.dot(dtest2, db) <= np.dot(db, db):
        return x3, y3
    else:
        return False

def intersection2D(X1, R1, X2, R2, reverse=False):
    """
    This function calculate intersection between two lines (X, R)

    # Arguments
        X1: (numpy array)
        R1: (numpy array)
        X2: (numpy array)
        R2: (numpy array)
        reverse: (bool)
            to inverse the way to explore the line (default = False)

    # Return
        intersection: (tuple)
            tuple containing the intersection coordonates (X, R)
    """
    A = []
    for j in range(len(X1)):
        A.append([X1[j], R1[j]])
    A = np.array(A)
    B = []
    for j in range(len(X2)):
        B.append([X2[j], R2[j]])
    B = np.array(B)
    res2 = __find_intersections(A, B)
    if res2 is None:
        res2 = __find_intersections(B, A)

    if res2 is None:
        ieter = list(range(len(X2) - 1))
        if reverse:
            ieter.reverse()
        for j in ieter:
            for k in range(len(X1) - 1):
                if __seg_intersect(np.array([X2[j], R2[j]]), np.array([X2[j + 1], R2[j + 1]]), np.array([X1[k], R1[k]]), np.array([X1[k + 1], R1[k + 1]])):
                    res = __seg_intersect(np.array([X2[j], R2[j]]), np.array([X2[j + 1], R2[j + 1]]), np.array([X1[k], R1[k]]), np.array([X1[k + 1], R1[k + 1]]))
                    return res
    else:
        try:
            return res2[0][0], res2[1][0]
        except:
            return None

import time

class GestionCarac:
    def __init__(self, tf, row, hauteurs):
        start_time = time.perf_counter()
        self.tf = tf
        self.row_obj = self.tf.get_row_zone(row)[0]
        self.hauteurs = hauteurs
        self.xr_le(self.row_obj)
        self.xr_te_caviar(self.row_obj)
        self.xr_te_carma(self.row_obj)
        self.xyzr_le_te_genepi()
        self.xr_mean()
        self.xr_emp()
        self.hh1 = self.hh1()
        self.hh2 = self.hh2()
        self.hhmean = self.hhmean()
        self.hhemp = self.hhemp()
        elapsed = time.perf_counter() - start_time
        print(f"{self.__class__.__name__}.__init__ exécutée en {elapsed:.6f} secondes.")

    def timed_init(self, tf, row, hauteurs):
        start = time.perf_counter()
        self.tf = tf
        print(f"self.tf = tf : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.row_obj = self.tf.get_row_zone(row)[0]
        print(f"self.row_obj = ... : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.hauteurs = hauteurs
        print(f"self.hauteurs = hauteurs : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xr_le(self.row_obj)
        print(f"self.xr_le : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xr_te_caviar(self.row_obj)
        print(f"self.xr_te_caviar : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xr_te_carma(self.row_obj)
        print(f"self.xr_te_carma : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xyzr_le_te_genepi()
        print(f"self.xyzr_le_te_genepi : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xr_mean()
        print(f"self.xr_mean : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.xr_emp()
        print(f"self.xr_emp : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.hh1 = self.hh1()
        print(f"self.hh1 = self.hh1() : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.hh2 = self.hh2()
        print(f"self.hh2 = self.hh2() : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.hhmean = self.hhmean()
        print(f"self.hhmean = self.hhmean() : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()

        self.hhemp = self.hhemp()
        print(f"self.hhemp = self.hhemp() : {time.perf_counter() - start:.6f} s"); start = time.perf_counter()



    # dict_keys(
    #     ['x', 'r', 'p', 'T', 'Vm', 'Vt', 'drdx', 'tau', 'psi', 'dpein', 'qdeb',
    #      'qdebz', 'h', 'Tt', 'pt', 'rho', 'alpha', 'V', 'a', 'M', 'Mm', 'S',
    #      'U', 'Wt', 'W', 'Mw', 'beta', 'Ttw', 'ptw'])
    def xr_le(self, row):
        self.xle, self.rle = row.le(row.qdebz).T
        return self.xle, self.rle

    def xr_te_caviar(self, row):
        te = row.te_caviar  # ← récupère le spline CACHÉ
        self.xte_caviar, self.rte_caviar = te(row.qdebz).T
        return self.xte_caviar, self.rte_caviar

    def xr_te_carma(self, row):
        self.xte_carma, self.rte_carma = row.te_carma(row.qdebz).T
        return self.xte_carma, self.rte_carma

    def xr_mean(self):
        self.xmean = (self.xle + self.xte_caviar) / 2
        self.rmean = (self.rle + self.rte_caviar) / 2

    def xr_emp(self):
        self.xemp = self.get_empilage_data()["x"]
        self.remp = self.get_empilage_data()["r"]

    def xyzr_le_te_genepi(self):
        ffzemp = self.get_empilage_data()["x"]

        # Leading edge
        Sup = 0, min(min(self.get_inlet_data()["r"]), min(self.get_outlet_data()["r"]))
        Inf = 0, max(max(self.get_inlet_data()["r"]), max(self.get_outlet_data()["r"]))

        delta = 0.01 * (Inf[1] - Sup[1])
        RBA = np.arange(101) / 100.0 * (Inf[1] - Sup[1] + 2 * delta) + Sup[1] - delta
        XBA = P3(self.row_obj.xle.coef, RBA)
        # XBA = Polynomial(self.row_obj.xle.coef)
        # XBA_ = self.row_obj.xle.coef[0] + self.row_obj.xle.coef[1] * RBA + self.row_obj.xle.coef[2] * RBA * RBA + \
        #       self.row_obj.xle.coef[3] * RBA * RBA * RBA

        xba, rba = [], []
        for i in range(self.row_obj.n_streamlines):
            streamline = self.row_obj.get_streamline(i)
            x_strl, r_strl = streamline.x, streamline.r
            # xr_strl = make_interp_spline(x_strl, r_strl, k=degree(len(x_strl)))
            res = intersection2D(XBA, RBA, x_strl, r_strl)
            if res is not None:
                xba.append(res[0])
                rba.append(res[1])
            # rle = intersect(XBA, xr_strl, estimate=[x_strl[-1], r_strl[-1]])[1]
            # xba.append(self.row_obj.xle(rle))
            # rba.append(rle)

        xba = np.array(xba)
        rba = np.array(rba)

        # calcul du polynome associé à la cordeaxiale
        dd = (rba[-1] - rba[0]) / 3.
        cordax_x = []
        cordax_r = []
        init = rba[0]
        dgamx = Polynomial(self.row_obj._dct["dgamx"])
        for indexJ in range(4):
            r = init + indexJ * dd
            # value = P3(bsam[0][row]["CRS"], R) * numpy.cos((P3(bsam[0][row]["CALAGE"], R) + bsam[0][row]["dgamx"]) * numpy.pi / 180.0)
            value = P3(self.row_obj.c.coef, r) * np.cos((P3(self.row_obj.stagger.coef, r) + np.radians(dgamx(r))) * np.pi/180.0)
            cordax_r.append(r)
            cordax_x.append(value)

        # polyCordeAx = cubain(cordax_r, cordax_x)
        polyCordeAx = lagrange(cordax_r, cordax_x).coef[::-1]

        # calcul du polyBF
        polyBF = [0, 0, 0, 0]
        for index in range(4):
            # polyBF[index] = bsam[0][row]["BA"][index] + polyCordeAx[index]
            polyBF[index] = self.row_obj.xle.coef[index] + polyCordeAx[index]

        # Trailing edge

        XBF2 = P3(polyBF, RBA)
        # XBF2 = Polynomial(polyBF)

        xbf, rbf = [], [],
        for i in range(self.row_obj.n_streamlines):
            streamline = self.row_obj.get_streamline(i)
            x_strl, r_strl = streamline.x, streamline.r
            xr_strl = make_interp_spline(x_strl, r_strl, k=degree(len(x_strl)))
            # rte = intersect(XBF2, xr_strl, estimate=[x_strl[-1], r_strl[-1]])[1]
            # xbf.append(XBF2(rte))
            # rbf.append(rte)
            res = intersection2D(XBF2, RBA, x_strl, r_strl, reverse=True)
            if res is not None:
                xbf.append(res[0])
                rbf.append(res[1])

        xbf = np.array(xbf)
        rbf = np.array(rbf)

        ffyuba = self.row_obj.delta_theta(rba)
        ffcalba = self.row_obj.stagger(rba)
        ftba = ffyuba + (xba - ffzemp) * np.tan(np.radians(ffcalba))
        hba = (rba ** 2 - ftba ** 2)

        for index, val in enumerate(hba):
            if val > 0:
                hba[index] = val ** 0.5
            else:
                hba[index] = self.row_obj.inlet.r[index]
        ftba_angle = np.arctan2(ftba, hba)

        # BF
        # xbf = self.xte_carma
        # rbf = self.rte_carma

        ffyubf = self.row_obj.delta_theta(rbf)
        ffcalbf = self.row_obj.stagger(rbf)
        ftbf = ffyubf + (xbf - ffzemp) * np.tan(np.radians(ffcalbf))
        hbf = (rbf ** 2 - ftbf ** 2)

        for index, val in enumerate(hbf):
            if val > 0:
                hbf[index] = val ** 0.5
            else:
                hbf[index] = self.row_obj.outlet.r[index]
        ftbf_angle = np.arctan2(ftbf, hbf)

        yinv = 1
        self.xle_genepi = xba
        self.yle_genepi = yinv * (rba * np.sin(ftba_angle))
        self.zle_genepi = rba * np.cos(ftba_angle)
        self.rle_genepi = rba

        self.xte_genepi = xbf
        self.yte_genepi = yinv * (rbf * np.sin(ftbf_angle))
        self.zte_genepi = rbf * np.cos(ftbf_angle)
        self.rte_genepi = rbf

    def hauteur_adim(self, x, r):
        dx = np.diff(x, prepend=x[0])
        dr = np.diff(r, prepend=r[0])
        dh = np.sqrt(np.power(dx, 2) + np.power(dr, 2))
        return dh.cumsum() / dh.sum()

    def hauteur_adim_genepi(self, r):
        return (r - r.min()) / (r.max() - r.min())

    def hhmean(self):
        return self.hauteur_adim(self.xmean, self.rmean)

    def hhemp(self):
        return self.hauteur_adim(self.xemp, self.remp)

    def hh1(self):
        return self.row_obj.inlet.h

    def hh2(self):
        return self.row_obj.outlet.h

    def get_data(self, section):
        return {
            feature: getattr(section, feature, None)
            for feature in getattr(section, "features_1d", [])
        }

    def get_inlet_data(self):
        return self.get_data(self.row_obj.inlet)

    def get_empilage_data(self):
        return self.get_data(self.row_obj.stations[self.row_obj._istack])

    def get_outlet_data(self):
        return self.get_data(self.row_obj.outlet)

    def calculer_values(self, var_name):
        methode = getattr(
            self, f"calculer_{var_name.lower().replace(' ', '_')}",
            None)
        if methode:
            return methode()

    def _calculer_avec_hauteur_new(self, x, y, height=None):
        interp_func = make_interp_spline(x, y, k=2)
        if height is None:
            height = self.hauteurs
        return [interp_func(h) for h in height]


class CaracCalculator(GestionCarac):
    def __init__(self, tf, row, hauteurs):
        super().__init__(tf, row, hauteurs)

    def surface(self, rmin, rmax):
        return np.pi * (rmax**2 - rmin**2)

    def surface_cone(self, xmin, xmax, rmin, rmax):
        l = math.hypot(xmax - xmin, rmax - rmin)
        return math.pi * (rmin + rmax) * l

    def calage(self):
        stagger = self.row_obj.stagger
        dgamx = Polynomial(self.row_obj._dct["dgamx"])
        return stagger(self.rmean) + dgamx(self.rmean)

    def calage_genepi(self):
        inv = -1 if self.yle_genepi[0] > self.yte_genepi[0] else 1
        return inv * np.degrees(np.arccos(self.corde_merid_genepi() / self.corde_genepi()))

    def s(self):
        return 2 * np.pi * self.rmean / self.row_obj.z

    def ssc(self):
        return self.s() / self.corde_aero()

    def ssc_genepi(self):
        return self.s() / self.corde_genepi()

    def emaxsc(self):
        tmax_c = self.row_obj.tmax_c
        return tmax_c(self.rmean)

    def emaxsc_genepi(self):
        tmax_c = P3(self.row_obj.tmax_c.coef, self.remp)
        corde = P3(self.row_obj.c.coef, self.remp)

        return tmax_c * corde / self.corde_genepi()

    def emax(self):
        return self.emaxsc() * self.corde_aero()

    def emax_genepi(self):
        tmax_c = P3(self.row_obj.tmax_c.coef, self.remp)
        corde = P3(self.row_obj.c.coef, self.remp)

        return tmax_c * corde

    def xemaxsc(self):
        xtmax_c = self.row_obj.xtmax_c
        return xtmax_c(self.rmean)

    def xemaxsc_genepi(self):
        return P3(self.row_obj.xtmax_c.coef, self.remp)

    def xemax(self):
        return self.xemaxsc() * self.corde_aero()

    def xemax_genepi(self):
        return self.xemaxsc_genepi() * self.corde_genepi()

    def corde_merid(self):
        return np.sqrt((self.rte_caviar - self.rle) ** 2 + (self.xte_caviar - self.xle) ** 2)

    def corde_merid_genepi(self):
        return np.sqrt((self.xte_genepi - self.xle_genepi) ** 2 + (self.zte_genepi - self.zle_genepi) ** 2)

    def corde_aero(self):
        cm = self.corde_merid()
        stagger = self.calage()
        return cm * np.sqrt(1 + np.tan(np.radians(stagger))**2)

    def corde_genepi(self):
        return ((self.xte_genepi - self.xle_genepi) ** 2 + (self.yte_genepi - self.yle_genepi) ** 2 + (self.zte_genepi - self.zle_genepi) ** 2)**0.5

    def corde_axial(self):
        cx = self.row_obj.cx_carma
        return cx(self.rmean)

    def w2_w1(self):
        w1 = self.get_inlet_data()["W"]
        w2 = self.get_outlet_data()["W"]
        return [b / a for a, b in zip(w1, w2)]

    def pi(self):
        pta1 = self.get_inlet_data()["pt"]
        pta2 = self.get_outlet_data()["pt"]
        return [b / a for a, b in zip(pta1, pta2)]

    def deviation(self):
        beta1 = self.get_inlet_data()["beta"]
        beta2 = self.get_outlet_data()["beta"]
        return [b2 - b1 for b1, b2 in zip(beta1, beta2)]

    def hsc_genepi(self):
        rbae = self.rle_genepi[-1]
        rbai = self.rle_genepi[0]

        rbfe = self.rte_genepi[-1]
        rbfi = self.rte_genepi[0]

        zbae = self.xle_genepi[-1]
        zbai = self.xle_genepi[0]

        zbfe = self.xte_genepi[-1]
        zbfi = self.xte_genepi[0]

        rme = (rbae + rbfe) * 0.5
        rmi = (rbai + rbfi) * 0.5
        zme = (zbae + zbfe) * 0.5
        zmi = (zbai + zbfi) * 0.5
        h_mean = ((rme - rmi) ** 2 + (zme - zmi) ** 2) ** 0.5

        corde = self.corde_genepi()
        rte_adim = self.hauteur_adim_genepi(self.rte_genepi)
        interp = interp1d(rte_adim, corde, kind='cubic', bounds_error=False)
        crdm = (interp(np.array([0.0]))[0] + interp(np.array([1.0]))[0] + 4 * interp(np.array([0.5]))[0]) / 6.0

        return h_mean / crdm

    def hsc(self):
        r_hub = self.rmean[0]
        r_shroud = self.rmean[-1]

        h_mean = (r_shroud - r_hub)

        c_loc = self._calculer_avec_hauteur_new(self.hh2, self.corde_aero(), height=[0.0, 0.5, 1.0])
        c_mean = (c_loc[0] + 4 * c_loc[1] + c_loc[2]) / 6

        return h_mean / c_mean

    def psia(self):
        w1 = self.get_inlet_data()["W"]
        w2 = self.get_outlet_data()["W"]
        beta1 = self.get_inlet_data()["beta"]
        beta2 = self.get_outlet_data()["beta"]
        ssc = self.ssc()
        dwu = np.abs(w1 * np.sin(beta1) - w2 * np.sin(beta2))
        wm = 0.5 * ((w1**2 + w2**2 + 2 * w1 * w2 * np.cos(beta2 - beta1))**0.5)
        return 2 * ssc * wm * dwu / w2**2

    def psia_genepi(self):
        w1 = self.get_inlet_data()["W"]
        w2 = self.get_outlet_data()["W"]
        beta1 = self.get_inlet_data()["beta"]
        beta2 = self.get_outlet_data()["beta"]
        ssc = self.ssc_genepi()
        dwu = np.abs(w1 * np.sin(beta1) - w2 * np.sin(beta2))
        wm = 0.5 * ((w1**2 + w2**2 + 2 * w1 * w2 * np.cos(beta2 - beta1))**0.5)
        return 2 * ssc * wm * dwu / w2**2

    def dli(self):
        w1 = self.get_inlet_data()["W"]
        w2 = self.get_outlet_data()["W"]
        ssc = self.ssc()
        wt1 = self.get_inlet_data()["Wt"]
        wt2 = self.get_outlet_data()["Wt"]

        return 1 - w2 / w1 + 0.5 * ssc * (np.abs(wt1 - wt2) / w1)

    def dli_genepi(self):

        r1 = self.rle_genepi
        r2 = self.rte_genepi
        rmoy = 0.5 * (r1 + r2)
        w1 = self.get_inlet_data()["W"]
        w2 = self.get_outlet_data()["W"]
        ssc = self.ssc_genepi()
        vt1 = self.get_inlet_data()["Vt"]
        vt2 = self.get_outlet_data()["Vt"]

        drwu = np.abs(r1 * vt1 - r2 * vt2)

        return 1 - w2 / w1 + 0.5 * ssc * (drwu / (rmoy * w1))


    def u(self, r):
        return self.row_obj.omega * r

    def dhsu2(self):
        tt1 = self.get_inlet_data()["Tt"]
        tt2 = self.get_outlet_data()["Tt"]
        cp_coeffs = self.cp_polynome(0.0, 0.0)

        h1 = self.enthalpy_fct_t(cp_coeffs, tt1, 0.0)
        h2 = self.enthalpy_fct_t(cp_coeffs, tt2, 0.0)
        r = self.get_outlet_data()["r"]
        u = self.u(r)

        return (h2 - h1) / u**2

    def vzsu(self):
        return self.row_obj.inlet.points.Vx / self.u(self.rle)

    def sigma(self):
        wt1 = self.get_inlet_data()["Wt"]
        wt2 = self.get_outlet_data()["Wt"]
        return 0.5 * (wt1 + wt2) / self.u(self.rte_genepi)

    def dstd(self,q, tt, pt):

        return q * np.sqrt(tt / 288.15) / (pt / 101325.)

    def dss_genepi(self):
        average = RadialEntropicAverage(self.row_obj.inlet)
        debit = self.tf.debn
        dstd1_average = self.dstd(debit, average.Tt, average.pt)
        alpha1_average = np.arctan2(average.Vt , average.Vm)

        rmin = self.get_inlet_data()["r"][0]
        rmax = self.get_inlet_data()["r"][-1]

        surf1 = self.surface(rmin, rmax)
        # kd1 = self.row_obj.inlet.kd
        kd1 = 1

        return dstd1_average / (surf1 * np.cos(alpha1_average) * kd1)

    def dss(self):
        average = RadialEntropicAverage(self.row_obj.inlet)
        debit = self.tf.debn * self.row_obj.inlet.qdjz
        dstd1_average = self.dstd(debit, average.Tt, average.pt)
        alpha1_average = np.arctan2(average.Vt , average.Vm)

        rmin = self.get_inlet_data()["r"][0]
        rmax = self.get_inlet_data()["r"][-1]

        surf1 = self.surface(rmin, rmax)

        kd1 = self.row_obj.inlet.kd

        return dstd1_average / (surf1 * np.cos(alpha1_average) * kd1)

    def RadialMassFlowAverage(self, var):
        qtot = self.tf.debn
        qdebz_delta =  np.diff(self.row_obj.qdebz)
        var_sum = [0.5 * (var[i] + var[i+1]) for i in range(len(var)-1)]
        var_average = (var_sum * qdebz_delta * qtot).sum() / qtot
        return var_average

    def cp_polynome(self, far, war):
        cp_ker = np.array(
            [1.2850007e+03, 2.3021158e+00, -5.2739400e-04, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00,
             0.0000000e+00])
        cp_air = np.array(
            [1.0684300e+03, -5.2174200e-01, 1.2378500e-03, -6.2798400e-07, -3.3094000e-10, 4.7097200e-13,
             -1.7961300e-16, 2.3582200e-20])
        cp_water = np.array(
            [0.188457E+04, -0.484304, 0.173478E-02, -0.114179E-05, 0.334500E-09, -0.386134E-13, 0.0000000e+00,
             0.0000000e+00])

        return (cp_air + far * cp_ker + war * cp_water) / (1 + far + war)

    def enthalpy_fct_t(self, cp_coeff, ts, h0):
        return h0 + cp_coeff[0] * ts + cp_coeff[1] / 2.0 * ts ** 2 + cp_coeff[2] / 3.0 * ts ** 3 + \
            cp_coeff[3] / 4.0 * ts ** 4 + cp_coeff[4] / 5.0 * ts ** 5 + cp_coeff[5] / 6.0 * ts ** 6 + \
            cp_coeff[6] / 7.0 * ts ** 7 + cp_coeff[7] / 8.0 * ts ** 8


    # -----------------------------------------------------------
    def calculer_rayon_from_hauteur_adim(self, r):
        return [r.min() + h * (r.max() - r.min()) for h in self.hauteurs]

    def calculer_nb_aubes(self):
        return [self.row_obj.z]

    def calculer_rba(self):
        hhba = self.hauteur_adim_genepi(self.rle)
        return self._calculer_avec_hauteur_new(hhba, 1000 * self.rle)

    def calculer_rba_genepi(self):
        hhba = self.hauteur_adim_genepi(self.rle_genepi)
        return self._calculer_avec_hauteur_new(hhba, 1000 * self.rle_genepi)

    def calculer_rbf(self):
        hhbf = self.hauteur_adim_genepi(self.rte_caviar)
        return self._calculer_avec_hauteur_new(hhbf, 1000 * self.rte_caviar)

    def calculer_rbf_genepi(self):
        hhbf = self.hauteur_adim_genepi(self.rte_genepi)
        return self._calculer_avec_hauteur_new(hhbf, 1000 * self.rte_genepi)

    def calculer_corde_meridienne(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.corde_merid())

    def calculer_corde(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.corde_aero())

    def calculer_corde_axial(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.corde_axial())

    def calculer_corde_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.corde_genepi())

    def calculer_emaxsc(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.emaxsc())

    def calculer_emaxsc_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.emaxsc_genepi())

    def calculer_xemaxsc(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.xemaxsc())

    def calculer_xemaxsc_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.xemaxsc_genepi())

    def calculer_emax(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.emax())

    def calculer_emax_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.emax_genepi())

    def calculer_xemax(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.xemax())

    def calculer_xemax_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.xemax_genepi())

    def calculer_calage(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.calage())

    def calculer_calage_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.calage_genepi())

    def calculer_hsc(self):
        return [self.hsc()]

    def calculer_hsc_genepi(self):
        return [self.hsc_genepi()]

    def calculer_s(self):
        return self._calculer_avec_hauteur_new(self.hhemp, 1000 * self.s())

    def calculer_ssc(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.ssc())

    def calculer_ssc_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.ssc_genepi())

    def calculer_mw1(self):
        mw = self.get_inlet_data()["Mw"]
        return self._calculer_avec_hauteur_new(self.hh1, mw)

    def calculer_mw2(self):
        mw = self.get_outlet_data()["Mw"]
        return self._calculer_avec_hauteur_new(self.hh2, mw)

    def calculer_beta1(self):
        beta = self.get_inlet_data()["beta"]
        return [math.degrees(val) for val in self._calculer_avec_hauteur_new(self.hh1, beta)]

    def calculer_beta2(self):
        beta = self.get_outlet_data()["beta"]
        return [math.degrees(val) for val in self._calculer_avec_hauteur_new(self.hh2, beta)]

    def calculer_ralentissement(self):
        return [val for val in self._calculer_avec_hauteur_new(self.hh2, self.w2_w1())]

    def calculer_pi(self):
        return [val for val in self._calculer_avec_hauteur_new(self.hh2, self.pi())]

    def calculer_deviation(self):
        return [math.degrees(val) for val in self._calculer_avec_hauteur_new(self.hh2, self.deviation())]

    def calculer_dhsu2(self):
        return self._calculer_avec_hauteur_new(self.hh2, self.dhsu2())

    def calculer_vzsu(self):
        return self._calculer_avec_hauteur_new(self.hh2, self.vzsu())

    def calculer_psia(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.psia())

    def calculer_psia_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.psia_genepi())

    def calculer_dli(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.dli())

    def calculer_dli_genepi(self):
        return self._calculer_avec_hauteur_new(self.hhemp, self.dli_genepi())

    def calculer_sigma(self):
        return self._calculer_avec_hauteur_new(self.hh2, self.sigma())

    def calculer_dss_genepi(self):
        return [self.dss_genepi()]

    def calculer_dss(self):
        return [self.dss()]

    def calculer_dstd1(self):
        average = RadialEntropicAverage(self.row_obj.inlet)
        debit = self.tf.debn
        return [self.dstd(debit, average.Tt, average.pt)]

    def calculer_kd(self):
        kd_all = []
        for zone in self.tf.zones:
            for station in zone.stations:
                kd_all.append(station.kd)
        return kd_all

    def calculer_xplane(self):
        xplane_all = []
        for zone in self.tf.zones:
            for station in zone.stations:
                xplane_all.append(station.points.x[0])

        return xplane_all

    def calculer_jeu_axial(self):

        lst_row = self.tf.rows_names
        irow_current = lst_row.index(self.row_obj.name)
        irow_next = irow_current + 1

        if irow_next < len(lst_row):
            row_next = lst_row[irow_next]
            row_obj_next = self.tf.get_row_zone(row_next)[0]

            xte_current, rte_current = self.xr_te_caviar(self.row_obj)
            xle_next, rle_next  = self.xr_le(row_obj_next)
            axial_gaps = 1000 * (xle_next - xte_current)

            hadim = self.hauteur_adim(xle_next, rle_next)

            return self._calculer_avec_hauteur_new(hadim, axial_gaps)


