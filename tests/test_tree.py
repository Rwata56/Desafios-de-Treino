from desafios_de_treino.tree import BinarySearchTree


def test_insert_smaller_value() -> None:
    tree = BinarySearchTree(4)
    tree.insert(2)
    assert tree.left is not None
    assert tree.left.data == 2


def test_insert_larger_value() -> None:
    tree = BinarySearchTree(4)
    tree.insert(5)
    assert tree.right is not None
    assert tree.right.data == 5


def test_insert_equal_value_goes_left() -> None:
    tree = BinarySearchTree(4)
    tree.insert(4)
    assert tree.left is not None
    assert tree.left.data == 4


def test_in_order_traversal_sorted() -> None:
    tree = BinarySearchTree(4)
    for v in [2, 6, 1, 3, 5, 7]:
        tree.insert(v)
    assert list(tree.each()) == [1, 2, 3, 4, 5, 6, 7]


def test_in_order_with_duplicates() -> None:
    tree = BinarySearchTree(4)
    for v in [4, 4, 5, 3]:
        tree.insert(v)
    assert list(tree.each()) == [3, 4, 4, 4, 5]
