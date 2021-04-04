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
        self._links = []

    def __str__(self):
        links = len(self.links)
        if self.is_portal:
            return f"room '{self.id}' has a portal"
        if links < 2:
            return f"room '{self.id}' is a dead end"
        string = f"room '{self.id}' leads to another room"
        if links > 2:
            string += f" links to {links - 2} external areas"
        return string

    def __repr__(self):
        return f"{'portal' if self.is_portal else 'room'} '{self.id}'"

    @property
    def id(self) -> int:
        return self._id

    @property
    def links(self) -> list:
        return self._links


class Hall:
    """A collection of areas linked to each other, if any of them
    are portals then it is considered a path, otherwise its a branch.
    """
    __id = 0

    def __init__(self, areas: list[Area] = None):
        self._id = Hall.__id + 1
        Hall.__id += 1
        self._areas = areas if areas else []

    def __str__(self):
        string = f"{'path' if self.is_path else 'branch'} '{self.id}'"
        if self.passages:
            string += " other halls can be reached from"
        passages = len(self.passages)
        for passage in self.passages:
            string += f" {passage[0]} to {passage[1]}"
            if
        return string

    def __repr__(self):
        string = f"{'path' if self.is_path else 'branch'} '{self.id}'"
        if self.passages:
            string += " passages on"
        for passage in self.passages:
            string += f" ({passage[0]} to {passage[1]})"
        return string

    @property
    def id(self) -> int:
        return self._id

    @property
    def areas(self) -> list:
        return self._areas

    @property
    def portals(self) -> list:
        return [area for area in self.areas if area.is_portal]

    @property
    def is_path(self) -> bool:
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

    def __str__(self):
        portals = []
        for hall in self.paths:
            portals.extend(hall.portals)
        portal_cnt = len(portals)
        exit_string = "no exits"
        if portal_cnt > 1:
            exit_string = "an exit" if portal_cnt < 3 else f"{portal_cnt - 1} exits"
        string = f"Maze '{self.id}', containing an entrance"\
                 f" and {exit_string}, composed of {len(self.halls)} halls"
        return string

    def __repr__(self):
        return self.__str__()

    @property
    def id(self):
        return self._id

    @property
    def halls(self):
        return self._halls

    @property
    def branches(self):
        return [branch for branch in self.halls if not branch.is_path]

    @property
    def paths(self):
        return [branch for branch in self.halls if branch.is_path]
