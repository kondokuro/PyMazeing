from enum import Enum
from src.components import Coordinate


class Directions(Enum):
        """The posible cardinal directions."""
        NORTH = "north"
        SOUTH = "south"
        EAST = "east"
        WEST = "west"
        UP = "up"
        DOWN = "down"

def get_adjacent_coordinate(origin: Coordinate, direction: Directions) -> Coordinate:
    """Provides the adjacent coordinate based on the direction."""
    x, y, z = origin.x, origin.y, origin.z
    if direction == Directions.NORTH:
        z += 1
    elif direction == Directions.SOUTH:
        z -= 1
    elif direction == Directions.EAST:
        y += 1
    elif direction == Directions.WEST:
        y -= 1
    elif direction == Directions.UP:
        x += 1
    elif direction == Directions.DOWN:
        x -= 1
    return Coordinate(x, y, z)