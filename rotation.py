import numpy as np
from config import I

def quaternion_product(q1, q2):
    w0, x0, y0, z0 = q1
    w1, x1, y1, z1 = q2
    return np.array([
        -x1 * x0 - y1 * y0 - z1 * z0 + w1 * w0,
         x1 * w0 + y1 * z0 - z1 * y0 + w1 * x0,
        -x1 * z0 + y1 * w0 + z1 * x0 + w1 * y0,
         x1 * y0 - y1 * x0 + z1 * w0 + w1 * z0
    ])

def rotational_dynamics(q, omega, torque):
    omega_quat = np.concatenate([[0], omega])
    q_dot = 0.5 * quaternion_product(q, omega_quat)
    omega_dot = np.linalg.inv(I) @ (torque - np.cross(omega, I @ omega))
    return q_dot, omega_dot

def pid_attitude_control(q, omega):
    kp = 0.1
    kd = 0.05
    q_desired = np.array([1, 0, 0, 0])
    q_error = q_desired - q
    torque = kp * q_error[1:] - kd * omega
    return torque
