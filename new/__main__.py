"""
Created on Fri Sep 29 14:15:07 2017

@author: sjchoi
"""


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%                               %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%  KAIST ACTM Simulation Start  %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%                               %%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")





#
#f = open("outputdir.txt",'r')
#workingdirectory = f.readline()
#f.close()


#
#with open("outputdir.txt", 'r') as f:
#    reader = f.readlines()
#    raw_data = list(reader)
#    
#with open("outputdir2.txt", 'w') as f:
#    for path0 in raw_data:
#        f.writelines(path0)
#        
        





print("\nImporting dependencies")
import numpy as np
import math
import random
import plotly.plotly as py
import networkx as nx
from plotly.graph_objs import *

print("\nInitializing Simulation Environment")
from new.initilize import *
from new.Gen_Demand import *

import csv

def writeIntInfo(path = "IntInfoCSV.csv"):
    global IntersectionList
    f = open(path,'w')
    write = csv.writer(f)
    
    ID  = [x.ID for x in IntersectionList]
    x0  = [x.xPoint for x in IntersectionList]
    y0  = [x.yPoint for x in IntersectionList]
    write.writerow(['ID', 'x', 'y'])    
    for i in range(len(ID)):
        write.writerow([ID[i],x0[i], y0[i]])
    f.close()
    
    
    
def writeCellInfo(path = 'CellInfoCSV.csv'):
    global CellList
    f = open(path,'w')
    write = csv.writer(f)
    
    ID = [x.ID for x in CellList]
    Lane= [x.Lane for x in CellList]
    Length= [x.Len for x in CellList]
    Netin= [x.NetIn for x in CellList]
    Netout= [x.NetOut for x in CellList]
    #    Link = [x.Link.ID for x in CellList]
    Loc= [x.Loc for x in CellList]
    Dir= [x.Dir for x in CellList]
    S_i= [x.Rel['in']['S'] for x in CellList]
    L_i= [x.Rel['in']['L'] for x in CellList]
    R_i= [x.Rel['in']['R'] for x in CellList]
    S_o= [x.Rel['out']['S'] for x in CellList]
    L_o= [x.Rel['out']['L'] for x in CellList]
    R_o= [x.Rel['out']['R'] for x in CellList]
    
    S_in = []
    for i in S_i:
        if(i==None):
            S_in.append(0)
        else:
            S_in.append(i.ID)
            
    L_in = []
    for i in L_i:
        if(i==None):
            L_in.append(0)
        else:
            L_in.append(i.ID)
    
    R_in = []
    for i in R_i:
        if(i==None):
            R_in.append(0)
        else:
            R_in.append(i.ID)
    
    S_out = []
    for i in S_o:
        if(i==None):
            S_out.append(0)
        else:
            S_out.append(i.ID)
            
    L_out = []
    for i in L_i:
        if(i==None):
            L_out.append(0)
        else:
            L_out.append(i.ID)
    
    R_out = []
    for i in R_o:
        if(i==None):
            R_out.append(0)
        else:
            R_out.append(i.ID)
    i=0
    
    x0= [x.x0 for x in CellList]
    y0= [x.y0 for x in CellList]
    x1= [x.x1 for x in CellList]
    y1= [x.y1 for x in CellList]
    #    write.writerow(['ID', 'Lane', 'Length', 'Netin', 'Netout', 'Int', 'Loc', 'Dir', 'S_in', 'L_in', 'R_in', 'S_out', 'L_out', 'R_out', 'x0', 'y0', 'x1', 'y1'])
    write.writerow(['ID', 'Lane', 'Length', 'Netin', 'Netout', 'Loc', 'Dir', 'S_in', 'L_in', 'R_in', 'S_out', 'L_out', 'R_out', 'x0', 'y0', 'x1', 'y1'])    
    for i in range(len(ID)):
        write.writerow([ID[i], Lane[i], Length[i], Netin[i], Netout[i], Loc[i], Dir[i], S_in[i], L_in[i], R_in[i], S_out[i], L_out[i], R_out[i], x0[i], y0[i], x1[i], y1[i]])
    f.close()



