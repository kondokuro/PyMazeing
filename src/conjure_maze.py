import random
import sys
from src.characters import wizard


HELP = "h", "help"


def main(*args):
    spell = "You"
    arg_count = len(args)
    if arg_count < 2:
        spell += f" conjured a random"
    else:
        if args[2] in HELP:
            print(  # CREATE A SEPARATE MESSAGE CONSTANT, ALSO UPDATE IT
                """
                Cast a magic spell to creates a maze. 
                A Maze is composed of halls, and the halls are divided
                into areas.
                There are two kinds of halls, paths and branches, where
                paths contain areas with portals, that are entrance
                or exit points from the maze.
    
                Arguments:
                - portals -- the number of portals in the maze
                - halls -- the number halls in the maze 
                - branching_limit -- max number of links in any area, a
                common limit is 4, as in 4 walls 4 doors to another room.
                Note that:
                   - if the value is 1 the maze will be a single portal 
                   room.
                   - if value is 2 the maze will be a two room path.
                - hall_length_range -- min-max number of areas a hall 
                can have
                """
            )
        spell += f" conjured a well defined"
    spell += " Maze spell"
    print(spell)
# REVIEW THE VALUES
    portals = args[1] if arg_count > 1 else random.randint(2, 8)
    halls = args[2] if arg_count > 2 else random.randint(22, 44)
    branching = args[3] if arg_count > 3 else random.randint(4, 8)
    length = args[4] if arg_count > 4 \
        else (random.randint(1, 15), random.randint(16, 30))

    labyrinth = wizard.conjure_maze(portals, halls, branching, length)
    print(labyrinth)
    for hall in labyrinth.halls:
        print(hall)


if __name__ == "__main__":
    main(sys.argv)
