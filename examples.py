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
SCREEN_DIVISION = 10
# Set up the drawing window
screen = pygame.display.set_mode(SCREEN_SIZE)
# Fill the background
screen.fill(WHITE)


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
        pass


class Room(pygame.sprite.Sprite):
    matrix = ScreenMatrix(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_DIVISION)
    area_x = matrix.width / matrix.divisions
    area_y = matrix.height / matrix.divisions
    side_border = 4
    size = (area_x - side_border, area_y - side_border)

    def __init__(self,
                 pos: tuple[int, int] = None,
                 color: tuple[int, int, int] = BLACK):
        super(Room, self).__init__()
        self.image = pygame.Surface(Room.size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        if pos is not None:
            self.matrix_pos = self.matrix.get_pos(pos[0], pos[1])
            self.rect.x = self.matrix_pos[0]
            self.rect.y = self.matrix_pos[1]


def create_hall_sprites(
        hall: sections.Hall,
        start_pos: tuple[int, int],
        horizontal: bool = True,
        ascending: bool = True) -> pygame.sprite.Group:
    sprite_group = pygame.sprite.RenderUpdates()
    matrix = ScreenMatrix(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_DIVISION)
    origin = matrix.get_pos(start_pos[0], start_pos[1])
    print(f" Creating sprites at {origin} for {hall}.")
    for i in range(len(hall.areas)):
        if horizontal:
            if ascending:
                pos = (start_pos[0] + i, start_pos[1])
            else:
                pos = (start_pos[0] - i, start_pos[1])
        else:
            if ascending:
                pos = (start_pos[0], start_pos[1] + i)
            else:
                pos = (start_pos[0], start_pos[1] - i)

        room = Room(pos)
        sprite_group.add(room)
        print(f"  added sprite for {hall.areas[i]} "
              f"at matrix {pos} - {room.matrix_pos}")
    return sprite_group


def create_maze_sprites(
        maze: sections.Maze,
        start_pos: tuple[int, int],
        horizontal: bool = True,
        ascending: bool = True) -> pygame.sprite.Group:
    print(f"{maze}, this is how it was created:")
    maze_sprites = create_hall_sprites(
        maze.halls[0], start_pos, horizontal, ascending)
    return maze_sprites


the_maze = wizard.cast_maze(2, 5, hall_length_range=(8, 12))
sprites = create_maze_sprites(the_maze, (1, int(SCREEN_DIVISION/2)))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw all sprites
    sprites.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
