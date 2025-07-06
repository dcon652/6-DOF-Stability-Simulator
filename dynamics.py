import numpy as np

def split_state(state):
    r = state[0:3]
    v = state[3:6]
    q = state[6:10]
    omega = state[10:13]
    m = state[13]
    return r, v, q, omega, m

def combine_state(r, v, q, omega, m):
    return np.concatenate([r, v, q, omega, [m]])
