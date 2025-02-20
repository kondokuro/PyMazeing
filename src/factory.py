"""
Create or modify mazes or its parts.

A Maze is composed of multiple areas.
A Maze must have at least one Entrance.

Areas can have zero or many Portals
Areas coordinates are unique, no two have the same coordinates
Areas are separated by walls
Walls are objects inside of the area space

Portals are located in Areas
Portals define entrance or exit from a Maze
Portals connect two Mazes
"""
from src.components import Area, Maze, Coordinate


class Forge:
    """Constructs mazes from scratch."""

    def __init__(self):
        self.maze = None

    def start_maze(self, name: str, origin: Coordinate) -> None:
        """Begins the construction process of a maze, creating one with a single area, its entrance."""
        self.maze = Maze(name, origin)
        self.add_area_at(origin)

    def add_area_at(self, location: Coordinate) -> None:
        """Adds a new area to the maze being constructed."""
        self.maze.areas[location] = Area(location)
