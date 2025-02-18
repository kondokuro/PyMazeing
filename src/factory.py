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
import typing
from enum import Enum, auto
from src.components import Wall, Area, Maze
from src.core import Coordinate, Size


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


class AreaForge:
    """Creates fixed size 3 areas with proper walls and available spaces."""

    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def _add_walls(self, area: Area, shape: AreaShape) -> None:
        """Places walls in the area based on the requested shape."""
        coords = area.position
        match shape:
            case AreaShape.CLOSED:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.DEAD_END_W:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.DEAD_END_S:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.DEAD_END_E:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.DEAD_END_N:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.WAY_WE:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.WAY_NS:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.CORNER_WS:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.CORNER_SE:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.CORNER_EN:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("w_wall", Coordinate(coords.x, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.CORNER_NW:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("e_wall", Coordinate(coords.x+2, coords.y+1, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.JUNCTION_WSE:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("n_wall", Coordinate(coords.x+1, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.JUNCTION_WNE:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("s_wall", Coordinate(coords.x+1, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
            case AreaShape.CROSSROAD:
                walls = [
                    Wall("nw_wall", Coordinate(coords.x, coords.y, coords.z), Size()),
                    Wall("ne_wall", Coordinate(coords.x+2, coords.y, coords.z), Size()),
                    Wall("sw_wall", Coordinate(coords.x, coords.y+2, coords.z), Size()),
                    Wall("se_wall", Coordinate(coords.x+2, coords.y+2, coords.z), Size()),
                ]
        for wall in walls:
            area.content.append(wall)  # TODO nothing is checking for space available for those elements

    def conjure_area(self, shape: AreaShape) -> Area:
        """
        Provides a fully shaped area instance.

        :param shape: The desired wall structure of the area.
        :returns: A default area containing walls arranged by the shape.
        """
        area = Area(
            "name", self.maze.origin, Size(3, 3, 3)  # TODO there is no way to define where to add the areaS
        )
        self._add_walls(area, shape)
        return area


class Wizzard:
    """Summon mazes with just a few parametes."""

    def __init__(self) -> None:
        self._maze = None
        self.area_forge = AreaForge(self._maze)

    def _summon_maze(self, name: str, origin: Coordinate = Coordinate()) -> None:
        """Instantiates an initial maze for the wizzard"""
        self._maze = Maze(name, origin)

    def cast_maze(
        self, name: str, origin: Coordinate, *args, **kwargs
    ) -> Maze:
        """
        Generates an initial maze to build up from.

        :param name: the label of the maze.
        :param origin: the initial location of the maze.
        """
        self._summon_maze(name, origin)
        return self._maze

    def add_area(
        self,
        location: Coordinate,
        size: Size = Size(),
    ) -> None:
        """
        Adds a new area to the maze being constructed.

        :param shape: An AreaShape enum to give the area its open spaces and walls
        :param location: The top left Coordinate of the area.
        :param size: Space the area will occupy TBD
        """
        self._maze.areas.append(Area("WIP", location, size))

    def branch(self, area: Area) -> typing.List[Area]:
        """The idea here is to take an area as the starting point and build a group of areas."""
        return list(area)
