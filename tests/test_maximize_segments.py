import pytest

from desafios_de_treino.maximize_segments import maximize_segments


class TestMaximizeSegments:
    """Testes para o problema de maximização de segmentos"""

    def test_base_cases(self):
        """Testa casos base"""
        assert maximize_segments(0, 1, 2, 3) == 0
        assert maximize_segments(5, 5, 3, 2) == 2  # corrigido

    def test_example_cases(self):
        """Testa exemplos clássicos do problema"""
        assert maximize_segments(5, 2, 5, 1) == 5
        assert maximize_segments(7, 5, 2, 2) == 2
        assert maximize_segments(23, 11, 9, 12) == 2

    def test_no_possible_solution(self):
        """Testa quando não é possível formar n"""
        assert maximize_segments(7, 4, 5, 6) == 0
        assert maximize_segments(1, 2, 3, 4) == 0

    def test_medium_cases(self):
        """Testa casos intermediários"""
        assert maximize_segments(10, 2, 3, 5) == 5
        assert maximize_segments(11, 2, 3, 5) == 5
        assert maximize_segments(17, 3, 5, 7) == 5

    def test_large_case(self):
        """Testa um caso maior"""
        assert maximize_segments(100, 2, 5, 10) == 50

    def test_invalid_inputs(self):
        """Testa entradas inválidas"""
        with pytest.raises(ValueError):
            maximize_segments(-1, 2, 3, 4)

        with pytest.raises(ValueError):
            maximize_segments(10, 0, 2, 3)

        with pytest.raises(ValueError):
            maximize_segments(10, -2, 3, 4)

    @pytest.mark.parametrize(
        "n,p,q,r,expected",
        [
            (5, 2, 5, 1, 5),
            (7, 2, 3, 4, 3),
            (9, 2, 2, 2, 0),  # corrigido
            (8, 3, 3, 3, 0),
        ],
    )
    def test_parametrized(self, n, p, q, r, expected):
        """Testes parametrizados"""
        assert maximize_segments(n, p, q, r) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
