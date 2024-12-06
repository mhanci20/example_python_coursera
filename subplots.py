#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Veri oluştur
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 alt grafik oluştur
fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# İlk alt grafiğe sinüs grafiği
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sinüs Grafiği')

# İkinci alt grafiğe kosinüs grafiği
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Kosinüs Grafiği')

# Üçüncü alt grafiğe iki grafiği birden
axs[1, 0].plot(x, y1, label='Sinüs')
axs[1, 0].plot(x, y2, label='Kosinüs')
axs[1, 0].legend()

# Dördüncü alt grafiği boş bırak
# ...

plt.show()
