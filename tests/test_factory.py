import pytest
from src.components import Maze, Area, Coordinate
from src.factory import Forge


class TestForForge:

    builder = Forge()

    def test_start_maze_sets_a_maze_instance(self):
        self.builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        assert isinstance(self.builder.maze, Maze)

    def test_start_maze_adds_an_entrance_to_the_maze(self):
        entrance = Coordinate(1,2,3)
        self.builder.start_maze("Test Labyrinth", entrance)
        assert True == self.builder.maze.areas.get(entrance).has_portal

    def test_extend_given_coordinates_sets_an_area_in_the_maze(self):
        given_coordinates = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        self.builder.extend(given_coordinates)
        assert isinstance(self.builder.maze.areas[given_coordinates], Area)

    def test_extend_as_portal_adds_a_portal_area_in_the_maze(self):
        given_coordinates = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        self.builder.extend(given_coordinates, with_portal=True)
        assert self.builder.maze.areas.get(given_coordinates).has_portal is True

    def test_exted_used_location_does_not_replace_area(self):
        given_coordinates = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        self.builder.extend(given_coordinates)
        self.builder.extend(given_coordinates, with_portal=True)
        assert self.builder.maze.areas[given_coordinates].has_portal is False
