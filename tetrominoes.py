import pygame


class Tetromino(object):
    def __init__(self, name):
        self.name = name
        self.img = None
        self.rect = None

    def load_image(self, path, size=(90, 60), l_topleft=(1, 1)):
        self.img = pygame.image.load(path).convert_alpha()
        pygame.transform.scale(self.img, size)
        self.rect = self.img.get_rect()
        self.rect.topleft = l_topleft

    def move(self, speed, screen, refresh, refrate=1000):
        if self.rect.bottom < 640:
            self.rect = self.rect.move(speed)
        refresh
        screen.blit(self.img, self.rect)
        pygame.display.flip()

