# PyMazeing

## About 

PyMazing is a D&D themed maze generator, it includes class definitions for the different maze sections and a few generator functions to create the parts.

It is intended for dungeon, level, or labyrinth design enthusiast, this means that the result can be used to render or build playable mazes anywhere.

The maze spell provides a complete structure to play in, this is, a collection of interconnected dead end hallways and a main path; then the designer can then focus on just placing interesting objectives.

Specific areas would contain entrance or exit from the maze, used for defining the main path that a traveller must cross to complete it.

The complexity of the maze is based on the number of halls and how many branches each hall can have, as well as how long the halls are. 

## User Interface 

From the wizard module use the cast_maze function to obtain a maze instance. 

```python
import wizard

labyrinth = wizard.cast_maze(
	total_portals:int=0,
	total_halls:int=1,
	min_hall_length:int=1,
	max_hall_length:int=1)
```

A simple function call returns the full maze structure. Alternatively, a maze can be constructed by using the more specific generator functions for the different maze sections, if the desire is to have more control over the shape of the maze.

## Technical Specification 

Mazes are composed of halls, which are logically divided into areas, as the representation of the hall’s lenght, areas hold the information to indicate their location in the maze via coordinates.

```
  ...... _____  _____  _____  ______  _____  _____  _____  _____  _____ 
||  P  ::  2  ::  2  ||  >  ::  >   ::  v  ||  >  ::  >  ::  >  ::  v  ||
|| _ _ ::_____:: _ _ || _ _ ::_____ :: _ _ || _ _ ::_____::_____:: _ _ ||
||  1  ||  2  ::  2  ||  ^  ::  <   ||  >  ::  ^  ||  6  ||  v  ::  <  ||
|| _ _ ||_____::_____||_____:: _ _  ||_____:: _ _ || _ _ || _ _ ::_____||
||  >  ::  v  ||  3  ||  3  ||  ^   ::  5  ::  6  ::  6  ||  v  ||  7  ||
||_____:: _ _ || _ _ ||_____|| _ _  :: _ _ ::_____::_____|| _ _ || _ _ ||
||  v  ::  <  ::  3  ||  >  ::  ^   ||  5  ::  5  ||  v  ::  <  ::  7  ||
|| _ _ ::_____::_____|| _ _ :: _ _  ||_____::_____|| _ _ ::_____::_____||
||  >  ::  >  ::  >  ::  ^  ||  4   ::  4  ||  8  ::  >  ::  >  ::  p  ||
||_____::_____::_____::_____||_____ ::_____||_____::_____::_____::.....||
```

This example figure is a representation of a 2D Maze with 9 halls, one path and 2 portals, the halls are numbered, the path is marked and the portals are located at the edges.

### Class definitions 

#### MAZE
The labyrinth representation
- Name, optional short and fun description of the maze
- Halls, list of all the halls of the maze

#### HALL
Representation of a path or a branch in the maze.
- Areas, list of spaces the hall is composed of

##### Categories
- Branch, a hall with no areas holding a portal.
- Path, a hall with at least an area holding a portal, with in turn can be sub-categorized in:
	- Complete, a hall that has more than one portal area.
	- Incomplete, a hall with just one portal area.
	- Connected, a path that branches from another path
	- Disconnected, a path that branches from a branch

#### AREA
The different spaces a hall is divided into
- Coordinates, represent the area’s location in the maze space
- Portall, list of entrances or exits from the maze

#### PORTAL
Defines entrance or exit from a maze, or the access to another maze
- Kind, is the portal an entrance, an exit or a maze connection
- Maze, maze name this portal conects to

### Module definitions

#### rogue
The functions in this module are named skills, used for gathering information from the maze structure.
- Find Paths, lists the halls in a maze that can be considered as paths
- Detect Branches, lists the halls in the maze that are considered as dead ends
- Track Portals, list of all the areas containing portals in the maze
- Gather Coordinates, lists the hall's map coodinates

#### wizard
The functions in this module are named spells, used to create mazes and other structures.

##### Conjure Maze, 
generates a single complete maze based on the following parameters
- Number of halls, total amount of halls the maze will have
- Number of portals, total entrances and exits the maze will have
- Max portals per hall, how many portals a hall in the maze can have
- Min hall length, used to define the smallest size of the many halls
- Max hall length, used to define the longest size of the many halls

##### Summon Hall, 
brings forth the desired hall based on the following parameters
- Length, how many areas the hall will be divided into
- Number of portals, how many portals should the hall have
- Branching from, an area or cordinate that will serve as the hall’s start point
- Existing halls, used to reference occupied coordinates so that the new hall does not collide with another


### Maze rules:
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

## Testing
Test for the generator functions are based on the use cases and the defined rules.

## Deployment 
This work is meant to be used as a library, to be used alongside another project.

## Broader Context 

### Limitations of the current design
The maximum number of “doors” an area can have is based on the square coordinate system; this means that in a 2D maze the max number of “doors” are 4 (North, East, South and West) and in 3D having 6 (up and down), no diagonals are considered because 3D maze construction would be a bit too complicated for now.

Another limitation is setting areas with only one portal, it will make things simpler to construct if we can assume that there is one portal per area.

### Possible extensions 
- Have portals connect different mazes
- Allow multiple portals per area, this will require another parameter to define the max number of portals per area when casting the maze spell and generating a randomized labyrinth
- Provide a spell to create multiple connected mazes
- Additional portal like element to teleport the player to another area (non connected link)
- Consider diagonal direction for “doorways” 
- Support for alternate coordinate systems, for example hex spaces instead of squares
- Definition of open and closed halls with keys to find.
- Definition of additional collectables to find, rather than just finding the exit.
- Adding traps into an area
- Additional portal like element to teleport the player to another area (non connected link).
