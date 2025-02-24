"""
Execute a text based maze forge and explore the maze.
"""
import textwrap

from src.factory import Forge
from src.components import Coordinate
from src.navigation import get_adjacent_coordinate, Directions


def main():
    """Create a maze and explore it."""

    name = input(textwrap.dedent(
        """
        Welcome to the PyMazing Forge!
        We are here to test maze creation.")
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

    # TODO start the building loop...
    done = False
    print("Next, let start expanding our maze by adding areas...")

    while not done:
        selection = input(textwrap.dedent(
            f"""
            Select where the next room should be: (use the numbers)")
            1. {Directions.NORTH.value}
            2. {Directions.SOUTH.value}
            3. {Directions.EAST.value}
            4. {Directions.WEST.value}
            5. {Directions.UP.value}
            6. {Directions.DOWN.value}
            """))
        extension_direction = list(Directions)[int(selection)-1]
        next_coordinate = get_adjacent_coordinate(builder.maze.origin, extension_direction)
        builder.extend(next_coordinate)
        print(f"Maze extended towars the {extension_direction.value} at {builder.maze.areas[next_coordinate].position}")


if __name__ == "__main__":
    main()
