import pygame
from balle import Balle
from murs import Mur

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()

murs = [
    Mur(0, 0, 1000, 70),      # plafond
    Mur(0, 0, 50, 700),       # mur de gauche
    Mur(1000,0,10,700),       # mur à droite (un peu) invisible
    Mur(0, 350, 500, 70),    # milieu
    Mur(0, 650, 1000, 70,0.5),    # sol bis
    
]
balle = Balle(100,100)

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. La balle agit (chaque méthode consulte les touches)
    balle.arreter_horizontal()
    balle.avancer()
    balle.reculer()
    balle.sauter()
    balle.plonger()

    # 2. Physique puis collisions
    balle.mettre_a_jour(dt)
    balle.collisions(murs)

    # 3. Affichage
    screen.fill("skyblue")
    for mur in murs:
        mur.dessiner(screen)
    balle.dessiner(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()