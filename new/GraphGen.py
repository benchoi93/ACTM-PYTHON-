#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:44:56 2017

@author: sjchoi
"""


import networkx as nx

def Generate_Graph(CellList):
    G = nx.DiGraph()
    for OCell in CellList:
        for key , DCell in OCell.Rel["out"].items():
            if DCell is not None:
                OCellNum = CellList.index(OCell)
                DCellNum = CellList.index(DCell)
                
                G.add_edge(OCellNum , DCellNum)

    return G