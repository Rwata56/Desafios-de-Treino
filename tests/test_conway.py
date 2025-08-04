import unittest

from desafios_de_treino.conway import next_generation


class GameOfLifeTest(unittest.TestCase):
    def test_case_1(self) -> None:
        self.assertEqual(
            next_generation([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )

    def test_case_2(self) -> None:
        self.assertEqual(
            next_generation([[0, 0, 0], [0, 1, 0], [0, 1, 0]]),
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        )

    def test_case_3(self) -> None:
        self.assertEqual(
            next_generation([[1, 0, 1], [1, 0, 1], [1, 0, 1]]),
            [[0, 0, 0], [1, 0, 1], [0, 0, 0]],
        )

    def test_case_4(self) -> None:
        self.assertEqual(
            next_generation([[0, 1, 0], [1, 0, 0], [1, 1, 0]]),
            [[0, 0, 0], [1, 0, 0], [1, 1, 0]],
        )

    def test_case_5(self) -> None:
        self.assertEqual(
            next_generation([[1, 1, 0], [0, 0, 0], [1, 0, 0]]),
            [[0, 0, 0], [1, 1, 0], [0, 0, 0]],
        )

    def test_case_6(self) -> None:
        self.assertEqual(
            next_generation([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        )

    def test_case_7(self) -> None:
        self.assertEqual(
            next_generation(
                [
                    [1, 1, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 1, 1, 0, 0],
                    [1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 1],
                ]
            ),
            [
                [1, 1, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 0, 0, 1],
                [1, 1, 0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1],
            ],
        )
