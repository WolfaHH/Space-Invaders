# -*- coding: utf-8 -*-
#imports de modules éxtérieurs
from random import choices
#imports de packages locaux :
from src.package_game_elements import *


class Spawning:
    """
    La classe Spawning a pour rôle de de gérer l'apparition, de manière globale, des monstres et des bonus, avec une gestion de la difficulté du jeu
    """

    def __init__(self, game):
        """

        Parameters
        ----------
        game
        """
        self.game = game  # récupération de l'instance game
        self.level = 0  # initialisation du Level, représentant un palier de difficulté
        self.wave = 0  # différentes vagues
        self.velocity = 3  # vélocité des aliens

    def spawn_alien(self, target=0):
        """

        Parameters
        ----------
        target: booléen, par défault à 0, signifiant si l'alien doit apparaitre au dessus du joueur

        Returns
        -------
        Ajout d'un alien dans la liste des alien de l'instance du jeu
        """
        alien = Alien(self.game, target, self.velocity)
        self.game.aliens.add(alien)

    def spawn_bonus(self, shift):
        """

        Parameters
        ----------
        shift: int, déplacement en abscisse du bonus

        Returns
        -------
        Ajout d'un bonus dans la liste des bonus de l'instance du jeu

        """
        self.game.bonus = Bonus(self.game, shift, 'Heal')
        self.game.bonuses.add(self.game.bonus)

    def spawning_run(self):
        """

        Returns
        -------
        Algorithme de gestion d'apparition des aliens & bonus, ainsi que de la difficulté
        """
        if not self.game.aliens: #quand y a plus d'aliens

            if self.wave == 0:
                self.spawn_alien(1)
                self.spawn_bonus(0.5)

            elif self.wave == 1 or self.wave == 5:
                for e in range(0, self.level + 2):
                    i = choices([0, 1], [75, 25], k=1)
                    self.spawn_alien(i[0])
                self.spawn_bonus(0.2)

            elif self.wave == 2 or self.wave == 3 or self.wave == 4:
                for e in range(0, self.level + 3):
                    i = choices([0, 1], [75, 25], k=1)
                    self.spawn_alien(i[0])

            self.wave += 1
            self.wave = 0 if self.wave == 5 else self.wave
            print('wave : ', self.wave, ' | level : ', self.level)

            if self.wave == 0:
                if not self.level > 7:
                    self.level += 1
                    self.velocity += 1
                    self.game.player.velocity += 1
                    self.game.velo_bg += 1

        else:

            return None
