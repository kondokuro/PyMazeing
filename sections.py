"""
Module containing all the pieces needed to represent a maze.
"""
from dataclasses import dataclass
from enum import Enum


PortalKind = Enum('PortalKind', 'ENTRANCE CONNECTION EXIT')


@dataclass
class Portal:
    """Definition of a maze entrance, exit or a connection between mazes."""
    kind: PortalKind
    maze: str


@dataclass
class Area:
    """The representation of a single space in a maze.
    There are two types of areas portals and rooms, portals represent an
    entrance or exist point of the maze.
    """
    coordinates: tuple
    portal: Portal


@dataclass
class Hall:
    """Representation of a passage in the maze, divided into areas. 
    Considered as a path If any of its areas have a portal, otherwise as a branch.
    """
    areas: list(Area)
    is_path: bool


@dataclass
class Maze:
    """The data representation of a labyrinth."""
    name: str
    halls: list(Hall)
