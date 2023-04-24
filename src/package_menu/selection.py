# -*- coding: utf-8 -*-
# imports de module extérieurs :
import pygame


class Selection:
    """
    Cette classe gère l'affichage de tout le menu selection
    """
    def __init__(self):
        # Charger le titre du menu
        self.titre = pygame.image.load("././assets/img/menu_selection/titre.png")
        self.titre_rect = self.titre.get_rect()
        self.titre_rect.x = 100
        self.titre_rect.y = 120

        # Charger le bouton pour lance la partie
        self.play_button = pygame.image.load("././assets/img/menu_selection/play_bouton.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 600
        self.play_button_rect.y = 415

        # Charger le bouton pour back to menu
        self.back_button = pygame.image.load("././assets/img/menu_selection/back_bouton.png")
        self.back_button = pygame.transform.scale(self.back_button, (150, 85))
        self.back_button_rect = self.play_button.get_rect()
        self.back_button_rect.x = 10
        self.back_button_rect.y = 510

        # Choix du vaisseau
        self.type_vaisseau = 1

        # Charger la grille de selection
        self.V1 = pygame.image.load("././assets/img/menu_selection/V1_grille.png")
        self.V1_rect = self.V1.get_rect()
        self.V1_rect.x = 100
        self.V1_rect.y = 230

        self.V2 = pygame.image.load("././assets/img/menu_selection/V2_grille.png")
        self.V2_rect = self.V2.get_rect()
        self.V2_rect.x = 240
        self.V2_rect.y = 230

        self.V3 = pygame.image.load("././assets/img/menu_selection/V3_grille.png")
        self.V3_rect = self.V3.get_rect()
        self.V3_rect.x = 380
        self.V3_rect.y = 230

        # Charger les stats du vaisseau
        self.S1 = pygame.image.load("././assets/img/menu_selection/V1_stat.png")
        self.S1_rect = self.S1.get_rect()
        self.S1_rect.x = 130
        self.S1_rect.y = 400

        self.S2 = pygame.image.load("././assets/img/menu_selection/V2_stat.png")
        self.S2_rect = self.S2.get_rect()
        self.S2_rect.x = 130
        self.S2_rect.y = 400

        self.S3 = pygame.image.load("././assets/img/menu_selection/V3_stat.png")
        self.S3_rect = self.S3.get_rect()
        self.S3_rect.x = 130
        self.S3_rect.y = 400

        # Charger l'histoire du vaisseau
        self.H1 = pygame.image.load("././assets/img/menu_selection/V1_histoire.png")
        self.H1_rect = self.H1.get_rect()
        self.H1_rect.x = 600
        self.H1_rect.y = 45

        self.H2 = pygame.image.load("././assets/img/menu_selection/V2_histoire.png")
        self.H2_rect = self.H2.get_rect()
        self.H2_rect.x = 600
        self.H2_rect.y = 45

        self.H3 = pygame.image.load("././assets/img/menu_selection/V3_histoire.png")
        self.H3_rect = self.H3.get_rect()
        self.H3_rect.x = 600
        self.H3_rect.y = 45

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

        screen.blit(self.titre, self.titre_rect)
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.back_button, self.back_button_rect)
        screen.blit(self.V1, self.V1_rect)
        screen.blit(self.V2, self.V2_rect)
        screen.blit(self.V3, self.V3_rect)


        if self.type_vaisseau == 1:
            screen.blit(self.S1, self.S1_rect)
            screen.blit(self.H1, self.H1_rect)

        if self.type_vaisseau == 2:
            screen.blit(self.S2, self.S2_rect)
            screen.blit(self.H2, self.H2_rect)

        if self.type_vaisseau == 3:
            screen.blit(self.S3, self.S3_rect)
            screen.blit(self.H3, self.H3_rect)

        # appliquer le nom du joueur
        font_score = pygame.font.Font('././assets/font/Starjedi.ttf',32)
        
        text_score = font_score.render('Welcome to you dear', 1, (230, 230, 230))
        screen.blit(text_score, (100, 55))
        
        text_score = font_score.render(str(game.username), 1, (180, 180, 180))
        screen.blit(text_score, (100, 85))
