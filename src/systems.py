"""
Definitions that supporting maze creation.
"""
import typing
import collections


class TypedList(collections.UserList):
    """A list bound to a single type of items."""

    def __init__(self, cls: typing.Type):
        """
        Initializes a new TypedList instance.

        :param cls: the class Type object representing the type of the elements that can be stored in the list.
        """
        super().__init__()
        self.cls = cls

    def __validate(self, item):
        """
        Validates that an item can be added to the list.

        :param item: The item to be validated.
        :raises TypeError: If the item is not of the type that the list is bound to.
        """
        if not isinstance(item, self.cls):
            raise TypeError(f"List items must be of type {self.cls}")

    def append(self, item):
        """
        Adds an item to the end of the list.

        :param item: The item to be added.
        :raises TypeError: If the item is not of the type that the list is bound to.
        """
        self.__validate(item)
        super().append(item)

    def insert(self, i, item):
        """
        Adds an item to the list at a specific index.

        :param i: The index at which to insert the item.
        :param item: The item to be inserted.
        :raises TypeError: If the item is not of the type that the list is bound to.
        """
        self.__validate(item)
        super().insert(i, item)

    def extend(self, iterable):
        """
        Adds multiple items to the end of the list.

        :param iterable: An iterable of items to be added.
        :raises TypeError: If any of the items are not of the type that the list is bound to.
        """
        for item in iterable:
            self.__validate(item)
        super().extend(iterable)


class Coordinate:
    """Identifies a location in space."""

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a new Coordinate instance. Defaults to the origin.

        :param x: An integer for the x-coordinate, defautls to zero.
        :param y: An integer for the y-coordinate, defautls to zero.
        :param z: An integer for the z-coordinate, defautls to zero.
        """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        """Verifies ecuality of two coordinates."""
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z


class Size:
    """Defines the dimentions area an entity occupies."""

    def __init__(self, length: int = 1, width: int = 1, height: int = 1) -> None:
        """
        Initializes a new Size instance, defaults to the minimum size of 1.

        :param length: An integer representing the depth.
        :param width: An integer representing the width.
        :param height: An integer representing the height.
        """
        self._length = self.__validate_value("length", length)
        self._width = self.__validate_value("width", width)
        self._height = self.__validate_value("height", height)

    def __validate_value(self, attribute: str, value: int) -> int:
        """
        Verifies that the value is positive.

        :param attribute: a string for the parameter to verigy.
        :param value: an integer to validate.
        :returns: the valid integer value.
        :raises: ValueError if the value is negative.
        """
        if value < 0:
            raise ValueError(f"Value: {value} needs to be possitive for {attribute}")
        return value

    def __validate_type(self, other: object) -> None:
        if not isinstance(other, Size):
            raise TypeError(f"{other} is not of type Size")

    def __eq__(self, other: object) -> bool:
        """Verifies ecuality of two sizes."""
        if not isinstance(other, Size):
            return False
        return (
            self.length == other.length
            and self.width == other.width
            and self.height == other.height
        )

    @property
    def length(self) -> int:
        """Size value on a horizontal plane (x)."""
        return self._length

    @length.setter
    def length(self, value: int) -> None:
        """Sets the length value raising ValueError if negative."""
        self._length = self.__validate_value("length", value)

    @property
    def width(self) -> int:
        """Size value on a vertical plane (y)."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """Sets the width value raising ValueError if negative."""
        self._width = self.__validate_value("width", value)

    @property
    def height(self) -> int:
        """Size value on an altitude plane (z)."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """Sets the height value raising ValueError if negative."""
        self._height = self.__validate_value("height", value)

    def is_longer(self, other: "Size") -> bool:
        self.__validate_type(other)
        return self.length > other.length

    def is_whider(self, other: "Size") -> bool:
        self.__validate_type(other)
        return self.width > other.width

    def is_taller(self, other: "Size") -> bool:
        self.__validate_type(other)
        return self.height > other.height
