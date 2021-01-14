# Ceci est le lieu de travail de Samir Abou Serhal pour le travail de Base de Pgzero. Ce fichier fut créer le 14 janvier 2020 pour le cours ICS3UA-01/51.
# Pour me contacter, envoyer moi un couriel à abosam30@ecolecatholique.ca

import pgzrun

WIDTH= 700   # les dimensions des fenetres
HEIGHT= 500

vert=(50, 220, 100)   # couleur de fond 
rotation= 2 # vitesse de rotation
text= ("Guide le ballon vers le but.")   
# text afficher en haut

ballon= Actor("ballon.png")  # création d'actor
ballon.pos=(175, 450)   # ces coordonnés fonctionnent dans repl.it, mais j'ai aucune idée si ils vont travaillés dans Vs code

joueur= Actor("joueur.png")  # création d'actor
joueur.pos=(170, 620)  # même situation pour ces coordonnés

fillet= Actor("fillet.png", anchor=("right", "bottom"))
# création d'un autre actor
fillet.pos=(700, 550)  # les coordonné ne devrait pas fonctionné, mais ils fonctionnent ici


def draw(): # le fonction draw qui crée la scene
  screen.fill(vert)
  joueur.draw()
  fillet.draw()
  ballon.draw()
  screen.draw.text(text,(250,10), color="red")

def update():
  ballon.angle += rotation

def on_mouse_move(pos):  # la fonction qui permet le ballon de suivre la souris de l'utilisateur
    ballon.pos = pos
    
pgzrun.go()