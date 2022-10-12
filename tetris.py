import sys
import pygame
from tetrominoes import Tetromino

screen = pygame.display.set_mode((322, 642))
board = pygame.image.load("Background322642.png").convert()
t = Tetromino("T")
t.load_image("tetromino_t.png")

screen.blit(board, (0, 0))
screen.blit(t.img, t.rect)
speed = (0, 32)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if t.rect.bottom > 640:
        speed = (0, 0)
    t.rect = t.rect.move(speed)
    screen.blit(board, (0, 0))
    screen.blit(t.img, t.rect)
    pygame.display.flip()
    pygame.time.delay(50)

