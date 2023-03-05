"""
Create or modify mazes or its parts.

A Maze is composed of multiple areas.
A Maze must have at least one Portal.

Areas can have zero or many Portals
Areas coordinates are unique, no two have the same coordinates
Areas are separated by walls
Walls are objects inside of the area space

Portals are located in Areas
Portals define entrance or exit from a Maze
Portals connect two Mazes
"""
from enum import Enum, auto
from src import components, systems


class AreaShape(Enum):
    """The different generic area shapes found in a maze, basd on their available open access."""

    CLOSED = auto()
    DEAD_END_W = auto()
    DEAD_END_S = auto()
    DEAD_END_E = auto()
    DEAD_END_N = auto()
    WAY_WE = auto()
    WAY_NS = auto()
    CORNER_WS = auto()
    CORNER_SE = auto()
    CORNER_EN = auto()
    CORNER_NW = auto()
    JUNCTION_WSE = auto()
    JUNCTION_WNE = auto()
    CROSSROAD = auto()


class Wizzard:
    """Summon mazes with just a few parametes."""

    def _summon_maze(self, name: str, origin: systems.Coordinate) -> None:
        """Instantiates an initial maze for the wizzard"""
        self._maze = components.Maze(name, origin)

    def _add_walls(self, area: components.Area, shape: AreaShape) -> None:
        """Places walls in the area based on the requested shape."""
        match shape:
            case AreaShape.CLOSED: 
                pass
            case AreaShape.DEAD_END_W: 
                pass
            case AreaShape.DEAD_END_S: 
                pass
            case AreaShape.DEAD_END_E: 
                pass
            case AreaShape.DEAD_END_N: 
                pass
            case AreaShape.WAY_WE: 
                pass
            case AreaShape.WAY_NS: 
                pass
            case AreaShape.CORNER_WS: 
                pass
            case AreaShape.CORNER_SE: 
                pass
            case AreaShape.CORNER_EN: 
                pass
            case AreaShape.CORNER_NW: 
                pass
            case AreaShape.JUNCTION_WSE: 
                pass
            case AreaShape.JUNCTION_WNE: 
                pass
            case AreaShape.CROSSROAD: 
                pass

    def cast_maze(
        self, name: str, origin: systems.Coordinate, branches: int, *args, **kwargs
    ) -> components.Maze:
        """
        Generates an initial maze to build up from.

        :param name: the label of the maze.
        :param origin: the initial location of the maze.
        :param branches: the total number of branches the maze will contain.
        """
        self._summon_maze(name, origin)
        return self._maze

    def cast_area(
        self,
        maze: components.Maze,
        shape: AreaShape,
        location: systems.Coordinate,
        portal: bool = False,
        size: systems.Size = systems.Size(),
    ) -> components.Area:
        """
        Creates areas surrounded by walls based on the parameters provided.

        :param shape: An AreaShape enum to give the area its open spaces and walls
        :param location: The top left Coordinate of the area.
        :param size: Space the area will occupy TBD
        """
        new_area = components.Area("WIP", location, size, maze.id)
        self._add_walls(new_area, shape)
        return new_area

    def branch(self, area: components.Area) -> systems.TypedList[components.Area]:
        """The idea here is to take an area as the starting point and build a group of areas."""
        return systems.TypedList(components.Area)
