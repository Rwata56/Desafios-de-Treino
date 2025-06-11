factorize <- function(n) {
  factors <- c()
  i <- 2
  while (i * i <= n) {
    while (n %% i == 0) {
      factors <- c(factors, i)
      n <- n / i
    }
    i <- i + 1
  }
  if (n > 1) factors <- c(factors, n)
  return(factors)
}

is.practical <- function(n) {
  if (n == 1) return(TRUE)
  factors <- as.data.frame(table(factorize(n)))
  primes <- as.numeric(as.character(factors$Var1))
  exponents <- factors$Freq

  if (primes[1] != 2) return(FALSE)

  sum_divisors <- 1
  for (i in seq_along(primes)) {
    p <- primes[i]
    a <- exponents[i]

    if (i > 1) {
      if (p > sum_divisors + 1) return(FALSE)
    }

    sum_divisors <- sum_divisors * sum(p^(0:a))
  }

  return(TRUE)
}

cat("Testes:\n")
cat("practical(1):", is.practical(1), "\n")
cat("practical(2):", is.practical(2), "\n")
cat("practical(3):", is.practical(3), "\n")
cat("practical(10):", is.practical(10), "\n")
cat("practical(12):", is.practical(12), "\n")

cat("\nSoma dos números práticos até 10000:\n")
sum_practical <- sum(sapply(1:10000, function(x) if (is.practical(x)) x else 0))
cat(sum_practical, "\n")

cat("\nSoma dos X tais que 1020 + X é prático:\n")
bonus_sum <- sum(sapply(1:10000, function(x) {
  if (is.practical(1020 + x)) x else 0
}))
cat(bonus_sum, "\n")
