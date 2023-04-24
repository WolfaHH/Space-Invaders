# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
from random import randint
from time import time


class Bonus(pygame.sprite.Sprite):
    """
    La classe Bonus gère l'apparition, et l'update de l'entité Bonus au long du jeu
    """
    def __init__(self, game, shift, tag=None, activated=0):
        super().__init__()
        self.game = game #Instance du jeu
        self.player = self.game.player
        self.type = 1  # 1:Bonus / 0:Malus
        self.length = 0 #durée de validité du bonus
        self.tag = tag #Tag/Nom du bonus

        #Gestion des images
        self.image = pygame.image.load("././assets/img/jeu/heal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image_bonus_on = pygame.image.load("././assets/img/jeu/heal.png")
        self.image_effect = pygame.image.load('././assets/img/jeu/heal.png')

        #Gestion de la position
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 800)
        self.rect.y = randint(-300, -50)

        self.velocity = 7
        self.shift = shift if self.rect.x <= 400 else (shift * (-1)) #déplacement en x
        self.activated = activated #si le bonus est activé sur le joueur

        self.time = time()

    def whichtype(self):
        """

        Returns
        -------
        Fonction effectuant les instructions en fonction du type du bonus récupéré par le joueur
        """
        if self.tag == 'Heal' and self.activated == 1:
            self.image = pygame.image.load("././assets/img/jeu/heal.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image_bonus_on = pygame.image.load("././assets/img/jeu/heal.png")
            self.image_bonus_on = pygame.transform.scale(self.image_bonus_on, (100, 100))
            # self.image_effect = pygame.image.load('././assets/img/jeu/V1.png')
            self.heal()
            self.length = 5
            self.time = time()
            self.type = 1
            self.game.audio.make_sound('sound_heal')

    def left_display(self):
        """

        Returns
        -------
        Gestion de l'affichage à gauche lorsqu'un bonus est actif
        """

        if not (self.tag == None) and self.activated == 1:
            self.game.screen.blit(self.image_bonus_on, (50, 450))
            if self.type == 1:
                font_bonus = font_score = pygame.font.Font('././assets/font/Starjedi.ttf', 25)
                text_bonus = font_bonus.render(str(self.tag) + ' Bonus', 1, (230, 230, 230))
                self.game.screen.blit(text_bonus, (20, 400))
            else:
                pass
        if time() - self.time >= self.length and self.activated == 1:
            self.activated = 0
            self.remove()

    def forward(self):
        """

        Returns
        -------
        Gestion du déplacement du bonus sur l'écran
        """
        # Le déplacement ne se fait si il n'y a pas de collision avec un joueur
        if not (self.game.check_collision(self.game.player, self.game.bonuses)) and self.activated == 0:
            self.rect.y += self.velocity
            self.rect.x += self.shift
        elif self.activated == 0:
            print('flag')
            self.activated = 1
            self.rect.x += 3000
            self.whichtype()

    def remove(self):
        """

        Returns
        -------
        On supprime l'entité bonus des bonuses de l'écran
        """
        self.game.bonuses.remove(self)

    def heal(self):
        """

        Returns
        -------
        Méthode actualisant le niveau de vie du joueur, lorsque le type de bonus est HEAL
        """
        # self.game.screen.blit(self.image_effect, (50, 500))
        if self.player.health + (0.3 * self.player.max_health) < self.player.max_health:
            self.player.health += (0.3 * self.player.max_health)
        else:
            self.player.health += (self.player.max_health - self.player.health)
        print(self.player.health)

    '''
    Idées de bonus, Work in progress
    
    def shield(self):  # bouclier autour du vaisseau d'une durée de 30s
        pass

    def slowness(self):  # malus: speed vaisseau ---
        pass

    def speed(self):  # Bonus; speed projectile + speed vaisseau
        pass

    def flashlight(self):  # Malus: met un espèse de voile noir sur l'écran, sauf sur un petit cercle autour du joueur
        pass

    def explosion(self):  # Malus, bombe de dégat de zone qui cause des dégats au joueur
        pass
    '''
