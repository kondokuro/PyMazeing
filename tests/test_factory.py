from src.components import Maze, Area, Coordinate
from src.factory import Forge

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
