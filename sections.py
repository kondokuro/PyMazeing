"""
Module containing all the pieces needed to represent a maze.
"""
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


@dataclass
class Portal:
    """Defines a maze entrance, exit or a connection between mazes."""
    kind: PortalType
    maze: str


@dataclass
class Area:
    """A single space in a hall."""
    coordinates: tuple[int]
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
