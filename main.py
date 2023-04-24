# -*- coding: utf-8 -*-
# imports de modules éxtérieurs
import pygame
# imports de packages locaux :
from src.package_general_game_management import Game
from src.package_menu import *

pygame.init()

# Générer la fenêtre de notre jeu
pygame.display.set_caption("Space Invaders | NSI Project by Nathanaël, Mathias, Lucas and Hugo")
screen = pygame.display.set_mode((1000, 600))
surface = pygame.display.get_surface()
x, y = size = surface.get_width, surface.get_height
#icon_32x32 = pygame.image.load("assets/img/icon.png")
#pygame.display.set_icon(icon_32x32)

# Charger le jeu
game = Game()
gameover = Game_over(game)
home = Home(screen, game)
selection = Selection()
pause = Pause()

current_music = 'music_theme'
game.audio.start_music('music_theme')

running = True


# Boucle tant que cette condition est vraie
while running:
    

    # Afficher l'arrière plan de notre jeu
    game.fond_dynamique()

    # Vérifier si le programme doit executer le menu home
    if game.is_playing == 'home':
        game.paused = False
        current_music = 'music_theme'
        # lancer le menu home
        home.update(screen)
        
    # Vérifier si le programme doit executer le menu selection    
    if game.is_playing == 'selection':
        game.paused = False
        # lancer le menu selection
        selection.update(screen, game)
        
    # Vérifier si le programme doit executer jeu
    if game.is_playing == 'game':
        game.paused = False
        # lancer le jeu
        game.update(screen)
    
    # Vérifier si le programme doit executer le menu pause
    if game.is_playing == 'pause':
        game.paused = True
        # lancer le menu pause
        pause.update(screen, game)
    
    # Vérifier si le programme doit executer le menu game over
    if game.is_playing == 'game_over_menu':
        game.paused = True
        # lancer le menu game over
        gameover.update(screen, game)

    
    # Actualiser la fenêtre
    pygame.display.flip()

    
    # Détections des interactions joueurs / périphériques
    for event in pygame.event.get():
 
        
        
        # Vérifier que l'event est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")



        # Vérifier que l'event est une touche enfoncée
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si une des touches "entrée" est enclenchée
            # -> le programme doit executer le menu selection  
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                game.audio.make_sound('sound_click')
                game.is_playing = 'selection'
                game.username = home.user_input_value
                game.set_highscore()
                game.set_username()
                
                break     
            
            
            # écrire l'username
            if event.key == pygame.K_BACKSPACE and game.is_playing == "home":
                home.user_input_value = home.user_input_value[:-1]
            
            elif game.is_playing == "home":
                home.user_input_value += event.unicode
                
            # mettre à jour les attributs liés à l'username
            home.user_input = home.font.render(home.user_input_value, True, home.GRAY)
            home.user_input_rect = home.user_input.get_rect()
            home.user_input_rect.x = 360
            home.user_input_rect.y = 390
            
            
            # détecter si la touche espace est enclenchée
            # -> Lancer un projectile
            if event.key == pygame.K_SPACE:
                
                game.player.launch_projectile(selection.type_vaisseau)


            # détecter si la touche echap est enclenchée
            # -> le programme doit executer le menu selection
            if event.key == pygame.K_ESCAPE and game.is_playing == "game":
                game.audio.end_music()
                game.audio.start_music('pause')
                game.is_playing = 'pause'


        # Vérifier que l'event est une touche relachée
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False



        # Vérifier que l'event est un click de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.audio.make_sound('sound_click')
            
            
            # Si menu home est executé 
            if game.is_playing == 'home':
                
                # et que la position de la souris est sur le bouton quit
                if home.quit_button_rect.collidepoint(event.pos):
                    
                    # -> fin de la boucle + fermeture de pygame
                    running = False
                    pygame.quit()


            # Si menu selection est executé
            elif game.is_playing == 'selection':
                
                # et que la position de la souris est sur la grille de selection
                # -> choix du type de vaisseau
                if selection.V1_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 1
                if selection.V2_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 2
                if selection.V3_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 3
                
                # et que la position de la souris est sur le bouton play
                # -> lancer le jeu
                if selection.play_button_rect.collidepoint(event.pos):
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                    game.start(selection.type_vaisseau)
                
                # et que la position de la souris est sur le bouton back
                # -> retour au menu home
                if selection.back_button_rect.collidepoint(event.pos):
                    game.is_playing = 'home'
                    
            
            # Si menu pause est executé
            elif game.is_playing == 'pause':
                
                # et que la position de la souris est sur
                # -> retour au jeu sans changement
                if pause.continue_button_rect.collidepoint(event.pos):
                    game.is_playing = 'game'
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                    
                # et que la position de la souris est sur le bouton retry
                # -> retour au jeu avec réinitialisation du jeu
                if pause.retry_button_rect.collidepoint(event.pos):
                    game.game_over(1)
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                    
                # et que la position de la souris est sur le bouton menu
                # -> retour au menu selection
                if pause.menu_button_rect.collidepoint(event.pos):
                    game.game_over(1)
                    game.is_playing = 'selection'
                    game.audio.end_music()
                    game.audio.start_music('music_theme')
            
            
            # Si menu pause est executé
            elif game.is_playing == 'game_over_menu':
                
                # et que la position de la souris est sur le bouton menu
                # -> retour au menu selection
                if gameover.menu_button_rect.collidepoint(event.pos):
                    game.game_over()
                    game.is_playing = 'selection'
                    game.audio.end_music()
                    game.audio.start_music('music_theme')
                
                # et que la position de la souris est sur
                # -> retour au jeu avec réinitialisation du jeu
                if gameover.retry_button_rect.collidepoint(event.pos):
                    game.game_over()
                    game.is_playing = 'game'
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')

