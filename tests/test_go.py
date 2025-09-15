import pytest

from desafios_de_treino.go import BLACK, NONE, WHITE, Board


class TestGoCounting:
    def test_black_corner_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=0, y=1)
        assert stone == BLACK
        assert territory == {(0, 0), (0, 1), (1, 0)}

    def test_white_center_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=2, y=3)
        assert stone == WHITE
        assert territory == {(2, 3)}

    def test_open_corner_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=1, y=4)
        assert stone == NONE
        assert territory == {(0, 3), (0, 4), (1, 4)}

    def test_a_stone_and_not_a_territory_on_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        stone, territory = board.territory(x=1, y=1)
        assert stone == NONE
        assert territory == set()

    def test_invalid_because_x_is_too_low_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with pytest.raises(ValueError) as excinfo:
            board.territory(x=-1, y=1)
        assert str(excinfo.value) == "Invalid coordinate"
        assert excinfo.type == ValueError

    def test_invalid_because_x_is_too_high_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with pytest.raises(ValueError) as excinfo:
            board.territory(x=5, y=1)
        assert str(excinfo.value) == "Invalid coordinate"
        assert excinfo.type == ValueError

    def test_invalid_because_y_is_too_low_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with pytest.raises(ValueError) as excinfo:
            board.territory(x=1, y=-1)
        assert str(excinfo.value) == "Invalid coordinate"
        assert excinfo.type == ValueError

    def test_invalid_because_y_is_too_high_for_5x5_board(self):
        board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
        with pytest.raises(ValueError) as excinfo:
            board.territory(x=1, y=5)
        assert str(excinfo.value) == "Invalid coordinate"
        assert excinfo.type == ValueError

    def test_one_territory_is_the_whole_board(self):
        board = Board([" "])
        territories = board.territories()
        assert territories[BLACK] == set()
        assert territories[WHITE] == set()
        assert territories[NONE] == {(0, 0)}

    def test_two_territory_rectangular_board(self):
        board = Board([" BW ", " BW "])
        territories = board.territories()
        assert territories[BLACK] == {(0, 0), (0, 1)}
        assert territories[WHITE] == {(3, 0), (3, 1)}
        assert territories[NONE] == set()

    def test_two_region_rectangular_board(self):
        board = Board([" B "])
        territories = board.territories()
        assert territories[BLACK] == {(0, 0), (2, 0)}
        assert territories[WHITE] == set()
        assert territories[NONE] == set()
