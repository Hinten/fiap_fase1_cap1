source("objetivo_g/utils.R")
source("objetivo_g/culturas.R")
source("objetivo_g/preparar_dados.R")
library(dplyr)

calculaMedia <- function (vetor, verbose = TRUE){

  assertVetorNumerio(vetor)

  if (verbose) {
    print(paste('Calculando media de ', paste(vetor, collapse = ', ')))
  }

  #aparentemente em R sempre retorna o ultimo valor numa função, não precisa usar return
  mean(vetor)

}

#{"cultura_1": [{"tipo": "1", "base": 12.0, "altura": 80.0}], "cultura_2": [{"tipo": "1", "base": 27.0, "altura": 10.0}, {"tipo": "1", "base": 12.0, "altura": 10.0}]}
calculaMediasFromJson <- function (json){

    cultura_1 <- getDadosCultura1(json)

    print(paste("Calculando a media da area de plantio de", CULTURA_1))

    area_media <- calculaMedia(cultura_1$area)

    print(paste("A media da area de plantio de", CULTURA_1, ":", area_media, "m2"))

    print(paste("Calculando a media da area de plantio de", CULTURA_2))

    cultura_2 <- getDadosCultura2(json)

    area_media2 <- calculaMedia(cultura_2$area)

    print(paste("A media da area de plantio de ", CULTURA_2, ":", area_media2, "m2"))

}

#executa somente se este for o arquivo principal
if (sys.nframe() == 0) {
  print(calculaMedia(c(1, 5, 4.3)))
}
