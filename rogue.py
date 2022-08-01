"""
Contains the definitions of the rogue skills used for navigating a maze.
"""
import sections


class SkillError(Exception):
    """Notice the mistake on the skill check."""
    pass


def find_paths(maze: sections.Maze) -> list[sections.Hall]:
    """Never get lost using this skill, get all the paths that lead from the 
    entrances to exits.
    """
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
