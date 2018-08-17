# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:26:22 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 1024)
Y1 = np.sinc(X)
Y2 = np.sinc(X)+1

plt.plot(X, Y1, marker='o', color='.75')
plt.plot(X, Y2, marker="o", color='k', markevery=32)

plt.show()