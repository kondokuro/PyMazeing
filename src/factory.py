"""
Create or modify mazes or its parts.

A Maze is composed of one or many Halls
A Maze must have at least one Portal

A Hall is divided into one or many Zones
Paths are Halls with at least a Zone with a Portal
Branches are Halls where no Zone has a Portal

Zones only belong to a single Hall ? who owns the crossroad
Zones can have zero or many Portals
Zones coordinates are unique, as in no two zones have the same coordinates

Portals are located in Zones
Portals define entrance or exit from a Maze
Portals can connect different Mazes

"""
from src import components

def create_maze(*args, **kwargs) -> components.SpatialContainer:
    """
    Generata a random maze based on the provided details.
    """
    pass


def add_branch(hall: components.SpatialContainer, *args, **kwargs) -> components.SpatialContainer:
    """
    Adds a new branch to an existing hall, based on the provided details.
    """
    pass

