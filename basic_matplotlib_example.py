#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Veri oluşturma
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 5, 4, 6]
y2 = [1, 3, 2, 5, 3]

# Grafiği çizme
plt.plot(x, y1, label='Veri Seti 1')
plt.plot(x, y2, label='Veri Seti 2')
plt.xlabel('X ekseni')
plt.ylabel('Y ekseni')
plt.title('Çoklu Veri Seti')
plt.legend()
plt.show()
