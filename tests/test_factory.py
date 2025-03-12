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

    def test_annex_given_existing_origin_adds_destination_and_sets_passages(self):
        origin = Coordinate(1, 2, 3)
        destination = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", origin)

        self.builder.annex(origin, destination)

        assert destination in self.builder.maze.areas
        assert destination in self.builder.maze.areas[origin].passages
        assert origin in self.builder.maze.areas[destination].passages

    def test_annex_given_new_coordinates_adds_new_areas_and_sets_passages(self):
        origin = Coordinate(1, 2, 3)
        destination = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(0, 0, 0))

        self.builder.annex(origin, destination)

        assert origin in self.builder.maze.areas
        assert destination in self.builder.maze.areas
        assert destination in self.builder.maze.areas[origin].passages
        assert origin in self.builder.maze.areas[destination].passages

    def test_annex_given_new_origin_existing_destination_adds_origin_and_sets_passages(self):
        origin = Coordinate(1, 2, 3)
        destination = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(0, 0, 0))
        self.builder.extend(destination)

        self.builder.annex(origin, destination)

        assert origin in self.builder.maze.areas
        assert destination in self.builder.maze.areas[origin].passages
        assert origin in self.builder.maze.areas[destination].passages

    def test_annex_given_existing_coordinates_sets_passages(self):
        origin = Coordinate(1, 2, 3)
        destination = Coordinate(1, 2, 4)
        self.builder.start_maze("Test Labyrinth", Coordinate(0, 0, 0))
        self.builder.extend(origin)
        self.builder.extend(destination)

        self.builder.annex(origin, destination)

        assert destination in self.builder.maze.areas[origin].passages
        assert origin in self.builder.maze.areas[destination].passages
