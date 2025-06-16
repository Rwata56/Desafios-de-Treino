from desafios_de_treino.SquareRoot import square_root
from desafios_de_treino.count import count_ways_to_make_200


def test_Square() -> None:
    assert 1 == square_root(1)


def test_Square1() -> None:
    assert 2 == square_root(4)
    assert 3 == square_root(9)
    assert 3 == square_root(9)
    # assert 2 == square_root(16)
    # assert 2 == square_root(25)
    # assert 2 == square_root(-1)
    # assert 2 == square_root(26)

def test_count_ways_to_make_200() -> None:
    assert 73682 == count_ways_to_make_200(200)  # £2 (200p)
    assert 1 == count_ways_to_make_200(0)        # 0p (nenhuma moeda)
    assert 1 == count_ways_to_make_200(1)        # Apenas 1 moeda de 1p
    assert 2 == count_ways_to_make_200(2)        # 1x2p ou 2x1p
    