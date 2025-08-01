# pared.py
import pygame

class Pared(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill((100, 100, 100))  # Gris
        self.rect = self.image.get_rect(topleft=(x, y))
