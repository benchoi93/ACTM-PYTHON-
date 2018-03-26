# -*- coding: utf-8 -*-
"""
Created on Wed Nov 08 16:54:27 2017

@author: jhsuh
"""
import os
import pandas as pd
import numpy as np
from new.GangDongCellInfoFtn import get_siginput

wd = os.getcwd() + "/"
Demandpath = wd+"Demand.csv"

TrafficDemand = pd.read_csv(Demandpath) ################check

# test_time = 15
# low_time  = 5
# low_time2 = 30

# total_time = (low_time + test_time + low_time2) * 60 # minutes
total_time = sum(TrafficDemand["Length"]) * 60 # minutes

dt = 5 #unit of timestep

timestep = total_time / dt  + 1
timestep = int(timestep)

vehlength = 7 #vehicle length
vf        = 50 #free-flow speed
qmax      = 1800 #maximum flow
w         = 20 #wave speed

kjam   =  1000/vehlength #jam density
kfree  =  qmax/vf #maximum free-flow density
kcap   =  kjam - qmax/w #capital density

#S_coef0, L_coef0, R_coef0 is the ration of straight, left, right to qmax
S_coef0 = 3
L_coef0 = 1
R_coef0 = 1

penalty_set = [0,7.2,7.2]

#if(kcap )

minLength  = vf * dt / 3600 * 1000 #minimum cell length
CellLength = 100


###############################################
###############Cell Setting####################
###############################################
def Generate_Format(CellList, timestep):
    NumCell = len(CellList)
    n          = np.zeros((NumCell, timestep))
    yin        = np.zeros((NumCell, timestep))
    yout       = np.zeros((NumCell, timestep))
    v          = np.ones((NumCell, timestep)) * vf
    n_agent    = np.zeros((NumCell, timestep))
    
    
    update_cell = {} #consist of list which contains information of relation of other cell (Cell ID, related Cell ID, relation(1,2,3), 0.0)
    
    for OCell in CellList:
        for key , DCell in OCell.Rel["out"].items():
            if DCell is not None:
                update_cell[(OCell.ID,DCell.ID)] = 0.0
            
    DCell_set = list(np.unique([x[1] for x in update_cell.keys()]))
    
    return n , yin, yout, v, n_agent, update_cell, DCell_set

# Agent_Cell_list = [] 
# for Cell0 in Cell_list
#   temp = Agent_Cell()
#   temp.Cell = Cell0
#
#   append!(Agent_Cell_list , [temp])
# end


