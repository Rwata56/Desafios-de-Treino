from typing import List, Dict


def knapsack(items: List[Dict], max_weight: int) -> List[Dict]:
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if items[i - 1]["weight"] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    items[i - 1]["value"] + dp[i - 1][w - items[i - 1]["weight"]],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    w = max_weight
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.insert(0, items[i - 1])
            w -= items[i - 1]["weight"]

    return sorted(selected, key=lambda x: x["weight"])


def selected_items() -> List[Dict]:
    items = [
        {"name": "item1", "weight": 10, "value": 60},
        {"name": "item2", "weight": 20, "value": 100},
        {"name": "item3", "weight": 30, "value": 120},
    ]
    max_weight = 50
    return knapsack(items, max_weight)


def total_value() -> int:
    return sum(item["value"] for item in selected_items())
