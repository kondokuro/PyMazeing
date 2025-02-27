from components import Area, Maze
from typing import Protocol


class Renderer(Protocol):
    """Interface for classes that display a structure."""
    def render(self) -> None:
        """Displays the structure completely."""
        ...

class AssciiMazeRenderer:
    """Displays a maze in ASCII."""
    def __init__(self, maze: Maze) -> None:
        self._maze = maze

    def render(self) -> None:
        print("Rendering maze in ASCII:")
    
    def get_area_asscii(area: Area) -> str:
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

    def render(self) -> None:
        print("Describing maze:")
        
    def get_area_description(area: Area) -> str:
        return ""
