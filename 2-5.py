# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:34:28 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

values = np.random.random_integers(99, size=50)
values.sort()
print(values)

color_set = ('.00', '.25', '.50', '.75')
color_list = [color_set[(len(color_set)*val)//100] for val in values]
plt.bar(np.arange(len(values)), values, color =color_list)
plt.show()