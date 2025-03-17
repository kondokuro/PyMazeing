import pytest
from src.components import Maze, Area, Coordinate
from src.factory import Forge
from src.navigation import Directions as dir
from src.navigation import get_adjacent_coordinate
from src.display import AssciiMazeRenderer, DescriptionMazeRenderer


class TestAssciiMazeRenderer:

    def test_show_maze_given_maze_returns_string(self):
        expected = ""
        maze = Maze()
        renderer = AssciiMazeRenderer(maze)
        result = renderer.render()
        assert result == expected

    def test_show_area_given_area_returns_string(self):
        expected = ""
        maze = Maze()
        renderer = AssciiMazeRenderer(maze)
        result = renderer.show_area(maze.areas[0])
        assert result == expected


class TestDescriptionMazeRenderer:

    def test_show_maze_given_maze_floor_returns_description_of_all_areas_in_floor(self):
        expected = """This are the areas of floor 1:
at Coordinate(x=1, y=0, z=0), in this area there is a way east.
at Coordinate(x=1, y=1, z=0), in this area there is a way west and north.
at Coordinate(x=1, y=1, z=1), in this area there is a way south and east.
at Coordinate(x=1, y=2, z=1), in this area there is a way west.
"""
        maze = Maze()
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_maze(floor=1)
        assert result == expected

    @pytest.mark.parametrize("passage_directions, expected", [
        ((dir.NORTH,), 
         "in this area there is a way north."),
        ((dir.NORTH, dir.SOUTH,), 
         "in this area there is a way north or south."),
        ((dir.NORTH, dir.SOUTH, dir.EAST,), 
         "in this area there is a way north, south or east."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST,), 
         "in this area there is a way north, south, east or west."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST, dir.UP,), 
         "in this area there is a way north, south, east, west or up."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST, dir.UP, dir.DOWN,), 
         "in this area there is a way north, south, east, west, up or down."),
    ])
    def test_show_area_given_area_returns_passage_based_description(self, passage_directions, expected):
        maze = Maze("testing description")
        area = Area(Coordinate(0, 0, 0))
        for direction in passage_directions:
            if direction == dir.NORTH:
                area.passages.append(Coordinate(0, 0, area.position.z+1))
            if direction == dir.SOUTH:
                area.passages.append(Coordinate(0, 0, area.position.z-1))
            if direction == dir.EAST:
                area.passages.append(Coordinate(0, area.position.y+1, 0))
            if direction == dir.WEST:
                area.passages.append(Coordinate(0, area.position.y-1, 0))
            if direction == dir.UP:
                area.passages.append(Coordinate(area.position.x+1, 0, 0))
            if direction == dir.DOWN:
                area.passages.append(Coordinate(area.position.x-1, 0, 0))
        maze.areas[area.position] = area
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_area(area.position)
        assert result == expected

    def test_show_are_given_area_with_portal_returns_portal_description(self):
        maze = Maze("testing description")
        area = Area(Coordinate(0, 0, 0), with_portal=True)
        maze.areas[area.position] = area
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_area(area.position)
        assert result == "in this area there is a portal and a way east."

    def test_show_area_given_empty_space_coordinate_returns_empty_description(self):
        maze = Maze("testing description")
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_area(Coordinate(1, 2, 3))
        assert result == "empty space..."

    def test_show_are_given_non_connected_area_returns_dead_end_description(self):
        maze = Maze("testing description")
        area = Area(Coordinate(0, 0, 0))
        maze.areas[area.position] = area
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_area(area.position)
        assert result == "dead end..."