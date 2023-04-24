# -*- coding: utf-8 -*-
# imports de module extérieurs :
import pygame


class Home:
    """
    Cette classe gère l'affichage de tout le menu D'accueil, lorsque l'on lance le jeu
    """

    def __init__(self, screen, game):
        self.game = game

        self.GRAY = (180, 180, 180)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('././assets/font/Starjedi.ttf', 38)

        self.user_input_value = ""
        self.user_input = self.font.render(self.user_input_value, True, self.GRAY)
        self.user_input_rect = self.user_input.get_rect()
        self.user_input_rect.x = 360
        self.user_input_rect.y = 420

        # Charger le title
        self.banner = pygame.image.load("././assets/img/menu_principal/baniere.png")
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = 0

        # Charger la zone du username pour lancer la partie
        self.selection_button = pygame.image.load("././assets/img/menu_principal/home.png")
        self.selection_button_rect = self.selection_button.get_rect()
        self.selection_button_rect.x = 300
        self.selection_button_rect.y = screen.get_height() // 2 + 40

        # Charger le bouton quit
        self.quit_button = pygame.image.load("././assets/img/menu_principal/quit.png")
        self.quit_button = pygame.transform.scale(self.quit_button, (150, 85))
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x = 10
        self.quit_button_rect.y = 510

        self.data = dict()

    def update(self, screen):
        """

        Parameters
        ----------
        screen

        Returns
        -------
        Applique tout l'affichage
        """
        screen.blit(self.banner, (self.banner_rect))
        screen.blit(self.selection_button, self.selection_button_rect)
        screen.blit(self.quit_button, self.quit_button_rect)

        screen.blit(self.user_input, self.user_input_rect)

        self.clock.tick(30)
