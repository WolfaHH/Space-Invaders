import pygame


# Définir la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):
    """
    Classe ayant pour rôle de gérer l'entité projectile, lazer tiré par le vaisseau
    """

    # Définier le constructeur de cette classe
    def __init__(self, player, vaisseau_type):
        super().__init__()

        self.player = player
        self.velocity = 5 #vitesse des tirs

        #Afficahge conditionnel en fonction du type de vaitesseau du joueur
        if vaisseau_type == 1:
            self.image = pygame.image.load("././assets/img/jeu/V1_projectile.png")

        elif vaisseau_type == 2:
            self.image = pygame.image.load("././assets/img/jeu/V2_projectile.png")

        elif vaisseau_type == 3:
            self.image = pygame.image.load("././assets/img/jeu/V3_projectile.png")

        #Gestion de la position
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y

    def remove(self):
        """

        Returns
        -------
        Supprime le projectile des entités présentes sur le jeu
        """
        self.player.all_projectiles.remove(self)
        # print("Projectile Supprimé")

    def move(self):
        """

        Returns
        -------
        Gère le déplacement du projectile sur l'écran, gère la sortie de l'écran et si il y a collission
        """
        self.rect.y -= self.velocity

        # verifier si le projectile entre en collision avec un monstre
        for alien in self.player.game.check_collision(self, self.player.game.aliens):
            # supprimer le projectile
            self.remove()
            # infliger les degats
            alien.damage(self.player.attack)
            # incrémentation du score
            self.player.game.update_score(1)

        # Vérifier si le prpjectile n'est plus présent sur l'écran
        if self.rect.y > 600:
            # Supprimer le projectile
            self.remove()
