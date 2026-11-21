Balle (jeu/balle.py) :
- attributs : position, vitesse, rayon, couleur, est_au_sol
- actions : avancer, reculer, sauter, plonger
- mettre_a_jour(dt) applique la gravité et le déplacement
- resoudre_collisions(murs) interroge chaque mur et réagit à sa réponse

Murs (jeu/murs.py) :
- la méthode tester(balle) vérifie le contact et renvoie None
  ou (normale, profondeur, rebond)
- la balle n'a pas à connaître la forme ni le nombre de murs :
  chaque mur gère sa propre collision

main.py : adaptation de la boucle de jeu à ces nouvelles classes."