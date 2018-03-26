n = read.csv("RESULT/n_result.csv",header = F)
nagent = read.csv("RESULT/nagent_result.csv",header =F)
v = read.csv("RESULT/v_result.csv",header =F)
Cellcoord = read.csv("RESULT/CellInfoCSV.csv")
Cell0  = Cellcoord[,c("ID" , "Lane","x0","y0","x1","y1")]
Cell0 = cbind(Cell0, nresult = 0 , vresult = 0 ,nagent = 0 )

timestep = dim(n)[2]
vf = max(v)

library(doParallel)
library(foreach)


dir.create("RESULT/Plot_agent" , showWarnings = F)
dir.create("RESULT/Plot_agent1" , showWarnings = F)
# 
# for (time0 in 1:timestep){
#   
# 
#     
#     
#   
# }


targetCell = c('C12400106001',
  'C12400106002',
  'C12400106003',
  'C12400106004',
  'C12400106005',
  'C12400106006',
  'C12400106007',
  'C12400106008',
  'C12400106009',
  'C124001060010',
  'C12400003031',
  'C12400003032',
  'C12400105001',
  'C12400105002',
  'C12400105003',
  'C12400105004',
  'C12400105005',
  'C12400105006',
  'C12400105007',
  'C12400105008',
  'C12400105009',
  'C124001050010',
  'C12400100001',
  'C12400100002',
  'C12400002021',
  'C12400002022',
  'C12400001021',
  'C12400001022',
  'C12400380001',
  'C12400380002',
  'C12400380003',
  'C12400099001',
  'C12400099002',
  'C12400381001',
  'C12400381002',
  'C12400381003',
  'C12400004021',
  'C12400004022',
  'C12400119021',
  'C12400119022',
  'C12400119023',
  'C12400119024',
  'C12400119025',
  'C12400003021',
  'C12400003022',
  'C12400120021',
  'C12400120022',
  'C12400120023',
  'C12400120024',
  'C12400120025',
  'C12400383001',
  'C12400383002',
  'C12400384001',
  'C12400384002',
  'C12400289001',
  'C12400289002',
  'C12400388001',
  'C12400388002',
  'C12400095021',
  'C12400095022',
  'C12400096021',
  'C12400096022',
  'C12400095011',
  'C12400095012',
  'C12400096011',
  'C12400096012',
  'C12400102021',
  'C12400089001',
  'C12400089002',
  'C12400089003',
  'C12400089004',
  'C12400089005',
  'C12400089006',
  'C12400089007',
  'C12400089008',
  'C12400101021',
  'C12400090001',
  'C12400090002',
  'C12400090003',
  'C12400090004',
  'C12400090005',
  'C12400090006',
  'C12400090007',
  'C12400090008',
  'C12400102031',
  'C12400102032',
  'C12400102033',
  'C12400101031',
  'C12400101032',
  'C12400101033',
  'C12400390001',
  'C12400390002',
  'C12400389001',
  'C12400389002',
  'C12400102041',
  'C12400102042',
  'C12400102043',
  'C12400102044',
  'C12400102045',
  'C12400102046',
  'C12400101041',
  'C12400101042',
  'C12400101043',
  'C12400101044',
  'C12400101045',
  'C12400101046',
  'C12400392001',
  'C12400392002',
  'C12400391001',
  'C12400391002',
  'C12400404001',
  'C12400404002',
  'C12400404003',
  'C12400404004',
  'C12400404005',
  'C12400404006',
  'C12400405001',
  'C12400405002',
  'C12400405003',
  'C12400405004',
  'C12400405005',
  'C12400405006',
  'C12400087001',
  'C12400087002',
  'C12400087003',
  'C12400087004',
  'C12400087005',
  'C12400087006',
  'C12400088001',
  'C12400088002',
  'C12400088003',
  'C12400088004',
  'C12400088005',
  'C12400088006',
  'C12400002031',
  'C12400002032',
  'C12400002033',
  'C12400002034',
  'C12400002035',
  'C12400002036',
  'C12400001031',
  'C12400001032',
  'C12400001033',
  'C12400001034',
  'C12400001035',
  'C12400001036',
  'C12400081011',
  'C12400081012',
  'C12400081013',
  'C12400081014',
  'C12400081015',
  'C12400081016',
  'C12400081017',
  'C12400081018',
  'C12400082011',
  'C12400082012',
  'C12400082013',
  'C12400082014',
  'C12400082015',
  'C12400082016',
  'C12400082017',
  'C12400082018',
  'C12400006011',
  'C12400005011',
  'C12400006021',
  'C12400006022',
  'C12400006023',
  'C12400006024',
  'C12400006025',
  'C12400006026',
  'C12400005021',
  'C12400005022',
  'C12400005023',
  'C12400005024',
  'C12400005025',
  'C12400005026',
  'C12400120011',
  'C12400119011',
  'C12400004031',
  'C12400004032')




