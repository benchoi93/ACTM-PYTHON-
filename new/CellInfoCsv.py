

import csv


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



#########################################################################################################3
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