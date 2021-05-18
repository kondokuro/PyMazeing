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
    def horizontal_half(self) -> int:
        return int(self.h_divisions / 2)

    @property
    def vertical_half(self) -> int:
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
    """A sprite that support screen matrix positioning."""

    def __init__(self,
                 screen_matrix: ScreenMatrix,
                 matrix_coord: MatrixCoord = MatrixCoord(0, 0),
                 color: Colors = Colors.BLACK):
        super(MatrixSprite, self).__init__()
        self.width = screen_matrix.width / screen_matrix.w_divisions
        self.height = screen_matrix.height / screen_matrix.h_divisions
        self.side_border = 4
        self.size = (self.width - self.side_border,
                     self.height - self.side_border)
        self.image = pygame.Surface(self.size)
        self.color = color
        self.screen_pos = screen_matrix.get_screen_pos(matrix_coord)
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


# A combination of a matrix sprite and an area.
class AreaSprite(NamedTuple):
    area: sections.Area
    sprite: MatrixSprite


class MazePainter:

    def __init__(self):
        self.maze_sprites = pygame.sprite.RenderUpdates()
        self.area_sprites = []

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
        x = matrix_coord.x
        y = matrix_coord.y
        areas = len(hall.areas)
        for i in range(areas):
            if horizontal:
                x = matrix_coord.x + i if ascending else matrix_coord.x - i
            else:
                y = matrix_coord.y + i if ascending else matrix_coord.y - i

            area_to_paint = hall.areas[i]

            color = Colors.GOLD if hall.is_path else Colors.BROWN
            if area_to_paint.is_portal:
                color = Colors.BLUE
            room_coord = MatrixCoord(x, y)
            room = MatrixSprite(labyrinth_screen, room_coord, color)
            self.maze_sprites.add(room)
            self.area_sprites.append(AreaSprite(area_to_paint, room))
            print(f"  drew {area_to_paint} "
                  f"at {room.matrix_pos} - {room.screen_pos}")

    def draw_maze(
            self,
            maze: sections.Maze,
            start_coord: MatrixCoord,
            start_horizontal: bool = True,
            start_ascending: bool = True) -> pygame.sprite.RenderUpdates:
        """Function that creates a sprite group for the maze.
        """
        print(f"{maze}:")
        halls_to_draw = [hall for hall in maze.halls]
        previous_hall = None
        # for hall in halls_to_draw:
        """process here is to dwaw the first maze hall and then 
        draw each passage of each hall
        """
        next_hall = halls_to_draw.pop(0)
        if previous_hall is None:
            self._draw_hall(
                next_hall, start_coord, start_horizontal, start_ascending)
            previous_hall = next_hall

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
painter = MazePainter()
maze_start = MatrixCoord(1, labyrinth_screen.vertical_half)
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
