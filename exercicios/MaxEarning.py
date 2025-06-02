def max_earnings(hours):
    if not hours:
        return 0
    n = len(hours)
    if n == 1:
        return hours[0]
    
    dp = [0] * n
    dp[0] = hours[0]
    dp[1] = max(hours[0], hours[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + hours[i])
    
    return dp[-1]

print(max_earnings([2, 4, 6, 2, 5]))  # Saída esperada: 13
print(max_earnings([5, 1, 1, 5]))     # Saída esperada: 10
print(max_earnings([3, 2, 5, 10, 7])) # Saída esperada: 15
