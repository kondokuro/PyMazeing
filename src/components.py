"""
Here we define all the pieces that compose mazes.
"""
from typing import NamedTuple, List, Dict


class Coordinate(NamedTuple):
    """
    A point in space.
    
    :param x: The vertical position, representing a floor or basement.
    :param y: The horizontal position, representing east and west sides.
    :param z: The depth position, represent front and back locations.
    """
    x: int
    y: int
    z: int


class Area:
    """A place in the space of a maze."""

    def __init__(self, position: Coordinate, with_portal: bool = False) -> None:
        """
        Initializes a new Area instance.

        :param position: A Coordinate as the top left Area location.
        :param with_portal: If the area has a portal, to mark it as entrance or exit.
        """
        if not isinstance(position, Coordinate):
            raise TypeError(f"Position must be a Coordinate, not {type(position)}")
        self._position = position
        self._passages = []
        self.has_portal = with_portal

    @property
    def position(self) -> Coordinate:
        """The point in the maze where the area is located."""
        return self._position

    @property
    def passages(self) -> List[Coordinate]:
        """The coordinates of areas connected to this one."""
        return self._passages
    
    def __repr__(self) -> str:
        return f"Area object at {self.position}" + (" with portal" if self.has_portal else "")
    
    def __str__(self) -> str:
        return f"Area at {self.position}" + (" with portal" if self.has_portal else "")
    


class Maze:
    """Labirinth with areas branching out and about."""

    def __init__(self, name: str) -> None:
        """
        Instantiates a new Maze, set to the spatial origin.

        :param name: Give the Maze a description.
        """
        self._name = name
        self._areas = {}

    @property
    def name(self) -> str:
        """The name of the maze."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def areas(self) -> Dict[Coordinate, Area]:
        """Areas in the maze mapped by its coordinates."""
        return self._areas

    @property
    def occupied_spaces(self) -> List[Coordinate]:
        """Maze coordinates containing areas."""
        return list(self.areas.keys())
    
    @property
    def portals(self) -> List[Area]:
        """Coordinates containing areas."""
        return [area for area in self.areas.values() if area.has_portal]
    
    def total_floors(self) -> int:
        """The number of floors in the maze."""
        return len(set(area.x for area in self.areas))

