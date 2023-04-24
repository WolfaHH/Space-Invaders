
"""
Ce package contient les modules des classes utilisées de fonctions de gestion de bases du jeu :
- Module Game, module coeur du jeu, mettant en relation les autres modules
- Module Audio, gère toute la partie audio (Ost's & Bruitages)
- Module Spawning, gère le spawn des éléments de type Aliens du jeu
- Module comet_event, gère le spawn des éléments de type comet du jeu

"""

#import des modules :

from .audio import Audio
from .comet_event import CometFallEvent
from .game import Game
from .spawning import Spawning




