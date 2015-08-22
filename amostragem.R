#Teorema do Limite Central 
#Central Limit Teorem
#by Kleber Povoacao

x<-c()
populacao<-1000
qtd_elemento_amostral<-30
qtd_coletas<-100

for(i in seq(1:qtd_coletas)){
  amostra<-sample(1:populacao,qtd_elemento_amostral)
  y=mean(amostra)
  x<-c(x,y)
  hist(x,breaks=7)
  Sys.sleep(0.1)
}


