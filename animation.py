#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Veri oluştur
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro-', animated=True)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1.1, 1.1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
