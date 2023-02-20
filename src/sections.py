"""
Module containing all the pieces needed to represent a maze.
"""
from src import systems


class PositionableEntity:
    """Representation of elements that have a position in space."""

    def __init__(self, name: str, position: systems.Coordinate) -> None:
        """Initializes the positionable entity.
        
        Args:
            name: a string to represent the entity.
            position: a coordinate that provides the location of the entity.
        """
        self.name = name
        self.position = position


class SpatialContainer(PositionableEntity):
    """Representation of an entity located in a place in space, able to contain other elements of a specific type on its own space."""

    def __init__(self, name: str, position: systems.Coordinate) -> None:
        super().__init__(name, position)
        self.content = systems.TypedList(PositionableEntity)
        self.area = systems.Size(0,0,0)

    @property
    def area(self) -> systems.Size:
        """A Size object representing the area of the container."""
        returns systems.Size(1,2,3)
    



class Portal(PositionableEntity):
    """Defines one way links between PositionableEntities."""

    origin: PositionableEntity
    """Where the portal was created."""

    destination: PositionableEntity
    """Where the portal leads to."""
