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

    def test_show_maze_given_maze_returns_string(self):
        expected = ""
        maze = Maze()
        renderer = DescriptionMazeRenderer(maze)
        result = renderer.show_maze()
        assert result == expected

    @pytest.mark.parametrize("passage_directions, expected", [
        ((dir.NORTH,), 
         "in this area there is a way north."),
        ((dir.NORTH, dir.SOUTH,), 
         "in this area there is a way north and south."),
        ((dir.NORTH, dir.SOUTH, dir.EAST,), 
         "in this area there is a way north, south and east."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST,), 
         "in this area there is a way north, south, east and west."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST, dir.UP,), 
         "in this area there is a way north, south, east, west and up."),
        ((dir.NORTH, dir.SOUTH, dir.EAST, dir.WEST, dir.UP, dir.DOWN,), 
         "in this area there is a way north, south, east, west, up and down."),
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