from desafios_de_treino.complex_number import ComplexNumber


def test_complex_creation():
    """Testa a criação de um número complexo"""
    num = ComplexNumber(3, 4)
    assert num.real == 3
    assert num.imaginary == 4


def test_complex_addition():
    """Testa a adição de números complexos"""
    a = ComplexNumber(1, 2)
    b = ComplexNumber(3, 4)
    result = a + b
    assert result.real == 4
    assert result.imaginary == 6


def test_complex_subtraction():
    """Testa a subtração de números complexos"""
    a = ComplexNumber(5, 7)
    b = ComplexNumber(3, 4)
    result = a - b
    assert result.real == 2
    assert result.imaginary == 3


def test_complex_multiplication():
    """Testa a multiplicação de números complexos"""
    a = ComplexNumber(1, 2)
    b = ComplexNumber(3, 4)
    result = a * b
    assert result.real == -5
    assert result.imaginary == 10


def test_complex_absolute():
    """Testa o cálculo do módulo"""
    num = ComplexNumber(3, 4)
    assert abs(num) == 5


def test_conjugate():
    """Testa o cálculo do conjugado"""
    num = ComplexNumber(3, 4)
    conj = num.conjugate()
    assert conj.real == 3
    assert conj.imaginary == -4