def writeLinkInfo(path = 'LinkInfoCSV.csv'):
    global LinkList 
    
    f = open(path,'w')
    write = csv.writer(f)
    
    ID = [x.ID for x in LinkList]
    #    Lane= [x.Lane for x in CellList]
    #    Length= [x.Len for x in CellList]
    #    Netin= [x.NetIn for x in CellList]
    #    Netout= [x.NetOut for x in CellList]
    #    Int= [x.Int.ID for x in CellList]
    #    Link = [x.Link.ID for x in CellList]
    #    Loc= [x.Loc for x in CellList]
    #    Dir= [x.Dir for x in CellList]
    #    S_in= [x.Rel['in']['Sin'] for x in CellList]
    #    L_in= [x.Rel['in']['Lin'] for x in CellList]
    #    R_in= [x.Rel['in']['Rin'] for x in CellList]
    #    S_out= [x.Rel['in']['Sout'] for x in CellList]
    #    L_out= [x.Rel['in']['Lout'] for x in CellList]
    #    R_out= [x.Rel['in']['Rout'] for x in CellList]
    x0= [x.O[0] for x in LinkList]
    y0= [x.O[1] for x in LinkList]
    x1= [x.D[0] for x in LinkList]
    y1= [x.D[1] for x in LinkList]
    #    rx0= [x.rx0 for x in CellList]
    #    ry0= [x.ry0 for x in CellList]
    #    rx1= [x.rx1 for x in CellList]
    #    ry1= [x.ry1 for x in CellList]
    #    write.writerow(['ID', 'Lane', 'Length', 'Netin', 'Netout', 'Int', 'Loc', 'Dir', 'S_in', 'L_in', 'R_in', 'S_out', 'L_out', 'R_out', 'x0', 'y0', 'x1', 'y1'])
    write.writerow(['ID', 'x0', 'y0', 'x1', 'y1'])    
    for i in range(len(ID)):
        write.writerow([ID[i], x0[i], y0[i], x1[i], y1[i]])
    f.close()

def isCell(CellID):
    filtered = list(filter(lambda x : x.ID == CellID , CellList))
    
    if(len(filtered) == 1):
        return(filtered[0])
    else:
        return False

def get_v(Cell, time0):
    if type(Cell) == "str":
        Cell = isCell(Cell)
    global timestep
    if ((Cell == False) or (time0 > timestep)): #########make time!!
        value = 0
    else:
        value = v[CellList.index(Cell) , time0] #######check v
    return value

def get_n(Cell, time0):######julia functions.jl line 32
#    input: CellID(ID of Cell, Int), time0(1:timestep, Int)
#    output: value(value of n_agent of CellID at timestep)
#    description: get_n gets CellID and time0 and returns value of n_agent of Cell at timestep
#    #original values
#       n=zeros(NumCell,timestep)
#       n_agent=zeros(NumCell,timestep)
    
    if type(Cell) == "str":
        Cell = isCell(Cell)
        
    global timestep
    if((Cell == False) or (time0 > timestep)): ################################################make time!!!!!!!!!!!!
        value = 0
    else:
        global CellList
        value = n[CellList.index(Cell) , time0] ####################################check v
    return value

def get_nagent(Cell, time0):######julia functions.jl line 32
#    input: CellID(ID of Cell, Int), time0(1:timestep, Int)
#    output: value(value of n_agent of CellID at timestep)
#    description: get_n gets CellID and time0 and returns value of n_agent of Cell at timestep
#    #original values
#       n=zeros(NumCell,timestep)
#       n_agent=zeros(NumCell,timestep)
    
    if type(Cell) == "str":
        Cell = isCell(Cell)
        
    global timestep
    if((Cell == False) or (t>timestep)): ################################################make time!!!!!!!!!!!!
        value = 0
    else:
        global CellList
        value = n_agent[CellList.index(Cell) , time0] ####################################check v
    return value
    
def Cell_relation(O_ID, D_ID):
#    input: O(ID of a Cell, Int), D(ID of a Cell, Int)
#    output: result(relation(straight=1, left=2, right=3), Int)
#    description: Cell_relation shows relation(straight, left, right) between origin cell and distination cell
    O_Cell = isCell(O_ID)
    D_Cell = isCell(D_ID)
    if (O_Cell.Rel["out"]["S"] == D_Cell): ##########S_out
        result = 1
    elif (O_Cell.Rel["out"]["L"] == D_Cell):
        result = 2
    elif(O_Cell.Rel["out"]["R"] == D_Cell):
        result = 3
    else:
        result = 0
    return result

