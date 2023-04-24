# -*- coding: utf-8 -*-
# imports de module extérieurs :
import pygame


class Pause:
    """
    Cette classe gère l'affichage de tout le menu pause, lorsque le joueur appuie sur échape lorsqu'"il est en jeu
    """

    def __init__(self):
        # Charger le bouton continue
        self.continue_button = pygame.image.load("././assets/img/menu_pause/continue.png")
        self.continue_button_rect = self.continue_button.get_rect()
        self.continue_button_rect.x = 323
        self.continue_button_rect.y = 78

        # Charger le bouton retry
        self.retry_button = pygame.image.load("././assets/img/menu_pause/retry.png")
        self.retry_button_rect = self.retry_button.get_rect()
        self.retry_button_rect.x = 604
        self.retry_button_rect.y = 300

        # Charger le bouton menu
        self.menu_button = pygame.image.load("././assets/img/menu_pause/menu.png")
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.x = 104
        self.menu_button_rect.y = 300

        # Charger le bouton settings
        self.setting_button = pygame.image.load("././assets/img/menu_pause/setting.png")
        self.setting_button = pygame.transform.scale(self.setting_button, (100, 100))
        self.setting_button_rect = self.setting_button.get_rect()
        self.setting_button_rect.x = 880
        self.setting_button_rect.y = 470

        # Charger l'affichage de current score
        self.currentscore_button = pygame.image.load("././assets/img/menu_pause/currentscore.png")
        self.currentscore_button_rect = self.currentscore_button.get_rect()
        self.currentscore_button_rect.x = 104
        self.currentscore_button_rect.y = 482

        # Charger l'affichage d'highest score
        self.highestscore_button = pygame.image.load("././assets/img/menu_pause/highestscore.png")
        self.highestscore_button_rect = self.highestscore_button.get_rect()
        self.highestscore_button_rect.x = 104
        self.highestscore_button_rect.y = 527

    def update(self, screen, game):
        """

        Parameters
        ----------
        screen
        game

        Returns
        -------
        Applique tout l'affichage
        """
        screen.blit(self.continue_button, self.continue_button_rect)
        screen.blit(self.retry_button, self.retry_button_rect)
        screen.blit(self.menu_button, self.menu_button_rect)
        screen.blit(self.setting_button, self.setting_button_rect)
        screen.blit(self.currentscore_button, self.currentscore_button_rect)
        screen.blit(self.highestscore_button, self.highestscore_button_rect)

        # appliquer le current score
        font_score = pygame.font.Font('././assets/font/Starjedi.ttf', 32)
        text_score = font_score.render(str(game.score), 1, (255, 255, 255))
        screen.blit(text_score, (392, 463))
        #applique le highest score
        text_hightscore = font_score.render(str(game.highestscore), 1, (180, 180, 180))
        screen.blit(text_hightscore, (392, 508))
