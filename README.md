# PyMazeing
There is a wizard here able to cast the maze spell.
The spell will generate the data of a maze for something else to build it.

Example:
```
import wizard


labyrinth = wizard.cast_maze(portals=2, halls=50, hall_length_range=(1, 100)
print(labyrinth)
for hall in labyrinth.halls:
    print(hall)
    for room in hall.areas:
        print(room)
```
