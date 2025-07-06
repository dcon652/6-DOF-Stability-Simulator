import numpy as np

def rk4(dynamics_fn, y0, t0, tf, dt):
    times = np.arange(t0, tf, dt)
    states = [y0]
    y = y0.copy()
    for t in times[:-1]:
        k1 = dynamics_fn(y, t)
        k2 = dynamics_fn(y + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = dynamics_fn(y + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = dynamics_fn(y + dt * k3, t + dt)
        y += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        states.append(y.copy())
    return np.array(states), times
