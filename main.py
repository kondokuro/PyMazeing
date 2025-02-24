"""
Execute a text based maze forge and explore the maze.
"""
import textwrap

from src.factory import Forge, DirectionProvider
from src.components import Coordinate


def main():
    """Create a maze and explore it."""
    name = input(textwrap.dedent(
        """
        Welcome to the PyMazing Forge!
        we are here to test the maze forge")
        Lets start by giving a name to the maze: 
        """))
    
    x, y, z = input(textwrap.dedent(
        """
        Ok, now lets set the initial position of the maze.
        Use 3 numbers separated by commas: 
        """)).split(",")

    builder = Forge()
    builder.start_maze(name, Coordinate(int(x), int(y), int(z)))
    print(f"Maze '{builder.maze.name}' at {builder.maze.origin} was created!")

    navigator = DirectionProvider()
    selection = input(textwrap.dedent(
        f"""
        Next, let start expanding our maze by adding rooms...
        select where the next room should be: (use the numbers)")
        1. {navigator.Directions.NORTH.value}
        2. {navigator.Directions.SOUTH.value}
        3. {navigator.Directions.EAST.value}
        4. {navigator.Directions.WEST.value}
        5. {navigator.Directions.UP.value}
        6. {navigator.Directions.DOWN.value}
        """))
    extension_direction = list(navigator.Directions)[int(selection)-1]
    next_coordinate = navigator.get_adjacent_coordinate(builder.maze.origin, extension_direction)
    builder.extend(next_coordinate)
    print(f"Maze extended to {builder.maze.areas[next_coordinate].position}")


if __name__ == "__main__":
    main()
