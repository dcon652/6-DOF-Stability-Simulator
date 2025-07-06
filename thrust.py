import numpy as np
from rotation import pid_attitude_control
from config import Isp, g0

def get_thrust(t):
    return np.array([0, 0, 10 if t < 100 else 0])

def get_torque(t, q, omega):
    return pid_attitude_control(q, omega)

def compute_mass_flow(thrust, m):
    mdot = np.linalg.norm(thrust) / (Isp * g0)
    return -mdot