def Cell_relation_C(O_Cell, D_Cell):
#    input: O(ID of a Cell, Int), D(ID of a Cell, Int)
#    output: result(relation(straight=1, left=2, right=3), Int)
#    description: Cell_relation shows relation(straight, left, right) between origin cell and distination cell
    if (O_Cell.Rel["out"]["S"] == D_Cell): ##########S_out
        result = 'S'
    elif (O_Cell.Rel["out"]["L"] == D_Cell):
        result = 'L'
    elif(O_Cell.Rel["out"]["R"] == D_Cell):
        result = 'R'
    else:
        result = 0
    return result

#       lane=3
#
#   filter(x -> x.ID == CellID , Cell_list)[1]
##################################################################################### 고쳐야함
        
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
        inflow0 = 0.0
    else:
        inflow0 = find_update_Cell(O_ID, D_ID)
    return inflow0

def find_update_Cell(O_ID, D_ID):
    global update_cell
    for i in update_cell:
        if((O_ID == i[0]) and (D_ID == i[1])):
            return update_cell[i]
    return 0

def update_v(k ,lane , qmax0):
#  #=input: k(amount of vehicle, Int), lane(length of lane, Int)
#    output: updated_v(velocity, Float64)
#    description:update_v calculates the velocity of each cell  =#
#
#  #change the unit of kfree, kcap, kjam, qmax
#  #= original values
#     kjam   =  1000/vehlength
#     kfree  =  qmax/vf
#     kcap   =  kjam - qmax/w =#
    global kfree
    global kcap
    global kjamj
    
    kfree0 = kfree * lane
    kcap0 = kcap * lane
    kjam0 = kjam * lane

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


def update_n(i, t):
#  #=input: CellID(ID of Cell, Int), time0(1:timestep, Int)
#    output: nresult(number of vehicles, Float64)
#    description: update_n gets number of vehicles in each cell by timestep, using inflow =#
    n0 = get_nagent(CellList[i], t-1)
    inflow = 0
    outflow = 0
    
    Cell_temp = CellList[i]
    
    incell = [Cell_temp.Rel['in']['S'], Cell_temp.Rel['in']['L'], Cell_temp.Rel['in']['R']]
    outcell = [Cell_temp.Rel['out']['S'], Cell_temp.Rel['out']['L'], Cell_temp.Rel['out']['R']]
    
    incell = [x for x in incell if x is not None]
    outcell = [x for x in outcell if x is not None]
    
    inflows = [get_inflow(x.ID , Cell_temp.ID) for x in incell]
    outflows = [get_inflow(Cell_temp.ID , x.ID) for x in outcell]
    
    nresult = n0 + sum(inflows) - sum(outflows)   #gets total number of vehicles
    
    if(nresult < 0):
        print("n0 : " + str(n0) + " inflow : " + str(sum(inflows)) + " outflows : " + str(sum(outflows)))
    
    
    #update information in yin & yout (global values)
    global yin
    global yout
    
    yin[i, t] = sum(inflows)
    yout[i, t] = sum(outflows)
    
    return nresult



def cellrel_to_num(cell_rel):
    if cell_rel == "S":
        return 0
    elif cell_rel == "L":
        return 1
    elif cell_rel == "R":
        return 2
    
def inflow(RCell , time0):
#  #=input: ReceiveID(Id of Cell, Int), time0(1:timestep, Int)
#    output: flowresult(inflow of each direction, Vector)
#    description: inflow finds the number of vehicles entering each cell over time =#

