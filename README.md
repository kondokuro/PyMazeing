# PyMazeing

## About 

As a game developer, one of the tasks is to create the playable space, also known as the game world, level, dungeon or even a room. The idea behind the PyMazing project is to provide a way to represent those spaces, using maze definitions, allowing for simple workflows to generate them, automatically or manually.

It is intended for dungeon, level or labyrinth design enthusiasts, this means that the result can be used to render or build playable Mazes anywhere.


## User Interface 

From the wizard module use the cast_maze function to obtain a maze instance. 

```python
TBD
```

A simple function call returns the full maze structure. Alternatively, a maze can be constructed by using the more specific generator functions for the different maze sections, if the desire is to have more control over the shape of the maze.

## Technical Specification 

Since the world is divided into continents, on PyMazing we took the world as a container of multiple areas, where the world would be a maze, which is composed of one or multiple branches, which then can be divided or contain inner areas, and those areas can be the place for other objects.

As mentioned above in the world of Mazes, they are composed of Halls or branching paths, which can be divided into Zones, which combined represent the Hall’s length. Each of these parts have information to indicate their location in the world via coordinates.


```
+  P  +-----+-----+-----+-----+-----+-----+-----+-----+-----+ 
|  1  .  2  .  2  |  >  .  >  .  v  |  >  .  >  .  >  .  v  |
|  .  +-----+  .  +  .  +-----+  .  +  .  +-----+-----+  .  |
|  v  |  2  .  2  |  ^  .  <  |  >  .  ^  |  6  |  v  .  <  |
+  .  +-----+-----+-----+  .  +-----+  .  +  .  +  .  +-----|
|  >  .  v  |  3  .  3  |  ^  .  5  .  6  .  6  |  v  |  7  |
+-----+  .  +  .  +-----+  .  +  .  +-----+-----+  .  +  .  |
|  v  .  <  .  3  |  >  .  ^  |  5  .  5  |  v  .  <  .  7  |
+  .  +-----+-----+  .  +  .  +-----+-----+  .  +-----+-----|
|  >  .  >  .  >  .  ^  |  4  .  4  |  8  .  >  .  >  .  1  |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+  P  +
```

This example figure is a representation of a 2D Maze with 9 halls, one path and 2 portals, the halls are numbered, the path is marked and the portals are located at the edges.

### Module definitions

#### rogue
The functions in this module are named skills, used for gathering information from the maze structure.

##### Find Paths
Lists the halls in a maze that can be considered as paths

##### Is Path
Defines if the current hall is a path

##### Detect Branches
Lists the halls in the maze that are considered as dead ends

##### Track Portals
List of all the areas containing portals in the maze

##### Track Hall Portals
List of all the areas containing portals in the hall

##### Map Maze
List of all the coordinates of the areas in the maze

##### Map Hall Location
List of all the coordinates of the areas in the hall

#### wizard
The functions in this module are named spells, used to create mazes and other structures.

##### Conjure Maze
Creates a single complete maze based on the following parameters
- Number of halls, total amount of halls the maze will have
- Number of portals, total entrances and exits the maze will have
- Max portals per hall, how many portals a hall in the maze can have
- Min hall length, used to define the smallest size of the many halls
- Max hall length, used to define the longest size of the many halls

##### Summon Hall
brings forth the desired hall based on the following parameters
- Length, how many areas the hall will be divided into
- Number of portals, how many portals should the hall have
- Branching from, an area or cordinate that will serve as the hall’s start point
- Existing halls, used to reference occupied coordinates so that the new hall does not collide with another

##### Invoke Area
Adds some space for a hall based on the following parameters
- Coordinates, target location of the space
- Occupied spaces, the coordinates not available for the invocation
- Portals, names of the mazes the portals of this area will have

#### sections

#### MAZE
The labyrinth representation
- Name, optional short and fun description of the maze
- Halls, list of all the halls of the maze

##### Categories

###### Dead End
- All portals are in the same area
- Has one path
- All other halls are branches

###### One Path
- All portals are in the same hall
- Some portals are in different areas
- All other halls are branches

###### Dungeon
- May have all the kinds of halls
- Has multiple portals
- Has multiple paths
- Some portals are in different areas

#### HALL
Representation of a stretch of space in the maze, divided into paths or branches.
- Areas, list of spaces the hall is composed of

##### Categories

###### Branch
Hall with no areas holding a portal.

###### Path
Hall with at least an area holding a portal, with in turn can be sub-categorized in:
- Complete, a hall that has more than one portal with at least one on a different area.
- Incomplete, a hall with just one portal area.
- Connected, a path that branches from another path
- Disconnected, a path that branches from a branch
- Composed, parts of different branches that lead to a path (only on mazes with more than one portal)

#### AREA
The different spaces a hall is divided into
- Coordinates, represent the area’s location in the maze space
- Portals, list of entrances or exits from the maze
- Passages, list of connections to areas in other halls

### systems
The classes in this module represent the utilities needed to define how the pieces of the maze connect to each other.

#### PASSAGE
Connection between two halls
- Origin, the connected area
- Connection, the external hall

#### PORTAL
Defines entrance or exit from a maze, or the access to another maze
- Destination, the name of the maze this portal connects to, empty values can be used to determine entrance or exit from the maze

#### COORDINATES
Defines the location of an area in the maze coordinate system, loosely based on the cartesian system
- X, horizontal axis, west will be negative values while east will be positive
- Y, vertical axis, where north is the positive value and south is the negative
- Z, height axis, where up is represented as positive values while down by negative

#### SIZE
Defines the square or cubed space where an entity is located
- width, horizontal space
- length, vertical space
- height, height space

### Maze rules
1.- A Maze is composed of one to many Halls
2.- A Maze must have at least one Portal
3.- A Hall is divided into one or many Areas
4.- Paths are Halls with at least an Area with a Portal
5.- Hall Areas do not cross over their Hall
6.- Branches are Halls without Portals
7.- Areas only belong to a single Hall
8.- Areas can have a maximum of one Portal
9.- Areas never have the same coordinates
10.- Portals belong to an Area
11.- Portals define entrance or exit from a maze
12.- Portals can connect different mazes
13.- Portals can exist in multiple areas from different mazes

## Testing
Every class and function is unit tested.

## Deployment 
This work is meant to be used as a library, to be used alongside another project. I will be published on Pipy for users to install.

## Broader Context 

### Possible extensions 
- Support for alternate coordinate systems, for example hex spaces instead of squares
- Definition of open and closed zones.
- Definition of additional collectables to find, rather than just finding the exit.
- Adding more objects for the zones
