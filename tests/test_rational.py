from desafios_de_treino.rational_numbers import Rational


def test_creation_and_equality():
    assert Rational(1, 2) == Rational(1, 2)
    assert Rational(2, 4) == Rational(1, 2)  # Testa simplificação
    assert Rational(-1, 2) == Rational(1, -2)  # Testa sinal no denominador


def test_addition():
    assert Rational(1, 2) + Rational(1, 3) == Rational(5, 6)
    assert Rational(1, 2) + Rational(1, 2) == Rational(1, 1)


def test_subtraction():
    assert Rational(1, 2) - Rational(1, 3) == Rational(1, 6)
    assert Rational(3, 4) - Rational(1, 4) == Rational(1, 2)


def test_multiplication():
    assert Rational(1, 2) * Rational(2, 3) == Rational(1, 3)
    assert Rational(3, 4) * Rational(4, 3) == Rational(1, 1)


def test_division():
    assert Rational(1, 2) / Rational(1, 4) == Rational(2, 1)
    assert Rational(3, 4) / Rational(3, 2) == Rational(1, 2)


def test_absolute_value():
    assert abs(Rational(-1, 2)) == Rational(1, 2)
    assert abs(Rational(3, -4)) == Rational(3, 4)


def test_exponentiation():
    assert Rational(1, 2) ** 2 == Rational(1, 4)
    assert Rational(2, 3) ** -1 == Rational(3, 2)
    assert 2 ** Rational(4, 2) == 4.0  # Teste __rpow__
