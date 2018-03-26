# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:18:06 2017

@author: jhsuh
"""

import os
import networkx as nx
import numpy as np

from new.GangDongCellInfo import *
import new.GraphGen
from new.Global import *

#
#pathl = "C:/Users/jhsuh/Desktop/JuliaToPython/LINKINPUT.csv"
#pathi = "C:/Users/jhsuh/Desktop/JuliaToPython/INTERSECTIONINPUT1.csv"

#pathl = "/Users/sjchoi/Google Drive/Julia/JuliaToPython/LINKINPUT.csv"
#pathi = "/Users/sjchoi/Google Drive/Julia/JuliaToPython/INTERSECTIONINPUT1.csv"

#wd = "C:/Users/jhsuh/Desktop/JuliaToPython/"

wd = os.getcwd() + "/"

cellrelpath = wd + "Cell_rel1.csv"
intersecpath = wd + "Intersection_GangDong.csv"
linkrelpath = wd + "Intersection65_New.csv"
linkpath = wd + "GangDong_Linkstudy5.csv"
nodepath = wd + "node_coord.csv"
linkrelnodepath = wd + "Intersection65_NodeInfo.csv"
siginfopath = wd + "signalinfo.csv"
siginputpath = wd + "SignalInput.csv"


LinkList, NodeList , CellList , IntersectionList, SignalList = NewCellInfo(cellrelpath, intersecpath, linkrelpath, linkpath, nodepath, linkrelnodepath, siginfopath, siginputpath)

NumCell = len(CellList)

n , yin, yout, v, n_agent, update_cell, DCell_set = Generate_Format(CellList, timestep)

G = new.GraphGen.Generate_Graph(CellList)



def Set_Intersection_Signal(siginputpath):
    global IntersectionList
    global timestep
    global dt

    SignalInput_info, ID, Offset, SigID, SigList = get_siginput(siginputpath)
    
    ID = list(ID)
    SigID = list(SigID)
    
    for i in range(len(IntersectionList)):
        Iid = IntersectionList[i].ID
        Iindex = ID.index(Iid)
        
        ISignal = SignalInput_info.iloc[Iindex]
        
        IOffset = ISignal['Offset']/dt

        summ = 0
        Signalset = []
        for j in SigID:
            summ += (ISignal[j])
            if(ISignal[j] != 0):
                Signalset.append(j)
            
            
        totallen = (summ)/dt
        
        rep0 = np.ceil((timestep + IOffset) / totallen)

        signal = []        
        for r in range(int(rep0)):
            for j in SigID:
                siglen =ISignal[j]
                if siglen != 0:
                    for n in range(int(siglen/dt)):
                        signal.append(j)
        signal0 = signal[int(IOffset): (int(IOffset+timestep))]
                
        IntersectionList[i].Signal = signal0 
        

Set_Intersection_Signal(siginputpath)

DemandCell = list(filter(lambda x : x.NetIn , CellList))
SinkCell   = list(filter(lambda x : x.NetOut , CellList))

ODpair = []
for OCell in DemandCell:
    OCellnum = CellList.index(OCell)    
    for DCellnum in nx.descendants(G, OCellnum):
        DCell = CellList[DCellnum]
        if DCell in SinkCell:
            ODpair.append((OCell, DCell))
        
OD_matrix = np.zeros((len(DemandCell) , len(SinkCell) ))
for i0 in range(len(ODpair)):
    origin = DemandCell.index(ODpair[i0][0])
    destin = SinkCell.index(ODpair[i0][1])
    OD_matrix[origin , destin] = 1
    
#
#amp_O = [473 , 384]
#amp_D = [734, 137, 336]
#amp_scale = 10
#
#for i0 in amp_O:
#    for j0 in amp_D:
#        OD_matrix[DemandCell.index(CellList[i0]) ,SinkCell.index(CellList[j0])] *= amp_scale

OD_matrix[ DemandCell.index([x for x in LinkList if x.ID == 1240040700][0].Cell[0])  , SinkCell.index([x for x in LinkList if x.ID == 1240001404][0].Cell[-1]) ]  = 1000
OD_matrix[ DemandCell.index([x for x in LinkList if x.ID == 1240001302][0].Cell[0])  , SinkCell.index([x for x in LinkList if x.ID == 1240040600][0].Cell[-1]) ]  = 1000



VehOutList = []