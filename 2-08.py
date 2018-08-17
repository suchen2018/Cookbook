# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:12:07 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N = 256
angle = np.linspace(0, 8*2*np.pi, N)
radius = np.linspace(.5, 1., N)

X = radius*np.cos(angle)
Y = radius*np.sin(angle)

plt.scatter(X, Y, c = angle, cmap=cm.hsv)
plt.show()
