"""
Here we define all the pieces to compose mazes.
"""
import typing
from src import systems


class PositionableEntity:
    """
    Representation of an entity located in a place in space.
    """

    def __init__(self, name: str, position: systems.Coordinate) -> None:
        """
        Initializes a new PositionableEntity instance.

        :param name: A string representing the name of the entity.
        :param position: A Coordinate object representing the position of the entity.
        """
        self.name = name
        self.position = position


class SpatialContainer(PositionableEntity):
    """
    Class that represents an entity located in a place in space, able to contain other
    elements of a specific type on its own space.
    """

    def __init__(
        self,
        name: str,
        position: systems.Coordinate,
        size: systems.Size,
        holder: typing.Optional["SpatialContainer"] = None,
    ) -> None:
        """
        Initializes a new SpatialContainer instance.

        :param name: A string representing the name of the container.
        :param position: A Coordinate object representing the position of the container.
        :param size: A Size object representing the size of the container.
        :param holder: A SpatialContainer containing the current container.
        """
        super().__init__(name, position)
        self.content = systems.TypedList(PositionableEntity)
        self.size = size
        if holder is not None and not isinstance(holder, SpatialContainer):
            raise TypeError("Parameter 'holder' must be of type SpatialContainer.")
        self.holder = holder


class Portal(PositionableEntity):
    """
    Class that represents a connection between two locations in a maze.
    """

    def __init__(
        self,
        name: str,
        position: systems.Coordinate,
        origin: PositionableEntity,
        destination: PositionableEntity,
    ) -> None:
        """
        Initializes a new Portal instance.

        :param name: A string representing the name of the portal.
        :param position: A Coordinate object representing the position of the portal.
        :param origin: A PositionableEntity object representing the origin of the portal.
        :param destination: A PositionableEntity object representing the destination of the portal.
        """
        super().__init__(name, position)
        self.origin = origin
        self.destination = destination
