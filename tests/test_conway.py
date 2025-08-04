import unittest

from desafios_de_treino.conway import next_generation


class GameOfLifeTest(unittest.TestCase):
    def test_empty_grid(self):
        """Testa uma grade vazia"""
        self.assertEqual(next_generation([]), [])

    def test_single_cell_dies(self):
        """Uma única célula viva deve morrer por solidão"""
        self.assertEqual(next_generation([[1]]), [[0]])

    def test_block_stays_alive(self):
        """Bloco 2x2 deve permanecer estável"""
        block = [[1, 1], [1, 1]]
        self.assertEqual(next_generation(block), block)

    def test_blinker_oscillator(self):
        """Testa o oscilador 'blinker' (barra horizontal/vertical)"""
        # Fase 1 - horizontal
        blinker_h = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        # Fase 2 - vertical (esperado após uma geração)
        blinker_v = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.assertEqual(next_generation(blinker_h), blinker_v)
        self.assertEqual(next_generation(blinker_v), blinker_h)

    def test_dead_cell_with_three_neighbors(self):
        """Célula morta com exatamente 3 vizinhos deve nascer"""
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(next_generation(grid), expected)

    def test_corner_cell_behavior(self):
        """Testa o comportamento de células nos cantos da grade"""
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(next_generation(grid), expected)
