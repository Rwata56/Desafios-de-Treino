from desafios_de_treino.Knapsack import selected_items, total_value


def test_selected_items():
    result = selected_items()
    expected_names = {"item2", "item3"}
    assert len(result) == 2
    assert all(item["name"] in expected_names for item in result)
    assert sum(item["weight"] for item in result) <= 50
    assert total_value() == 220


def test_total_value():
    assert total_value() == 220
