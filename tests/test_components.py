import pytest
from src.components import Area, Maze, Coordinate



class TestForArea:

    def test_new_area_position_is_not_coordinate_raises_type_error(self):
        with pytest.raises(TypeError):
            Area((1, 2, 3))


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_creating_new_maze_without_location_parameter_has_origin_at_zero(self):
        assert self.test_maze.origin == Coordinate(0,0,0)

    def test_creating_new_maze_with_initial_location_has_origin_at_location(self):
        direction = Coordinate(3, 3, 3)
        placed_maze = Maze("with location", direction)
        assert placed_maze.origin == direction

    def test_ocupied_spaces_returns_list_of_coordinates(self):
        assert isinstance(self.test_maze.occupied_spaces, list)
        assert all(isinstance(c, Coordinate) for c in self.test_maze.occupied_spaces)
