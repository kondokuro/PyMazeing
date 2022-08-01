"""
Contains the definitions of the rogue skills used for navigating a maze.
"""
import errors
import sections


def find_paths(maze: sections.Maze) -> list[sections.Hall]:
    """"""
    pass


def detect_branches(maze: sections.Maze) -> list[sections.Hall]:
    """With this skill the rogue can map out all the dead ends in a maze."""
    pass


def track_portals(maze: sections.Maze) -> list[sections.Area]:
    """This skill allows the rogue to identify the location of all portals 
    in a maze.
    """
    pass


def gather_coordinaes(hall: sections.Hall) -> list[tuple[int]]:
    """This skill notes the coordinates that occupies the hall."""
    pass
