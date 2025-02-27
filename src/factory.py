"""
Create or modify mazes or its parts.

A Maze is composed of multiple areas.
A Maze must have at least one Entrance.

Areas coordinates are unique, no two have the same coordinates

Portals are located in Areas
Portals define entrance or exit from a Maze
Portals connect two Mazes
"""
from src.components import Area, Maze, Coordinate


class Forge:
    """Constructs mazes from scratch."""

    def __init__(self):
        self._maze = None

    @property
    def maze(self) -> Maze:
        """The maze being constructed."""
        return self._maze
    

    def start_maze(self, name: str, origin: Coordinate) -> None:
        """Begins the construction process of a maze, creating one with a single area, its entrance."""
        self._maze = Maze(name)
        self.extend(origin, with_portal=True)

    def extend(self, location: Coordinate, with_portal: bool = False) -> None:
        """Adds a new area to the maze being constructed."""
        if location not in self.maze.areas:
            self.maze.areas[location] = Area(location, with_portal)
