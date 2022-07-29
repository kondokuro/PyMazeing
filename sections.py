"""
Module containing all the pieces needed to represent a maze.
"""
from dataclasses import dataclass
from enum import Enum


PortalKind = Enum('PortalKind', 'ENTRANCE CONNECTION EXIT')


@dataclass
class Portal:
    """Defines a maze entrance, exit or a connection between mazes."""
    kind: PortalKind
    maze: str


@dataclass
class Area:
    """A single space in a hall."""
    coordinates: tuple
    portal: Portal


@dataclass
class Hall:
    """A passage in the maze, divided into areas."""
    areas: list(Area)
    is_path: bool


@dataclass
class Maze:
    """The labyrinth."""
    name: str
    halls: list(Hall)
