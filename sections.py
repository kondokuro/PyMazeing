class Area:
    """The representation of a room in a maze.
    There are two types of areas portals and rooms, portals represent an
    entrance or exist point of the maze.
    """
    __id = 0

    def __init__(self, is_portal: bool = False):
        self._id = Area.__id + 1
        Area.__id += 1
        self.is_portal = is_portal
        self.links = []

    def __str__(self):
        links = len(self.links)
        if self.is_portal:
            return f"portal room '{self.id}'"
        if links < 2:
            return f"dead end room '{self.id}'"
        string = f"room '{self.id}'"
        return string

    def __repr__(self):
        return f"{'portal' if self.is_portal else 'room'} '{self.id}'"

    @property
    def id(self) -> int:
        return self._id


class Hall:
    """A collection of areas linked to each other, if any of them
    are portals then it is considered a path, otherwise its a branch.
    """
    __id = 0

    def __init__(self, areas: list[Area] = None):
        self._id = Hall.__id + 1
        Hall.__id += 1
        self.areas = areas if areas else []

    def __str__(self):
        string = f"The {'path' if self.is_path else 'branch'} '{self.id}'"
        areas = len(self.areas)
        string += f" is {areas} room{'s' if areas > 1 else ''} long"
        if self.passages:
            string += ", and has access to other halls"
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
    def portals(self):
        return [area for area in self.areas if area.is_portal]

    @property
    def is_path(self):
        """The hall is a path if any of its areas are portals, otherwise
        its a branch.
        """
        return True if self.portals else False

    @property
    def passages(self) -> list[tuple[Area, Area]]:
        """Entrances to other halls.
        The first element belongs to this hall, the second one is part
        of the branching hall.
        """
        all_links = []
        for area in self.areas:
            all_links.extend(area.links)
        connections = [area for area in all_links if area not in self.areas]
        passages = []
        for connection in connections:
            for area in self.areas:
                if connection in area.links:
                    passages.append((area, connection))
        return passages


class Maze:
    """The data representation of a labyrinth."""
    __id = 0

    def __init__(self, branches: list = None):
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
