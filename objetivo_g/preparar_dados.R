library(dplyr)

getDadosCultura1 <- function(json){
  cultura_1 <- data.frame(json$cultura_1)

  cultura_1$area <- ifelse(cultura_1$tipo == 1, cultura_1$base * cultura_1$altura, cultura_1$base * cultura_1$altura / 2)

  return(cultura_1)
}

getDadosCultura2 <- function(json){
  cultura_2 <- data.frame(json$cultura_2)

  cultura_2$area <- ifelse(cultura_2$tipo == 1, cultura_2$base * cultura_2$altura, cultura_2$base * cultura_2$altura / 2)


  return(cultura_2)
}