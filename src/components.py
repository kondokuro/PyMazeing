"""
Here we define all the pieces that compose mazes.
"""
from src import systems
from uuid import uuid4, UUID


class Positionable:
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

    def __repr__(self) -> str:
        return f"{self.name} at {self.position}"


class Portal(Positionable):
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
        maze_id: UUID,
    ) -> None:
        """
        Initializes a new SpatialContainer instance.

        :param name: The Areas' name.
        :param position: A Coordinate as the top left Area location.
        :param size: The space the area occupies in coordinates.
        :param maze: The ID of maze holding the area.
        """
        super().__init__(name, position)
        if size is not None and not isinstance(size, systems.Size):
            raise TypeError("Parameter 'size' must be of type Size.")
        self.size = size
        if maze_id is not None and not isinstance(maze_id, UUID):
            raise TypeError("Parameter 'maze_id' must be of type Maze.")
        self.maze_id = maze_id
        self._content = systems.TypedList(Positionable)

    @property
    def content(self) -> systems.TypedList:
        return self._content


class Maze(Positionable):
    """Labirinth with areas branching out."""

    def __init__(self, name: str, origin: systems.Coordinate = systems.Coordinate()) -> None:
        """
        Instantiates a new Maze, set to the spatial origin.

        :param name: The name of the Maze.
        """
        super().__init__(name, origin)
        self.areas = systems.TypedList(Area)
        #self.space = systems.TypedList(systems.Coordinate)

    # @property
    # def occupied_space(self) -> systems.TypedList:
    #     """Coordinates occupied by areas."""
    #     return self._occupied_space

    # @property
    # def available_space(self) -> systems.TypedList:
    #     """"""
    #     return self._available_space
