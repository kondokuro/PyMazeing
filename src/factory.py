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


class AreaForge:
    """Creates areas with proper walls and available spaces."""

    def __init__(self, maze: components.Maze) -> None:
        self.maze = maze

    def _add_walls(self, area: components.Area, shape: AreaShape) -> None:
        """Places walls in the area based on the requested shape."""
        coords = area.position
        match shape:
            case AreaShape.CLOSED:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.DEAD_END_W:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.DEAD_END_S:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.DEAD_END_E:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.DEAD_END_N:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.WAY_WE:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.WAY_NS:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.CORNER_WS:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.CORNER_SE:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.CORNER_EN:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("w_wall", systems.Coordinate(coords.x, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.CORNER_NW:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("e_wall", systems.Coordinate(coords.x+2, coords.y+1, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.JUNCTION_WSE:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("n_wall", systems.Coordinate(coords.x+1, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.JUNCTION_WNE:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("s_wall", systems.Coordinate(coords.x+1, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
            case AreaShape.CROSSROAD:
                walls = [
                    components.Wall("nw_wall", systems.Coordinate(coords.x, coords.y, coords.z), systems.Size()),
                    components.Wall("ne_wall", systems.Coordinate(coords.x+2, coords.y, coords.z), systems.Size()),
                    components.Wall("sw_wall", systems.Coordinate(coords.x, coords.y+2, coords.z), systems.Size()),
                    components.Wall("se_wall", systems.Coordinate(coords.x+2, coords.y+2, coords.z), systems.Size()),
                ]
        for wall in walls:
            area.content.append(wall)

    def conjure_area(self, shape: AreaShape) -> components.Area:
        area = components.Area(
            "name", self.maze.position, systems.Size(3), self.maze.id
        )
        self._add_walls(area, shape)
        return area


class Wizzard:
    """Summon mazes with just a few parametes."""

    def __init__(self) -> None:
        self._maze = components.Maze("unamed", systems.Coordinate())
        self.area_forge = AreaForge(self._maze)

    def _summon_maze(self, name: str, origin: systems.Coordinate) -> None:
        """Instantiates an initial maze for the wizzard"""
        self._maze = components.Maze(name, origin)

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
        return new_area

    def branch(self, area: components.Area) -> systems.TypedList[components.Area]:
        """The idea here is to take an area as the starting point and build a group of areas."""
        return systems.TypedList(components.Area)
