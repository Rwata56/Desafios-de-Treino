def square_root(n: int) -> int:
    return int(n**0.5)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def get_rotations(n: int) -> list[int]:
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_circular_prime(n: int, primes: set[int]) -> bool:
    return all(rotation in primes for rotation in get_rotations(n))


def circular_primes_below(limit: int = 1_000_000) -> int:
    list = [True] * limit
    list[0:2] = [False, False]

    for num in range(2, int(limit**0.5) + 1):
        if list[num]:
            list[num * num : limit : num] = [False] * len(list[num * num : limit : num])

    primes = {i for i, is_p in enumerate(list) if is_p}
    circular_primes: set[int] = set()

    for p in primes:
        if p not in circular_primes:
            rotations = get_rotations(p)
            if all(r in primes for r in rotations):
                circular_primes.update(rotations)

    return len(circular_primes)
