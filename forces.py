import numpy as np
from config import mu_earth, R_earth, J2

def j2_gravity(r):
    x, y, z = r
    r_norm = np.linalg.norm(r)
    factor = 1.5 * J2 * mu_earth * R_earth**2 / r_norm**5
    ax = x / r_norm * (5 * z**2 / r_norm**2 - 1)
    ay = y / r_norm * (5 * z**2 / r_norm**2 - 1)
    az = z / r_norm * (5 * z**2 / r_norm**2 - 3)
    return -mu_earth * r / r_norm**3 + factor * np.array([ax, ay, az])

def atmospheric_drag(r, v):
    rho = 1e-12
    Cd = 2.2
    A = 0.1
    v_rel = v
    return -0.5 * rho * Cd * A * np.linalg.norm(v_rel) * v_rel

def solar_radiation(r):
    Ps = 4.5e-6
    A = 0.1
    Cr = 1.2
    r_sun = np.array([1.496e11, 0, 0])
    r_rel = r - r_sun
    return -Ps * A * Cr * r_rel / np.linalg.norm(r_rel)

def third_body(r, t):
    return 1e-5 * np.sin(t) * np.array([1, 1, 1])
