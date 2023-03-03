"""
Create or modify mazes or its parts.

A Maze is composed of multiple areas.
A Maze must have at least one Portal.

Areas can have zero or many Portals
Areas coordinates are unique, as in no two zones have the same coordinates
Non connected Areas are separated by a space of size 1

Portals are located in Zones
Portals define entrance or exit from a Maze
Portals can connect different Mazes
"""
from src import components, systems


class Wizzard:
    """Generates mazes with just a few parametes."""

    def cast_maze(self, name: str, origin: systems.Coordinate, *args, **kwargs) -> components.Maze:
        """Generates an initial maze to build up from."""
        return components.Maze(name, origin)

    def cast_area(
        self, position: systems.Coordinate, size: systems.Size) -> components.Area:
        """
        Creates areas surrounded by walls based on the parameters provided.

        :param position: Coordinates from the center of the area.
        :param size: Space the area will occupy
        """

        # must check if the maze space is free.. so maybe this should be part of the mase class
        pass

    def branch(self, area: components.Area) -> list[components.Area]:
        """The idea here is to take an area as the starting point and build a group of areas."""
        pass
