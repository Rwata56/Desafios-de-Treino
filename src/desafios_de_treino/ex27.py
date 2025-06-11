import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def find_max_consecutive_primes():
    max_primes = 0
    best_a = 0
    best_b = 0
    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            primes = count_consecutive_primes(a, b)
            if primes > max_primes:
                max_primes = primes
                best_a = a
                best_b = b
    return best_a, best_b, best_a * best_b


a, b, product = find_max_consecutive_primes()
print(f"Valores de a e b: a = {a}, b = {b}")
print(f"Produto a * b: {product}")

# a=1 e b=41, a fórmula 𝑛^2 + 𝑎 ⋅ 𝑛 + 𝑏

# n=0   0^2+1⋅0+41=410 2 +1⋅0+41=41 (primo)

# n=1   1^2+1⋅1+41=431 2 +1⋅1+41=43 (primo)

# n=2   2^2+1⋅2+41=472 2 +1⋅2+41=47 (primo)

# n=3   3^2+1⋅3+41=533 2+1⋅3+41=53 (primo)