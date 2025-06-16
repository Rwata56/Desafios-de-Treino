def count_ways_to_make_200(target: int = 200) -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]