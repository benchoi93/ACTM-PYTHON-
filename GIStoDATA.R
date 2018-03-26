


temp = read.csv("GangDong_Link.csv")
temp2 = temp[25:29]

library(ggplot2)
ggplot(temp2 , aes(x = x0 , y = y0 , xend = x1 , yend = y1)) + geom_segment(arrow = arrow(length=unit(0.2, "cm")) ) 
minmin



gen_rel = function(input){
  ns1 = input[1]
  ns2 =input[2]
  ns3 =input[3]
  ns4 =input[4]
  ew1 =input[5]
  ew2 =input[6]
  ew3 =input[7]
  ew4 =input[8]
  
  result = matrix(c(ns1,ns2,1,
           ns3,ns4,1,
           ew1,ew2,1,
           ew3,ew4,1,
           ns3,ew2,2,
           ew1,ns2,2,
           ns1,ew4,2,
           ew3,ns4,2,
           ns3,ew4,3,
           ew1,ns4,3,
           ns1,ew2,3,
           ew3,ns2,3),ncol=3,byrow = T)
  temp = c()
  for(i in 1:length(result[,1])){
    if(!(0 %in% result[i,])){
      temp = append(temp,i)
    }
  }
  result = result[temp,]
  return(result)
}

gen_rel(271, 568,276,565,268,284,545,281)
gen_rel(527,538,534,541,246,0,0,247)

gen_rel(c(0	,572,	569,	0,	292,	287,	286,	290))



inter = read.csv("intersection_Gangdong.csv")
result = c()
for(i0 in 1:length(inter[,1])){
  interID = inter[i0,1]
  reltable = gen_rel(inter[i0,2:9])
  
  result = rbind(result , cbind(interID, reltable))
}
temp = unlist(result)
result = matrix(temp , ncol = 4)
write.csv(result , "Cell_rel1.csv")





nodeID = unique(as.vector(as.matrix(inter[,2:9])))
nodeID = nodeID[which(nodeID != 0)]
nodeID = nodeID[order(nodeID)]



temp = rep(0,644)
temp[nodeID] = 1


node = read.csv("node_coord.csv")
node = cbind(node, temp)
write.csv(node,"node_coord.csv")
