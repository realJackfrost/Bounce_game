import pygame
from balle import Balle
from murs import Mur
from danger import obstacle_sommet
from Interface import Interface

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
largeur, hauteur = 1000,700
interface = Interface(largeur,hauteur)
etat = "Menu principal"



murs = [
    Mur(0, 0, 1000, 70),      # plafond
    Mur(0, 0, 50, 700),       # mur de gauche
    Mur(1000,0,10,700),       # mur à droite (un peu) invisible
    Mur(0, 350, 500, 70),    # milieu
    Mur(0, 650, 1000, 70,0.5),    # sol bis
    
]


balle = Balle(100,100)



obstacles = [
    obstacle_sommet([(50, 650), (75, 600), (100, 650)]),     # triangle 1
    obstacle_sommet([(100, 650), (125, 600), (150, 650)]),   # triangle 2
    obstacle_sommet([(150, 650), (175, 600), (200, 650)]),   # triangle 3
]

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if etat == "Menu principal":
            if(interface.bouton_clique(event)) :
                etat = "jeu Bounce"

    if etat == "Menu principal" :
        interface.dessiner(screen)

    elif etat == "jeu Bounce":


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

        #Vérifier les collisisons avec les pics

        for obstacle in obstacles:
            obstacle.dessiner(screen)
            if obstacle.verifier_collision(balle):
                balle.perdre_hp(obstacle)
        
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()