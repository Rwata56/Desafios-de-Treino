from desafios_de_treino.CountCoin import count_ways_to_make_200
from desafios_de_treino.Hangman import (  # type: ignore
    get_display_word,
    guess,
    is_finished,
    is_lost,
    is_won,
    start_game,
)
from desafios_de_treino.prime_circular import circular_primes_below
from desafios_de_treino.SpiralMatrix import generate_spiral_matrix
from desafios_de_treino.SquareRoot import square_root  # type: ignore


def test_Square() -> None:
    assert 1 == square_root(1)


def test_Square1() -> None:  # type: ignore
    assert 2 == square_root(4)
    assert 3 == square_root(9)


def test_count_ways_to_make_200() -> None:
    assert 73682 == count_ways_to_make_200(200)  # £2 (200p)


def test_spiral_matrix() -> None:
    expected_3 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert generate_spiral_matrix(3) == expected_3

    expected_4 = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    assert generate_spiral_matrix(4) == expected_4

    assert generate_spiral_matrix(1) == [[1]]

    assert generate_spiral_matrix(0) == []


def test_circular_primes_below_1_million() -> None:
    assert circular_primes_below(1_000_000) == 55


def test_hangman_final_result() -> None:
    # Vitória
    game = start_game("exercism", max_attempts=7)
    for letter in "exrcism":
        guess(game, letter)

    assert is_won(game) is True
    assert is_finished(game) is True
    assert get_display_word(game) == "exercism"

    # Derrota
    game2 = start_game("python", max_attempts=3)
    for letter in "abc":
        guess(game2, letter)

    assert is_lost(game2) is True
    assert is_finished(game2) is True
    assert get_display_word(game2) == "______"
