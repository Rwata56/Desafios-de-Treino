# test_rpn.py
import pytest
from desafios_de_treino.rpn import evaluate_rpn


def test_simple_add_mul():
    tokens = ["2", "1", "+", "3", "*"]
    assert evaluate_rpn(tokens) == 9  # (2 + 1) * 3 = 9


def test_div_and_add():
    tokens = ["4", "13", "5", "/", "+"]
    # 13/5 = 2 (truncado), 4 + 2 = 6
    assert evaluate_rpn(tokens) == 6


def test_complex():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert evaluate_rpn(tokens) == 22


def test_negative_numbers():
    tokens = ["-4", "2", "*", "3", "+"]
    assert evaluate_rpn(tokens) == -5  # -4 * 2 = -8; -8 + 3 = -5


def test_division_truncate_positive():
    tokens = ["7", "3", "/"]
    assert evaluate_rpn(tokens) == 2  # 7/3 truncado = 2


def test_division_truncate_negative():
    tokens = ["-7", "3", "/"]
    assert evaluate_rpn(tokens) == -2  # -7/3 truncado = -2


def test_multiple_operations():
    tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
    # 5 + ((1 + 2) * 4) - 3 = 14
    assert evaluate_rpn(tokens) == 14
