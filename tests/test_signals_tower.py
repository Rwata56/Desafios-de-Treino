from desafios_de_treino.signals_tower import SignalTowers


def test_example_case() -> None:
    towers = [(1, 1), (2, 1), (4, 3)]
    st = SignalTowers(towers)
    assert st.max_redundant() == 1


def test_two_towers_no_redundant() -> None:
    towers = [(0, 5), (10, 5)]
    st = SignalTowers(towers)
    assert st.max_redundant() == 0


def test_three_towers_middle_redundant() -> None:
    towers = [(0, 10), (5, 1), (10, 10)]
    st = SignalTowers(towers)
    assert st.max_redundant() == 1


def test_all_increasing_ki() -> None:
    towers = [(0, 1), (1, 2), (2, 3), (3, 4)]
    st = SignalTowers(towers)
    assert st.max_redundant() >= 1  # algumas vão ser redundantes


def test_large_gap() -> None:
    towers = [(0, 100), (1000, 1), (2000, 100)]
    st = SignalTowers(towers)
    assert st.max_redundant() == 1
