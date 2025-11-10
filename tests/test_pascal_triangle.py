import pytest
from desafios_de_treino.pascal_triangle import nth_row_pascal, nth_row_pascal_optimized

class TestPascalTriangle:
    """Testes para as funções do Triângulo de Pascal"""
    
    def test_nth_row_pascal_base_cases(self):
        """Testa os casos base"""
        assert nth_row_pascal(0) == [1]
        assert nth_row_pascal(1) == [1, 1]
        assert nth_row_pascal(2) == [1, 2, 1]
    
    def test_nth_row_pascal_medium_cases(self):
        """Testa casos médios"""
        assert nth_row_pascal(3) == [1, 3, 3, 1]
        assert nth_row_pascal(4) == [1, 4, 6, 4, 1]
        assert nth_row_pascal(5) == [1, 5, 10, 10, 5, 1]
    
    def test_nth_row_pascal_larger_cases(self):
        """Testa casos maiores"""
        assert nth_row_pascal(6) == [1, 6, 15, 20, 15, 6, 1]
        assert nth_row_pascal(7) == [1, 7, 21, 35, 35, 21, 7, 1]
    
    def test_nth_row_pascal_negative_input(self):
        """Testa entrada negativa"""
        with pytest.raises(ValueError, match="n deve ser um número não negativo"):
            nth_row_pascal(-1)
        with pytest.raises(ValueError, match="n deve ser um número não negativo"):
            nth_row_pascal(-5)
    
    def test_nth_row_pascal_properties(self):
        """Testa propriedades matemáticas do Triângulo de Pascal"""
        # A soma dos elementos da linha n deve ser 2^n
        for n in range(8):
            row = nth_row_pascal(n)
            assert sum(row) == 2 ** n
        
        # A linha deve ser simétrica
        for n in range(8):
            row = nth_row_pascal(n)
            assert row == row[::-1]
    
    def test_both_implementations_consistency(self):
        """Testa que ambas as implementações retornam o mesmo resultado"""
        for n in range(10):
            result1 = nth_row_pascal(n)
            result2 = nth_row_pascal_optimized(n)
            assert result1 == result2, f"Diferença na linha {n}: {result1} vs {result2}"

    @pytest.mark.parametrize("n,expected", [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
    ])
    def test_nth_row_pascal_parametrized(self, n, expected):
        """Testes parametrizados para várias entradas"""
        assert nth_row_pascal(n) == expected
        assert nth_row_pascal_optimized(n) == expected

    def test_nth_row_pascal_edge_cases(self):
        """Testa casos de borda"""
        # n = 0 (primeira linha)
        assert nth_row_pascal(0) == [1]
        
        # Verifica que o primeiro e último elementos são sempre 1
        for n in range(1, 10):
            row = nth_row_pascal(n)
            assert row[0] == 1
            assert row[-1] == 1

if __name__ == "__main__":
    # Executa os testes diretamente (útil para debugging)
    pytest.main([__file__, "-v"])