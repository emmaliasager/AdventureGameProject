import pygame
import sys
import random

pygame.init()

GRID_SIZE = 10
SQUARE_SIZE = 32
WIDTH, HEIGHT = GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Encounter Game!")

clock = pygame.time.Clock()


CHARACTER_IMAGE_PATH = "assets/character.png"
MONSTER_IMAGE_PATH = "assets/monster.png"

def load_image(path, fallback_color, size=(SQUARE_SIZE, SQUARE_SIZE)):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error:
        print(f"Warning: Unable to load {path}. Using fallback shape.")
        surface = pygame.Surface(size)
        surface.fill(fallback_color)
        return surface

character_image = load_image(CHARACTER_IMAGE_PATH, BLACK)
monster_image = load_image(MONSTER_IMAGE_PATH, RED)

player_pos = [WIDTH // 2, HEIGHT //2]
monsters = [WanderingMonster(GRID_SIZE) for _ in range(3)]

class WanderingMonster:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.x = random.randint(0, grid_size - 1) * SQUARE_SIZE
        self.y = random.randint(0, grid_size - 1) * SQUARE_SIZE

    def move(self):
        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)

        if direction == 'up' and self.y > 0:
            self.y -= SQUARE_SIZE
        elif direction == 'down' and self.y < (self.grid_size - 1) * SQUARE_SIZE:
            self.y += SQUARE_SIZE
        elif direction == 'left' and self.x > 0:
            self.x -= SQUARE_SIZE
        elif direction == 'right' and self.x < (self.grid_size - 1) * SQUARE_SIZE:
            self.x += SQUARE_SIZE

    def get_location(self):
        return (self.x, self.y)

    def check_encounter(player_pos, monsters):
        for monster in monsters:
            if tuple(player_pos) == monster.get_location():
                print("Encounter! You ran into a monster!")
                return True
        return False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= SQUARE_SIZE
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - SQUARE_SIZE:
        player_pos[1] += SQUARE_SIZE
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= SQUARE_SIZE
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - SQUARE_SIZE:
        player_pos[0] += SQUARE_SIZE


    if check_encounter(player_pos, monsters):
        print("Game Over!")
        running = False

    for monster in monsters:
        monster.move()


    screen.fill(WHITE)
    screen.blit(character_image, player_pos)
    for monster in monsters:
        screen.blit(monster_image, monster.get_location())

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

                                            

                           
    
