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

        """avec ça on vérifie la proximité de la balle avec les somments ça PREND PAS LES COTES EN COMPTE"""
        for s in self.sommets:
            if (pygame.Vector2(s).distance_to(balle.position) < balle.rayon):
               return True

        #--------------On va tester les cotés 

        # for i in range (3):
        #    #On est dans le plan (vectors) 2D
        #    #trouver le vecteur de chaque coté 
        #     A = self.sommets[i]
        #     B = self.sommets[(i+1)%3]
        #     ab = B-A #droite (AB)
        #     # il faut avoir le segment AB ça revient à limiter la droite a la distance entre A et B
        #     AB = A + ab*dt

        #     ab.dot(balle.position) # projection de balle sur (AB)

        return False

    def dessiner(self, ecran):
     pygame.draw.polygon(ecran, self.couleur, self.sommets)