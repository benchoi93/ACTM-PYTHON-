# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:44:13 2017

@author: jhsuh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:27:45 2017

@author: jhsuh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import new.NewDefClass as cl
from new.GangDongCellInfoFtn import *

def NewCellInfo(cellrelpath, intersecpath, linkrelpath, linkpath, nodepath, linkrelnodepath, siginfopath, siginputpath):
    L_info, L_ID, L_x0, L_y0, L_x1, L_y1, L_NumCell, L_Lane, L_Len, L_CellLen = get_link(linkpath)
#    , L_Demand, L_Sink

    LinkList = []
    for i in range(len(L_ID)):
        ID = L_ID[i]
        x0 = L_x0[i]
        y0 = L_y0[i]
        x1 = L_x1[i]
        y1 = L_y1[i]
        NumCell = L_NumCell[i]
        CellLen = L_CellLen[i]
        Lane = L_Lane[i]
        Len = L_Len[i]
#        Demand = L_Demand[i]
#        Sink = L_Sink[i]
        global Link
        L = cl.Link(ID, x0, y0, x1, y1, NumCell, CellLen, Lane, Len)
#                 , Demand, Sink)
        LinkList.append(L)
    

    N_info, N_ID, x, y = get_node(nodepath)
    NodeList = []
    for i in range(len(N_ID)):
        check = 0
        for j in range(len(LinkList)):
            if(LinkList[j].O[0] == x[i]):
                if(LinkList[j].O[1] == y[i]):
                    check = 1
                    ID = 'O'
                    NID = str(N_ID[i])
                    Link = LinkList[j]
                    N = cl.Node(ID, NID, Link)
                    LinkList[j].ONode = N
                    NodeList.append(N)
                    break
                    
            elif(LinkList[j].D[0] == x[i]):
                if(LinkList[j].D[1] == y[i]):
                    check = 1
                    ID = 'D'
                    NID = str(N_ID[i])
                    Link = LinkList[j]
                    N = cl.Node(ID, NID, Link)
                    LinkList[j].DNode = N
                    NodeList.append(N)
                    break
        if(check == 0):
            ID = None
            NID = str(N_ID[i])
            Link = (x[i], y[i])
            N = cl.Node(ID, NID, Link)
            NodeList.append(N)
            
#    get_siginfo(signalsetpath) = Siganl_info, Int, Loc, S, L, R
#    signalList = {}
#    for i in range(len(Signal_info)):
#        if str(Int[i]) in signalList:
#            signalList[str(Int[i])][str(Loc[i])] = [S[i], L[i], R[i]]
#        else:
#            signalList[str(Int[i])] = {}
#            signalList[str(Int[i])][str(Loc[i])] = [S[i], L[i], R[i]]

    I_info, I_ID, NS1, NS2, NS3, NS4, EW1, EW2, EW3, EW4 = get_intersection(intersecpath)
    
    IntersectionList = []
    for i in range(len(I_info)):
        IntersecNode = []
        x = 0
        y = 0
        if(NS1[i] != 0):
            N = find_node(NodeList, str(NS1[i]))
            N.Pos = 'NS'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(NS2[i] != 0):
            N = find_node(NodeList, str(NS2[i]))
            N.Pos = 'NS'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(NS3[i] != 0):
            N = find_node(NodeList, str(NS3[i]))
            N.Pos = 'NS'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(NS4[i] != 0):
            N = find_node(NodeList, str(NS4[i]))
            N.Pos = 'NS'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(EW1[i] != 0):
            N = find_node(NodeList, str(EW1[i]))
            N.Pos = 'EW'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(EW2[i] != 0):
            N = find_node(NodeList, str(EW2[i]))
            N.Pos = 'EW'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(EW3[i] != 0):
            N = find_node(NodeList, str(EW3[i]))
            N.Pos = 'EW'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        if(EW4[i] != 0):
            N = find_node(NodeList, str(EW4[i]))
            N.Pos = 'EW'
            x += int(N.Point[0])
            y += int(N.Point[1])
            IntersecNode.append(N)
        
        x = x/len(IntersecNode)
        y = y/len(IntersecNode)
#        Signal = signalList[str(I_ID[i])]
        Signal0 = None
        I = cl.Intersection(I_ID[i], IntersecNode, Signal0, x, y)
        for j in IntersecNode:
            j.Intsec = I            
        IntersectionList.append(I)
        
    

    
    
    LR_info, LR_Intsec, LR_OLink, LR_DLink, LR_rel = get_linkrel(linkrelpath)
    
    curint = 651
    IntersecNode = []
