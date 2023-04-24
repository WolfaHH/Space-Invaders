# MODULE WORKING IN PROGRESS
# -*- coding: utf-8 -*-
# imports de module extérieurs :
import pygame


class Setting:
    def __init__(self):
        # Charger le bouton continue
        self.continue_button = pygame.image.load("././assets/img/menu_pause/continue.png")
        self.continue_button = pygame.transform.scale(self.continue_button, (350, 140))
        self.continue_button_rect = self.continue_button.get_rect()
        self.continue_button_rect.x = 335
        self.continue_button_rect.y = 70

    def update(self, screen):
        screen.blit(self.continue_button, self.continue_button_rect)
