# PyMazeing

## About 

The idea behind the PyMazing project is to provide a way to represent spaces, using maze definitions, allowing for simple workflows to generate them, manually and automatically.

It is intended for labyrinth, dungeon or level design enthusiasts, this means that the result can be used to render or build playable Mazes anywhere.


## User Interface 

From factory module the main tool will be the Forge we have access to the means of building up our maze piece by piece. 

```python
import factory

forge = Forge()
forge.start_maze("corn field")

```

A simple function call returns the full maze structure. 
Alternatively, a maze can be constructed by using the more specific generator functions for the different maze sections, if the desire is to have more control over the shape of the maze.

## Technical Specification 

On PyMazing we defined the Maze as a container of multiple areas, and those areas can be the place for other objects. Each of these parts have information to indicate their location in the world via coordinates.

```
+-----+           +-----+-----+-----+-----+-----+-----+-----+ 
|  p  |           |  >     >     v  |  >     >     >     v  |
+     +           +     +-----+     +     +-----+-----+     +
|  v  |           |  ^     <  |  >     ^  |     |  v     <  |
+     +-----+-----+-----+     +-----+     +     +     +-----+
|  >     v  |     |     |  ^  |     |           |  v  |
+-----+     +     +-----+     +     +-----+-----+     +
|  v     <        |  >     ^  |           |  v     <  |
+     +-----+-----+     +     +     +-----+     +-----+-----+
|  >     >     >     ^  |     |     |        >     >     p  |
+-----+-----+-----+-----+-----+     +-----+-----+-----+-----+
```
This example figure is a representation of a 2D Maze with a single path and 2 portals located at the edges.

### Modules

#### factory
The functions and classes in this module are used to create mazes and their inner structures.

##### Forge
This class is used to manually build a maze from scratch.
It has simple methods to extend the areas of the maze.
- Expanding will add a new area to the maze
- Annexing will add and link areas in the maze to each other

##### Conjure Maze
Creates a single complete maze based on the following parameters
- Number of halls, total amount of halls the maze will have
- Number of portals, total entrances and exits the maze will have
- Max portals per hall, how many portals a hall in the maze can have
- Min hall length, used to define the smallest size of the many halls
- Max hall length, used to define the longest size of the many halls

##### Summon Hall (halls have been deprecated)
brings forth the desired hall based on the following parameters
- Length, how many areas the hall will be divided into
- Number of portals, how many portals should the hall have
- Branching from, an area or cordinate that will serve as the hall’s start point
- Existing halls, used to reference occupied coordinates so that the new hall does not collide with another

##### Expand
Adds some space with a new area based on the following parameters
- Coordinates, target location of the space
- (deprecated)Occupied spaces, the coordinates not available for the invocation
- Portals, names of the mazes the portals of this area will have, currently just a boolean

#### componenst

##### Area
A single unit occupiying a maze coordinate, represents a room or space in the maze.
- name? should areas be named
- location: use also as its unique identifier, tells the place it has in the maze space.
- size: defines how much space it actually has to hold other objects. (WIP)

An idea of the area is that it belongs to a single point of the maze and it also holds space itself, this permits mapping the maze paths without caring about the size or shape of the actual areas.
Another probably better idea is that Areas should be of unique size so that having a bigger space is a matter of combining areas.

##### Coordinate
Defines the location of an area in the maze coordinate system, loosely based on the cartesian system
- X, the vertical axis, represents the levels or floors of a structure, where negative values are ment as the basement or underground levels.
- Y, horizontal axis, where the east side is represented by the positive values and west uses the negative ones.
- Z, depth axis, representint the front as positive values while back by negative.

### Maze rules
1.- A Maze must have at least one Portal
2.- Portals define entrance or exit from a maze
4.- A Maze is composed of one to many Areas
5.- Areas never have the same coordinates
6.- Portals belong to an Area
7.- Portals can connect different Areas

## Testing
Every class and function is unit tested.

## Deployment 
This work is meant to be used as a library, to be used alongside another project. I will be published on Pipy for users to install.

## Broader Context 

### Possible extensions 
...
