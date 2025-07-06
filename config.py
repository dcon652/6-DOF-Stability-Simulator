import numpy as np

# gravity and environment constants
G = 6.67430e-11
mu_earth = 3.986e14
R_earth = 6378.137e3
J2 = 1.08263e-3

# engine and vehicle constants
g0 = 9.80665
Isp = 300
I = np.diag([10, 10, 10])
