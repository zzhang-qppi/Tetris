import pygame


class Tetromino(object):
    def __init__(self, name):
        self.name = name
        self.img = None
        self.rect = None

    def load_image(self, path, size=(90, 60), l_topleft=(1, 1)):
        self.img = pygame.image.load(path).convert_alpha()
        pygame.transform.scale(self.img, size)
        self.rect = self.rect.get_rect()
        self.rect.topleft = l_topleft

    def drop(self, speed, screen, refrate = 1000):
        self.rect = self.rect.move(speed)
        screen.

