import numpy as np
from dynamics import combine_state
from integrators import rk4
from full_dynamics import full_dynamics
from visuals import plot_trajectory
from config import R_earth

def monte_carlo_sim(n_runs=10):
    for i in range(n_runs):
        perturb = np.random.normal(0, 1, size=3)
        r0 = np.array([R_earth + 400e3, 0, 0]) + perturb
        v0 = np.array([0, 7670, 0]) + np.random.normal(0, 0.1, 3)
        q0 = np.array([1, 0, 0, 0])
        omega0 = np.random.normal(0, 0.01, 3)
        m0 = 500
        state0 = combine_state(r0, v0, q0, omega0, m0)
        states, times = rk4(full_dynamics, state0, 0, 300, 1)
        plot_trajectory(states)
