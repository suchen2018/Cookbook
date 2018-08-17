# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:01:21 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.standard_normal((100, 2))

plt.scatter(data[:, 0], data[:, 1], color = '1.0', 
            edgecolor = '0.0')
plt.show()
