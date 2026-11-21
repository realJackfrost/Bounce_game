# j'appelle mur tout ce qui peut empecher la balle d'avancer, grand mur tout à gauche de la fenetre comme un petit bloc juste pour forcer le joueur à sauter, il en est tout autant pour le sol et le plafond


import pygame


class Mur:

    def __init__(self, x, y, largeur, hauteur, rebond=0.0, couleur=(250, 170, 0)):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.rebond = rebond      # 0 = pas de rebond, 1 = rebond complet
        self.couleur = couleur

    def isthisCollision(self, balle):

        # Point du mur le plus proche du centre de la balle

        proche_x = max(self.rect.left, min(balle.position.x, self.rect.right))
        proche_y = max(self.rect.top, min(balle.position.y, self.rect.bottom))
        espace = balle.position - pygame.Vector2(proche_x, proche_y)
        distance = espace.length()

        # pas de contact
        if distance >= balle.rayon:
            return None

        # collision 
        if distance == 0:
            return pygame.Vector2(0, -1), balle.rayon, self.rebond

        direction_opposee = espace / distance            # direction qui s'éloigne du mur
        decalage = balle.rayon - distance      # de combien la balle est enfoncé 
        return direction_opposee, decalage, self.rebond

    def dessiner(self, ecran):
        pygame.draw.rect(ecran, self.couleur, self.rect)