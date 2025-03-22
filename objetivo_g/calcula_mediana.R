source("objetivo_g/utils.R")
source("objetivo_g/preparar_dados.R")

calculaMediana <- function(vetor, verbose = TRUE){

  assertVetorNumerio(vetor)

  mediana <- median(vetor)

  if (verbose) {
    print(paste('A mediana e: ', mediana))

  }
  return(mediana)
}

calculaMedianaFromJson <- function(json){

  cultura_1 <- getDadosCultura1(json)

  print(paste("Calculando a mediana da area de plantio de", CULTURA_1))

  mediana <- calculaMediana(cultura_1$area)

  print(paste("A mediana da area de plantio de", CULTURA_1, ":", mediana, "m2"))

  print(paste("Calculando a mediana da area de plantio de", CULTURA_2))

  cultura_2 <- getDadosCultura2(json)

  mediana2 <- calculaMediana(cultura_2$area)

  print(paste("A mediana da area de plantio de ", CULTURA_2, ":", mediana2, "m2"))

}