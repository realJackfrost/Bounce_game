# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
running = True
sommets = [(50, 650), (75, 600), (100, 650)]
sommets2= [(100, 650), (125, 600), (150, 650)]
sommets3= [(150, 650), (175, 600), (200, 650)]
obstacles = [sommets, sommets2, sommets3]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    pygame.draw.polygon(screen, (250, 0, 0), sommets)
    pygame.draw.polygon(screen, (250, 0, 0), sommets2)
    pygame.draw.polygon(screen, (250, 0, 0), sommets3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    class obstacle_sommet:

     def __init__(self, sommets, couleur=(250, 0, 0)):
     self.sommets = sommets
     self.couleur = couleur
     self.a_touche = False
    
    # création du rectangle de test le plus petit possible pour les triangle selon leur coordonées 
     xs = [p[1] for p in sommets]
     ys = [p[2] for p in sommets]
     self.rect = pygame.Rect(
        min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    )

     def verifier_collision(self, balle):
      balle_rect = pygame.Rect(
        balle.position.x - balle.rayon,
        balle.position.y - balle.rayon,
        balle.rayon * 2,
        balle.rayon * 2,

pygame.quit()