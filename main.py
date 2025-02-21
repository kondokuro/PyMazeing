"""
Execute a text based maze forge and explore the maze.
"""
import os
from enum import Enum
from src.factory import Forge
from src.components import Coordinate

class Directions(Enum):
    """The four cardinal directions."""
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

def main():
    """Create a maze and explore it."""
    name = input("""
                 Welcome to the PyMazing Forge!
                 we are here to test the maze forge")
                 Lets start by giving a name to the maze: 
                 """)
    print("Ok, now lets set the initial position of the maze.")
    x, y, z = input("Use 3 numbers separated by commas: ").split(",")

    builder = Forge()
    builder.start_maze(name, Coordinate(x, y, z))
    print(f"Maze '{builder.maze.name}' at {builder.maze.origin} was created!")
    
    direction = input(f"""
                      Next, let start expanding our maze by adding rooms...
                      select where the next room should be: ")
                        1. {Directions.NORTH.value}
                        2. {Directions.SOUTH.value}
                        3. {Directions.EAST.value}
                        4. {Directions.WEST.value}
""")
    #TODO calculate the next coordinate based on the direction


if __name__ == "__main__":
    main()