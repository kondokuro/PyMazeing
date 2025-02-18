import pytest
from src.core import Coordinate
from src.components import Maze
from src.factory import AreaShape, AreaForge, Wizzard


class TestsForAreaForge:
    forge = AreaForge(Maze("test", Coordinate()))

    @pytest.mark.parametrize(
        "test_shape, wall_count",
        [
            (AreaShape.CLOSED, 8),
            (AreaShape.DEAD_END_E, 7),
            (AreaShape.DEAD_END_N, 7),
            (AreaShape.DEAD_END_W, 7),
            (AreaShape.DEAD_END_S, 7),
            (AreaShape.CORNER_EN, 6),
            (AreaShape.CORNER_NW, 6),
            (AreaShape.CORNER_SE, 6),
            (AreaShape.CORNER_WS, 6),
            (AreaShape.WAY_NS, 6),
            (AreaShape.WAY_WE, 6),
            (AreaShape.JUNCTION_WNE, 5),
            (AreaShape.JUNCTION_WNE, 5),
            (AreaShape.CROSSROAD, 4),
        ],
    )
    def test_CastArea_AreaShape_AreaHasEnoughWalls(self, test_shape, wall_count):
        area = self.forge.conjure_area(test_shape)
        assert len(area.content) == wall_count

class TestForWizzard:
    mage = Wizzard()

    def test_CastMaze_NameAndOrigin_ReturnsAMazeOnPosition(self):
        origin = Coordinate(1,2,3)
        Labyrinth = self.mage.cast_maze("Test Labyrinth", origin, 5)
        assert isinstance(Labyrinth, Maze)
        assert origin == Labyrinth.origin

class TestForBuilder:

    def test_start_maze_sets_a_maze_instance(self):
        builder = Builder()
        builder.start_maze("Test Labyrinth", Coordinate(1,2,3))
        assert isinstance(builder.maze, Maze)