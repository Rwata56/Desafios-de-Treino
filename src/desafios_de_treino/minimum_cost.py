from typing import Optional


def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    Calculate the minimum cost to reach the top of the floor by climbing stairs.

    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1.
    Return the minimum cost to reach the top of the floor.

    Args:
        cost: List of integers representing cost at each step

    Returns:
        Minimum cost to reach the top

    Raises:
        ValueError: If cost list is empty or contains negative values
    """
    if not cost:
        raise ValueError("Cost list cannot be empty")
    
    if any(c < 0 for c in cost):
        raise ValueError("Cost values cannot be negative")
    
    n = len(cost)
    
    if n == 1:
        return cost[0]
    if n == 2:
        return min(cost[0], cost[1])
    
    dp = [0] * n
    
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    return min(dp[n-1], dp[n-2])


def min_cost_climbing_stairs_space_optimized(cost: list[int]) -> int:
    """
    Space-optimized version of min_cost_climbing_stairs.
    Uses O(1) space instead of O(n).

    Args:
        cost: List of integers representing cost at each step

    Returns:
        Minimum cost to reach the top

    Raises:
        ValueError: If cost list is empty or contains negative values
    """
    if not cost:
        raise ValueError("Cost list cannot be empty")
    
    if any(c < 0 for c in cost):
        raise ValueError("Cost values cannot be negative")
    
    n = len(cost)
    
    # Base cases
    if n == 1:
        return cost[0]
    if n == 2:
        return min(cost[0], cost[1])
    
    # Track only previous two values
    prev2: int = cost[0]
    prev1: int = cost[1]
    
    # Calculate minimum cost
    for i in range(2, n):
        current: int = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = current
    
    return min(prev1, prev2)


class MinimumCostCalculator:
    """Class-based implementation with additional utilities"""
    
    def __init__(self, cost: Optional[list[int]] = None):
        self.cost = cost if cost is not None else []
        self._validate_cost()
    
    def _validate_cost(self) -> None:
        """Validate the cost list"""
        if not self.cost:
            raise ValueError("Cost list cannot be empty")
        if any(c < 0 for c in self.cost):
            raise ValueError("Cost values cannot be negative")
    
    def calculate_min_cost(self, optimized: bool = True) -> int:
        """
        Calculate minimum cost to reach top.
        
        Args:
            optimized: If True, uses space-optimized approach
        
        Returns:
            Minimum cost to reach the top
        """
        if optimized:
            return min_cost_climbing_stairs_space_optimized(self.cost)
        return min_cost_climbing_stairs(self.cost)
    
    @staticmethod
    def from_string(cost_str: str, separator: str = ',') -> 'MinimumCostCalculator':
        """
        Create calculator from string representation of costs.
        
        Args:
            cost_str: String containing costs separated by separator
            separator: Character used to separate costs
            
        Returns:
            MinimumCostCalculator instance
        """
        try:
            cost = [int(x.strip()) for x in cost_str.split(separator) if x.strip()]
            return MinimumCostCalculator(cost)
        except ValueError as e:
            raise ValueError(f"Invalid cost string: {cost_str}") from e