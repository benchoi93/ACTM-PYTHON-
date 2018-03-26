#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:15:07 2017

@author: sjchoi
"""
import math
import random
import plotly.plotly as py
import networkx as nx
from plotly.graph_objs import *
from new.initilize import  * 

def isCell(CellID):
    filtered = list(filter(lambda x : x.ID == CellID , CellList))
    
    if(len(filtered) == 1):
        return(i[0])
    else:
        return False
    
def gen_veh(ID, O, D, t):
    veh = Veh(ID, O, D, t)
    return veh

def get_CellMaxVeh(CellID):###Cell안의 ftn
    temp_Cell = isCell(CellID)
    maxveh = temp_Cell.Len/vehlength * temp_Cell.Lane ######make vehlength!!
    return maxveh

def get_v(CellID, t):
    if ((isCell(CellID) == False) or (t>time)): #########make time!!
        value = 0
    else:
        value = v[CellID][t] #######check v
    return value

def get_n(CellID, t):######julia functions.jl line 32
#    input: CellID(ID of Cell, Int), time0(1:timestep, Int)
#    output: value(value of n_agent of CellID at timestep)
#    description: get_n gets CellID and time0 and returns value of n_agent of Cell at timestep
#    #original values
#       n=zeros(NumCell,timestep)
#       n_agent=zeros(NumCell,timestep)
    if((isCell(CellID) == False) or (t>time)):################################################make time!!!!!!!!!!!!
        value = 0
    else:
        value = v[CellID][t]####################################check v
    return 0

def get_nagent(CellID, t):
    
    return 0

def get_Q(CellID,t): ###Cell안의 ftn
#    input: CellID(ID of Cell, Int)
#    output: (qmax * lane )/3600*dt (Float64)
#    description: get_Q gets CellID and returns capacity during dt
#    original values
#       qmax=1800
#       lane=3
#
#   filter(x -> x.ID == CellID , Cell_list)[1]
    return (qmax*lane)/3600*dt

##################################################################################### 고쳐야함
def find_update_Cell(O_ID, D_ID):
    for i in update_cell:
        if((O_ID == i[0]) and (D_ID == i[1])):
            return i
    return 0
        

def get_inflow(O_ID , D_ID): #originID : 시작하는 cellID, destinID: 도착하는 cellID
#  #=input: OriginID(ID of a Cell, Int), DestinID(ID of a Cell, Int)
#    output: inflow0(inflow between two Cell, Float64)
#    description: get_inflow returns inflow between two Cells=#
#
#  #exception when ID=0
    if ((O_ID == 0) or (D_ID == 0)):
        return 0.0
    
    cell_rel = Cell_relation(O_ID, D_ID)
    
    if (cell_rel == 0):
        inflow = 0.0
    else:
        update_cell_temp = find_update_Cell(O_ID, D_ID)
        inflow0 = update_cell_temp[4] #0.0, originally
    return inflow0


def Cell_relation(O_ID, D_ID):
#    input: O(ID of a Cell, Int), D(ID of a Cell, Int)
#    output: result(relation(straight=1, left=2, right=3), Int)
#    description: Cell_relation shows relation(straight, left, right) between origin cell and distination cell
    O_Cell = isCell(O_ID)
    D_Cell = isCell(D_ID)
    if (O_Cell.Rel[1][2] == D_Cell): ##########S_out
        result = 1
    elif (O_Cell.Rel[2][2] == D_Cell):
        result = 2
    elif(O_Cell.Rel[3][2] == D_Cell):
        result = 3
    else:
        result = 0
    return result
      

def update_v(k ,lane):
#  #=input: k(amount of vehicle, Int), lane(length of lane, Int)
#    output: updated_v(velocity, Float64)
#    description:update_v calculates the velocity of each cell  =#
#
#  #change the unit of kfree, kcap, kjam, qmax
#  #= original values
#     kjam   =  1000/vehlength
#     kfree  =  qmax/vf
#     kcap   =  kjam - qmax/w =#
    kfree0 = kfree * lane
    kcap0 = kcap * lane
    kjam0 = kjam * lane
    qmax0 = qmax * lane

    if ((0 <= k) and (k < kfree0)):
        updated_v = vf
    elif (k < kcap0):
        updated_v = qmax0 / k
    elif (k <= kjam0):
        q = qmax0 - (k-kcap0) * w
        updated_v = q/k
    else:
        updated_v = 0
    return updated_v


def update_n(CellID, t):
#  #=input: CellID(ID of Cell, Int), time0(1:timestep, Int)
#    output: nresult(number of vehicles, Float64)
#    description: update_n gets number of vehicles in each cell by timestep, using inflow =#
    n = get_n(CellID, t-1)
    inflow = 0
    outflow = 0
    
    Cell_temp = isCell(CellID)
    
    incell = [Cell_temp.Rel[1][1], Cell_temp.Rel[2][1], Cell_temp.Rel[3][1]]
    outcell = [Cell_temp.Rel[1][2], Cell_temp.Rel[2][2], Cell_temp.Rel[3][2]]
    
    for i in range(1,len(incell)):
        inflow_input = get_inflow(incell[i], CellID)
        inflow += inflow_input
    
    for i in range(1,len(outcell)):
        outflow_input = get_inflow(CellID, outcell[i])
        outflow += outflow_input
    
    nresult = n + inflow + outflow   #gets total number of vehicles
    
    #update information in yin & yout (global values)

    yin[CellID, t] = inflow
    yout[CellID, t] = outflow
    
    return nresult


def find_agent_cell(Cell):
    filtered = list(filter(lambda x : x == Cell , Agent_Cell_list))
    
    if (len(filtered) == 1):
        return filtered[0]
    else:
        0
    

def get_frac(incell , cell_rel):
#  #=input: incell(Cell), cell_rel(Cell Relation, Int)
#    output: frac(percentage of capacity, Float64), split(percentage of total n, Float64)
#    description: get_frac returns percentage of capacity and total n =#

    Agent_Cell0 = find_agent_cell(incell) #Agent_Cell0 is Agent_Cell which has same Cell with incell
    
    #number of cell which goes straight/left/right from the network
    Num_S = len(Agent_Cell0.Straight) -1
    Num_L = len(Agent_Cell0.Left) -1
    Num_R = len(Agent_Cell0.Right) -1
    
    nume = ((S_coef0 * (Num_S != 0)) + (L_Coef* (Num_L != 0) ) + (R_coef0 * (Num_R != 0) ))
    
    if (cell_rel == 1):
        dino = (S_coef0 * (Num_S != 0) )
    elif (cell_rel == 2):
        dino = (L_coef0 * (Num_L != 0) )
    elif (cell_rel == 3):
        dino = (R_coef0 * (Num_R != 0) )
    else:
        dino = 0
    
    frac = dino / nume #percentage of capacity
    
    if (not frac.isnumeric()): #test whether a floating point number frac is not a number (NaN)
        frac = 1

    Split_list = [Num_S , Num_L , Num_R]

    if (sum(Split_list) == 0):
        split = 0
    else:
        split = Split_list[cell_rel] / sum(Split_list) #percentage of total n

    return frac , split


def inflow(ReceiveID , time0):
#  #=input: ReceiveID(Id of Cell, Int), time0(1:timestep, Int)
#    output: flowresult(inflow of each direction, Vector)
#    description: inflow finds the number of vehicles entering each cell over time =#
    if (ReceiveID == 0):
        return [0.0,0.0,0.0]

    RCell = filter(lambda x: x.ID==ReceiveID, CellList)

    incell_id = [RCell.Rel[1][1], RCell.Rel[2][1] , RCell.Rel[3][1]]

    flowdemand= [0.0,0.0,0.0]



    for m in range(1,len(incell_id)):
        incell0 = incell_id[m]
        if (incell0 == 0):
            value = 0
        else:
            incell = filter(lambda x: x.ID==incell0, CellList)
            cell_rel = Cell_relation(incell0 , ReceiveID)
            coef0 = minLength / incell.Len
            frac, split = get_frac(incell , cell_rel)
        
        if (incell.Int == 0):
            if (cell_rel == 1):
                value = coef0 * min(  get_n(incell0,time0) * split , get_Q(incell0)  * frac  )
            else:
              value = 0

        else:
            loc      = incell.Loc
            dire      = incell.Dir
        # @show(cell_rel * 100 + loc)
            if (loc == dire):
                signal_now = True
            else:
                signal_id = IntSignal[incell.Int , time0]
                signal    = filter(lambda x: x.ID == signal_id , Signal_list)
                signal_now = signal.signal[cell_rel , loc]

            if (signal_now):
                value = coef0 * min( get_n(incell0 , time0) * split , get_Q(incell0) * frac  )
            else:
                value = 0
    
        flowdemand[m] = value


    coef1 = minLength / RCell.Len
    Receivable = coef1 * max(0, min(get_Q(ReceiveID) , w/vf*(get_CellMaxVeh(ReceiveID) - get_n(ReceiveID , time0) )  ) )
    sum_flowdemand = sum(flowdemand)
    if (sum_flowdemand == 0):
        f0 = 0
    else:
        f0 = min(1 , Receivable / sum_flowdemand )
    flowresult = flowdemand * f0
    
    return flowresult


def Veh_Update(update_cell0 , t):
#  #=input: update_cell0(element in update_cell, Vector), time0(1:timestep, Int)
#    output: None
#    description: Veh_Update gets element in update_cell and timestep and changes values in Agent_Cell_list =#
    O_Cell   = int(update_cell0[1]) #Cell ID
    D_Cell   = int(update_cell0[2]) #related Cell ID
    Cell_rel = int(update_cell0[3]) #relation(1,2,3)
    inflow0  = update_cell0[4]
    
    prob0 = inflow0 - math.floor(inflow0)
    prob1 = random.random()

    if (prob0 < prob1):
        inflow_input = math.floor(inflow0)
    else:
        inflow_input = math.ceil(inflow0)

    if (inflow_input != 0):
        veh_set = []
        inflow_input = int(inflow_input)
        target_Cell = list(filter(lambda x: x.Cell.ID==O_Cell , Agent_Cell_list))[0]

    if (Cell_rel == 1):
        inflow_input1 = min( inflow_input , len(target_Cell.Straight) - 1)
        if(inflow_input1 > 0 ):
            veh_set.append(target_Cell.Straight[2:(inflow_input1+1)]  )
            del target_Cell.Straight[2:(inflow_input1+1)]
    elif (Cell_rel == 2):
        inflow_input1 = min( inflow_input , len(target_Cell.Left) - 1)
        if(inflow_input1 > 0 ):
            veh_set.append(target_Cell.Left[2:(inflow_input1+1)]  )
            del target_Cell.Left[2:(inflow_input1+1)]
    elif (Cell_rel == 3):
        inflow_input1 = min( inflow_input , len(target_Cell.Right) - 1)
        if(inflow_input1 > 0 ):
            veh_set.append(target_Cell.Right[2:(inflow_input1+1)]  )
            del target_Cell.Right[2:(inflow_input1+1)]



    if (len(veh_set) > 0):
        for veh0 in veh_set:
            route0 = veh0.Route
            target_Cell = filter(lambda x: x.Cell.ID==D_Cell , Agent_Cell_list)[1]
            loc = route0.index(D_Cell)

            if (len(route0) == loc):
                target_Cell.Out.append([veh0])
            else:
                target_Cell.Wait.append([veh0])
