import unittest

from desafios_de_treino.KangarooRace import kangaroo  # Importa a função diretamente


class TestKangarooRace(unittest.TestCase):
    def test_meet_in_future(self):
        """Testa quando os cangurus se encontram no futuro."""
        self.assertTrue(kangaroo(0, 3, 4, 2))
        self.assertTrue(kangaroo(-10, 5, 0, 3))

    def test_never_meet(self):
        """Testa quando os cangurus nunca se encontram."""
        self.assertFalse(kangaroo(0, 2, 5, 3))
        self.assertFalse(kangaroo(5, 3, 0, 2))

    def test_same_position_start(self):
        """Testa quando os cangurus já começam na mesma posição."""
        self.assertTrue(kangaroo(3, 2, 3, 1))
        self.assertTrue(kangaroo(-4, 3, -4, 5))

    def test_same_speed(self):
        """Testa quando os cangurus têm a mesma velocidade."""
        self.assertFalse(kangaroo(0, 2, 5, 2))
        self.assertFalse(kangaroo(-3, 4, 1, 4))

    def test_negative_positions(self):
        """Testa com posições iniciais negativas."""
        self.assertTrue(kangaroo(-10, 3, -4, 2))
        self.assertFalse(kangaroo(-5, 1, -3, 2))


if __name__ == "__main__":
    unittest.main()
