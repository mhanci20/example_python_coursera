#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 1, 5]

# Çizimi oluşturma
plt.plot(x, y, 'ro-', label='Veri Seti')

# Başlık ve etiketler ekleme
plt.title("Benim İlk Grafiğim")
plt.xlabel("X Değerleri")
plt.ylabel("Y Değerleri")

# Eksen sınırlarını ayarlama
plt.xlim(0.5, 4.5)
plt.ylim(0, 6)

# Çizgi kalınlığı ve eksen çentikleri
plt.grid(True) # Grid çizgilerini ekle
plt.xticks([1, 2, 3, 4]) # X ekseninde çentikleri belirle
plt.yticks([1, 2, 3, 4, 5]) # Y ekseninde çentikleri belirle

# Efsane ekleme
plt.legend()

# Grafiği gösterme
plt.show()
