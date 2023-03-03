import pytest
from src import factory, systems, components

class TestForWizzard:
    mage = factory.Wizzard()

    def test_CastMaze_NameAndOrigin_ReturnsAMazeOnPosition(self):
        origin = systems.Coordinate(1,2,3)
        Labyrinth = self.mage.cast_maze("Test Labyrinth", origin)
        assert isinstance(Labyrinth, components.Maze)
        assert origin == Labyrinth.position