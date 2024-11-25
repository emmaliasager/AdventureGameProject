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

x, y = 0, 0

class WanderingMonster:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.x = random.randint(0, grid_size - 1) * SQUARE_SIZE
        self.y = random.randint(0, grid_size - 1) * SQUARE_SIZE

    def move(self):
        directions = ['up', 'down', 'left', 'right']
        direction= random.choice(directions)

        if direction == 'up' and self.y > 0:
            self.y -= SQUARE_SIZE
        elif direction == 'down' and self.y < (self.grid_size -1) * SQUARE_SIZE:
            self.y += SQUARE_SIZE
        elif direction == 'left' and self.x > 0:
            self.x -= SQUARE_SIZE
        elif direction == 'right' and self.x < (self.grid_size -1) * SQUARE_SIZE:
            self.x += SQUARE_SIZE

    def get_location(self):
        return (self.x, self.y)

def check_encounter(player_pos, monsters):
    for monster in monsters:
        if player_pos == monster.get_location():
            print("Encounter! You ran into a monster!")
            return True
    return False

monsters = [WanderingMonster(GRID_SIZE)]

running = True
player_pos = (x, y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y > 0:
                y -= SQUARE_SIZE
            elif event.key == pygame.K_DOWN and y < HEIGHT - SQUARE_SIZE:
                y += SQUARE_SIZE
            elif event.key == pygame.K_LEFT and x > 0:
                x -= SQUARE_SIZE
            elif event.key == pygame.K_RIGHT and x < WIDTH - SQUARE_SIZE:
                x += SQUARE_SIZE
            elif event.key == pygame.K_q:
                running = False

    player_pos = (x, y)

    if check_encounter(player_pos, monsters):
        print("Game Over!")
        running = False

    for monster in monsters:
        monster.move()
        
    
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()




                                            

                           
    
