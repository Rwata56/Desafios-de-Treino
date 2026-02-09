import pytest

from desafios_de_treino.minimum_cost import (
    MinimumCostCalculator,
    min_cost_climbing_stairs,
    min_cost_climbing_stairs_space_optimized,
)


class TestMinCostClimbingStairs:
    """Testes para as funções de custo mínimo ao subir escadas"""

    def test_base_cases(self):
        """Testa casos base"""
        assert min_cost_climbing_stairs([10]) == 10
        assert min_cost_climbing_stairs([10, 15]) == 10

        assert min_cost_climbing_stairs_space_optimized([10]) == 10
        assert min_cost_climbing_stairs_space_optimized([10, 15]) == 10

    def test_example_cases(self):
        """Testa exemplos clássicos (LeetCode style)"""
        cost = [10, 15, 20]
        assert min_cost_climbing_stairs(cost) == 15
        assert min_cost_climbing_stairs_space_optimized(cost) == 15

        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        assert min_cost_climbing_stairs(cost) == 6
        assert min_cost_climbing_stairs_space_optimized(cost) == 6

    def test_medium_cases(self):
        """Testa casos intermediários"""
        assert min_cost_climbing_stairs([5, 10, 5, 10, 5]) == 15
        assert min_cost_climbing_stairs_space_optimized([5, 10, 5, 10, 5]) == 15

        assert min_cost_climbing_stairs([3, 2, 1, 0]) == 2
        assert min_cost_climbing_stairs_space_optimized([3, 2, 1, 0]) == 2

    def test_large_case(self):
        """Testa um caso grande"""
        cost = [1] * 1000
        assert min_cost_climbing_stairs(cost) == 500
        assert min_cost_climbing_stairs_space_optimized(cost) == 500

    def test_empty_cost_list(self):
        """Testa lista vazia"""
        with pytest.raises(ValueError, match="Cost list cannot be empty"):
            min_cost_climbing_stairs([])

        with pytest.raises(ValueError, match="Cost list cannot be empty"):
            min_cost_climbing_stairs_space_optimized([])

    def test_negative_cost_values(self):
        """Testa valores negativos"""
        with pytest.raises(ValueError, match="Cost values cannot be negative"):
            min_cost_climbing_stairs([1, -2, 3])

        with pytest.raises(ValueError, match="Cost values cannot be negative"):
            min_cost_climbing_stairs_space_optimized([1, -2, 3])

    def test_both_implementations_consistency(self):
        """Testa se ambas as implementações retornam o mesmo resultado"""
        test_cases = [
            [10, 15, 20],
            [1, 100, 1, 1, 1, 100, 1],
            [5, 5, 5, 5],
            [2, 7, 9, 3, 1],
        ]

        for cost in test_cases:
            assert min_cost_climbing_stairs(
                cost
            ) == min_cost_climbing_stairs_space_optimized(cost)


class TestMinimumCostCalculator:
    """Testes para a classe MinimumCostCalculator"""

    def test_calculator_default_behavior(self):
        """Testa comportamento padrão"""
        calc = MinimumCostCalculator([10, 15, 20])
        assert calc.calculate_min_cost() == 15
        assert calc.calculate_min_cost(optimized=False) == 15

    def test_calculator_invalid_cost(self):
        """Testa inicialização inválida"""
        with pytest.raises(ValueError, match="Cost list cannot be empty"):
            MinimumCostCalculator([])

        with pytest.raises(ValueError, match="Cost values cannot be negative"):
            MinimumCostCalculator([1, -1, 2])

    def test_calculator_from_string(self):
        """Testa criação a partir de string"""
        calc = MinimumCostCalculator.from_string("10, 15, 20")
        assert calc.calculate_min_cost() == 15

        calc = MinimumCostCalculator.from_string("1|100|1|1", separator="|")
        assert calc.calculate_min_cost() == 2

    def test_calculator_from_string_invalid(self):
        """Testa string inválida"""
        with pytest.raises(ValueError, match="Invalid cost string"):
            MinimumCostCalculator.from_string("10,a,20")

    def test_calculator_consistency_with_functions(self):
        """Testa consistência entre classe e funções"""
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

        calc = MinimumCostCalculator(cost)

        assert calc.calculate_min_cost() == min_cost_climbing_stairs_space_optimized(
            cost
        )
        assert calc.calculate_min_cost(False) == min_cost_climbing_stairs(cost)


@pytest.mark.parametrize(
    "cost,expected",
    [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1], 4),
        ([0, 0, 0, 0], 0),
        ([5, 10, 5, 10, 5], 15),
    ],
)
def test_parametrized_cases(cost, expected):
    """Testes parametrizados"""
    assert min_cost_climbing_stairs(cost) == expected
    assert min_cost_climbing_stairs_space_optimized(cost) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