# plot(as.vector(as.matrix(n)) , as.vector(as.matrix(nagent)))
# 
# 
# plot0 <- ggplot() + 
#   geom_segment(data = Cell0 , aes( x=x0,y=y0,xend=x1,yend=y1, size = nresult , colour = vresult) , arrow = arrow(length=unit(0.2, "cm"))  ) + 
#   scale_colour_gradient2(low = "red",mid = "yellow",high = "green", midpoint = vf/2 ,limits = c(0,vf) , "Speed")+
#   scale_size_continuous( breaks = c(seq(0,100,5) , Inf), range = c(0.5,3) , limits= c(0,150)) + theme(text = element_text(size = 10))
# png("RESULT/Plot_agent/temp.png", width = 6000, height = 6000 , res = 500)
# print(plot0)
# dev.off()


cl <- makeCluster(4)
registerDoParallel(cl, cores = 4)
getDoParName()


time111 <- proc.time()
AllFig <- list()

colorset = RColorBrewer::brewer.pal(9,"Set1")
AllFig <- foreach(time0 = 1:timestep, .packages = c("ggplot2")) %dopar% {
  Cell0$nresult = n[,time0]
  Cell0$vresult = v[,time0]
  Cell0$nagent1  = nagent[,time0]
  
  plot0 <- ggplot() + 
    geom_segment(data = Cell0 , aes( x=x0,y=y0,xend=x1,yend=y1, size = nresult , colour = vresult) , arrow = arrow(length=unit(0.2, "cm"))  ) + 
    scale_colour_gradient2(low = colorset[1],mid = colorset[6],high = colorset[3], midpoint = vf/2 ,limits = c(0,vf) , "Speed")+
    scale_size_continuous( breaks = c(seq(0,100,5) , Inf), range = c(0.5,4) , limits= c(0,150))+ theme(text = element_text(size = 20))
  
  plot0
}

stopCluster(cl)




for(time0 in 1:length(AllFig)) {
  png(paste0("RESULT/Plot_agent/time_",formatC(time0 , width = 5 , flag = "0"),".png"), width = 4500, height = 4500 , res = 250)
  print(AllFig[[time0]])
  dev.off()
}
print(proc.time() - time111)





cl <- makeCluster(4)
registerDoParallel(cl, cores = 4)
getDoParName()


time111 <- proc.time()
AllFig <- list()

AllFig <- foreach(time0 = 1:timestep, .packages = c("ggplot2")) %dopar% {
  Cell0$nresult = n[,time0]
  Cell0$vresult = v[,time0]
  Cell0$nagent1  = nagent[,time0]
  
  plot0 <- ggplot() + 
    geom_segment(data = Cell0[which(Cell0$ID %in% targetCell),] , aes( x=x0,y=y0,xend=x1,yend=y1, size = nresult , colour = vresult) , arrow = arrow(length=unit(0.2, "cm"))  ) + 
    geom_text(data = Cell0[which(Cell0$ID %in% targetCell),] , aes(x = (x0+x1)/2 , y = (y0+y1)/2 , label = nagent1 ) , size = 2.5)+
    scale_colour_gradient2(low = colorset[1],mid = colorset[6],high = colorset[3], midpoint = vf/2 ,limits = c(0,vf) , "Speed")+
    scale_size_continuous( breaks = c(seq(0,100,5) , Inf), range = c(1,4) , limits= c(0,150))+ theme(text = element_text(size = 20)) +
    xlim(211600 , 212580) + ylim(548100 , 548860)
  
  plot0
}

stopCluster(cl)

for(time0 in 1:length(AllFig)) {
  png(paste0("RESULT/Plot_agent1/time_",formatC(time0 , width = 5 , flag = "0"),".png"), width = 4500, height = 4500 , res = 250)
  print(AllFig[[time0]])
  dev.off()
}
print(proc.time() - time111)

