import pytest
from src.components import Maze, Area, Coordinate
from src.factory import Forge, DirectionProvider


class TestForForge:

    def test_start_maze_sets_a_maze_instance(self):
        builder = Forge()
        builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        assert isinstance(builder.maze, Maze)

    def test_extend_given_coordinates_sets_an_area_in_the_maze(self):
        builder = Forge()
        given_coordinates = Coordinate(1, 2, 4)
        builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        builder.extend(given_coordinates)
        assert isinstance(builder.maze.areas[given_coordinates], Area)


class TestDirectionProvider:
    
    def setup_class(self):
        self.direction_provider = DirectionProvider()

    @pytest.mark.parametrize("origin_coordinate, given_direction, expected_value", [
        (Coordinate(0, 0, 0), DirectionProvider.Directions.NORTH, Coordinate(0, 0, 1)),
        (Coordinate(0, 0, 0), DirectionProvider.Directions.SOUTH, Coordinate(0, 0, -1)),
        (Coordinate(0, 0, 0), DirectionProvider.Directions.EAST, Coordinate(0, 1, 0)),
        (Coordinate(0, 0, 0), DirectionProvider.Directions.WEST, Coordinate(0, -1, 0)),
        (Coordinate(0, 0, 0), DirectionProvider.Directions.UP, Coordinate(1, 0, 0)),
        (Coordinate(0, 0, 0), DirectionProvider.Directions.DOWN, Coordinate(-1, 0, 0)),
    ])
    def test_get_adjacent_coordinate_given_direction_returns_the_adjacent_coordinate(
        self, origin_coordinate, given_direction, expected_value):
        result = self.direction_provider.get_adjacent_coordinate(
            origin_coordinate, given_direction)
        assert result == expected_value