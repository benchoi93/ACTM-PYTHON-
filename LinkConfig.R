


dir.create("PLOT",showWarnings = F)



Linkcoord = read.csv("RESULT/LinkInfoCSV.csv")
Intecoord = read.csv("RESULT/IntInfoCSV.csv")

LinkPlot = ggplot() + geom_segment(data = Linkcoord , aes( x=x0,y=y0,xend=x1,yend=y1) ,arrow = arrow(length=unit(0.2, "cm"))  ) + guides(color = F) + geom_text(data = Intecoord , color = "blue",aes(label = (ID) , x = x , y = y))
ggsave("PLOT/LinkPlot.png",LinkPlot , width  = 20 , heigh = 20)