#    if (ReceiveID == 0):
#        return [0.0,0.0,0.0]

    incell = RCell.Rel['in']

    flowdemand= {}
    for key in incell.keys():
        flowdemand[key] = 0.0

    for key in incell.keys():
        SCell = incell[key] # SCell for Source Cell
        value = 0
        if SCell is not None:
            global minLength
            LenCoef = min(minLength / SCell.Len , 1)
            
            Num_S = SCell.veh_q.get_Num()[0]
            Num_L = SCell.veh_q.get_Num()[1]
            Num_R = SCell.veh_q.get_Num()[2]
            
            cell_rel = key

            global S_coef0
            global L_coef0
            global R_coef0
            
            nume = ((S_coef0 * (Num_S != 0)) + (L_coef0* (Num_L != 0) ) + (R_coef0 * (Num_R != 0) ))
            
            if (cell_rel == "S"):
                dino = (S_coef0 * (Num_S != 0) )
            elif (cell_rel == "L"):
                dino = (L_coef0 * (Num_L != 0) )
            elif (cell_rel == "R"):
                dino = (R_coef0 * (Num_R != 0) )
            else:
                dino = 0.0
            
            if nume == 0:#test whether a floating point number frac is not a number (NaN)
                frac = 1.0
            else:
                frac = dino / nume #percentage of capacity
            
            Split_list = [Num_S , Num_L , Num_R]
            
            
            Int0 = list(set(SCell.Int).intersection(RCell.Int))
            
            if len(Int0) == 0:
                if key == "S":
                    value = LenCoef * min( Num_S , SCell.get_Q()*frac  )
                else:
                    value = 0.0
            else:
                if(len(Int0) > 1):
                    print("inflow error with more than one Intersection")
                    
                IntRel = Int0[0].Rel["in"]
                keys = list(IntRel.keys())
                values = list(IntRel.values())
                        
                loc = keys[values.index(SCell)]
                
                curSig = Int0[0].get_curSig(time0)
                        
                global SignalList
                signal0 = SignalList[str(curSig)][str(loc)].signal[cellrel_to_num(cell_rel)]
                
                if signal0:
                    value = LenCoef * min( Split_list[cellrel_to_num(cell_rel)] , SCell.get_Q()*frac  )
                else:
                    value = 0.0
                    
        flowdemand[key] = value
        

    LenCoef2 = minLength / RCell.Len
    Receivable = LenCoef2 * max(0, min(RCell.get_Q() , w/vf*(RCell.get_CellMaxVeh() - get_nagent(RCell , time0) )  ) )
    
    sum_flowdemand = sum(flowdemand.values())
    if (sum_flowdemand == 0):
        f0 = 0.0
    else:
        f0 = min(1 , Receivable / sum_flowdemand )
        
    flowresult = flowdemand
    for key in flowresult.keys():
        flowresult[key] = flowdemand[key] * f0
    
    return flowresult , incell


def Veh_Update(update_cell0 , inflow0 , t):
#  #=input: update_cell0(element in update_cell, Vector), time0(1:timestep, Int)
#    output: None
#    description: Veh_Update gets element in update_cell and timestep and changes values in Agent_Cell_list =#
    OCellID = update_cell0[0]
    DCellID = update_cell0[1]
    
    cell_rel = Cell_relation(OCellID , DCellID)
    
    prob0 = inflow0 - math.floor(inflow0)
    prob1 = random.random()

    if (prob0 < prob1):
        inflow_input = math.floor(inflow0)
    else:
        inflow_input = math.ceil(inflow0)



    if (inflow_input != 0):
        veh_set = []
        inflow_input = int(inflow_input)
        
        OCell = isCell(OCellID)
        DCell = isCell(DCellID)
        
        if cell_rel == 1:
            
            for veh0 in range(inflow_input):
                veh_set.append(OCell.veh_q.straight.pop(0))
                
        elif cell_rel == 2:
            
            for veh0 in range(inflow_input):
                veh_set.append(OCell.veh_q.left.pop(0))
                
        elif cell_rel == 3:
            
            for veh0 in range(inflow_input):
                veh_set.append(OCell.veh_q.right.pop(0))
                
        else:
            print("Veh_Update error // OCell:" + str(OCellID) +" and DCell:" + str(DCellID))
        
        
        global VehOutList
        if (len(veh_set) > 0):
            for veh0 in veh_set:
#                route0 = veh0.route
                if DCell in veh0.route:
                    cnt = veh0.route.index(DCell)
                else:
                    print("Veh_Update error // veh: " + str(veh0.ID) + " OCell:" +str(OCellID) +" and DCell:" + str(DCellID) )
                
                if cnt == len(veh0.route)-1 :
                    veh0.Endtime = t
                    veh0.active = False
                    VehOutList.append(veh0)
                else:                    
                    DCell.veh_q.add_veh(veh0 , "W")
                

