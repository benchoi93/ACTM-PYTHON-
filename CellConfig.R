


dir.create("PLOT",showWarnings = F)



Cellcoord = read.csv("RESULT/CellInfoCSV.csv")
Intecoord = read.csv("RESULT/IntInfoCSV.csv")

CellPlot = ggplot() + geom_segment(data = Cellcoord , aes( x=x0,y=y0,xend=x1,yend=y1) ,arrow = arrow(length=unit(0.2, "cm"))  ) + guides(color = F) + geom_text(data = Intecoord , color = "blue",aes(label = (ID) , x = x , y = y))
ggsave("PLOT/CellPlot.png",CellPlot , width  = 20 , heigh = 20)
