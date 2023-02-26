import pytest
from src.components import Area, Portal, Maze, PositionableEntity
from src.systems import Coordinate, Size


class TestForPositionalEntity:
    def test_OnInstantiation_NameIsNotString_RaisesTypeError(self):
        with pytest.raises(TypeError):
            PositionableEntity(2, Coordinate(1,1,1))

    def test_OnInstantiation_PossitionIsNotCoordinate_RaisesTypeError(self):
        with pytest.raises(TypeError):
            PositionableEntity("bad location", (1, 2, 3))


class TestForPortals:
    test_area = Area("test area", Coordinate(0,0,0), Size(1,1,1), Maze("test maze"))

    def test_OnInstantiation_WithProperParameters_ReturnsaPortal(self):
        exit = Portal("the way out", Coordinate(5,5,5), self.test_area, self.test_area)
        assert isinstance(exit, Portal)

    def test_OnInstantiation_OriginIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad orgin", Coordinate(1, 1, 1), "not an area", self.test_area)

    def test_OnInstantiation_DestinationIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad destination", Coordinate(1, 2, 3), self.test_area, "not an area")


class TestForArea:
    test_maze = Maze("labirinth")

    def test_OnInstantiation_WithProperParameters_ReturnsAnArea(self):
        maze_area = Area("room 2", Coordinate(1,2,2), Size(1,1,1), self.test_maze)
        assert isinstance(maze_area, Area)

    def test_OnInstantiation_MazeIsNotAMaze_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Area("invalid", Coordinate(1, 2, 3), Size(2, 2, 2), "not a maze")


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_OnInstantiation_WithProperParamenters_ReturnsAMaze(self):
        assert isinstance(self.test_maze, Maze)

    def test_OnInstantiation_MazeIsAtOrigin(self):
        assert self.test_maze.position == Coordinate(0,0,0)

