  # ici nous allons créer la classe
#définir tous ces attributs 
#et créer toutes les méthodes (tout ce que la balle devra être capable de faire)

#on suivra le meme process pour tous les elements du jeu cad un fichier .py avec le nom dans lequel on créra une classe les attributs et les méthodes

# La balle doit pouvoir sauter,
#  aller à gauche ou à droite, 
# flotter dans une certaine zone "avec de l'eau" (et coller au plafond dans un zone sans graviter on verra après)
# Changer de forme un petit peu plus grosse (moins lourde qui flottera sur l'eau) ou plus petite plus lourde (qui coulera au fond de l'eau)
# Revenir à un check point si elle touche un danger
# Avoir une jauge de vie (3 vie en général) qui va diminuer ou augmenter selon si elle touche un danger ou un power up

import pygame


class Balle:
    """La balle du joueur : elle sait agir, la boucle de jeu décide quand."""

    def __init__(self, x, y, rayon=40, couleur=(200,30,150)):
        self.position = pygame.Vector2(x, y)
        self.vitesse = pygame.Vector2(0, 0)      # pixels par seconde (x et y)
        self.rayon = rayon
        self.couleur = couleur
        self.est_au_sol = False

        # Réglages (Valeurs pour les tests)
        self.vitesse_marche = 300
        self.force_saut = 500
        self.vitesse_plongeon = 700
        self.gravite = 1000

    # Déplacements de la balle

    def arreter_horizontal(self):

    # Faire en sorte que la balle s'arrete au moment où la touche n'est plus pressée
        self.vitesse.x = 0

    def avancer(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.vitesse.x += self.vitesse_marche 

    def reculer(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.vitesse.x -= self.vitesse_marche
        # Si droite ET gauche sont pressées, les deux s'annulent (+300 - 300)

    def sauter(self):
        touches = pygame.key.get_pressed()
        if (touches[pygame.K_SPACE] or touches[pygame.K_UP]) and self.est_au_sol:
            self.vitesse.y = -self.force_saut
            self.est_au_sol = False

    def plonger(self):
        """Descendre plus vite en l'air (flèche bas)."""
        if pygame.key.get_pressed()[pygame.K_DOWN] and not self.est_au_sol:
            self.vitesse.y = max(self.vitesse.y, self.vitesse_plongeon)

    # ---------- Physique ----------

    def mettre_a_jour(self, dt):
        """Gravité, puis déplacement (une seule fois par image)."""
        self.vitesse.y += self.gravite * dt
        self.position += self.vitesse * dt

    
    def collisions(self, murs):
        """Interroge chaque mur et obéit à sa réponse."""
        self.est_au_sol = False
        for mur in murs:
            resultat = mur.isthisCollision(self)

# Le décalage c'est la distance de laquelle la balle s'enfonce dans le mur avant d'être ramené à la surface

            if resultat is None:
                continue
            direction_opposee, decalage, rebond = resultat 

            # 1. Se replacer au bord du mur
            self.position += direction_opposee * decalage

            # 2. Annuler (ou inverser, si rebond) la vitesse qui rentre dans le mur
            vitesse_vers_mur = self.vitesse.dot(direction_opposee)
            if vitesse_vers_mur < 0:
                self.vitesse -= (1 + rebond) * vitesse_vers_mur * direction_opposee

            # 3. Si la surface regarde vers le haut, on est posé dessus
            if direction_opposee.y < -0.5:
                self.est_au_sol = True

    # ---------- Affichage ----------

    def dessiner(self, ecran):
        pygame.draw.circle(ecran, self.couleur, self.position, self.rayon)