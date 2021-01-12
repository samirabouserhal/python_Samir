import pgzrun

WIDTH= 700
HEIGHT= 500

vert=(50, 220, 100)
speed = 2
height_gain= 1

ballon= Actor("ballon.png")
ballon.pos=(175, 450)

joueur= Actor("joueur.png")
joueur.pos=(170, 620)

def draw():
  screen.fill(vert)
  ballon.draw()
  joueur.draw()

def update():
  ballon.x = ballon.x + speed
  ballon.y = ballon.y - height_gain
    
pgzrun.go()