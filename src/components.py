"""
Here we define all the pieces that compose mazes.
"""

import typing
from collections import namedtuple


Coordinate = namedtuple("Coordinate", ["x", "y", "z"])
Coordinate.__doc__ = "A point in space."
Coordinate.x.__doc__ = "The vertical position, representing a floor or basement."
Coordinate.y.__doc__ = "The horizontal position, representing east and west sides."
Coordinate.z.__doc__ = "The depth position, represent front and back locations."


class Area:
    """A place in the space of a maze."""

    def __init__(self, position: Coordinate) -> None:
        """
        Initializes a new Area instance.

        :param position: A Coordinate as the top left Area location.
        """
        if not isinstance(position, Coordinate):
            raise TypeError(f"Position must be a Coordinate, not {type(position)}")
        self._position = position
        self._passages = []

    @property
    def position(self) -> Coordinate:
        """The point in the maze where the area is located."""
        return self._position

    @property
    def passages(self) -> typing.List[Coordinate]:
        """The coordinates of areas connected to this one."""
        return self._passages


class Maze:
    """Labirinth with areas branching out and about."""

    def __init__(self, name: str, origin: Coordinate = None) -> None:
        """
        Instantiates a new Maze, set to the spatial origin.

        :param name: Give the Maze a description.
        :param origin: Desired initil location of the Maze.
        """
        self._origin = origin if origin is not None else Coordinate(0, 0, 0)
        self._name = name
        self._areas = {}

    @property
    def origin(self) -> Coordinate:
        """The maze's center."""
        return self._origin

    @property
    def name(self) -> str:
        """The name of the maze."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def areas(self) -> typing.Dict[Coordinate, Area]:
        """Areas in the maze organized by its coordinates."""
        return self._areas

    @property
    def occupied_spaces(self) -> typing.List[Coordinate]:
        """Maze coordinates containing areas."""
        return list(self.areas.keys())

