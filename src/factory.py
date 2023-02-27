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


class AreaFactory:

    def get_area(self, position: systems.Coordinate, size: systems.Size) -> components.Area:
        """
        Creates areas surrounded by walls based on the parameters provided.
        
        :param position: Coordinates from the center of the area.
        :param size: Space the area will occupy
        """

        match size: 
