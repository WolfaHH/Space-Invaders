# -*- coding: utf-8 -*-
# imports de module extérieurs :
import pygame


class Game_over:
    """
    Cette classe gère l'affichage de tout le menu game_over, lorsque le joueur meurt
    """
    def __init__(self, game):
        """
        Gère les paramètres
        """
        self.game = game

        self.GRAY = (180, 180, 180)

        # Charger le bouton retry
        self.retry_button = pygame.image.load("././assets/img/menu_gameover/retry.png")
        self.retry_button = pygame.transform.scale(self.retry_button, (260, 140))
        self.retry_button_rect = self.retry_button.get_rect()
        self.retry_button_rect.x = 604
        self.retry_button_rect.y = 384

        # Charger le bouton menu
        self.menu_button = pygame.image.load("././assets/img/menu_gameover/menu.png")
        self.menu_button = pygame.transform.scale(self.menu_button, (260, 140))
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.x = 104
        self.menu_button_rect.y = 384

    def update(self, screen, game):
        """

        Parameters
        ----------
        screen: Fenetre du jeu
        game: Instance du jeu
        Returns
        -------
        Gère tout l'affichage
        """

        screen.blit(self.retry_button, self.retry_button_rect)
        screen.blit(self.menu_button, self.menu_button_rect)

        font_score = pygame.font.Font('././assets/font/Starjedi.ttf', 32)

        if game.score >= game.highestscore:
            # appliquer le current score
            text_score = font_score.render('congratulations !! new highest score : ' + str(game.score), 1, self.GRAY)
            screen.blit(text_score, (80, 150))
            # appliquer la diff de score
            text_score = font_score.render(
                'you beated your old score from ' + str(game.score - game.highestscore_tampon) + ' points', 1,
                self.GRAY)
            screen.blit(text_score, (80, 220))
        else:
            # appliquer le current score
            text_score = font_score.render('you are sooo bad : D', 1, self.GRAY)
            screen.blit(text_score, (100, 100))

            text_score = font_score.render('you didn\'t beat your score : ' + str(game.score), 1, self.GRAY)
            screen.blit(text_score, (100, 150))
            # appliquer la diff
            text_score = font_score.render(
                'at ' + str(game.highestscore_tampon - game.score) + ' from beating your highest score', 1, self.GRAY)
            screen.blit(text_score, (100, 200))
