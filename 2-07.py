# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:07:05 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt

values = np.random.randn(100)
b = plt.boxplot(values)

for name, line_list in b.iteritems():
    for line in line_list:
        line.set_color('k')
        
plt.show()
