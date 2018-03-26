# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:34:03 2017

@author: jhsuh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def get_linkrel(path):
    LR_info = pd.read_csv(path)
    LR_Intsec = LR_info['Intersection']
    LR_OLink = LR_info['OLINK']
    LR_DLink = LR_info['DLINK']
    LR_rel = LR_info['Relation']
    return LR_info, LR_Intsec, LR_OLink, LR_DLink, LR_rel

def get_linkrelnode(path):
    NR_info = pd.read_csv(path)
    NR_ID = NR_info['LINK_ID']
    NR_ONode = NR_info['ONode']
    NR_DNode = NR_info['DNode']
    return NR_info, NR_ID, NR_ONode, NR_DNode

def get_link(path):
    L_info = pd.read_csv(path)
    L_ID = L_info['LINK_ID']
    L_x0 = L_info['x0']
    L_y0 = L_info['y0']
    L_x1 = L_info['x1']
    L_y1 = L_info['y1']
    L_NumCell = L_info['NumCell']
    L_Lane = L_info['LANES']
    L_Len = L_info['Length']
    L_CellLen = L_info['CellLen']
#    L_Demand = L_info['Demand']
#    L_Sink = L_info['Sink']
    return L_info, L_ID, L_x0, L_y0, L_x1, L_y1, L_NumCell, L_Lane, L_Len, L_CellLen
#, L_Demand, L_Sink

def get_node(path):
    N_info = pd.read_csv(path)
    N_ID = N_info['ID']
    x = N_info['x']
    y = N_info['y']
    return N_info, N_ID, x, y


def get_intersection(path):
    I_info = pd.read_csv(path)
    I_ID = I_info['ID']
    NS1 = I_info['NS1']
    NS2 = I_info['NS2']
    NS3 = I_info['NS3']
    NS4 = I_info['NS4']
    EW1 = I_info['EW1']
    EW2 = I_info['EW2']
    EW3 = I_info['EW3']
    EW4 = I_info['EW4']
    return I_info, I_ID, NS1, NS2, NS3, NS4, EW1, EW2, EW3, EW4
    
def find_node(NodeList, ID):
    for i in range(len(NodeList)):
        if(NodeList[i].ID[1] == 'O' or NodeList[i].ID[1] == 'D'):
            if(NodeList[i].ID[2:] == ID):
                return NodeList[i]
        else:
            if(NodeList[i].ID[1:] == ID):
                return NodeList[i]
            
def get_cellrel(path):
    Crel_info = pd.read_csv(path)
    Intersec = Crel_info['V1']
    C_O = Crel_info['V2']
    C_D = Crel_info['V3']
    C_qDes = Crel_info['V4']
    return Crel_info, Intersec, C_O, C_D, C_qDes

def get_CellLocDir(IntersectionList):
    for I in IntersectionList:
        inNode = list(filter(lambda x: x == x.Link.DNode, I.Node))
        outNode = list(filter(lambda x: x == x.Link.ONode, I.Node))
        inCellList = []
        outCellList = []
        for N in inNode:
            inCell = list(filter(lambda c: c.x1 == c.Link.DNode.Point[0], N.Link.Cell))
            inCellList += inCell
        for N in outNode:
            outCell = list(filter(lambda c: c.x0 == c.Link.ONode.Point[0], N.Link.Cell))
            outCellList += outCell
        angDic = {'in': {}, 'out': {}}
        angList = []
        for C in inCellList:
            ax = C.y1
            ay = C.x1
            cx = C.y0
            cy = C.x0
            if (ay > cy):
                ang = math.atan((cy - ay)/(cx - ax)) * 180/math.pi
                angList.append(ang)
                angDic['in'][ang] = C
            else:
                ang = 360 - (math.atan((cy - ay)/(cx - ax)) * 180/math.pi)
                angList.append(ang)
                angDic['in'][ang] = C
        angList = sorted(angList)
        j = 1
        for i in range(len(angList)):
            angDic['in'][j] = angDic['in'][angList[i]]
            del angDic['in'][angList[i]]
            j+=1

        angList = []
        for C in outCellList:
            ax = C.y0
            ay = C.x0
            cx = C.y1
            cy = C.x1
            if(cy > ay):
                ang = 360 - math.atan((cy - ay)/(cx - ax)) * 180/math.pi
                angList.append(ang)
                angDic['out'][ang] = C
            else:
                ang = math.atan((cy - ay)/(cx - ax)) * 180/math.pi
                angList.append(ang)
                angDic['out'][ang] = C
        angList = sorted(angList)
        j = 1
        for i in range(len(angList)):
            angDic['out'][j] = angDic['out'][angList[i]]
            del angDic['out'][angList[i]]
            j+=1

        for e in angDic['in']:
            angDic['in'][e].Loc = e
            angDic['in'][e].Dir = 1
        for e in angDic['out']:
            angDic['out'][e].Loc = e
            angDic['out'][e].Dir = 2

        I.Rel = angDic

def get_siginfo(path):
    Signal_info = pd.read_csv(path)
    ID = Signal_info['ID']
    Loc = Signal_info['Loc']
    S = Signal_info['S']
    L = Signal_info['L']
    R = Signal_info['R']
    return Signal_info, ID, Loc, S, L, R
    
def get_siginput(path):
    SignalInput_info = pd.read_csv(path)
    ID = SignalInput_info['ID']
    Offset = SignalInput_info['Offset']
    
    SigList = []
    for SigID0 in SignalInput_info.columns[2:]:
        SigList.append(list(SignalInput_info[SigID0]))
        
    SigID = SignalInput_info.columns[2:]
    
    return SignalInput_info, ID, Offset, SigID , SigList

def get_sig(Intersection, signal_set, time):
    ID = Intersection.Signal[time-1]
    sig = signal_set[str(ID)]
    return sig
    

    
