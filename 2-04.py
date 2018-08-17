# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:08:28 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

women_pop = np.array([5., 30., 45., 22.])
men_pop = np.array([5., 25., 50., 20.])

X = np.arange(4)
plt.barh(X, women_pop, color = '.25')
plt.barh(X, -men_pop, color = '.75')
plt.show()
