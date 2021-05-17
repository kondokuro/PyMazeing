from collections import namedtuple


class Area:
    """The representation of a room or part of a hall in a maze.
    There are two types of areas portals and rooms, where portals
    represent a room with an entrance or exit point of the maze.
    """
    __id = 0

    def __init__(self, is_portal: bool = False):
        self._id = Area.__id + 1
        Area.__id += 1
        self._is_portal = is_portal
        self.links = []
        self.hall = None

    def __str__(self):
        links = len(self.links)
        if self.is_portal:
            return f"with_portal room '{self.id}'"
        if links < 2:
            return f"dead end room '{self.id}'"
        string = f"room '{self.id}'"
        return string

    def __repr__(self):
        return f"{'with_portal' if self.is_portal else 'room'} '{self.id}'"

    @property
    def id(self) -> int:
        return self._id

    @property
    def is_portal(self) -> bool:
        return self._is_portal


"""Represents a connection between an area an its linked hall."""
Passage = namedtuple("Passage", "entrance hall")


class Hall:
    """A collection of areas linked to each other, if any of them
    are portals then it is considered a path, otherwise its a branch.
    """
    __id = 0

    def __init__(self):
        self._id = Hall.__id + 1
        Hall.__id += 1
        self._areas = []

    def __str__(self):
        string = f"{'Path' if self.is_path else 'Branch'} '{self.id}'"
        areas = len(self.areas)
        string += f", which is {areas} room{'s' if areas > 1 else ''} long"
        if self.passages:
            string += ", with access to other halls"
            for passage in self.passages:
                string += f" from {passage[0]} to {passage[1]},"
            string = string[0:-1]
        return string

    def __repr__(self):
        string = f"{'path' if self.is_path else 'branch'} '{self.id}'"
        if self.passages:
            string += " with passages on:"
            for passage in self.passages:
                string += f" ({passage[0]} to {passage[1]})"
        return string

    @property
    def id(self) -> int:
        return self._id

    @property
    def areas(self) -> list[Area]:
        return self._areas

    @property
    def portals(self) -> list[Area]:
        return [area for area in self.areas if area.is_portal]

    @property
    def is_path(self) -> bool:
        """The hall is a path if any of its areas are portals, otherwise
        its a branch.
        """
        return True if self.portals else False

    @property
    def passages(self) -> list[Passage]:
        """Represents access to other halls. Each passage has the entrance
        area and the hall it gives access to.
        """
        all_links = set()
        for area in self.areas:
            all_links.update(area.links)
        connections = {area for area in all_links if area not in self.areas}
        passages = set()
        for connection in connections:
            for area in self.areas:
                if connection in area.links:
                    passages.add(Passage(area, connection))
        return list(passages)

    def add_area(self, with_portal: bool = False, entrance: Area = None):
        """Gives this hall a new area. The new area will be linked with
        the last hall area and be part of this hall.

        Keyword arguments:

        - with_portal -- the area will be with_portal (default False)
        - entrance -- is the area with access to this hall (default None)
        """
        new_area = Area(with_portal)
        new_area.hall = self
        if len(self.areas) > 0:
            last_area = self.areas[-1]
            new_area.links.append(last_area)
            last_area.links.append(new_area)
        if entrance:
            new_area.links.append(entrance)
            entrance.links.append(new_area)
        self._areas.append(new_area)


class Maze:
    """The data representation of a labyrinth."""
    __id = 0

    def __init__(self, branches: list[Hall] = None):
        self._id = Maze.__id + 1
        Maze.__id += 1
        self._halls = branches if branches else []

    def __get_portals(self):
        portals = []
        for hall in self.paths:
            portals.extend(hall.portals)
        return portals

    def __get_exit_string(self):
        portal_cnt = len(self.__get_portals())
        exit_string = "no exits"
        if portal_cnt > 1:
            exit_string = "an exit" if portal_cnt < 3 \
                else f"{portal_cnt - 1} exits"
        return exit_string

    def __str__(self):
        hall_count = len(self.halls)
        string = f"You have landed at PyMaze '{self.id}', created with"
        string += " a hall" if hall_count < 2 else f" {hall_count} halls"
        string += f" an entrance and {self.__get_exit_string()}"
        return string

    def __repr__(self):
        string = f"Maze '{self.id}'"
        string += f" halls: {len(self.halls)}"
        string += f" portals: {len(self.__get_portals())}"
        return string

    @property
    def id(self):
        return self._id

    @property
    def halls(self):
        return self._halls

    @property
    def paths(self):
        return [branch for branch in self.halls if branch.is_path]

    @property
    def branches(self):
        return [branch for branch in self.halls if not branch.is_path]
