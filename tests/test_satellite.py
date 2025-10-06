# test_satellite.py
import pytest
from desafios_de_treino.satellite import tree_from_traversals

# Testes convertidos de:
# https://github.com/exercism/problem-specifications/tree/main/exercises/satellite/canonical-data.json

def test_empty_tree():
    preorder = []
    inorder = []
    expected = {}
    assert tree_from_traversals(preorder, inorder) == expected

def test_tree_with_one_item():
    preorder = ["a"]
    inorder = ["a"]
    expected = {"v": "a", "l": {}, "r": {}}
    assert tree_from_traversals(preorder, inorder) == expected

def test_tree_with_many_items():
    preorder = ["a", "i", "x", "f", "r"]
    inorder = ["i", "a", "f", "x", "r"]
    expected = {
        "v": "a",
        "l": {"v": "i", "l": {}, "r": {}},
        "r": {
            "v": "x",
            "l": {"v": "f", "l": {}, "r": {}},
            "r": {"v": "r", "l": {}, "r": {}},
        },
    }
    assert tree_from_traversals(preorder, inorder) == expected

def test_reject_traversals_of_different_length():
    preorder = ["a", "b"]
    inorder = ["b", "a", "r"]
    with pytest.raises(ValueError, match="traversals must have the same length"):
        tree_from_traversals(preorder, inorder)

def test_reject_inconsistent_traversals_of_same_length():
    preorder = ["x", "y", "z"]
    inorder = ["a", "b", "c"]
    with pytest.raises(ValueError, match="traversals must have the same elements"):
        tree_from_traversals(preorder, inorder)

def test_reject_traversals_with_repeated_items():
    preorder = ["a", "b", "a"]
    inorder = ["b", "a", "a"]
    with pytest.raises(ValueError, match="traversals must contain unique items"):
        tree_from_traversals(preorder, inorder)