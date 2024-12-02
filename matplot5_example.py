#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 1, 5]

font1 = {'family':'serif', 'color':'blue','size':20}
font2 = {'family':'serif', 'color':'darkred','size':15}

plt.plot(x, y)

# ' Loc to position the title'
plt.title("Title", fontdict = font1, loc = 'right')
plt.xlabel("x axis", fontdict = font2)
plt.ylabel("y axis", fontdict = font2)

plt.show()
