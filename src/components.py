"""
Here we define all the pieces that compose mazes.
"""
from src import systems
from uuid import uuid4, UUID
from typing import Protocol
from abc import ABC, abstractmethod

class Positionable(Protocol):
    @property
    def position(self) -> "systems.Coordinate":
        """The entity's position."""

class MazeElement(ABC):
    """An entity located in a place in the space of a maze."""

    @property
    def position(self) -> "systems.Coordinate":
        """The entity's position."""
        return self._position;

    @property
    def id(self) -> UUID:
        """The entity's unique identifier."""
        return self._id;

    def __init__(self, position: systems.Coordinate) -> None:
        """
        Initializes a new PositionableEntity instance with an unique ID.

        :param name: The entitys' name.
        :param position: A Coordinate for the location of the entity.
        """
        self._id = uuid4()
        if position is not None and not isinstance(position, systems.Coordinate):
            raise TypeError("Parameter 'position' must be of type Coordinate, but got {}".format(type(position)))
        self._position = position
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, at {self.position})"

    def __str__(self) -> str:
        return repr(self);



class Portal(MazeElement):
    """Connection between two Maze Areas."""

    @property
    def origin(self) -> "Area":
        """The portal entrance."""
        return self._origin
    
    @origin.setter
    def origin(self, origin: "Area") -> None:
        self._origin = origin

    @property
    def destination(self) -> "Area":
        """The portal exit."""
        return self._destination
    
    @destination.setter
    def destination(self, destination: "Area") -> None:
        self._destination = destination


    def __init__(
        self,
        position: systems.Coordinate,
        origin: "Area",
        destination: "Area",
    ) -> None:
        """
        Initializes a new Portal instance.

        :param position: A Coordinate for the position of the portal.
        :param origin: An Area as the the portal entrance.
        :param destination: An Area as the portal exit.
        """
        super().__init__(position)
        if origin is not None and not isinstance(origin, Area):
            raise TypeError("Parameter 'origin' must be of type Area, but got {}".format(type(origin)))
        self._origin = origin
        if destination is not None and not isinstance(destination, Area):
            raise TypeError("Parameter 'destination' must be of type Area, but got {}".format(type(destination)))
        self._destination = destination
    

class Wall(Positionable):
    """Division between adjasent areas."""

    def __init__(self, name: str, position: systems.Coordinate, size: systems.Size) -> None:
        super().__init__(name, position)
        self.size = size
        

class Area(Positionable):
    """A place in space able to contain other positionalbe entities."""

    def __init__(
        self,
        name: str,
        position: systems.Coordinate,
        size: systems.Size,
    ) -> None:
        """
        Initializes a new SpatialContainer instance.

        :param name: The Areas' name.
        :param position: A Coordinate as the top left Area location.
        :param size: The space the area occupies in the maze.
        """
        super().__init__(name, position)
        if size is not None and not isinstance(size, systems.Size):
            raise TypeError("Parameter 'size' must be of type Size.")
        self.size = size

    @property
    def content(self) -> systems.TypedList:
        """Entities in the area."""
        if (self._content is None):
            self._content = systems.TypedList(MazeElement)
        return self._content


class Maze:
    """Labirinth with areas branching out."""

    def __init__(self, name: str, origin: systems.Coordinate = systems.Coordinate()) -> None:
        """
        Instantiates a new Maze, set to the spatial origin.

        :param name: The name of the Maze.
        """
        self._origin = origin
        self._name = name

    @property
    def origin(self) -> systems.Coordinate:
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
    def areas(self) -> systems.TypedList:
        """Areas in the maze."""
        if (self._areas is None):
            self._areas = systems.TypedList(Area)
        return self._areas

    @property
    def occupied_space(self) -> systems.TypedList:
        """Coordinates with areas."""
        if (self._occupied_space is None):
            self._occupied_space = systems.TypedList(systems.Coordinate)
        return self._occupied_space
