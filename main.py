"""
Execute a text based maze forge and explore the maze.
"""
import textwrap

from src.factory import Forge
from src.components import Coordinate
from src.navigation import get_adjacent_coordinate, Directions
from src.display import DescriptionMazeRenderer


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
        Ok, now lets set the entrance of the maze.
        Use 3 numbers separated by commas: 
        """)).split(",", 2)

    builder = Forge()
    origin = Coordinate(int(x), int(y), int(z))
    builder.start_maze(name, origin)
    print(f"Created '{builder.maze.name}'! its entrance at {origin}")

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
        destination = get_adjacent_coordinate(origin, extension_direction)
        builder.annex(origin, destination)
        print(f"Maze extended towars the {extension_direction.value} at {destination}")
        move = input("Do you want to move to this area? (y/n) ") == "y"
        if move:
            origin = destination
            print(f"Moved to {origin}, next expassion starts from here...")

        done = input("Continue building? (y/n) ") == "n"
    
    # Display the maze
    print("Here is the maze you created:")
    scribe = DescriptionMazeRenderer(builder.maze)
    for place in builder.maze.areas.keys():
        print(f"at {place}, {scribe.show_area(place)}")

if __name__ == "__main__":
    main()
