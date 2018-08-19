# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 22:34:16 2018

@author: Chen
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

a, b, c = 10., 28., 8./3.

def lorenz_map(X, dt=1e-2):
    X_dt = np.array([a*(X[1]-X[0]),
                     X[0]*(b-X[2])-X[1],
                     X[0]*X[1]-c*X[2]])
    return X+dt*X_dt

points = np.zeros((10000, 3))
X = np.array([.1, .0, .0])
for i in range(points.shape[0]):
    points[i], X = X, lorenz_map(X)
    
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(points[:, 0], points[:, 1], points[:, 2], c='k')
plt.show()