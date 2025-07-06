# visuals.py
# handles plots and animation of satellite trajectory and attitude

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from rotation import quaternion_product

# helper function to compute quaternion conjugate
def quaternion_conjugate(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])

# rotate a 3d vector using a quaternion (q * v * q_conj)
def rotate_vector_by_quaternion(v, q):
    q_v = np.concatenate([[0], v])
    return quaternion_product(
        quaternion_product(q, q_v),
        quaternion_conjugate(q)
    )[1:]  # remove scalar part, keep x, y, z

# plots trajectory in 3d space
def plot_trajectory(states):
    r = states[:, 0:3]  # extract position
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(r[:, 0], r[:, 1], r[:, 2])
    ax.set_title("3d trajectory")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")
    plt.show()

# animates orientation of satellite over time using quaternion
def animate_orientation(states):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ln, = ax.plot([], [], [], 'ro-', markersize=8)  # red dot and line

    def init():
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_zlim(-1.5, 1.5)
        ax.set_title("attitude orientation")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        return ln,

    def update(i):
        q = states[i, 6:10]
        print(f"Frame {i} quaternion: {q}")  
        q = q / np.linalg.norm(q)  # normalize quaternion
        v = np.array([0, 0, 1])  # z-axis unit vector
        v_rot = rotate_vector_by_quaternion(v, q)
        ln.set_data([0, v_rot[0]], [0, v_rot[1]])
        ln.set_3d_properties([0, v_rot[2]])
        return ln,

    ani = animation.FuncAnimation(fig, update, frames=len(states), init_func=init, blit=True)
    plt.show()
