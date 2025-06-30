from desafios_de_treino.zebra import water_drinker, zebra_owner


def test_zebra_owner():
    assert zebra_owner() == "japonês"


def test_water_drinker():
    assert water_drinker() == "norueguês"