def get_distmx(graph0 , v, t): 
#      #=input: graph0(Directed graph made from NumCell, LightGraphs.Digraph), v(matrix of vf, Matrix), time0(1:timestep, Int)
#    output: distmx(,Matrix)
#    description:  =#
#    #=original values
#      v=ones(NumCell,timestep)*vf=#

    distmx = np.zeros((len(CellList), len(CellList)))
    for edge in graph0.edges(): #############################################LightGraphs => igraph
        CellLength0 = CellList[edge[0]].Len
        if (t == 1):
            v0 = vf
        else:
            v0 = v[edge[0],t-1]
        v0 = v0 / 3.6
    # penalty = 0
        cell_rel = Cell_relation(CellList[edge[0]].ID , CellList[edge[1]].ID)
        penalty = penalty_set[cell_rel-1]
        
        if v0 == 0 :
            v0 = 0.01
            
        distmx[edge[0],edge[1]] = CellLength0/v0 + penalty
    return distmx



def dist(OCell , DCell):
    CellLength0 = CellList[OCell].Len
    global t
    if (t == 1):
        v0 = vf
    else:
        v0 = v[OCell,t-1]
    v0 = v0 / 3.6
    cell_rel = Cell_relation(CellList[OCell].ID , CellList[DCell].ID)
    penalty = penalty_set[cell_rel-1]
    
    if v0 == 0:
        v0 = 0.0001
    
    
    return CellLength0/v0 + penalty




def Sim_update_VehGen(time0):
    veh_gen_set = list(filter(lambda x: x.time == time0 , Veh_Q))
    if len(veh_gen_set) >= 1:
        for veh in range(len(veh_gen_set)):
            origin  =  veh_gen_set[veh].O_cell
            destin  =  veh_gen_set[veh].D_cell

            
            global CellList
            global G
            route = nx.astar_path(G , CellList.index(origin) ,CellList.index(destin) , dist )
            
            route_Cell = []
            for r0 in route:
                route_Cell.append(CellList[r0])
                
            veh_gen_set[veh].route = tuple(route_Cell)
            veh_gen_set[veh].active = True
            
            if (len(route) > 1):
                rel = Cell_relation(route_Cell[0].ID , route_Cell[1].ID)
            else:
                print("Sim_update_VehGen Error at " + str(veh) )

# check if it really overwrites global Cells 
            O_Cell = veh_gen_set[veh].O_cell

            if rel == 1:
                CellList[CellList.index(O_Cell)].veh_q.add_veh(veh_gen_set[veh] , "S")
            elif rel == 2:
                CellList[CellList.index(O_Cell)].veh_q.add_veh(veh_gen_set[veh] , "L")
            elif rel == 3:
                CellList[CellList.index(O_Cell)].veh_q.add_veh(veh_gen_set[veh] , "R")
            else:
                print("Sim Update Vehicle Generation Error")
            
            global n_agent
            n_agent[route[0], time0] +=  1
            

def Sim_update_UpdateN(time0):
    global CellList
    global n
    
    for i in range(len(CellList)):    
        n[i,time0] = update_n( i , time0 )
        

def Sim_update_VehtoW(time0):
    global update_cell
    
    update_cell_filtered = [x for x in update_cell.keys() if update_cell[x] > 0]
    
    
    for input0 in update_cell_filtered:
        if sum(isCell(input0[0]).veh_q.get_Num()) < update_cell[input0]:
            print("Sim_update_VehtoW Error")
    
    
    
    for input0 in update_cell_filtered:
#        if update_cell[input0] > 0:
            Veh_Update(input0 , update_cell[input0] , time0)


def Sim_update_UpdateW(time0):
    global CellList
    
    update_wait_pre = [x for x in CellList if len(x.veh_q.wait) > 0]
