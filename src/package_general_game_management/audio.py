# -*- coding: utf-8 -*-
#imports de modules éxtérieurs
import pygame


class Audio:
    """
    La Audio Game à pour rôle de manage tout la partie son du jeu, les ost et les différents bruitages
    """

    def __init__(self, game):

        self.game = game #récupération de l'instance game
        pygame.mixer.init() #initialisation du module mixer

        self.playlist = list()

        #Les osts du jeu (note nath: seule les formats mp3 sont accetpés)
        self.music_theme = '././assets/audio/ost/theme.mp3'
        self.music_theme2 = '././assets/audio/ost/theme2.mp3'
        self.pause = '././assets/audio/ost/pause.mp3'
        self.over = '././assets/audio/ost/over.mp3'

        #Les bruitages du jeu
        #Note Nath : seules les format .ogg et wav sont acceptés
        self.sound_click = pygame.mixer.Sound('././assets/audio/sounds/click.wav')
        self.sound_laser = pygame.mixer.Sound('././assets/audio/sounds/laser.ogg')
        self.sound_heal = pygame.mixer.Sound('././assets/audio/sounds/heal.wav')
        self.sound_comet = pygame.mixer.Sound('././assets/audio/sounds/comet.wav')

    def start_music(self, song):
        """

        Parameters
        ----------
        song: nom de la musique, initialisé dans init

        Returns
        -------
        Exécute la musique choisi
        """
        if type(song) != list: #si on ne veux pas éxécuter une playlist

            pygame.mixer.music.load(getattr(self, song, 'the song entered isn\'t settled ;p'))
            pygame.mixer.music.play(-1, 0)

        else: #si une playliste est voulu, fonctionne, mais non-utilisé pour le moment, au final
            self.playlist.clear()
            self.playlist.extend([s for s in song])
            pygame.mixer.music.load(self.playlist.pop())  # Get the first track from the playlist
            pygame.mixer.music.queue(self.playlist.pop())  # Queue the 2nd song,...
            pygame.mixer.music.play()  # Play the music

    @staticmethod
    def end_music():
        """
        Returns
        -------
        stop la musique actuellement en cours
        """
        pygame.mixer.music.stop()

    def make_sound(self, sound):
        """

        Parameters
        ----------
        sound: nom du bruitage, initialisé dans init

        Returns
        -------
        Produit le son voulu

        """
        t = getattr(self, sound, 'le song n\'est pas chargé')
        t.set_volume(2)
        t.play()
