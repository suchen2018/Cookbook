# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:26:07 2018

@author: Chen
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Generate torus mesh
angle = np.linspace(0, 2*np.pi, 32)
theta, phi = np.meshgrid(angle, angle)
r, R = .25, 1.
X = (R+r*np.cos(phi))*np.cos(theta)
Y = (R+r*np.cos(phi))*np.sin(theta)
Z = r*np.sin(phi)

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-.25, .25)
#ax.plot_surface(X, Y, Z, color='w', rstride=1, cstride=1)
ax.plot_wireframe(X, Y, Z, color='k', rstride=1, cstride=1)
plt.show()