#    list(filter(lambda x: len(x.veh_q.wait) != 0, CellList))

    for Cell0 in update_wait_pre:
        veh_wait = Cell0.veh_q.wait

        for veh0 in veh_wait:
            
            if Cell0 in veh0.route:
                cnt = veh0.route.index(Cell0)                
            else:
                print("Sim_update_UpdateW error // veh: " + str(veh0.ID) + " OCell:" +str(Cell0.ID)  )

            Cell_rel = Cell_relation(Cell0.ID , veh0.route[cnt+1].ID)
            
            if (Cell_rel == 1):
                Cell0.veh_q.add_veh(veh0 , "S")
                veh_wait.remove(veh0)
#                Cell0.veh_q.straight.append(Cell0.veh_q.wait.pop(0))

            elif (Cell_rel == 2):
                Cell0.veh_q.add_veh(veh0 , "L")                
                veh_wait.remove(veh0)
#                Cell0.veh_q.left.append(Cell0.veh_q.wait.pop(0))

            elif (Cell_rel == 3):
                Cell0.veh_q.add_veh(veh0 , "R")
                veh_wait.remove(veh0)
            else:
                print("Sim_update_UpdateW Cell_rel Error : " + str(Cell_rel))
#                Cell0.veh_q.right.append(Cell0.veh_q.wait.pop(0))
    
    update_wait_pre = list(filter(lambda x: len(x.veh_q.wait) != 0, CellList))
    
    if len(update_wait_pre) != 0:
#        print("Sim_update_UpdateW Recursive Run at time " + str(time0) + " length " +str(len(update_wait_pre)))
        Sim_update_UpdateW(time0)
    
    
    update_nagent_filter = [x for x in CellList if sum(x.veh_q.get_Num()) > 0 ]
    for Cell0 in update_nagent_filter:
        n_agent[CellList.index(Cell0) , time0] = sum(Cell0.veh_q.get_Num()[:3])


def Sim_update_UpdateV(time0):
    global CellList
    global v
    
    CellList_filtered = [x for x in CellList if sum(x.veh_q.get_Num()) > 0 ]
    
    for Cell0 in CellList:
        i = CellList.index(Cell0)
        k = get_n(Cell0 , time0-1) / (Cell0.Len / 1000)
        
        lane = Cell0.Lane
        qmax0 = Cell0.get_Q() / dt * 3600
        
        updated_v = update_v(k , lane , qmax0)
        if updated_v < 0:
            print("Sim_update_UpdateV Error // Cell : " + str(Cell0.ID))
            v[i,time0] = 0
        else:
            v[i,time0] = updated_v
        

def get_curn(Cell):
    return sum(Cell.veh_q.get_Num())

def check_DCell(c):
    
    cL  = list(c.Rel["in"].values())
    cL = [x for x in cL if x is not None]
    cLmap = list(map( get_curn , cL))
    cLmap = [x for x in cLmap if x is not 0]
    
    return len(cLmap) != 0
    
def Sim_update_UpdateInflow(time0):
    global update_cell
    
    for key in update_cell.keys():
        update_cell[key] = 0
    
    DCellList = list(filter(lambda x : x.ID in DCell_set , CellList))
    DCellfiltered = [x for x in DCellList if check_DCell(x)]
    
    for i0 in range(len(DCellfiltered)):
        DCell      = DCellfiltered[i0]
        DCellID    = DCell.ID
        
        inflow0 , SCelldict    = inflow(DCell , time0)
        
        for key in inflow0.keys():
            SCell = SCelldict[key]
            
            if SCell is not None:
                SCellID = SCell.ID
                numflow = inflow0[key]
                if (SCellID , DCellID) in update_cell.keys():
                    update_cell[(SCellID , DCellID)] = numflow
                else:
                    print("Sim_update_UpdateInflow Error " + str(i0) +" " + str(key))

def Sim_update(time0):
#  #=input:
#    output:
#    description:  =#
    # Step 1 : Vehicle Generation
    Sim_update_VehGen(time0)   #done

    if (time0 != 1):
        # Step 2 : Update n (flow)
        Sim_update_UpdateN(time0) #done
        
        # Step 3 : Update Agent to Wait :S,L,R
        Sim_update_VehtoW(time0)    #done
    
        # Step 4 : Update Wait
        Sim_update_UpdateW(time0)   
    
        # Step 5 : Update Cell Speed
        Sim_update_UpdateV(time0) #done
    
    if (time0 != timestep):
        # Step 6 : Update Inter-cell flow (y_i_to_j)
        Sim_update_UpdateInflow(time0) #done
        
    
