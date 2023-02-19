"""
Module containing all the pieces needed to represent a maze.
"""
import typing
from src import systems


class Portal(typing.NamedTuple):
    """Defines a maze entrance, exit or a connection between mazes."""

    destination: str


class SpatialEntity(typing.Protocol):
    """Representation of a place in space that can contain other elements."""

    name: str
    position: systems.Coordinate
    area: systems.Size
    content: systems.containers.TypedList
