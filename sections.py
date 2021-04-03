class Area:
    """The representation of a room in a maze, its property is_portal indicates
    that this area is an entrance or exist point of the maze.
    """
    __id = 0

    def __init__(self, is_portal: bool = False):
        self.id = Area.__id + 1
        Area.__id += 1
        self.is_portal = is_portal
        self.links = []

    def __str__(self):
        if self.is_portal:
            return f"area marked as '{self.id}' has a portal"
        if len(self.links) < 2:
            return f"area marked as '{self.id}' is a dead end"
        return f"area marked as '{self.id}'"

    def __repr__(self):
        return f"{'portal' if self.is_portal else 'area'} '{self.id}'"


class Hall:
    """A collection of areas linked to each other, if any of them
    are portals then it is considered a path, otherwise its a branch.
    """
    __id = 0

    def __init__(self, areas: list = None):
        self.id = Hall.__id + 1
        Hall.__id += 1
        self.areas = areas if areas else []

    def __str__(self):
        string = f"{'path' if self.is_path else 'branch'} '{self.id}'"
        if self.passages:
            string += " joint on"
        for joint in self.passages:
            string += f" ({joint[0]} with {joint[1]})"
        return string

    def __repr__(self):
        return self.__str__()

    @property
    def portals(self):
        return [area for area in self.areas if area.is_portal]

    @property
    def is_path(self):
        """A hall is a path if it has any portals, otherwise its a hall."""
        return True if self.portals else False

    @property
    def passages(self):
        """List of area tuples where other halls branch from. The first element
        is part of the current hall while the other belongs to the connected hall.
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
        self.id = Maze.__id + 1
        Maze.__id += 1
        self.halls = branches if branches else []

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
    def branches(self):
        return [branch for branch in self.halls if not branch.is_path]

    @property
    def paths(self):
        return [branch for branch in self.halls if branch.is_path]
