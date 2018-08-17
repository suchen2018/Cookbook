# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 23:07:51 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rc('lines', linewidth=2.)
mpl.rc('axes', facecolor='k', edgecolor='w')
mpl.rc('xtick', color='w')
mpl.rc('ytick', color='w')
mpl.rc('text', color='w')
mpl.rc('figure', facecolor='k', edgecolor='w')
mpl.rc('axes', color_cycle=('w', '.5', '.75'))

X = np.linspace(0, 7, 1024)

plt.plot(X, np.sin(X))
plt.plot(X, np.cos(X))
plt.show()