"""
Module containing all the pieces needed to represent a maze.
"""
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum

"""Simple tag to identify the portal purpose."""
PortalType = Enum('PortalType', 'ENTRANCE EXIT CONNECTION')

"""The different hall structures:
Path has entrance and exit areas
Exit only has an exit area
Branch has no portal areas
"""
HallType = Enum('HallType', 'PATH EXIT BRANCH')

"""Simple definition of plane coordinates for maps."""
Coordinates = namedtuple('Coordinates', ['X', 'Y', 'Z'], defaults=[0, 0, 0])


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
    areas: tuple[Area]


@dataclass
class Maze:
    """The labyrinth."""
    name: str
    halls: tuple[Hall]
