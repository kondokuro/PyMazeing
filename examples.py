import pygame
import wizard
import sections
import random


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (200, 0, 200)
GOLD = (218, 165, 32)
PURPLE = (106, 90, 205)
BROWN = (139, 69, 19)
TAN = (210, 180, 140)
RANDOM = (random.randint(0, 255),
          random.randint(0, 255),
          random.randint(0, 255))

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_DIVISION = 25
# Set up the drawing window
screen = pygame.display.set_mode(SCREEN_SIZE)
# Fill the background
screen.fill(WHITE)


class Cardinal:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def get_cardinals() -> list[int]:
        return [Cardinal.UP, Cardinal.RIGHT, Cardinal.DOWN, Cardinal.LEFT]


class ScreenMatrix:
    """Divides the screen pixel area into simple equivalent positions."""
    def __init__(self, w: int, h: int, div: int):
        self.width = w
        self.height = h
        self.divisions = div

    def get_pos(self, matrix_x: int, matrix_y: int) -> tuple[int, int]:
        pos_x = matrix_x * (self.width / self.divisions) + 1
        pos_y = matrix_y * (self.height / self.divisions) + 1
        return int(pos_x), int(pos_y)

    def get_matrix(self, pos_x: int, pos_y: int) -> tuple[int, int]:
        # return matrix_x, matrix_y
        pass


class Room(pygame.sprite.Sprite):
    matrix = ScreenMatrix(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_DIVISION)
    area_x = matrix.width / matrix.divisions
    area_y = matrix.height / matrix.divisions
    side_border = 4
    size = (area_x - side_border, area_y - side_border)

    def __init__(self,
                 area: sections.Area,
                 pos_x: int = 0,
                 pos_y: int = 0,
                 color: tuple[int, int, int] = BLACK):
        super(Room, self).__init__()
        self.image = pygame.Surface(Room.size)
        self.rect = self.image.get_rect()
        self.area = area
        self.color = color
        self.matrix_x = pos_x
        self.matrix_y = pos_y
        self.matrix_points = (self.matrix_x, self.matrix_y)
        self.matrix_pos = self.matrix.get_pos(pos_x, pos_y)
        self.rect.x = self.matrix_pos[0]
        self.rect.y = self.matrix_pos[1]
        self.available_cardinals = Cardinal.get_cardinals()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: tuple[int, int, int]):
        self.image.fill(value)
        self._color = value


def create_hall_sprites(
        hall: sections.Hall,
        start_x: int,
        start_y: int,
        horizontal: bool = True,
        ascending: bool = True) -> pygame.sprite.Group:
    sprite_group = pygame.sprite.RenderUpdates()
    print(f" Creating sprites for {hall}.")
    x = start_x
    y = start_y
    areas = len(hall.areas)
    color = GOLD if hall.is_path else BROWN
    for i in range(areas):
        if horizontal:
            x = start_x + i if ascending else start_x - i
        else:
            y = start_y + i if ascending else start_y - i
        room = Room(hall.areas[i], x, y, color)
        if hall.areas[i].is_portal:
            room.color = BLUE

        sprite_group.add(room)
        print(f"  added sprite for {room.area} "
              f"at matrix {x, y} - {room.matrix_pos}")
    return sprite_group


def create_maze_sprites(
        maze: sections.Maze,
        start_x: int,
        start_y: int,
        horizontal: bool = True,
        ascending: bool = True) -> pygame.sprite.Group:
    print(f"{maze}:")
    maze_sprites = pygame.sprite.RenderUpdates()
    halls_to_draw = [hall for hall in maze.halls]
    previous_hall = None
    # for hall in halls_to_draw:
    next_hall = halls_to_draw.pop(0)
    if previous_hall is None:
        hall_sprites = create_hall_sprites(
            next_hall, start_x, start_y, horizontal, ascending)
        maze_sprites.add(hall_sprites)
        previous_hall = next_hall

    next_hall = halls_to_draw.pop(0)
    hall_entrance = next_hall.areas[0]
    passage = None
    for area in previous_hall.areas:
        if hall_entrance in area.links:
            passage = area
    passage_sprite = None
    for room in hall_sprites.sprites():
        if room.area == passage:
            passage_sprite = room
    x = passage_sprite.matrix_x
    y = passage_sprite.matrix_y + 1
    hall_sprites = create_hall_sprites(next_hall, x, y, False)
    maze_sprites.add(hall_sprites)

    return maze_sprites


the_maze = wizard.cast_maze(2, 5, hall_length_range=(8, 12))
sprites = create_maze_sprites(the_maze, 1, int(SCREEN_DIVISION/2))

running = True
while running:

    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        running = False

    sprites.draw(screen)
    # Update the display
    pygame.display.flip()

pygame.quit()
