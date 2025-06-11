from desafios_de_treino.SquareRoot import square_root


def test_Square() -> None:
    assert 1 == square_root(1)


def test_Square1() -> None:
    assert 2 == square_root(4)
    assert 2 == square_root(9)
    assert 2 == square_root(16)
    assert 2 == square_root(25)
    assert 2 == square_root(-1)
    assert 2 == square_root(26)
