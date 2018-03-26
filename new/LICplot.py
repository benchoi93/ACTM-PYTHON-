# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 08:12:21 2017

@author: jhsuh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:03:16 2017

@author: jhsuh
"""
import numpy as np
import matplotlib.pyplot as plt
import pylab

from NewCellInfo import *

fig = plt.figure(figsize = (50,50))

#for i in range(len(LinkList)):
#    w = LinkList[i].Lane*0.5
#    plt.quiver((LinkList[i].O[0]),(LinkList[i].O[1]),((LinkList[i].D[0] - LinkList[i].O[0])),((LinkList[i].D[1] - LinkList[i].O[1])), width=w, scale=1, units = 'xy', angles = 'uv', color='b')


for i in range(len(CellList)):
    w = CellList[i].Link.Lane*0.5
    plt.quiver((CellList[i].x0),(CellList[i].y0),((CellList[i].x1 - CellList[i].x0)),((CellList[i].y1 - CellList[i].y0)), width = w, scale=1, units = 'xy', angles = 'uv', color='r')

t = []
y = []

for i in range(len(IntersectionList)):
    t.append(IntersectionList[i].xPoint)
    y.append(IntersectionList[i].yPoint)
    
plt.scatter(t, y, color='b', label = str(IntersectionList[i].ID), marker='s', s= 1.5)
pylab.savefig('LIC.png')
plt.grid()
plt.draw()
plt.show()