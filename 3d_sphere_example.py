#!/usr/bin/env python3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 3 boyutlu bir grafik oluşturma
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Küre için koordinatları oluşturma (x, y, z)
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

# Küreyi çizdirme
ax.plot_surface(x, y, z, color='blue')

# Görselleştirme
plt.show()
