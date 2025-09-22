import pytest
from desafios_de_treino.zip  import Zipper


def test_data_is_retained():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }
z
    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.to_tree()
    assert result == expected


def test_left_right_and_value():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.right.value
    assert result == 3


def test_dead_end():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.left
    assert result is None


def test_tree_from_deep_focus():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.right.to_tree()
    assert result == expected


def test_traversing_up_from_top():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.up()
    assert result is None


def test_left_right_and_up():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.up.right.up.left.right.value
    assert result == 3


def test_test_ability_to_descend_multiple_levels_and_return():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.right.up.up.value
    assert result == 1


def test_set_value():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 5,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.set_value(5).to_tree()
    assert result == expected


def test_set_value_after_traversing_up():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 5,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.right.up.set_value(5).to_tree()
    assert result == expected


def test_set_left_with_leaf():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": {"value": 5, "left": None, "right": None},
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.set_left({"value": 5, "left": None, "right": None}).to_tree()
    assert result == expected


def test_set_right_with_null():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {"value": 2, "left": None, "right": None},
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.set_right(None).to_tree()
    assert result == expected


def test_set_right_with_subtree():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {
            "value": 6,
            "left": {"value": 7, "left": None, "right": None},
            "right": {"value": 8, "left": None, "right": None},
        },
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.set_right(
        {
            "value": 6,
            "left": {"value": 7, "left": None, "right": None},
            "right": {"value": 8, "left": None, "right": None},
        }
    ).to_tree()
    assert result == expected


def test_set_value_on_deep_focus():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    expected = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 5, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    result = zipper.left.right.set_value(5).to_tree()
    assert result == expected


def test_different_paths_to_same_zipper():
    initial = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }
    result = Zipper.from_tree(initial).left.up.right.to_tree()

    final = {
        "value": 1,
        "left": {
            "value": 2,
            "left": None,
            "right": {"value": 3, "left": None, "right": None},
        },
        "right": {"value": 4, "left": None, "right": None},
    }
    expected = Zipper.from_tree(final).right.to_tree()

    assert result == expected