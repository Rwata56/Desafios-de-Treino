"""
Project Euler Problem 30: Digit Fifth Powers

Find the sum of all numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_digit_powers(n, power):
    """Calcula a soma dos dígitos de n elevados à potência especificada."""
    return sum(int(digit)**power for digit in str(n))

def find_power_sum(power):
    """
    Encontra todos os números que são iguais à soma de seus dígitos elevados à potência dada.
    Retorna a soma desses números.
    """
    max_num = (9**power) * (power + 1)

    result = []
    for num in range(2, max_num + 1):
        if num == sum_of_digit_powers(num, power):
            result.append(num)

    return sum(result)

solution = find_power_sum(5)
print(f"A soma de todos os números que podem ser escritos como a soma da quinta potência de seus dígitos é: {solution}")