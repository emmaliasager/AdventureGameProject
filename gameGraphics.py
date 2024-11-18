import pygame
import sys

pygame.init()

GRID_SIZE = 10
SQUARE_SIZE = 32
WIDTH, HEIGHT = GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Square!")

x, y = 0, 0


running = True
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

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()




                                            

                           
    
