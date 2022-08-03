"""
Module with the spells for creating mazes.
"""
import random
import sys
from src.maze import sections


class SpellError(Exception):
    """Receive a message why the spell failed."""
    pass


def summon_hall(length: int = 1,
                number_of_portals: int = 0,
                branching_from: sections.Area = None,
                occupied_spaces: list[sections.Coordinates] = [(0, 0), ]) -> sections.Hall:
    """Cast this spell to a invoque an enchanted hall, to complement
    an existing magical maze, or to start creating one. 

    Keyword arguments:

    - length --  number of areas this hall is dived itnto, minimum values is 
    one, which creates a single room hall.
    - number_of_portals -- amount of portals the hall will have, it will be
    validated against the length of the hall.
    - branching_from --  an area from another hall that will be the starting 
    point of the new hall, if none is given the hall assumes strating from the 
    origin.
    - occupied_spaces -- list of spaces in the maze occupied by an area.
    """
    # parameter validation lenght is >1,
    # number of portals is > 0 and <= than the hall length
    # gather non available coordinates
    # replace the coordinate for an available one
    # update the non available coordinates

    # length considerations starting from inxex zero
    for i in range(length - 1):
        new_area = sections.Area((0, 0))
        # new_hall.areas.append(new_area)

    # create resulting hall
    # new_hall = sections.Hall()
    #end = _summon_area(has_end, new_hall.areas[-1])
    # new_hall.areas.append()
    areas = [sections.Area(), ]
    return sections.Hall(areas)


def conjure_maze(portals: int = 1,
                 halls: int = 1,
                 min_hall_length: int = 1,
                 max_hall_length: int = 1) -> sections.Maze:
    """Magic spell to creates a maze. Defaults to a single portal room.

    Keyword arguments:

    - portals -- the number of portals in the maze (default 1)
    - halls -- the number halls in the maze (default 1)
    - min_hall_length -- min number of areas a hall can have
    - max_hall_length -- max number of areas a hall can have
    """
    halls_to_build = halls
    #new_maze = sections.Maze([sections.Hall()])

    hall_length = random.randint(min_hall_length, max_hall_length)
    #add_exit = True if portals > 1 and max_hall_length > 1 else False
    main_path = sections.Hall(hall_length, None, True, add_exit)
    # new_maze.halls.append(main_path)
    # if halls == 1:
    #    return new_maze

    #halls_to_build -= 1
    #portals_to_build = portals - len(main_path.portals)

    #add_entrance = False
    #add_exit = False
    # if portals_to_build > 0:
    #    entrance_or_exit = random.choice((True, False))
    #    if entrance_or_exit:
    #        add_entrance = random.choice((True, False))
    #    else:
    #        add_exit = random.choice((True, False))
    #    if add_entrance or add_exit:
    #        portals_to_build -= 1

    #    new_branch = sections.Hall()
    # new_maze.halls.append(new_branch)

    return sections.Maze('wip', sections.Hall(sections.Area(sections.Coordinates())))
