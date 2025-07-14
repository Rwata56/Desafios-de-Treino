import math


class Rational:
    def __init__(self, numerator, denominator=1):
        """Inicializa um número racional na forma reduzida"""
        if denominator == 0:
            raise ValueError("Denominator não pode ser zero")

        # Simplifica a fração
        common_divisor = math.gcd(numerator, denominator)
        simplified_num = numerator // common_divisor
        simplified_den = denominator // common_divisor

        # Garante que o denominador seja positivo
        if simplified_den < 0:
            simplified_num *= -1
            simplified_den *= -1

        self.numerator = simplified_num
        self.denominator = simplified_den

    def __eq__(self, other):
        """Comparação de igualdade"""
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __repr__(self):
        """Representação do objeto"""
        return f"Rational({self.numerator}, {self.denominator})"

    def __add__(self, other):
        """Adição de racionais"""
        new_num = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __sub__(self, other):
        """Subtração de racionais"""
        new_num = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __mul__(self, other):
        """Multiplicação de racionais"""
        return Rational(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def __truediv__(self, other):
        """Divisão de racionais"""
        if other.numerator == 0:
            raise ValueError("Não é divisivel por 0")
        return Rational(
            self.numerator * other.denominator, self.denominator * other.numerator
        )

    def __abs__(self):
        """Valor absoluto"""
        return Rational(abs(self.numerator), self.denominator)

    def __pow__(self, power):
        """Exponenciação"""
        if isinstance(power, int):
            if power >= 0:
                return Rational(self.numerator**power, self.denominator**power)
            else:
                return Rational(
                    self.denominator ** abs(power), self.numerator ** abs(power)
                )
        else:
            raise TypeError("A potência deve ser um número inteiro")

    def __rpow__(self, base):
        """Exponenciação com o racional como expoente"""
        return base ** (self.numerator / self.denominator)
