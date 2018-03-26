# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:50:04 2017

@author: jhsuh
"""


import numpy as np
from new.Global import dt, qmax , vehlength

class Link:
    def __init__(self, ID, x0, y0, x1, y1, NumCell, CellLen, Lane, Len):
#                 , Demand, Sink):
        self.ID      = ID
        self.O       = (x0, y0)
        self.D       = (x1, y1)
        
        if(CellLen != 0):
            if(Len < CellLen):
                CellLen = Len
            self.NumCell = int(Len / CellLen)
            self.CellLen = CellLen
        else:
            self.NumCell = NumCell
            self.CellLen = Len/NumCell
        self.Lane    = Lane
        self.Len     = Len
        self.Demand  = True
        self.Sink    = True
        self.ONode   = None
        self.DNode   = None
        self.NRel = {'in' : {'S' : None, 'L' : None, 'R' : None}, 'out' : {'S' : None, 'L' : None, 'R' : None}}
        self.Cell = []
        self.info = "ID, O, D, NumCell, CellLen, Lane, Len, Demand, Sink, ONode, DNode, NRel, LRel, Cell"

class Node:
    def __init__(self, ID, NID, Link):
        if (ID == 'O'):
            self.ID = 'N'+ 'O' + NID
            self.Point = Link.O
            self.Link   = Link
        elif (ID == 'D'):
            self.ID = 'N'+ 'D' + NID
            self.Point = Link.D
            self.Link   = Link
        elif (ID == None):
            self.ID = 'N'+ NID
            self.Point = Link
            self.Link = None
        self.Intsec = None
        self.Pos = None
        self.Rel = {'in' : {'S' : None, 'L' : None, 'R' : None}, 'out' : {'S' : None, 'L' : None, 'R' : None}}
        self.info = "ID, Point, Link, Intsec, Pos, Rel"
        
class Intersection:
    def __init__(self,ID, Node, Signal, xPoint, yPoint):
        self.ID     = ID
        self.Node   = Node
        self.Lnum   = len(Node)
        self.Signal = Signal
        self.xPoint = xPoint
        self.yPoint = yPoint
        self.Rel = {}
        self.info = "ID, Node, Lnum, Signal, xPoint, yPoint, Rel"
    def get_curSig(self, time0): 
        return self.Signal[time0-1]
        
class Cell:
##=ID: index of each cell
#  Length: length of one cell
#  Lane: size of the lane
#  NetIn: indicates if the cell gets flow
#  NetOut: indicates if the cell gives flow
#  Int: indicates if the cell directly connected with intersection (Int 'ID of intersection')
#  Loc: indicates location of the cell at intersection reference (Int '1' or '2' or '3' or '4')
#  Dir: indicates direction of the cell (Int '1' or '2' or '3' or '4')
#  S_in: indicates if other cell goes straight to the cell (Int '0' or 'ID of other Cell')
#  L_in: indicates if other cell turn left to the cell (Int '0' or 'ID of other Cell')
#  R_in: indicates if other cell turn right to the cell (Int '0' or 'ID of other Cell')
#  S_out: indicates if other cell goes straight ahead from the cell (Int '0' or 'ID of other Cell')
#  L_out: indicates if other cell turn left ahead from the cell (Int '0' or 'ID of other Cell')
#  R_out: indicates if other cell turn right ahead from the cell (Int '0' or 'ID of other Cell')
#  x: indicates the start of the horizontal arrow in the figure (float64)
#  y: indicates the start of the vertical arrow in the figure (float64)
#  xend: indicates the end of the horizontal arrow in the figure (float64)
#  yend: indicates the end of the vertical arrow in the figure (float64)=#
    def __init__(self, ID, CellLen, NumCell, Link):
        self.ID = 'C'+str(Link.ID)+ID
        self.Ind = ID
        self.Len = min(Link.Len , CellLen)
        xlen = (self.Len / Link.Len)*abs(Link.ONode.Point[0]-Link.DNode.Point[0])
        ylen = (self.Len / Link.Len)*abs(Link.DNode.Point[1]-Link.ONode.Point[1])
        xlenL = np.repeat(xlen, NumCell)
        ylenL = np.repeat(ylen, NumCell)
        if (sum(xlenL) != abs(Link.ONode.Point[0]-Link.DNode.Point[0])):
            xlenL[-1] += abs(Link.ONode.Point[0]-Link.DNode.Point[0]) - sum(xlenL)
        if (sum(ylenL) != abs(Link.DNode.Point[1]-Link.ONode.Point[1])):
            ylenL[-1] += abs(Link.DNode.Point[1]-Link.ONode.Point[1]) - sum(ylenL)
        xlenLCum = [0] + list(np.cumsum(xlenL))
        ylenLCum = [0] + list(np.cumsum(ylenL))
            
        self.Lane = Link.Lane
        self.Link = Link
        
#        
#        if(ID == '1'):
#            self.Int = self.Link.ONode.Intsec
#        elif (ID == str(Link.NumCell)):
#            self.Int = self.Link.DNode.Intsec
#        else:
#            self.Int = None
#            
            
        self.Int = []
        if(ID == '1'):
            self.Int.append(self.Link.ONode.Intsec)
        if (ID == str(Link.NumCell)):
            self.Int.append(self.Link.DNode.Intsec)
            
        while None in self.Int:
            self.Int.remove(None)
            
        self.NetIn = len(self.Int) == 0
        self.NetOut = len(self.Int) == 0
        
        
        self.Loc = 0 #1,2,3,4,5,
        self.Dir = 0 #in out
        #out(2): 나가는, in(1): 들어오는
        self.Rel = {'in' : {'S' : None, 'L' : None, 'R' : None}, 'out' : {'S' : None, 'L' : None, 'R' : None}} ##dic
#        self.rx0 = Link.O[0] + (int(ID)-1)*self.Len
#        self.ry0 = Link.D[1] + (int(ID)-1)*self.Len
#        self.rx1 = Link.O[0] + int(ID)*self.Len
#        self.ry1 = Link.D[1] + int(ID)*self.Len
        #x
        if(Link.ONode.Point[0]>Link.DNode.Point[0]): #O>D
            self.x0 = Link.O[0] - xlenLCum[int(ID) - 1]
            self.x1 = Link.O[0] - xlenLCum[int(ID) ]
        else: #D>O
            self.x0 = Link.O[0] + xlenLCum[int(ID) - 1]
            self.x1 = Link.O[0] + xlenLCum[int(ID)]
        #y
        if(Link.ONode.Point[1]>Link.DNode.Point[1]): #O>D
            self.y0 = Link.O[1] - ylenLCum[int(ID) - 1]
            self.y1 = Link.O[1] - ylenLCum[int(ID)]
        else: #D>O
            self.y0 = Link.O[1] + ylenLCum[int(ID) - 1]
            self.y1 = Link.O[1] + ylenLCum[int(ID)]
            
        
        self.veh_q = VehQ() #striaight, left, right, wait
        self.info = "ID, Len, Lane, NetIn, NetOut, Int, Rel, rx0, ry0, rx1, ry1, x0, y0, x1, y1, Link, veh_q"
    def get_Q(self):
        return qmax * self.Lane / 3600 * dt
    
    def get_CellMaxVeh(self):###Cell안의 ftn
        maxveh = self.Len/vehlength * self.Lane ######make vehlength!!
        return maxveh

    
        
class VehQ:
    def __init__(self):
        self.straight = []
        self.left = []
        self.right = []
        self.wait = []
        self.info = "straight, left, right, wait"
    
    def get_Num(self):
        return (len(self.straight) , len(self.left) ,len(self.right) , len(self.wait))
        
    def add_veh(self, Veh, Rel):
        if Rel == "S":
            self.straight.append(Veh)
        elif Rel == "L":
            self.left.append(Veh)
        elif Rel == "R":
            self.right.append(Veh)
        elif Rel == "W":
            self.wait.append(Veh)
        else:
            print("Error VehQ Rel wrong")
        
        
        
class Veh:
    def __init__(self, ID, Ocell, Dcell, time):
        self.ID = ID
        self.O_cell = Ocell
        self.D_cell = Dcell
        self.time = time
        self.route = None
        self.info = "ID, O_cell, D_cell, time, route"
        self.active = False
        self.Endtime = time

class Signal:
    def __init__(self, ID, signal):
        self.ID = ID
        self.signal = signal
        self.info = "ID, signal"


        


    

            
        
        
        
        
        
        