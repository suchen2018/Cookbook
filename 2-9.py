# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:17:33 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as col

values = np.random.random_integers(99, size=50)
values.sort()
cmap = cm.ScalarMappable(col.Normalize(0, 99), cm.binary)

plt.bar(np.arange(len(values)), values, color =cmap.to_rgba(values))
plt.show()