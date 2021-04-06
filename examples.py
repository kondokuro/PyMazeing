import pygame
import wizard
import sections


pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (200, 0, 200)
GOLD = (218, 165, 32)
PURPLE = (106, 90, 205)
BROWN = (139, 69, 19)

WIDTH = 500
HEIGHT = 500
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_DIVISION = 10
# Set up the drawing window
screen = pygame.display.set_mode(SCREEN_SIZE)
# Fill the background
screen.fill(WHITE)


class ScreenDivisor:
    def __init__(self, w: int, h: int, div: int):
        self.width = w
        self.height = h
        self.divisions = div

    def get_pos(self, x: int, y: int) -> tuple[int, int]:
        pos_x = x * (self.width/self.divisions) + 1
        pos_y = y * (self.height/self.divisions) + 1
        return int(pos_x), int(pos_y)


class Room(pygame.sprite.Sprite):
    area_x = WIDTH/SCREEN_DIVISION
    area_y = HEIGHT/SCREEN_DIVISION
    sides = 4
    size = (area_x - sides, area_y - sides)

    def __init__(self, pos: tuple[int, int] = None):
        super(Room, self).__init__()
        self.image = pygame.Surface(Room.size)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        if pos is not None:
            self.rect.x = pos[0]
            self.rect.y = pos[1]


def create_hall_sprites(
        hall: sections.Hall, sprite_group: pygame.sprite.Group,
        start_pos: tuple[int, int]):
    for area in hall.areas:
        room = Room(start_pos)
        sprite_group.add(room)


def create_maze(
        maze: sections.Maze,
        sprite_group: pygame.sprite.Group,
        start_pos: tuple[int, int]):
    for hall in maze.halls:
        create_hall_sprites(hall, sprite_group, start_pos)


matrix = ScreenDivisor(WIDTH, HEIGHT, SCREEN_DIVISION)
all_sprites = pygame.sprite.RenderUpdates()
the_maze = wizard.cast_maze(2, 5, hall_length_range=(8, 12))
create_maze(the_maze, all_sprites, matrix.get_pos(5, 1))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
