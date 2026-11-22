# ce sont les objets qui peuvent tuer le main character

# des épines 
# des perso tueurs mouvants ( certains qui vont de haut en bas, d'autres de bas en haut)
import pygame

class obstacle_sommet:
    #---------------Definition des pics en triangles et de leurs dégats----------------------
    def __init__(self, sommets, couleur=(250, 0, 0), degats = 1):
        self.sommets = sommets
        self.couleur = couleur
        self.degats = degats
        self.a_touche = False

    def verifier_collision(self,balle):
        balle_rect = pygame.Rect()
        balle.position.x - balle.rayon
        balle.position.y - balle.rayon
        balle.rayon*2
        balle.rayon*2
