# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
import json
from random import uniform

# imports de packages locaux :
from src.package_general_game_management.comet_event import CometFallEvent
from src.package_general_game_management.audio import Audio
from src.package_general_game_management.spawning import Spawning
from src.package_user_elements.player import Player


class Game:
    """
    La classe Game à pour rôle de représenter le jeu. Elle compile les classes
    Player, Spawning, CometFallEvent et Audio et les met en relation.
    """

    def __init__(self):

        # Définir ce que notre programme execute
        self.is_playing = 'home'
        self.paused = False

        # Intégration de la classe Audio
        self.audio = Audio(self)

        # Intégration de la clsse Spawning
        self.spawning = Spawning(self)

        # Générer le fond d'écran
        self.screen = pygame.display.set_mode((1000, 600))
        self.background = pygame.image.load("././assets/img/fond.png")
        self.background_position = 0
        self.background_bis_position = -600
        self.velo_bg = 3

        # Générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self, 1)
        self.all_players.add(self.player)
        self.type_vaisseau = 1

        # Dictionnaire des touches pressées
        self.pressed = {}

        # Générer la pluie de comètes
        self.comet_event = CometFallEvent(self)

        # Groupe d'aliens (cf doc methode sprite)
        self.aliens = pygame.sprite.Group()

        # Groupe de bonus (cf doc methode sprite)
        self.bonuses = pygame.sprite.Group()

        # Score et Hightest score par rapport à l'username
        self.score = 0
        self.username = 'None'
        # ouvrir le fichier data.json : un dictionnaire qui enregistre les 
        # données des joueurs
        with open('././data/user/local_saves.json', 'r') as file:
            self.data = json.load(file)

        self.highestscore = 0
        self.highestscore_tampon = 0


    def fond_dynamique(self):

        """
        La méthode fon_dynamique afficher un fond arrière plan qui défile.
        La vitesse de cet arrière plan mouvant est altérée par le niveau et la
        vague que le joueur traverse.
        """

        # Si le jeu n'est pas en pause l'arrière plan défile
        if not self.paused:
            self.background_position += self.velo_bg
            if self.background_position != 0:
                background_bis_position = self.background

            self.background_bis_position += self.velo_bg
            if self.background_bis_position > 0:
                self.background_position = 0
                self.background_bis_position = -600

        self.screen.blit(self.background, (0, self.background_position))

        # Si le jeu est en pause l'arrière plan ne défile plus
        if not self.paused:
            self.screen.blit(background_bis_position, (0, self.background_bis_position))

    def start(self, type_vaisseau):

        """
        La méthode start lance le jeu par : self.is_playing = 'game' avec le 
        type de vaisseau choisi par le joueur.
        """

        self.is_playing = 'game'
        self.type_vaisseau = type_vaisseau

        if self.type_vaisseau == 1:
            self.player = Player(self, 1)
        if self.type_vaisseau == 2:
            self.player = Player(self, 2)
        if self.type_vaisseau == 3:
            self.player = Player(self, 3)

    def game_over(self, t=0):

        """
        La méthode game_over remet le jeu à neuf : retire les monstres,
        réinitialise les niveaux et les vagues, réinitialise la progression de
        la pluie de comètes, réinitialise la vie du vaisseau, remet le jeu en 
        attente et sauvegarde les scores en fonction de t.
        """

        self.aliens = pygame.sprite.Group()
        self.spawning.wave = 0
        self.spawning.level = 0
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = 'game_over_menu' if self.is_playing == 'game' else 'game'
        self.save_score(t)

    def save_score(self, t=0):

        """
        Dans le cas où la méthode save_score est éxecutée avec t = 0 
        (par défaut), le highest score est sauvegardé pour cet username.
        Puis le score est réinitialisé.
        """
        if self.score > self.highestscore:
            self.highestscore = self.score

        if t == 0:
            self.data[self.username]['highestscore'] = self.highestscore
            with open("././data/user/local_saves.json", 'w') as file:
                file.write(json.dumps(self.data, indent=4))

        self.score = 0

    def update_score(self, x):

        """
        La méthode update_score permet au score du joueur de pouvoir augmenter
        en fonction de l'action qu'il aura faite (cette action est x).
        """

        self.score = int(self.score + ((100 * x) * uniform(0.8, 1.8)))

    def update(self, screen):

        """
        La méthode update actualise tout ce qui peut se passer quand on joue
        (quand self.is_playing = 'game').
        """

        ### UPDATE JOUEUR ###

        # Afficher l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Afficher l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # Vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 450:
            self.player.move_up()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 500:
            self.player.move_down()

        if self.check_collision(self.player, self.comet_event.all_comets):
            self.player.damage(9999)

        ### UPDATE BONNUS ET ALIENS ###

        # Spawn des bonnus  et des aliens 
        self.spawning.spawning_run()

        # Récupérer les bonus de notre jeu
        for bonus in self.bonuses:
            bonus.forward()
            # affichage du bonus en cours, si il y en a un
            bonus.left_display()

        # Récuperer les monstres de notre jeu
        for alien in self.aliens:
            alien.forward()
            alien.update_health_bar(screen)

        # Vérifier que si le bonus sort de l'écran on le supprime
        try:
            if bonus.rect.y > 600:
                print('Bye bye bonnus')
                bonus.remove()
        except UnboundLocalError:
            pass

        # Vérifier que si l'alien sort de l'écran on le supprime
        if alien.rect.y > 600:
            alien.remove()

        # Afficher l'ensemble des images de du groupe de bonnus
        self.bonuses.draw(screen)

        # Afficher l'ensemble des images de du groupe de monstres
        self.aliens.draw(screen)

        ### UPDATE PLUIE DE COMETES ###

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les comètes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images des comètes
        self.comet_event.all_comets.draw(screen)

        ### UPDATE DU SCORE ###

        font_score = pygame.font.Font('././assets/font/Starjedi.ttf', 32)
        text_score = font_score.render(str(self.score), 1, (180, 180, 180))
        screen.blit(text_score, (880, 530))

    @staticmethod
    def check_collision(sprite, group):
        """
        La méthode check_collision vérifie si deux éléments sont en contacts
        """

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def set_username(self):

        """
        La méthode set_username permet d'enregistrer les réglages et le
        highest score de l'username'
        Note: Certaines infos stockés ne sont pas encore utilisé, et seront utilisé uniquement pour le menu setting, mais qui restait facultatif
        """
        self.data[self.username] = {
            "control": {
                "right": "K_RIGHT",
                "left": "K_LEFT",
                "up": "K_UP",
                "down": "K_DOWN"
            },
            "language": "french",
            "luminosity": 100,
            "resolution": [
                1000,
                600
            ],
            "volume": [
                100,
                100,
                100
            ],
            "last_vaisseau_chosen": "v1",
            "highestscore": self.highestscore
        }
        
    def set_highscore(self):
        """ Actualise le highscore en fonction du joueur rentré"""
        # récupérer le highest score si username est dans data
        if self.username in self.data:
            self.highestscore = self.data[self.username]['highestscore']
            self.highestscore_tampon = self.data[self.username]['highestscore']

        elif not self.username in self.data:
            self.highestscore = 0
            self.highestscore_tampon = 0
            
