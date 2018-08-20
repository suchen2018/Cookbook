# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:55:06 2018

@author: Chen
"""

import numpy as np
from matplotlib import cm
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Data generation
alpha = 1./np.linspace(1, 8, 5)
t = np.linspace(0, 5, 16)
T, A = np.meshgrid(t, alpha)
data = np.exp(-T*A)

fig = plt.figure()
ax = fig.gca(projection='3d')
cmap = cm.ScalarMappable(col.Normalize(0, len(alpha)), cm.gray)
for i, row in enumerate(data):
    ax.bar(4*t, row, zs=i, zdir='y', alpha=0.8, color=cmap.to_rgba(i))
    
plt.show()