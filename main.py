# main.py
#this is the script to run the 6-dof simulation

import numpy as np
from config import R_earth
from dynamics import combine_state
from integrators import rk4
from full_dynamics import full_dynamics
from visuals import plot_trajectory, animate_orientation
from exporter import export_to_csv, export_to_json
from montecarlo import monte_carlo_sim

if __name__ == "__main__":
    # set initial conditions
    r0 = np.array([R_earth + 400e3, 0, 0])
    v0 = np.array([0, 7670, 0])
    q0 = np.array([1, 0, 0, 0])
    omega0 = np.array([0.1, 0.1, 0.1])  # rad/s
    m0 = 500
    state0 = combine_state(r0, v0, q0, omega0, m0)

    # run simulation
    states, times = rk4(full_dynamics, state0, 0, 300, 1)

    # show and save output
    plot_trajectory(states)
    animate_orientation(states)
    export_to_csv(states)
    export_to_json(states)
    monte_carlo_sim(n_runs=5)
