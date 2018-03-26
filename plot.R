


Cellcoord = read.csv("CellInfoCSV.csv")
Linkcoord = read.csv("LinkInfoCSV.csv")
Intecoord = read.csv("temp.csv")
Intecoord = t(Intecoord)
Intecoord = data.frame(Intecoord)
colnames(Intecoord) = c("ID" , "x","y")
Intecoord = Intecoord[-1,]

library(ggplot2)
ggplot() + 
  geom_segment(data = Cellcoord , aes( x=x0,y=y0,xend=x1,yend=y1, color = factor(ID %in% c("C12300367011" , "C12400080061" , "C12400093009", "C12400091001"))) , arrow = arrow(length=unit(0.2, "cm"))  ) + guides(color = F)

ggplot() +
  geom_segment(data = Cellcoord , aes( x=x0,y=y0,xend=x1,yend=y1, color = factor(ID %in% c( "C12400096022" ,"C12400100002","","C12400106001"))) , arrow = arrow(length=unit(0.2, "cm"))  ) + 
  guides(color = F) + 
  geom_text(data = Intecoord , aes(label = (ID) , x = x , y = y))








link  =c('C12400407001',
         'C12400407002',
         'C12400407003',
         'C12400407004',
         'C12400407005',
         'C12400407006',
         'C12400407007',
         'C12400407008',
         'C12400007031',
         'C12400007032',
         'C12400007033',
         'C12400007034',
         'C12400007035',
         'C12400007036',
         'C12400007037',
         'C12400007021',
         'C12400007022',
         'C12400001031',
         'C12400001032',
         'C12400001033',
         'C12400001034',
         'C12400001035',
         'C12400001036',
         'C12400001021',
         'C12400001022',
         'C12400004021',
         'C12400004022',
         'C12400004031',
         'C12400004032',
         'C12400006011',
         'C12400006021',
         'C12400006022',
         'C12400006023',
         'C12400006024',
         'C12400006025',
         'C12400006026',
         'C12400006031',
         'C12400006032',
         'C12400006033',
         'C12400010011',
         'C12400010012',
         'C12400010013',
         'C12400010031',
         'C12400014051',
         'C12400014041',
         'C12400014042',
         'C12400014043',
         'C12400014044',
         'C12400014045',
         'C12400014046',
         'C12400014047',
         'C12400014048',
         'C12400014049',
         'C124000140410',
         'C124000140411',
         'C124000140412',
         'C124000140413',
         'C124000140414',
         'C124000140415',
         'C124000140416') 
ggplot() + 
  geom_segment(data = Cellcoord , aes( x=x0,y=y0,xend=x1,yend=y1, color = factor(ID %in% link)) , arrow = arrow(length=unit(0.2, "cm"))  ) + guides(color = F)



ggplot() + geom_segment(data = Linkcoord , aes( x=x0,y=y0,xend=x1,yend=y1, color = factor(ID == 1240001404)) , arrow = arrow(length=unit(0.2, "cm"))  )   +guides(color = F)
ggplot() + geom_segment(data = Linkcoord , aes( x=x0,y=y0,xend=x1,yend=y1, color = factor(ID %in% c(1240039600,1240009702))) , arrow = arrow(length=unit(0.2, "cm"))  )   +guides(color = F)




library(ggplot2)
temp = ggplot() + geom_segment(data = Linkcoord , aes( x=x0,y=y0,xend=x1,yend=y1) , arrow = arrow(length=unit(0.2, "cm"))  )   + geom_text(data= Linkcoord , aes(x=(x1+x0)/2,y=(y1+y0)/2,label=num,angle= atan((y0-y1)/(x0-x1)) * 180 / pi  ) , color  = "red" , size = 3)
ggsave("temp.pdf",temp , width = 30 , height= 30)






