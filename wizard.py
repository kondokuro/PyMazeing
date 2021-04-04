import sections
import random


def _summon_area(with_portal: bool = False,
                 linked_to: sections.Area = None) -> sections.Area:
    """Magic spell to get a new maze area. Defaults to a single room.

    Keyword arguments:

    - with_portal -- the area will hold a portal (default False)
    - linked_to -- connects the area with the given one (default None)
    """
    new_area = sections.Area(with_portal)
    if linked_to:
        new_area.links.append(linked_to)
        linked_to.links.append(new_area)
    return new_area


def _summon_hall(length: int = 1,
                 branching_from: sections.Area = None,
                 has_start: bool = False,
                 has_end: bool = False) -> sections.Hall:
    """Magic spell to a get new maze hall.
    All areas in th hall are sequentially connected.
    Defaults to a single room hall.

    Keyword arguments:

    - length --  number of areas in the hall (default 1)
    - branching_from --  an area from another hall (default None)
    - has_start --  first area is a portal (default False)
    - has_end --  last area is a portal (default False)
    """
    new_hall = sections.Hall()
    start = _summon_area(has_start, branching_from)
    new_hall.areas.append(start)

    for i in range(length - 2):
        new_area = _summon_area(linked_to=new_hall.areas[i])
        new_hall.areas.append(new_area)

    end = _summon_area(has_end, new_hall.areas[-1])
    new_hall.areas.append(end)

    return new_hall


def _find_connectable_areas(halls: list, link_limit: int) -> list:
    """Returns a list of areas with less links than link_limit."""
    areas = []
    for hall in halls:
        available = [area for area in hall.areas
                     if len(area.links) < link_limit]
        areas.extend([area for area in available])
    return areas


def cast_maze(portals: int = 1,
              halls: int = 1,
              branching_limit: int = 4,
              hall_length_range: tuple = (1, 1)) -> sections.Maze:
    """Magic spell to creates a maze. Defaults to a single portal room.

    Keyword arguments:

    - portals -- the number of portals in the maze (default 1)
    - halls -- the number halls in the maze (default 1)
    - branching_limit -- max number of links in any area (default 4)

      - if the value is 1 the maze will be a portal room.
      - if value is 2 the maze will be a two room path.

    - hall_length_range -- min-max number of areas a hall can have
    """
    halls_to_build = halls
    length_min = hall_length_range[0]
    length_max = hall_length_range[1]
    new_maze = sections.Maze()

    hall_length = random.randint(length_min, length_max)
    add_exit = True if portals > 1 and length_max > 1 else False
    main_path = _summon_hall(hall_length, None, True, add_exit)
    new_maze.halls.append(main_path)
    if halls == 1:
        return new_maze

    halls_to_build -= 1
    portals_to_build = portals - len(main_path.portals)

    for i in range(halls_to_build):
        connections = _find_connectable_areas(
            new_maze.halls, branching_limit)
        hall_length = random.randint(length_min, length_max)
        branch_from = random.choice(connections) if connections else None

        add_entrance = False
        add_exit = False
        if portals_to_build > 0:
            entrance_or_exit = random.choice((True, False))
            if entrance_or_exit:
                add_entrance = random.choice((True, False))
            else:
                add_exit = random.choice((True, False))
            if add_entrance or add_exit:
                portals_to_build -= 1

        new_branch = _summon_hall(
            hall_length, branch_from, add_entrance, add_exit)
        new_maze.halls.append(new_branch)

    return new_maze
