import sys
import pygame
from tetrominoes import Tetromino

pygame.init()
screen = pygame.display.set_mode((322, 642))
board = pygame.image.load("Background322642.png").convert()
t = Tetromino("T")
t.load_image("tetromino_t.png")

screen.blit(board, (0, 0))
screen.blit(t.img, t.rect)

rate = 800
pygame.display.flip()

going = True
time = pygame.time.get_ticks()

pygame.key.set_repeat()

while going:
    drop_speed = (0, 32)
    right_speed = (32, 0)
    left_speed = (-32, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if t.rect.right < 300:
                t.move(right_speed, screen, screen.blit(board, (0, 0)))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if t.rect.left > 20:
                t.move(left_speed, screen, screen.blit(board, (0, 0)))
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        #     if t.rect.bottom < 640:
        #         t.move(drop_speed, screen, screen.blit(board, (0, 0)))
        while pygame.key.get_pressed()[pygame.K_DOWN]:
            t.move(drop_speed, screen, screen.blit(board, (0, 0)))
            pygame.time.delay(100)
            if pygame.key.get_pressed()[pygame.K_DOWN] is False:
                break

    if t.rect.bottom > 640:
        drop_speed = (0, 0)
        right_speed = (0, 0)
        left_speed = (0, 0)

    if pygame.time.get_ticks() - time >= rate:
        t.move(drop_speed, screen, screen.blit(board, (0, 0)))
        time = pygame.time.get_ticks()

    # rate decreases by time
sys.exit()

