import pgzrun

WIDTH= 700 # Largeur de la fenêtre
HEIGHT= 500 # Hauteur de la fenêtre

score= 0 # Score initial

lives= 3 # nombre de vie

time_played= 0 # Temps initial

game=True  # Booléan pour commencer le jeu

l_target_speed_x=-2 # Vitesse sur l'axe des x pour la grande cible
l_target_speed_y=1 # Vitesse sur l'axe des y pour la grande cible

m_target_speed_x=3 # Vitesse sur l'axe des x pour la cible moyenne
m_target_speed_y=-2 # Vitesse sur l'axe des y pour la cible moyenne

s_target_speed_x=-3 # Vitesse sur l'axe des x pour la petite cible
s_target_speed_y=2 # Vitesse sur l'axe des y pour la petite cible

l_target = Actor("l_target.png") # Actor pour la grande cible
l_target.pos=(WIDTH/2, HEIGHT/2) # Position de départ pour la grande cible

m_target = Actor("m_target.png")  # Actor pour la cible moyenne
m_target.pos=(WIDTH/2, HEIGHT/2)  # Position de départ pour la cible moyenne

s_target= Actor("s_target.png")  # Actor pour la petite cible
s_target.pos=(WIDTH/2, HEIGHT/2) # Position de départ pour la petite cible 

# Ce qui serait montrer lorsque le jeu est en train de jouer:

def game():
  screen.fill("white") # Couleur de l'arrière plan
  screen.draw.text("Score: " +str(score), (10,10), color= "black") # Le score en direct
  screen.draw.text("Vie: " +str(lives), (10,30), color="black") # Affiche le montant de score que le joueur a
  screen.draw.text("Temps: " +str(time_played), (600, 10), color="black") # Affiche le temps en direct
  l_target.draw() # Dessine la grande cible
  m_target.draw() # Dessine la cible moyenne
  s_target.draw() # Dessine la petite cible
 

# Ce qui serait montrer lorsque le jeu est terminé et que le joueur n'a plus de vie:

def game_over():
  screen.fill("black") # Couleur de l'arrière plan
  screen.draw.text("Game over", (300,150))  # Dessine game over sur l'écran
  screen.draw.text("Score: "+ str(score), (300,200)) # Affiche le score final
  screen.draw.text("Temps: " +str(time_played), (300,250)) # Affiche le temps que le joueur a survie

# La logique qui permet un écran de jeu et un écran de gamme over:

def draw():
  if lives:
    game()
  else:
    game_over()

# Le code qui gère les interactions du joueur avec le programme:

def on_mouse_down(pos):
  global score, lives
  if l_target.collidepoint(pos):
      if lives >=1:
        score += 1  # Si le joueur frappe la grande cible, ils sont données 1 point

  elif m_target.collidepoint(pos):
    if lives>=1:
      score += 2 # Si le joueur frappe la cible moyenne, ils sont données 2 point

  elif s_target.collidepoint(pos):
    if lives >=1:
      score += 3  # Si le joueur frappe la petite cible, ils sont donnée 3 points
      
  else: 
    if lives>=1:
      lives -=1  # Si le joueur manque les cibles, ils pertent une vie


# La logique qui controllent le mouvement des cibles ainsi que la perte des vie:

# Tous les cibles sont contenus entre 0 et le WIDTH ainsi qu'entre 100 et le HEIGHT

# Si les cibles touchent les bordures que j'ai désigné, ils seront renvoyer dans le sens opposés

def update():
  global l_target_speed_x, l_target_speed_y, m_target_speed_x, m_target_speed_y, s_target_speed_x, s_target_speed_y, lives

  l_target.x= l_target.x + l_target_speed_x
  if l_target.x < 0 or l_target.x > WIDTH:
    l_target_speed_x=-l_target_speed_x
  
  l_target.y= l_target.y + l_target_speed_y
  if l_target.y < 100 or l_target.y > HEIGHT:
    l_target_speed_y=-l_target_speed_y


  m_target.x = m_target.x + m_target_speed_x
  if m_target.x < 0 or m_target.x > WIDTH:
    m_target_speed_x= -m_target_speed_x
  
  m_target.y = m_target.y + m_target_speed_y
  if m_target.y < 100 or m_target.y > HEIGHT:
    m_target_speed_y= -m_target_speed_y


  s_target.x = s_target.x + s_target_speed_x
  if s_target.x < 0 or s_target.x > WIDTH:
    s_target_speed_x= -s_target_speed_x
 
  s_target.y = s_target.y + s_target_speed_y
  if s_target.y < 100 or s_target.y > HEIGHT:
    s_target_speed_y= -s_target_speed_y
    
  if lives == 0: # La logique qui vérifie le montant de vie que le joueur a et qui décide si le jeu continue
    game=False


def update_timer():  # La logique qui permet un timer
  global time_played, game
  if lives>=1: # Cela assure que le temps arrête lorsque le joueur a plus de vie
    time_played += 1


# Cette ligne assure que le timer compte 1 secondes à la fois:

clock.schedule_interval(update_timer, 1.0)

pgzrun.go()

# Améliorement:
#   Avec le temps j'aimerais soit ajouté plusieur niveau limité par le temps ou ajouté un facteur de placement random pour varié le positionnement des cibles infinis