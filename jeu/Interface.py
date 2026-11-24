import pygame

class Interface:
    def __init__(self, largeur=1000, hauteur=700):
      self.police = pygame.font.Font(None, 50)
      self.bouton_play = pygame.Rect(0, 0, 220, 70)
      self.bouton_play.center = (largeur // 2, hauteur // 2)

    def dessiner(self, ecran):
       ecran.fill("black")
       pygame.draw.rect(ecran, (255, 110, 10), self.bouton_play)

       texte = self.police.render("Jouer", True, (255, 255, 255))
       texte_rect = texte.get_rect(center=self.bouton_play.center)
       ecran.blit(texte, texte_rect)

    def bouton_clique(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.bouton_play.collidepoint(event.pos)
        return False