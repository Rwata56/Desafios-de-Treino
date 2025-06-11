# Função para verificar se um número é primo
is_prime <- function(n) {
  if (n <= 1) return(FALSE)   # Números menores ou iguais a 1 não são primos
  if (n == 2) return(TRUE)    # O número 2 é primo
  if (n %% 2 == 0) return(FALSE)  # Números pares maiores que 2 não são primos
  
  # Testar os números ímpares de 3 até sqrt(n)
  for (i in seq(3, floor(sqrt(n)))) {
    if (n %% i == 0) return(FALSE)  # Se n for divisível por i, não é primo
  }
  return(TRUE)
}

# calcular o número de primos consecutivos
count_consecutive_primes <- function(a, b) {
  n <- 0
  while (is_prime(n^2 + a*n + b)) {
    n <- n + 1
  }
  return(n)
}

# encontra o valor de a e b com o maior número de primos consecutivos
find_max_consecutive_primes <- function() {
  max_primes <- 0
  best_a <- 0
  best_b <- 0
  for (a in -999:999) {
    for (b in -999:999) {
      primes <- count_consecutive_primes(a, b)
      if (primes > max_primes) {
        max_primes <- primes
        best_a <- a
        best_b <- b
      }
    }
  }
  return(list(a = best_a, b = best_b, product = best_a * best_b))
}

# Rodar a função para encontrar a solução
result <- find_max_consecutive_primes()
print(result)
