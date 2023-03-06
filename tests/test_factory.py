import pytest
from src import factory, systems, components


class TestsForAreaForge:
    forge = factory.AreaForge(components.Maze("test", systems.Coordinate()))

    @pytest.mark.parametrize(
        "test_shape, wall_count",
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
    def test_CastArea_AreaShape_AreaHasEnoughWalls(self, test_shape, wall_count):
        area = self.forge.conjure_area(test_shape)
        assert len(area.content) == wall_count

    @pytest.mark.parametrize(
        "test_shape, wall_count",
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
    def test_CastArea_AreaTypes_AreaHasEnoughWalls(self, test_shape, wall_count):
        area = self.forge.conjure_area(test_shape)
        assert len(area.content) == wall_count


class TestForWizzard:
    mage = factory.Wizzard()

    def test_CastMaze_NameAndOrigin_ReturnsAMazeOnPosition(self):
        origin = systems.Coordinate(1,2,3)
        Labyrinth = self.mage.cast_maze("Test Labyrinth", origin, 5)
        assert isinstance(Labyrinth, components.Maze)
        assert origin == Labyrinth.position
