# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:42:16 2018

@author: Chen
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath

shape_description = [
        (1., 2., mpath.Path.MOVETO),
        (1., 1., mpath.Path.LINETO),
        (2., 1., mpath.Path.LINETO),
        (2., -1., mpath.Path.LINETO),
        (1., -1., mpath.Path.LINETO),
        (1., -2., mpath.Path.LINETO),
        (-1., -2., mpath.Path.LINETO),
        (-1., -1., mpath.Path.LINETO),
        (-2., -1., mpath.Path.LINETO),
        (-2., 1., mpath.Path.LINETO),
        (-1., 1., mpath.Path.LINETO),
        (-1., 2., mpath.Path.LINETO),
        (0., 0., mpath.Path.CLOSEPOLY),]

u, v, codes = zip(*shape_description)
my_marker = mpath.Path(np.asanyarray((u, v)).T, codes)
data = np.random.rand(8, 8)
plt.scatter(data[:, 0], data[:, 1], c='.75', marker=my_marker, s=64)
plt.show()