#    for i in range(8):
    for i in range(len(LR_info)):
        if(curint != LR_Intsec[i]):
            x = 0
            y = 0
            for n in IntersecNode:
                x+=int(n.Point[0])
                y+=int(n.Point[1])
            x = x/len(IntersecNode)
            y = y/len(IntersecNode)
            signal0 = None
            I = cl.Intersection(curint, IntersecNode, signal0, x, y)
            for n in IntersecNode:
                n.Intsec = I
            IntersectionList.append(I)
                
            IntersecNode = []
            curint = LR_Intsec[i]

        OLink = list(filter(lambda x: x.ID == LR_OLink[i], LinkList))[0]
        DLink = list(filter(lambda x: x.ID == LR_DLink[i], LinkList))[0]
        
        if(OLink.DNode == DLink.ONode):
            
            Node1 = cl.Node('D', str(curint)+'1', OLink)
            Node2 = cl.Node('O', str(curint)+'0', DLink)
            Node1.ID += '1'
            Node2.ID += '0'
          
            NodeList.append(Node1)
            NodeList.append(Node2)
            OLink.DNode = Node1
            DLink.ONode = Node2
            IntersecNode.append(OLink.DNode)
            IntersecNode.append(DLink.ONode)
            
        elif(OLink.DNode == None):
            Node1 = cl.Node('D', DLink.ONode.ID[2:]+'1', OLink)
            NodeList.append(Node1)
            OLink.DNode = Node1
            IntersecNode.append(OLink.DNode)
            if(DLink.ONode not in IntersecNode): 
                DLink.ONode.ID += '0'
                IntersecNode.append(DLink.ONode)

        elif(DLink.ONode == None):
            Node2 = cl.Node('O',OLink.DNode.ID[2:]+'0', DLink)
            NodeList.append(Node2)
            DLink.ONode = Node2
            IntersecNode.append(DLink.ONode)
            if(OLink.DNode not in IntersecNode):
                OLink.DNode.ID += '1'
                IntersecNode.append(OLink.DNode)
            
        if(LR_rel[i] == 1):
            OLink.DNode.Rel['out']['S'] = DLink.ONode
            DLink.ONode.Rel['in']['S']  = OLink.DNode
        elif(LR_rel[i] == 2):
            OLink.DNode.Rel['out']['L'] = DLink.ONode
            DLink.ONode.Rel['in']['L']  = OLink.DNode
        elif(LR_rel[i] == 3):
            OLink.DNode.Rel['out']['R'] = DLink.ONode
            DLink.ONode.Rel['in']['R']  = OLink.DNode
    x = 0
    y = 0
    for n in IntersecNode:
        x+=int(n.Point[0])
        y+=int(n.Point[1])
    x = x/len(IntersecNode)
    y = y/len(IntersecNode)
    signal0 = None
    I = cl.Intersection(curint, IntersecNode, signal0, x, y)
    for n in IntersecNode:
        n.Intsec = I
    IntersectionList.append(I)


        
        
        
    

#    
#    
#    for i in range(len(LR_info)):
#        for j in LinkList:
#            if(j.ID == LR_OLink[i]):
#                if(LR_rel[i] == 1):
#                    j.DNode.Rel['out']['S'] = list(filter(lambda x: x.ID == LR_DLink[i], LinkList))[0].ONode
#                elif(LR_rel[i] == 2):
#                    j.DNode.Rel['out']['L'] = list(filter(lambda x: x.ID == LR_DLink[i], LinkList))[0].ONode
#                elif(LR_rel[i] == 3):
#                    j.DNode.Rel['out']['R'] = list(filter(lambda x: x.ID == LR_DLink[i], LinkList))[0].ONode
#
#
##                LRel = [LR_DLink[i], 0, LR_rel[i]]
##                j.LRel.append(LRel)
#
#            elif(j.ID == LR_DLink[i]):
#                if(LR_rel[i] == 1):
#                    j.ONode.Rel['in']['S'] = list(filter(lambda x: x.ID == LR_OLink[i], LinkList))[0].DNode
#                elif(LR_rel[i] == 2):
#                    j.ONode.Rel['in']['L'] = list(filter(lambda x: x.ID == LR_OLink[i], LinkList))[0].DNode
#                elif(LR_rel[i] == 3):
#                    j.ONode.Rel['in']['R'] = list(filter(lambda x: x.ID == LR_OLink[i], LinkList))[0].DNode
##                LRel = [LR_OLink[i], 1, LR_rel[i]]
##                j.LRel.append(LRel)

