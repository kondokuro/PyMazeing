
from typing import Protocol
from src.components import Area, Maze, Coordinate


class Renderer(Protocol):
    """Interface for classes that display a structure."""
    def show_maze(self) -> str:
        """Displays the structure completely."""
        ...

    def show_area(self, area: Area) -> str:
        """Displays a single area."""
        ...

class AssciiMazeRenderer:
    """Displays a maze in ASCII."""
    def __init__(self, maze: Maze) -> None:
        self._maze = maze

    def show_maze(self) -> str:
        return "Rendering maze in ASCII:"
    
    def show_area(self, location: Coordinate) -> str:
        """
        Each area has 3 lines, top, middle and bottom.
        Empty spaces need to be represented as big as existing area space.
        There is a fix horizontal and vertical size for each area.
        Top and bottom define the corners, with H_WALL.
        The middle is defined as |    | or | P | if the area has a portal.
        In order to render multiple areas each line must be concatenated.
        Empty walls need to be filled with spaces.
        Width is 7 characters.
        Areas share walls, both top and middle. (not important to render one area)
        U and D are used to define changing floors 
        """
        H_WALL = "+-----+"

        return ""

class DescriptionMazeRenderer:
    """Descrives a maze in text."""
    def __init__(self, maze: Maze) -> None:
        self._maze = maze

    def show_maze(self) -> str:
        return "Describing maze:"
        
    def show_area(self, location: Coordinate) -> str:
        area = self._maze.areas.get(location)
        if not area:
            return "empty space..."
        
        if not area.passages:
            return "dead end..."

        directions = []
        for passage in area.passages:
            if passage.x > area.position.x:
                directions.append("up")
            if passage.x < area.position.x:
                directions.append("down")
            if passage.y > area.position.y:
                directions.append("east")
            if passage.y < area.position.y:
                directions.append("west")
            if passage.z > area.position.z:
                directions.append("north")
            if passage.z < area.position.z:
                directions.append("south")

        last_direction = directions.pop()
        description = "in this area there is a way " + ", ".join(directions)
        if directions:
            description += " and " + last_direction
        else:
            description += last_direction
        return description + "."
