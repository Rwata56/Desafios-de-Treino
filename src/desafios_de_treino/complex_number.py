import math
from typing import Any


class ComplexNumber(object):
    def __init__(self, real: int | float, imaginary: int | float) -> None:
        """Inicializa um número complexo com partes real e imaginária"""
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: "ComplexNumber| Any") -> bool:
        """Comparação de igualdade entre números complexos"""
        if isinstance(other, ComplexNumber):
            return (self.real == other.real) and (self.imaginary == other.imaginary)
        raise ValueError("tipo invalido para comparação")

    def __add__(self, other):
        """Soma dois números complexos"""
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        """Subtrai dois números complexos"""
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        """Multiplica dois números complexos"""
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        """Retorna o módulo (valor absoluto) do número complexo"""
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        """Retorna o conjugado do número complexo"""
        return ComplexNumber(self.real, -self.imaginary)

    def __repr__(self):
        """Representação do objeto como string"""
        return f"ComplexNumber({self.real}, {self.imaginary})"
