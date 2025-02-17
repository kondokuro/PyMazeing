"""
Definitions that supporting maze creation.
"""
import typing
import collections


class Coordinate:
    """Identifies a location in space."""

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        """
        Initializes a new Coordinate instance. Defaults to the origin.

        :param x: An integer value for the x-coordinate, representing a level
        or floor location in the structure, defautls to zero.
        :param y: An integer value for the y-coordinate, representing east or
        west side locations of a strucure, defautls to zero.
        :param z: An integer value for the z-coordinate, represents the
        front or back sides of a structure, defautls to zero.
        """
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: object) -> bool:
        """Verifies ecuality of two coordinates."""
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __repr__(self) -> str:
        return f"(x: {self.x}, y: {self.y}, z: {self.z})"
    
    def __str__(self) -> str:  # TODO add test to include building like notation
        return f"coordinates ({self.x}, {self.y}, {self.z})"


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

    def __repr__(self) -> str:
        return f"(l: {self.length}, w: {self.width}, h: {self.height})"

    def __str__(self) -> str:
        return f"size of length {self.length}, width {self.width} and height {self.height}"

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
