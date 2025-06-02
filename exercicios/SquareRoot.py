def square_root(number):
    if number < 0:
        return "invalido"
    if number == 0:
        return 0
    if number == 1:
        return 1
    for i in range(1, (number // 2) + 1):
        if i * i == number:
            return i
    return "não é quadrado perfeito"

if __name__ == "__main__":
    print(square_root(1))   # Saída: 1
    print(square_root(4))   # Saída: 2
    print(square_root(9))   # Saída: 3
    print(square_root(16))  # Saída: 4
    print(square_root(25))  # Saída: 5
    print(square_root(-1))  # Saída: "invalido"
    print(square_root(26))  # Saída: "não é quadrado perfeito"