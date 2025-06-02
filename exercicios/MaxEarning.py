def max_earnings(earnings, k):
    if not earnings:
        return 0

    n = len(earnings)

    if (k*2) > n:
        return("invalido")

    dp_work = [0] * n
    dp_skip = [0] * n

    # Initialize first day
    dp_work[0] = earnings[0]
    dp_skip[0] = 0

    for i in range(1, n):
        max_work = 0
        for j in range(1, min(k, i + 1) + 1):
            if i - j >= 0:
                current = dp_skip[i - j] + sum(earnings[i - j + 1:i + 1])
            else:
                current = sum(earnings[:i + 1])
            if current > max_work:
                max_work = current
        dp_work[i] = max_work
        dp_skip[i] = max(dp_work[i - 1], dp_skip[i - 1])

    return max(dp_work[-1], dp_skip[-1])

# Test cases
print(max_earnings([60, 70, 80, 40, 80, 90, 100, 20], 3))  # Output: 480
print(max_earnings([45, 12, 78, 34, 56, 89, 23, 67, 91], 4))  # Output: 460
print(max_earnings([45, 12, 78, 34, 56, 89, 23, 67, 91], 5))  # Output: 460