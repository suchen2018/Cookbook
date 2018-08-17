# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:37:52 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.random.standard_normal((1000, 2))
R = np.sum(M**2, axis=1)

plt.scatter(M[:, 0], M[:, 1], c='w', marker='s', edgecolor='k', s=32.*R)
plt.show()