# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:48:31 2018

@author: Chen
"""
import numpy as np
import matplotlib.pyplot as plt

value = np.random.rand(8)
color_set = ('.00', '.25', '.50', '.75')

plt.pie(value, colors = color_set)
plt.show()