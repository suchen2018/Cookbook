# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:32:52 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.random.standard_normal((100, 2))
A += np.array((1, 1))
B = np.random.standard_normal((100, 2))
B += np.array((1, 1))

plt.scatter(B[:, 0], B[:, 1], c='k', s=100.)
plt.scatter(A[:, 0], A[:, 1], c='b', s=25.)

plt.show()