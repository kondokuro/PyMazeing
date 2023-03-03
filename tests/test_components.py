import pytest
from src.components import Area, Portal, Maze, Positionable
from src.systems import Coordinate, Size


class TestForPositionable:
    def test_OnInstantiation_NameIsNotString_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Positionable(2, Coordinate())

    def test_OnInstantiation_PossitionIsNotCoordinate_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Positionable("bad location", (1, 2, 3))


class TestForPortal:
    test_area = Area("test area", Coordinate(), Size(), Maze("test maze").id)

    def test_OnInstantiation_WithProperParameters_ReturnsaPortal(self):
        exit = Portal("the way out", Coordinate(), self.test_area, self.test_area)
        assert isinstance(exit, Portal)

    def test_OnInstantiation_OriginIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad orgin", Coordinate(), "not an area", self.test_area)

    def test_OnInstantiation_DestinationIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad destination", Coordinate(), self.test_area, "not an area")


class TestForArea:
    test_maze = Maze("labirinth")

    def test_OnInstantiation_WithProperParameters_ReturnsAnArea(self):
        maze_area = Area("room 2", Coordinate(), Size(), self.test_maze.id)
        assert isinstance(maze_area, Area)

    def test_OnInstantiation_MazeIdIsNotUuid_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Area("invalid", Coordinate(), Size(), "not a uuid")


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_OnInstantiation_WithProperParamenters_ReturnsAMaze(self):
        assert isinstance(self.test_maze, Maze)

    def test_OnInstantiation_MazeIsAtOrigin(self):
        assert self.test_maze.position == Coordinate()

    def test_OnInstantiation_WithInitialLocation_MazePossitionIsSet(self):
        direction = Coordinate(3, 3, 3)
        placed_maze = Maze("with location", direction)
        assert placed_maze.position == direction
