set.seed(42)

simulacao_aleatoria <- function() {
  prisioneiros <- 1:100
  gavetas <- sample(prisioneiros, 100)

  sucesso <- 0
  for (prisioneiro in prisioneiros) {
    gavetas_abertas <- sample(prisioneiros, 50)
    if (prisioneiro %in% gavetas[gavetas_abertas]) {
      sucesso <- sucesso + 1
    }
  }
  return(sucesso == 100)
}

simulacao_otima <- function() {
  prisioneiros <- 1:100

  gavetas <- sample(prisioneiros, 100)

  sucesso <- 0

  for (prisioneiro in prisioneiros) {
    atual <- prisioneiro
    encontrado <- FALSE

    for (i in 1:50) {
      if (gavetas[atual] == prisioneiro) {
        encontrado <- TRUE
        break
      }
      atual <- gavetas[atual]
    }

    if (encontrado) {
      sucesso <- sucesso + 1
    }
  }
  return(sucesso == 100)
}

n_simulacoes <- 1000
resultados_aleatorios <- replicate(n_simulacoes, simulacao_aleatoria())
resultados_otimos <- replicate(n_simulacoes, simulacao_otima())

probabilidade_aleatoria <- mean(resultados_aleatorios)
probabilidade_otima <- mean(resultados_otimos)

cat("Probabilidade de sucesso (estratégia aleatória):", probabilidade_aleatoria, "\n")
cat("Probabilidade de sucesso (estratégia ótima):", probabilidade_otima, "\n")
