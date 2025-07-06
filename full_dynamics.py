from dynamics import split_state, combine_state
from forces import j2_gravity, atmospheric_drag, solar_radiation, third_body
from thrust import get_thrust, get_torque, compute_mass_flow
from rotation import rotational_dynamics

def full_dynamics(state, t):
    r, v, q, omega, m = split_state(state)
    F = j2_gravity(r) + atmospheric_drag(r, v) + solar_radiation(r) + third_body(r, t) + get_thrust(t)
    acc = F / m
    dm = compute_mass_flow(get_thrust(t), m)
    torque = get_torque(t, q, omega)
    q_dot, omega_dot = rotational_dynamics(q, omega, torque)
    return combine_state(v, acc, q_dot, omega_dot, dm)
