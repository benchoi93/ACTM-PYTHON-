# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:03:16 2017

@author: jhsuh
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab

from NewCellInfo import *

fig = plt.figure(figsize = (30,30))



for i in range(len(LinkList)):
    w = LinkList[i].Lane*0.5
    plt.quiver((LinkList[i].O[0]),(LinkList[i].O[1]),((LinkList[i].D[0] - LinkList[i].O[0])),((LinkList[i].D[1] - LinkList[i].O[1])), width=w, scale=1, units = 'xy', angles = 'uv', color='r')



t = []
y = []

for i in range(len(IntersectionList)):
    t.append(IntersectionList[i].xPoint)
    y.append(IntersectionList[i].yPoint)
    

plt.scatter(t, y, color='b', label = str(IntersectionList[i].ID), marker='s', s= 1.5)
pylab.savefig('LI.png')
plt.grid()
plt.draw()
plt.show()

