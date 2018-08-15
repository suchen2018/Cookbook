# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:54:11 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

plt.bar(X, A, color='w', hatch='x')
plt.bar(X, A+B, bottom=A, color='g', hatch='/')

plt.show()