import pytest
from src.navigation import Directions, get_adjacent_coordinate
from src.components import Coordinate


class TestGetAdjacentCoordinate:

    @pytest.mark.parametrize("origin_coordinate, given_direction, expected_value", [
        (Coordinate(0, 0, 0), Directions.NORTH, Coordinate(0, 0, 1)),
        (Coordinate(0, 0, 0), Directions.SOUTH, Coordinate(0, 0, -1)),
        (Coordinate(0, 0, 0), Directions.EAST, Coordinate(0, 1, 0)),
        (Coordinate(0, 0, 0), Directions.WEST, Coordinate(0, -1, 0)),
        (Coordinate(0, 0, 0), Directions.UP, Coordinate(1, 0, 0)),
        (Coordinate(0, 0, 0), Directions.DOWN, Coordinate(-1, 0, 0)),
    ])
    def test_get_adjacent_coordinate_given_direction_returns_the_adjacent_coordinate(
        self, origin_coordinate, given_direction, expected_value):
        result = get_adjacent_coordinate(origin_coordinate, given_direction)
        assert result == expected_value