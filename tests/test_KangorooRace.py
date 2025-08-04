import unittest

from desafios_de_treino.KangarooRace import kangaroo


class TestKangarooRace(unittest.TestCase):
    def test_meet_in_future(self):
        """Testa quando os cangurus se encontram no futuro."""
        self.assertEqual(kangaroo(0, 3, 4, 2), "YES")
        self.assertEqual(kangaroo(-10, 5, 0, 3), "YES")

    def test_never_meet(self):
        """Testa quando os cangurus nunca se encontram."""
        self.assertEqual(kangaroo(0, 2, 5, 3), "NO")
        self.assertEqual(kangaroo(5, 3, 0, 2), "NO")

    def test_same_position_start(self):
        """Testa quando os cangurus já começam na mesma posição."""
        self.assertEqual(kangaroo(3, 2, 3, 1), "YES")
        self.assertEqual(kangaroo(-4, 3, -4, 5), "YES")

    def test_same_speed(self):
        """Testa quando os cangurus têm a mesma velocidade."""
        self.assertEqual(kangaroo(0, 2, 5, 2), "NO")
        self.assertEqual(kangaroo(-3, 4, 1, 4), "NO")

    def test_negative_positions(self):
        """Testa com posições iniciais negativas."""
        self.assertEqual(kangaroo(-10, 3, -4, 2), "YES")
        self.assertEqual(kangaroo(-5, 1, -3, 2), "NO")

    def test_large_numbers(self):
        """Testa com números grandes."""
        self.assertEqual(kangaroo(0, 1_000_000, 1_000_000, 1), "NO")
        self.assertEqual(kangaroo(0, 1, 1_000_000, 2), "NO")


if __name__ == "__main__":
    unittest.main()
