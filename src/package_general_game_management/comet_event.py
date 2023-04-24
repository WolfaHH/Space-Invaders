# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
# imports de packages locaux :
from src.package_game_elements.comet import Comet


class CometFallEvent:
    """
    La classe CometFallEvent permet de générer une pluie de météorites ou de comètes
    dans le jeu lorsque la barre en bas de celui-ci atteint le maximum. Il y a aura
    plusieurs méthodes, tout d'abord tout ce qui concerne la barre d'activation
    de l'évènement et puis la pluie de comètes.
    """

    # lors du chargement --> creer un compteur
    def __init__(self, game):

        # caractéristiques de la barre avec un pourcentage de vitesse
        self.percent = 0
        self.percent_speed = 4

        # appel de la classe game
        self.game = game

        self.fall_mode = False

        # definir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        '''
        Cette méthode permet à la barre d'activation de se remplir avec une
        addition avec la vitesse du pourcentage.
        '''
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        '''
        Cette méthode permet de vérifier si la barre d'activiation est remplie
        à son maximum, dans cette situation c'est à 100.
        '''
        return self.percent >= 100

    def meteor_fall(self):
        '''
        Cette méthode génère la pluie de météorites en faisant apparaitre 7. Avec la
        boucle for, on fait apparaitre la comète en ajoutant une comète avec toutes
        les caractéristiques de celui-ci grâce à la classe Comet et en émettant
        le son d'une comète.
        '''
        # boucle pour les valeurs entre 1 et 7
        self.game.audio.make_sound('sound_comet')
        for i in range(1, 8):
            # apparaitre une premiere comète
            self.all_comets.add(Comet(self))
        self.fall_mode = False

    def attempt_fall(self):
        '''
        Cette méthode permet de vérifier si la barre d'activiation est remplie
        à son maximum, alors on active l'évènement.
        '''
        # la jauge d'evenement est totalement chargée
        if self.is_full_loaded():
            print("Pluie de comètes !")
            self.meteor_fall()
            self.fall_mode = True  # activer l'event

    def reset_percent(self):
        '''
        Réinitialise le pourcentage qui permet d'activer l'évènement.
        '''
        self.percent = 0

    def update_bar(self, surface):
        '''
        Cette méthode permet d'afficher la barre sur l'écran de jeu avec la méthode
        add_percent pour faire avancer la barre.
        '''

        # ajouter du pourcentage à la barre
        self.add_percent()

        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (80, 80, 80),
                         [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
