import pytest
from src.components import Area, Portal, Maze, MazeElement
from src.systems import Coordinate, Size


class TestForMazeElement:
    def test_OnInstantiation_NameIsNotString_RaisesTypeError(self):
        with pytest.raises(TypeError):
            MazeElement(2, Coordinate())  # type: ignore

    def test_OnInstantiation_PossitionIsNotCoordinate_RaisesTypeError(self):
        with pytest.raises(TypeError):
            MazeElement("bad location", (1, 2, 3))  # type: ignore


class TestForPortal:
    test_area = Area("test area", Coordinate(), Size(), Maze("test maze").id)

    def test_NewPortal_WithProperParameters_ReturnsaPortal(self):
        exit = Portal("the way out", Coordinate(), self.test_area, self.test_area)
        assert isinstance(exit, Portal)

    def test_NewPortal_OriginIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad orgin", Coordinate(), "not an area", self.test_area)  # type: ignore

    def test_NewPortal_DestinationIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal("bad destination", Coordinate(), self.test_area, "not an area")  # type: ignore


class TestForArea:

    def test_NewArea_WithProperParameters_ReturnsAnArea(self):
        maze_area = Area("room 2", Coordinate(), Size(), self.test_maze.id)
        assert isinstance(maze_area, Area)


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_NewMaze_MazeIsAtOrigin(self):
        assert self.test_maze.position == Coordinate()

    def test_NewMaze_WithInitialLocation_MazePossitionIsSet(self):
        direction = Coordinate(3, 3, 3)
        placed_maze = Maze("with location", direction)
        assert placed_maze.position == direction