#    NR_info, NR_ID, NR_ONode, NR_DNode = get_linkrelnode(linkrelnodepath)
#    for i in range(len(NR_info)):
#        LinkList_filtered = [x for x in LinkList if x.ID in NR_ID]
#        for j in LinkList:
#            if(j.ID == NR_ID[i]):
#                ONode = find_node(NodeList, str(NR_ONode[i]))
#                DNode = find_node(NodeList, str(NR_DNode[i]))
#                j.ONode = ONode
#                j.DNode = DNode
#                break
    
    CellList = []
    for i in range(len(LinkList)):
        
        for j in range(LinkList[i].NumCell):
            ID = str(j+1)
            CellLen = LinkList[i].CellLen
            NumCell = LinkList[i].NumCell
            Link = LinkList[i]
            C = cl.Cell(ID, CellLen, NumCell, Link)
            CellList.append(C)
            Link.Cell.append(C)

            
    Crel_info, Intersec, C_O, C_D, C_qDes = get_cellrel(cellrelpath)
    for i in range(len(Crel_info)):
        ONode = find_node(NodeList, str(C_O[i]))
        DNode = find_node(NodeList, str(C_D[i]))
        
        if(C_qDes[i] == 1):
            ONode.Rel['out']['S'] = DNode
            ONode.Link.NRel['out']['S'] = [ONode, DNode]
            DNode.Rel['in']['S'] = ONode
            DNode.Link.NRel['in']['S'] = [DNode, ONode]
        elif(C_qDes[i] == 2):
            ONode.Rel['out']['L'] = DNode
            ONode.Link.NRel['out']['L'] = [ONode, DNode]
            DNode.Rel['in']['L'] = ONode
            DNode.Link.NRel['in']['L'] = [DNode, ONode] 
        elif(C_qDes[i] == 3):
            ONode.Rel['out']['R'] = DNode
            ONode.Link.NRel['out']['R'] = [ONode, DNode]
            DNode.Rel['in']['R'] = ONode
            DNode.Link.NRel['in']['R'] = [DNode, ONode]
            
    for i in range(len(CellList)):
        c= CellList[i]
        if(len(c.Int) == 0):
            if(int(c.Ind) > 1 and int(c.Ind) < c.Link.NumCell):
                c.Rel['in']['S'] = CellList[i-1]
                c.Rel['out']['S'] = CellList[i+1]
            elif(c.Ind == '1'):
                c.Rel['out']['S'] = CellList[i+1]
            elif(c.Ind == str(c.Link.NumCell)):
                c.Rel['in']['S'] = CellList[i-1]
        else:
            if(str(c.Link.NumCell) == '1'):
                if c.Link.ONode.Rel['in']['S'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['S'].Link
                    c.Rel['in']['S'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                if c.Link.ONode.Rel['in']['L'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['L'].Link
                    c.Rel['in']['L'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                if c.Link.ONode.Rel['in']['R'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['R'].Link
                    c.Rel['in']['R'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                if c.Link.DNode.Rel['out']['S'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['S']
                    c.Rel['out']['S'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                if c.Link.DNode.Rel['out']['L'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['L']
                    c.Rel['out']['L'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                if c.Link.DNode.Rel['out']['R'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['R']
                    c.Rel['out']['R'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                
            elif(c.Ind == '1'):
                if c.Link.ONode.Rel['in']['S'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['S'].Link
                    c.Rel['in']['S'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                if c.Link.ONode.Rel['in']['L'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['L'].Link
                    c.Rel['in']['L'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                if c.Link.ONode.Rel['in']['R'] is not None:
                    sourceLink = c.Link.ONode.Rel['in']['R'].Link
                    c.Rel['in']['R'] = list(filter( lambda x : x.Ind == str(sourceLink.NumCell) ,  sourceLink.Cell))[0]
                c.Rel['out']['S'] = CellList[i+1]
            elif(c.Ind == str(c.Link.NumCell)):
#                c.Rel['out']['S'] = c.Link.DNode.Rel['out']['S']
#                c.Rel['out']['L'] = c.Link.DNode.Rel['out']['L']
#                c.Rel['out']['R'] = c.Link.DNode.Rel['out']['R']
                
                if c.Link.DNode.Rel['out']['S'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['S']
                    c.Rel['out']['S'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                if c.Link.DNode.Rel['out']['L'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['L']
                    c.Rel['out']['L'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                if c.Link.DNode.Rel['out']['R'] is not None:
                    ReceiveCell = c.Link.DNode.Rel['out']['R']
                    c.Rel['out']['R'] = list(filter( lambda x : x.Ind == "1" ,  ReceiveCell.Link.Cell))[0]
                c.Rel['in']['S'] = CellList[i-1]
                    
            
        
    get_CellLocDir(IntersectionList)
    
    
    Signal_info, ID, Loc, S, L, R = get_siginfo(siginfopath) 
    signal_set = {}
    for i in range(len(Signal_info)):
        signal = cl.Signal(ID[i], [S[i], L[i], R[i]])
        if not(str(ID[i]) in signal_set) :
            signal_set[str(ID[i])] = {}
        signal_set[str(ID[i])][str(Loc[i])] = signal


    return LinkList, NodeList , CellList , IntersectionList, signal_set

