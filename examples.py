import pygame
import wizard
import sections
import random
from typing import NamedTuple


class Cardinal:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def get_cardinals() -> list[int]:
        return [Cardinal.UP, Cardinal.RIGHT, Cardinal.DOWN, Cardinal.LEFT]


class Colors(NamedTuple):
    """A container for many pre-defined color tuples."""
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    BROWN = (139, 69, 19)
    GREEN = (0, 255, 0)
    GOLD = (218, 165, 32)
    PINK = (200, 0, 200)
    PURPLE = (106, 90, 205)
    RED = (255, 0, 0)
    TAN = (210, 180, 140)
    WHITE = (255, 255, 255)

    @staticmethod
    def random():
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))


# Coordinate representation when using the matrix screen system.
class MatrixCoord(NamedTuple):
    x: int
    y: int


# Coordinate representation of a screen pixel point.
class ScreenCoord(NamedTuple):
    x: int
    y: int


class ScreenMatrix:
    """Divides the screen pixel area into simple positions."""
    def __init__(self,
                 screen_width: int,
                 vertical_divisions: int,
                 screen_height: int,
                 horizontal_divisions: int):
        self.width = screen_width
        self.height = screen_height
        self.w_divisions = horizontal_divisions
        self.h_divisions = vertical_divisions

    @property
    def horizontal_center(self) -> int:
        return int(self.h_divisions / 2)

    @property
    def vertical_center(self) -> int:
        return int(self.w_divisions / 2)

    @property
    def size(self) -> tuple[int, int]:
        return self.width, self.height

    def get_screen_pos(self, matrix_coord: MatrixCoord) -> ScreenCoord:
        pos_x = matrix_coord.x * (self.width / self.w_divisions) + 1
        pos_y = matrix_coord.y * (self.height / self.h_divisions) + 1
        return ScreenCoord(int(pos_x), int(pos_y))

    def get_matrix_pos(self, screen_coord: ScreenCoord) -> MatrixCoord:
        # return matrix_x, matrix_y
        pass


class MatrixSprite(pygame.sprite.Sprite):
    """A sprite that support screen matrix positioning, with an area that
    is bound to the matrix division size.
    """
    __matrix = ScreenMatrix(500, 25, 500, 25)

    def __init__(self,
                 matrix_coord: MatrixCoord = MatrixCoord(0, 0),
                 color: tuple[int, int, int] = Colors.BLACK):
        super(MatrixSprite, self).__init__()
        self.width = self.__matrix.width / self.__matrix.w_divisions
        self.height = self.__matrix.height / self.__matrix.h_divisions
        self.side_border = 4
        self.size = (self.width - self.side_border,
                     self.height - self.side_border)
        self.image = pygame.Surface(self.size)
        self.color = color
        self.screen_pos = self.__matrix.get_screen_pos(matrix_coord)
        self.matrix_pos = matrix_coord
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_pos.x
        self.rect.y = self.screen_pos.y
        self.available_cardinals = Cardinal.get_cardinals()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: Colors):
        self.image.fill(value)
        self._color = value


class SpriteArea(sections.Area):
    """Subclass of Area that holds a reference to its sprite."""

    def __init__(self,
                 original_area: sections.Area,
                 matrix_coord: MatrixCoord = MatrixCoord(0, 0),
                 color: tuple[int, int, int] = Colors.BLACK):
        """Takes its data from an existing area."""
        self._id = original_area.id
        self._is_portal = original_area.is_portal
        self.links = original_area.links
        self.hall = original_area.hall
        self.matrix_sprite = MatrixSprite(matrix_coord, color)


class HallSprites(NamedTuple):
    """A combination of a hall and its area sprites."""
    hall: sections.Hall = None
    sprites: list = []


class MazePainter2D:
    """In charge of drawing the sprites of a maze."""

    def __init__(self):
        self.maze_sprites = pygame.sprite.RenderUpdates()
        self.drawn_hall = HallSprites()

    def __get_color(self, hall: sections.Hall, index: int) -> tuple[int, int, int]:
        """Returns a color tuple based on the hall type or area type."""
        if hall.areas[index].is_portal:
            return Colors.BLUE
        return Colors.GOLD if hall.is_path else Colors.BROWN

    def __get_matrix_location(self,
            matrix: MatrixCoord,
            index,
            horizontal: bool,
            ascending: bool) -> MatrixCoord:
        """Calculate matrix coordinates from a starting point and modified
        by the index.
        """
        x = matrix.x
        y = matrix.y
        if horizontal:
            x = matrix.x + index if ascending else matrix.x - index
        else:
            y = matrix.y + index if ascending else matrix.y - index
        return MatrixCoord(x, y)

    def _draw_hall(
            self,
            hall: sections.Hall,
            matrix_coord: MatrixCoord,
            horizontal: bool = True,
            ascending: bool = True):
        """Function that creates sprites for all areas in a hall.

        params:

        - hall: a hall instance
        - start_coord: matrix position
        - horizontal: indicates the hall orientation
        - ascending: indicates the direction the hall will grow towards,
          a value of true indicates that the direction will follow positive
          growth of the axis, this is positive as towards the right side of
          the x axis and down on the y axis.
        """
        print(f" Drawing {hall}.")
        areas = len(hall.areas)
        for i in range(areas):
            room_coord = self.__get_matrix_location(
                matrix_coord, i, horizontal, ascending)
            color = self.__get_color(hall, i)
            # this replaces the area in the hall with a
            hall.areas[i] = MatrixSprite(room_coord, color)
            room = self.__get_sprite(room, horizontal, ascending, i)

            self.maze_sprites.add(room)
            print(f"  drew {hall.areas[i]} "
                  f"at {room.matrix_pos} - {room.screen_pos}")
        self.drawn_hall = HallSprites(hall, drawn_areas)

    def draw_maze(
            self,
            maze: sections.Maze,
            start_coord: MatrixCoord,
            start_horizontal: bool = True,
            start_ascending: bool = True):
        """Function that creates a sprite group for the maze.
        """
        print(f"{maze}:")
        halls_to_draw = [hall for hall in maze.halls]
        previous_hall = None
        # for hall in halls_to_draw:
        """
        the process here is to draw the first maze hall and then 
        on each hall passage draw its hall
        """
        next_hall = halls_to_draw.pop(0)
        if previous_hall is None:
            self._draw_hall(
                next_hall, start_coord, start_horizontal, start_ascending)

            for passage in self.drawn_hall.hall.passages:
                print(passage.hall)
                # self._draw_hall(passage.hall, )
        #    previous_hall = next_hall

        # next_hall = halls_to_draw.pop(0)
        # hall_entrance = next_hall.passages
        # passage = None
        # for area in previous_hall.areas:
        #     if hall_entrance in area.links:
        #         passage = area
        # passage_sprite = None
        # for room in hall_sprites.sprites():
        #     if room.area == passage:
        #         passage_sprite = room
        # x = passage_sprite.matrix_x
        # y = passage_sprite.matrix_y + 1
        # create_hall_sprites(next_hall, x, y, False)


the_maze = wizard.cast_maze(2, 5, hall_length_range=(8, 12))
labyrinth_screen = ScreenMatrix(500, 25, 500, 25)
painter = MazePainter2D()
maze_start = MatrixCoord(1, labyrinth_screen.vertical_center)
painter.draw_maze(the_maze, maze_start)

pygame.init()
screen = pygame.display.set_mode(labyrinth_screen.size)
screen.fill(Colors.WHITE)

running = True
while running:

    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        running = False

    painter.maze_sprites.draw(screen)
    # Update the display
    pygame.display.flip()

pygame.quit()
