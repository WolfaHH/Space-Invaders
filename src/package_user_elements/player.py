# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
# imports de packages locaux :
from .projectile import Projectile


class Player(pygame.sprite.Sprite):
    """
    La classe Player à pour rôle de représenter le joueur. 
    Elle défini qui est le joueur : quel vaisseau, quels points de vie, quelle 
    vitesse, quelle puissance, ainsi que ses projectiles. 
    Elle donne aussi les actions qu'il est possible de faire : se déplacer,
    tirer, se prendre des dégats.'
    """

    def __init__(self, game, vaisseau_type):

        # La fonction super() est très vague quand on regarde la documentation
        # autour d'elle. Mais en somme, elle nous permet de "transporter" la
        # classe vaisseau et plus particulièrement son constructeur (__init__)
        super().__init__()

        # Intégration de la classe Game
        self.game = game

        ### 3 types de vaisseau disponnibles au choix pour le joueur ###

        if vaisseau_type == 1:

            # Propriétés du premier vaisseau 
            self.health = 20
            self.max_health = 20
            self.coef_health = 3.75
            self.attack = 1000
            self.velocity = 7
            self.image = pygame.image.load("././assets/img/jeu/V1.png")
            self.color = (85, 50, 85)

        elif vaisseau_type == 2:

            # Propriétés du deuxième vaisseau 
            self.health = 50
            self.max_health = 50
            self.coef_health = 1.5
            self.attack = 12
            self.velocity = 30
            self.image = pygame.image.load("././assets/img/jeu/V2.png")
            self.color = (45, 120, 60)

        elif vaisseau_type == 3:

            # Propriétés du troisième vaisseau 
            self.health = 75
            self.max_health = 75
            self.coef_health = 1
            self.attack = 50
            self.velocity = 4
            self.image = pygame.image.load("././assets/img/jeu/V3.png")
            self.color = (100, 25, 25)

        # Groupe de projectile (cf doc méthode sprite)
        self.all_projectiles = pygame.sprite.Group()

        # Hitbox représentée par l'image
        self.rect = self.image.get_rect()

        # Position du vaisseau
        self.rect.x = 480
        self.rect.y = 450

    def damage(self, amount):

        """
        La méthode damage applique des dégats au joueur. Si le joueur peut
        survivre au coup, l'amount sera soustrait à ses points de vie,
        dans l'autre cas c'est que le joueur meurt et game over.
        """

        # Le joueur peut survivre
        if self.health - amount > amount:
            self.health -= amount
            print(self.health)

        # Le joueur n'a plus de points de vie    
        else:
            self.game.audio.end_music()
            self.game.audio.start_music('over')
            self.game.game_over()

    def update_health_bar(self, surface):

        """
        La méthode update_health_bar rend compte des points de vie du joueur par
        une barre de vie qui est affichée sur la surface.
        """

        # Déssiner le fond de la barre de vie
        pygame.draw.rect(surface, (30, 30, 30), [self.rect.x, self.rect.y + 115, self.max_health * self.coef_health, 6])

        # Désiner la barre de vie qui évoluz avec la vie du joueur
        pygame.draw.rect(surface, self.color, [self.rect.x, self.rect.y + 115, self.health * self.coef_health, 6])

    def launch_projectile(self, vaisseau_type):

        """
        La méthode lauch_projectile est l'action de tirer des lasers, ceux-ci
        sont adaptés au type de vaisseau'
        """

        # Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self, vaisseau_type))
        self.game.audio.make_sound('sound_laser')

    def move_right(self):

        """
        La méthode move_right permet au joueur de se déplacer vers la droite
        """

        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.x += self.velocity

    def move_left(self):

        """
        La méthode move_left permet au joueur de se déplacer vers la gauche
        """

        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.x -= self.velocity

    def move_up(self):

        """
        La méthode move_up permet au joueur de se déplacer vers le haut
        """

        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.y -= self.velocity

    def move_down(self):

        """
        La méthode move_down permet au joueur de se déplacer vers le bas
        """

        # Pas de condition ici car c'est un échapatoire, une façon d'esquiver
        self.rect.y += self.velocity
