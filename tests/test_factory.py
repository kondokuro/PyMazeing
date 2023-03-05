import pytest
from src import factory, systems, components

class TestForWizzard:
    mage = factory.Wizzard()

    def test_CastMaze_NameAndOrigin_ReturnsAMazeOnPosition(self):
        origin = systems.Coordinate(1,2,3)
        Labyrinth = self.mage.cast_maze("Test Labyrinth", origin, 5)
        assert isinstance(Labyrinth, components.Maze)
        assert origin == Labyrinth.position

    @pytest.mark.parametrize(
            "shape, walls",
            [
                (factory.AreaShape.CLOSED, 8),
                (factory.AreaShape.DEAD_END_E, 7),
                (factory.AreaShape.DEAD_END_N, 7),
                (factory.AreaShape.DEAD_END_W, 7),
                (factory.AreaShape.DEAD_END_S, 7),
                (factory.AreaShape.CORNER_EN, 6),
                (factory.AreaShape.CORNER_NW, 6),
                (factory.AreaShape.CORNER_SE, 6),
                (factory.AreaShape.CORNER_WS, 6),
                (factory.AreaShape.WAY_NS, 6),
                (factory.AreaShape.WAY_WE, 6),
                (factory.AreaShape.JUNCTION_WNE, 5),
                (factory.AreaShape.JUNCTION_WNE, 5),
                (factory.AreaShape.CROSSROAD, 4),
            ],
        )
    def test_CastArea_AreaTypes_AreaHasEnoughWalls(self, shape, walls):
        labyrinth = self.mage.cast_maze("corn", systems.Coordinate(), 5)
        area = self.mage.cast_area(labyrinth, shape, systems.Coordinate())
        assert len(area.content) == walls

    def test_CastArea_InitialLocation_AreaSizeIsThree(self):
        initial = systems.Coordinate(5, -4)
        area = self.mage.cast_area(factory.AreaShape.CLOSED, initial)
        assert area.size.length == 3
        assert area.size.height == 3