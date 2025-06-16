from typing import Literal


def square_root(
    number, # type: ignore
) -> int | Literal["invalido"] | Literal["não é quadrado perfeito"]:
    if number < 0:
        return "invalido"
    if number == 0:
        return 0
    if number == 1:
        return 1
    for i in range(1, (number // 2) + 1): # type: ignore
        if i * i == number:
            return i
    return "não é quadrado perfeito"
