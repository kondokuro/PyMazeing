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


class Orientation:
    HORZ = "horizontal"
    VERT = "vertical"


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
        hall: sections.Hall,
        sprite_group: pygame.sprite.Group,
        start_pos: tuple[int, int],
        orientation: Orientation = Orientation.HORZ):
    xy = matrix.get_pos(start_pos[0], start_pos[1])
    print(f"creating room sprites from {xy}")
    for i in range(len(hall.areas)):
        print(f"making room sprite {i}")
        pos = None
        if orientation == Orientation.HORZ:
            pos = matrix.get_pos(start_pos[0] + i, start_pos[1])
        else:
            pos = matrix.get_pos(start_pos[0], start_pos[1] + i)
        room = Room(pos)
        sprite_group.add(room)
        print(f"added sprite at {pos}")


def create_maze_sprites(
        maze: sections.Maze,
        sprite_group: pygame.sprite.Group,
        start_pos: tuple[int, int]):
    create_hall_sprites(maze.halls[0], sprite_group, start_pos)
    # for hall in maze.halls:
    #     create_hall_sprites(hall, sprite_group, start_pos)


matrix = ScreenDivisor(WIDTH, HEIGHT, SCREEN_DIVISION)
maze_sprites = pygame.sprite.RenderUpdates()
the_maze = wizard.cast_maze(2, 5, hall_length_range=(8, 12))
create_maze_sprites(the_maze, maze_sprites, (1, 5))

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw all sprites
    maze_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
