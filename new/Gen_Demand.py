# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 01:02:23 2017

@author: jhsuh
"""
import math
import random
import numpy as np
from new.NewDefClass import Veh
from new.Global import dt
from new.initilize import OD_matrix ,ODpair, DemandCell,  SinkCell


def rand_exponential(mean):
    if mean <= 0.0:
        error("mean must be positive")
    -mean*math.log(random.random())

def Gen_Demand(time_length, demand , cur_veh ,cur_time):

  time_length0 = time_length * 60 / dt

  time_in = [0.0]
  while sum(time_in) < time_length0 :
    time_temp = random.expovariate((demand/3600*dt))
#    rand_exponential(1/(demand*NumCell))
    time_in.append( time_temp  )

  time_in = np.cumsum(time_in)

  VehQ = []

  for veh in range(len(time_in)):
      
    result = Generate_OD(OD_matrix)
    while result is None:          
        result = Generate_OD(OD_matrix)
      
    origin_num = result[0]
    destin_num = result[1]
      
    origin = DemandCell[origin_num]
    destin = SinkCell[destin_num]
    
    time0  = time_in[veh]

    prob0 = random.random()
    thre0 = time0 - np.floor(time0)

    if prob0 < thre0:
      time0 = np.ceil(time0)
    else:
      time0 = np.floor(time0)

    cur_time0 = cur_time * 60 / dt
    time0 = cur_time0 + time0
    

    veh0 = Veh(veh + cur_veh , origin , destin , time0)
    
    VehQ.append( veh0 )
  return VehQ


def Generate_OD(OD_matrix):
    O_demand = np.sum(OD_matrix,axis = 1)
    O_demand = O_demand / sum(O_demand)
    origin_num = np.random.choice(range(len(O_demand)), size = 1, p =  O_demand)[0]
    D_demand = OD_matrix[origin_num , :]    
    D_demand = D_demand / sum(D_demand)
    destin_num = np.random.choice(range(len(D_demand)), size = 1, p =  D_demand)[0]    
    origin = DemandCell[origin_num]
    destin = SinkCell[destin_num]
    
    if (origin , destin) in ODpair :      
        return (origin_num , destin_num)
    else:
        return None
