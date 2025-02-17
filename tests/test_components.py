import pytest
from src.components import Area, Portal, Maze, MazeElement
from src.systems import Coordinate, Size


class TestForMazeElement:
    def test_OnInstantiation_NameIsNotString_RaisesTypeError(self):
        with pytest.raises(TypeError):
            MazeElement(Coordinate())  # type: ignore

    def test_OnInstantiation_PossitionIsNotCoordinate_RaisesTypeError(self):
        with pytest.raises(TypeError):
            MazeElement((1, 2, 3))  # type: ignore


class TestForPortal:
    test_area = Area("test area", Coordinate(), Size())

    def test_new_portal_valid_parameters_returns_portal(self):
        exit_way = Portal(Coordinate(), self.test_area, self.test_area)
        assert isinstance(exit_way, Portal)

    def test_NewPortal_OriginIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal(Coordinate(), "not an area", self.test_area)  # type: ignore

    def test_NewPortal_DestinationIsNotArea_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Portal(Coordinate(), self.test_area, "not an area")  # type: ignore


class TestForArea:
    test_maze = Maze("Labirinth")

    def test_NewArea_NameIsNotString_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Area(2, Coordinate(), Size())  # type: ignore

    def test_NewArea_PositionIsNotCoordinate_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Area("bad location", (1, 2, 3), Size())  # type: ignore

    def test_NewArea_SizeIsNotSize_RaisesTypeError(self):
        with pytest.raises(TypeError):
            Area("bad size", Coordinate(), (1, 2, 3))  # type: ignore


class TestForMaze:
    test_maze = Maze("Labirinth")

    def test_NewMaze_MazeIsAtOrigin(self):
        assert self.test_maze.origin == Coordinate()

    def test_NewMaze_WithInitialLocation_MazePossitionIsSet(self):
        direction = Coordinate(3, 3, 3)
        placed_maze = Maze("with location", direction)
        assert placed_maze.origin == direction
