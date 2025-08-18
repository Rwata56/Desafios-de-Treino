def square_root(
    number: int,
) -> int:
    if number < 0:
        raise Exception("invalid")
    if not number:
        return 0
    if number == 1:
        return 1
    for i in range(1, (number // 2) + 1):
        if i * i == number:
            return i
    raise Exception("is not a square perfect")
