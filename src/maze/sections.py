"""
Module containing all the pieces needed to represent a maze.
"""
from dataclasses import dataclass, field
from enum import Enum

"""Simple tag to identify the portal purpose."""
PortalType = Enum('PortalType', 'ENTRANCE EXIT CONNECTION')

"""The different hall structures:
Path has entrance and exit areas
Exit only has an exit area
Branch has no portal areas
"""
HallType = Enum('HallType', 'PATH BRANCH')


@dataclass
class Coordinates:
    """Simple definition of coordinates for maps."""
    X: int = 0
    Y: int = 0
    Z: int = 0


@dataclass
class Portal:
    """Defines a maze entrance, exit or a connection between mazes."""
    #kind: PortalType
    maze: str = ''
    # tuple of strings containing all the maze names the portal connects to


@dataclass
class Area:
    """A single space in a hall."""
    coordinates: Coordinates = Coordinates()
    portal: Portal = None


@dataclass
class Hall:
    """A passage in the maze, divided into areas."""
    areas: list[Area] = field(default_factory=list)


@dataclass
class Maze:
    """The labyrinth."""
    name: str
    halls: list[Hall] = field(default_factory=list)
