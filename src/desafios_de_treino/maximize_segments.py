def maximize_segments(n: int, p: int, q: int, r: int) -> int:
    """
    Retorna o número máximo de segmentos de tamanho p, q ou r
    que podem ser usados para formar exatamente n.

    Se não for possível, retorna 0.
    """
    if n < 0:
        raise ValueError("n deve ser um número não negativo")
    if p <= 0 or q <= 0 or r <= 0:
        raise ValueError("p, q e r devem ser maiores que zero")

    # dp[i] = máximo de segmentos para comprimento i
    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for seg in (p, q, r):
            if i - seg >= 0 and dp[i - seg] != -1:
                dp[i] = max(dp[i], dp[i - seg] + 1)

    return max(dp[n], 0)