#    vehlist = [x for x in Veh_Q if x.active]
#    for veh0 in vehlist:
#        sC = [x for x in CellList if veh0 in x.veh_q.straight]
#        lC = [x for x in CellList if veh0 in x.veh_q.left]        
#        rC = [x for x in CellList if veh0 in x.veh_q.right]        
#        wC = [x for x in CellList if veh0 in x.veh_q.wait] 
#        
#        if(len(wC) >0):
#            print("error wait "+str(veh0.ID))
#        
#        C = sC+lC+rC        
#        if(len(C) > 1):
#            print("error")
#        if len(sC) == 1:
#            rel= "S"
#        elif len(lC) == 1:
#            rel= "L"
#        elif len(rC) == 1:
#            rel= "R"
#        
#        
#        Cell0 = C[0]
#        if Cell0 in veh0.route and  Cell0.Rel["out"][rel] in veh0.route:
#            next
#        else:
#            print(veh0.ID)

            
            
        
            
        
        
print("\nVehicle Queue Generation Start")
#if name == "__main__":
Veh_Q = []
for i0 in range(len(TrafficDemand["ID"])):
  demand_id   = TrafficDemand["ID"][i0]
  time_length = TrafficDemand["Length"][i0]
  demand      = TrafficDemand["Demand"][i0]

  if i0 == 1:
    cur_time = 0
  else:
    cur_time = sum(TrafficDemand["Length"][:(i0-1)])


  Veh_Q_temp = Gen_Demand(time_length ,demand , len(Veh_Q) , cur_time)

  Veh_Q += Veh_Q_temp

temp = list(filter(lambda x : x.time == 0 , Veh_Q))
while len(temp) > 0:
    list(filter(lambda x : x.time == 0 , Veh_Q))[0].time = 1
    temp = list(filter(lambda x : x.time == 0 , Veh_Q))


savepath = "RESULT"
if not os.path.exists(savepath):
    os.makedirs(savepath)

writeIntInfo(savepath + "/IntInfoCSV.csv")
writeCellInfo(savepath + "/CellInfoCSV.csv")
writeLinkInfo(savepath + "/LinkInfoCSV.csv")
print("\nGeometry Info saved at "+savepath)

print("\nSimulation Start")
import time
start_time  = time.time()
process = 0
for t in range(1,timestep):
    Sim_update(t)
    if process < np.round(t/timestep*100):
        process= np.round(t/timestep*100)
        print( "\r" +    str(int(np.round(t/timestep*100) )) + " % completed"   , end = "")
    if t == timestep:
        print(    str(int(np.round(t/timestep*100) )) + " % completed"  )
        
        
time_pass = time.time() - start_time
m, s = divmod(time_pass, 60)
print("--- RUNNING TIME :  %02d : %02d  ---" % (m , s))
print("\nSimulation End")
np.savetxt(savepath+"/n_result.csv", n, delimiter=",")
np.savetxt(savepath+"/nagent_result.csv", n_agent, delimiter=",")
np.savetxt(savepath+"/v_result.csv", v, delimiter=",")






#import matplotlib.pyplot as plt
#plt.plot(np.ndarray.flatten(n) , np.ndarray.flatten(n_agent)  ,'ro')
#plt.show()




#
#
#targetLink = [1240010600,1240000303,1240010500,1240010000,1240000202,1240000102,1240038000,1240009900,1240038100,1240000402,1240011902,1240000302,1240012002,1240038300,1240038400,1240028900,1240038800,1240009502,1240009602,1240009501,1240009601,1240010202,1240008900,1240010102,1240009000,1240010203,1240010103,1240039000,1240038900,1240010204,1240010104,1240039200,1240039100,1240040400,1240040500,1240008700,1240008800,1240000203,1240000103,1240008101,1240008201,1240000601,1240000501,1240000602,1240000502,1240012001,1240011901,1240000403]
#result = []
#for l in targetLink:
#    celllist = [x.Cell for x in LinkList if x.ID == l ][0]
#    result += celllist
#
#[x.ID for x in result]


