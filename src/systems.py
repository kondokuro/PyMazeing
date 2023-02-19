import typing
from collections import UserList


class TypedList(UserList):
    """A list bound to a single type of items."""

    def __init__(self, cls: typing.Type):
        super().__init__()
        self.cls = cls

    def __validate(self, item):
        if not isinstance(item, self.cls):
            raise TypeError(f"List items must be of type {self.cls}")

    def append(self, item):
        self.__validate(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate(item)
        super().insert(i, item)

    def extend(self, iterable):
        for item in iterable:
            self.__validate(item)
        super().extend(iterable)


class Coordinate:
    """Identifies a location in space."""

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


class Size:
    """Provides information of the size of an area."""

    def __init__(self, depth: int, width: int, height: int) -> None:
        self.depth = depth
        self.width = width
        self.height = height
