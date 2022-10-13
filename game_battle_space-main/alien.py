import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий единственного инопланетянина во флоте."""

    def __init__(self, ai_settings, screen):
        """Инициализируeт инопланетянина и устанавливает его начальное положение."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загружает изображение инопланетянина и устанавливает его атрибут rect.
        self.image = pygame.image.load('images/1.png')
        self.rect = self.image.get_rect()

        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        
        self.x = int(self.rect.x)
        
    def check_edges(self):
        
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left >= 0:
            return True
        
    def update(self):
        
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        # self.rect.x = self.x

    def blitme(self):
        
        self.screen.blit(self.image, self.rect)
