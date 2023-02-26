"""
Here we define all the pieces that compose mazes.
"""
import typing
from src import systems
from uuid import uuid4


class PositionableEntity:
    """An entity located in a place in space."""

    def __init__(self, name: str, position: systems.Coordinate) -> None:
        """
        Initializes a new PositionableEntity instance with an unique ID.

        :param name: The entitys' name.
        :param position: A Coordinate for the location of the entity.
        """
        self.id = uuid4()
        if name is not None and not isinstance(name, str):
            raise TypeError("Parameter 'name' must be of type str.")
        self.name = name
        if position is not None and not isinstance(position, systems.Coordinate):
            raise TypeError("Parameter 'position' must be of type Coordinate.")
        self.position = position


class Portal(PositionableEntity):
    """Connection between two Maze Areas."""

    def __init__(
        self,
        name: str,
        position: systems.Coordinate,
        origin: "Area",
        destination: "Area",
    ) -> None:
        """
        Initializes a new Portal instance.

        :param name: A string to name the portal.
        :param position: A Coordinate for the position of the portal.
        :param origin: An Area as the the portal entrance.
        :param destination: An Area as the portal exit.
        """
        super().__init__(name, position)
        if origin is not None and not isinstance(origin, Area):
            raise TypeError("Parameter 'origin' must be of type Area.")
        self.origin = origin
        if destination is not None and not isinstance(destination, Area):
            raise TypeError("Parameter 'destination' must be of type Area.")
        self.destination = destination


class Area(PositionableEntity):
    """A zone in space able to contain other positionalbe entities."""

    def __init__(
        self,
        name: str,
        position: systems.Coordinate,
        size: systems.Size,
        maze: "Maze",
    ) -> None:
        """
        Initializes a new SpatialContainer instance.

        :param name: The Areas' name.
        :param position: A Coordinate as the Area location.
        :param size: A Size object.
        :param maze: The maze holding the area.
        """
        super().__init__(name, position)
        if size is not None and not isinstance(size, systems.Size):
            raise TypeError("Parameter 'size' must be of type Size.")
        self.size = size
        if maze is not None and not isinstance(maze, Maze):
            raise TypeError("Parameter 'maze' must be of type Maze.")
        self.maze = maze
        self._entities = systems.TypedList(PositionableEntity)
        self._occupied_space = systems.TypedList(systems.Coordinate)
        self._available_space = systems.TypedList(systems.Coordinate)

    @property
    def entities(self) -> systems.TypedList:
        return self._entities

    @property
    def occupied_space(self) -> systems.TypedList:
        """"""
        return self._occupied_space

    @property
    def available_space(self) -> systems.TypedList:
        """"""
        return self._available_space
    

class Maze(PositionableEntity):
    """Labirinth with areas branching out."""

    def __init__(self, name: str) -> None:
        """
        Instantiates a new Maze, set to the spatial origin.

        :param name: The name of the Maze.
        """
        super().__init__(name, systems.Coordinate(0,0,0))
        self.areas = systems.TypedList(Area)