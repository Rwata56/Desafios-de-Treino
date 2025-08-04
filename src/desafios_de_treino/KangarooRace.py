def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """
    Determina se dois cangurus irão se encontrar no mesmo ponto ao mesmo tempo.

    Returns:
        'YES' se os cangurus se encontrarem, 'NO' caso contrário
    """
    if x1 == x2:
        return "YES"

    if v1 == v2:
        return "NO"

    numerator = x2 - x1
    denominator = v1 - v2

    if denominator == 0:
        return "NO"

    if numerator % denominator != 0:
        return "NO"

    return "YES" if (numerator / denominator) > 0 else "NO"
