# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:23:50 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

plt.bar(X, A, color='.75')
plt.bar(X, A+B, bottom=A, color='k', linestyle='dashed')

plt.show()