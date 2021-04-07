# PyMazeing
There is a wizard here able to cast the maze spell.
The spell will generate a magical structure of a maze for something else to build it.
A Maze is composed of halls, and the halls are divided into rooms.
There are two kinds of halls, paths and branches, where paths contain rooms referred as portals, that are entrance or exit points from the maze.

### Arguments:
- portals: the number of portals in the maze
- halls: the number halls in the maze 
- branching_limit: max number of links in any area, a common limit is 4, as in 4 walls 4 doors to another room.
Note that:
   - if the value is 1 the maze will be a single portal room.
   - if value is 2 the maze will be a two room path.
- hall_length_range: min-max tuple, the number of areas a hall can have

### Example:
```python
import wizard


labyrinth = wizard.cast_maze(portals=2, halls=50, hall_length_range=(1, 100)
print(labyrinth)
for hall in labyrinth.halls:
    print(hall)
    for room in hall.areas:
        print(room)
```
