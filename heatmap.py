#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Rastgele bir matris oluştur
data = np.random.rand(10, 10)

# Heatmap çizdir
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
