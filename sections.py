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

Coordinates = namedtuple('Coordinates', ['X', 'Y', 'Z'], defaults=[0, 0, 0])


@dataclass
class Portal:
    """Defines a maze entrance, exit or a connection between mazes."""
    kind: PortalType
    maze: str


@dataclass
class Area:
    """A single space in a hall."""
    coordinates: Coordinates
    portal: Portal


@dataclass
class Hall:
    """A passage in the maze, divided into areas."""
    areas: tuple[Area]


@dataclass
class Maze:
    """The labyrinth."""
    name: str
    halls: list[Hall]
