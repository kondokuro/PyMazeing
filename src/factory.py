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
from enum import Enum
from src.components import Area, Maze, Coordinate


class DirectionProvider:
    """Provides coordinates based on a direction."""
    
    class Directions(Enum):
        """The posible cardinal directions."""
        NORTH = "north"
        SOUTH = "south"
        EAST = "east"
        WEST = "west"
        UP = "up"
        DOWN = "down"

    def get_adjacent_coordinate(self, origin: Coordinate, direction: Directions) -> Coordinate:
        """Provides the adjacent coordinate based on the direction."""
        x, y, z = origin.x, origin.y, origin.z
        if direction == self.Directions.NORTH:
            z += 1
        elif direction == self.Directions.SOUTH:
            z -= 1
        elif direction == self.Directions.EAST:
            y += 1
        elif direction == self.Directions.WEST:
            y -= 1
        elif direction == self.Directions.UP:
            x += 1
        elif direction == self.Directions.DOWN:
            x -= 1
        return Coordinate(x, y, z)


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
        self._maze = Maze(name, origin)
        self.extend(origin)

    def extend(self, location: Coordinate) -> None:
        """Adds a new area to the maze being constructed."""
        self.maze.areas[location] = Area(location)
