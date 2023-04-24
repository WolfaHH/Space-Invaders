# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
import random


class Comet(pygame.sprite.Sprite):
    """
    La classe Comet a pour rôle définir les propriétés d'une seule comète
    parmis toutes les comètes dans l'event_comet, l'évènement qui permet de générer
    une pluie de comètes dans le jeu. Elle a 2 caractéristiques principales : fall,
    cela permet de faire tomber une comète de haut en bas et le remove, qui permet
    de supprimer la comète dès que celui-ci dépasse l'écran pour éviter de faire 
    laguer le jeu à cause d'identités qu'on ne voit plus et qu'ils ne servent à rien.
    """

    def __init__(self, comet_event):

        super().__init__()
        # definir l'image de la comete
        self.image = pygame.image.load("././assets/img/jeu/comet.png")

        # redimensionner l'image de la comète
        self.image = pygame.transform.scale(self.image, (80, 80))

        # générer une hitbox de la comète pour les collisions avec le joueur
        self.rect = self.image.get_rect()

        # sa vitesse avec un peu d'aléatoire
        self.velocity = random.randint(3, 5)

        # ses coordonnées (x, y)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)

        # on appelle l'évènement event_comet
        self.comet_event = comet_event

    def remove(self):
        '''
        La méthode remove supprime la comète avec la fonction remove() proposée
        par pygame. Lorsque l'évènement se déclenche, si toutes les comètes sont
        détruites ( ne sont plus dans le jeu ), alors on remet à 0 la barre qui
        permet de rafraichir l'évènement comet_event et fait apparaitre des ennemis
        par la suite.'
        '''
        self.comet_event.all_comets.remove(self)

        # si le nombre de comete est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0
            self.comet_event.reset_percent()

            # apparaitre des monstres à la suite de l'event
            self.comet_event.game.spawning.spawn_alien()
            self.comet_event.game.spawning.spawn_alien()
            self.comet_event.game.spawning.spawn_alien()

    def fall(self):
        '''
        La méthode fall permet de faire avancer la comète de haut en bas. Si la 
        comète atteint le sol, c'est-à-dire le bas de l'écran, on retire la comète
        avec la méthode remove(). Il y a aussi la collision avec le joueur, pour
        cela la comète disparait et le joueur pert des dégats grâce à une de ses
        méthodes ( du joueur )
        '''
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 700:

            print("Sol")

            # retirer comète
            self.remove()

            # si il n'y a plus de comètes sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("l'event est fini")

                # remmettre la jauge de départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la comète touche le joueur
        if self.comet_event.game.check_collision(self.comet_event.game.player, self.comet_event.all_comets):
            print("Joueur touché")

            # retirer la comète
            self.remove()

            # subir degats
            self.comet_event.game.player.damage(20)
