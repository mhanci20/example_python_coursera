#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parametreler
a = 0.5  # Av türünün üreme hızı
b = 0.01  # Yırtıcı türünün avı tüketme oranı
c = 0.2  # Yırtıcı türünün ölüm hızı
d = 0.001  # Av türünün yırtıcı tarafından üremeye olan etkisi

# Başlangıç koşulları
x0 = 100  # Av türünün başlangıç popülasyonu
y0 = 20   # Yırtıcı türünün başlangıç popülasyonu

# Zaman aralığı
t = np.linspace(0, 15, 1000)

# Lotka-Volterra denklemleri
def lotka_volterra(state, t, a, b, c, d):
    x, y = state
    dxdt = a*x - b*x*y
    dydt = -c*y + d*x*y
    return [dxdt, dydt]

# Denklemi çözme
state0 = [x0, y0]
states = odeint(lotka_volterra, state0, t, args=(a, b, c, d))

# Grafik çizme
plt.figure(figsize=(10, 6))
plt.plot(t, states[:, 0], label='Av')
plt.plot(t, states[:, 1], label='Yırtıcı')
plt.xlabel('Zaman')
plt.ylabel('Popülasyon')
plt.title('Lotka-Volterra Modeli')
plt.legend()
plt.grid(True)
plt.show()
