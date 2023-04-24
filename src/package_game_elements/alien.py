# -*- coding: utf-8 -*-
#imports de modules éxtérieurs
import pygame
from random import randint


class Alien(pygame.sprite.Sprite):
    """
    La classe Alien gère l'apparition, et l'update de l'entité d'alien au long du jeu
    """

    def __init__(self, game, target, velocity):
        """

        Parameters
        ----------
        game: Instance du jeu
        target: booléen, par défault à 0, signifiant si l'alien doit apparaitre au dessus du joueur
        velocity: INT, vélocité de l'alien en y
        """
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("././assets/img/jeu/alien.png")

        #coordonées
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 800) if target == 0 else self.game.player.rect.x
        self.rect.y = randint(-300, -50)
        self.velocity = velocity

    def damage(self, amount):
        """

        Parameters
        ----------
        amount: Int, dégat reçu (puissance d'attaque du joueur)

        Returns
        -------
        Gestion de l'alien lorsqu'il recoit des dégats

        """
        # infliger les degats
        self.health -= amount

        # Vérifier si son nouveau nombre de point de vie est inférieur ou égal à 0
        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.remove()

        # si la barre d'evenement est chargé à son max
        if self.game.comet_event.is_full_loaded():
            # retirer du jeu
            self.game.aliens.remove(self)

            # appel de la méthode pour essayer de declencher la pluie de comete
            self.game.comet_event.attempt_fall()

    def remove(self):
        """

        Returns
        -------
        Retire l'alien de la liste d'aliens présents du jeu
        """
        self.game.aliens.remove(self)

    def update_health_bar(self, surface):
        """

        Parameters
        ----------
        surface: écran

        Returns
        -------
        Actualise la barre de vie de l'alien
        """

        # Définir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
        bar_position = [self.rect.x - 3, self.rect.y - 10, self.health / 2, 5]
        # Définir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x - 3, self.rect.y - 10, self.max_health / 2, 5]

        # Dessiner notre barre de vie
        pygame.draw.rect(surface, (30, 30, 30), back_bar_position)
        pygame.draw.rect(surface, (70, 70, 120), bar_position)

    def forward(self):
        """

        Returns
        -------
        Gère le déplacement en ordonnée de l'alien
        """
        # Le déplacement ne se fait si il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self.game.player, self.game.aliens):
            self.rect.y += self.velocity
        else:
            # Infliger des degats (au joueur)
            self.game.player.damage(self.attack)
