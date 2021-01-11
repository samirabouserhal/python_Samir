import pgzrun

WIDTH= 700
HEIGHT= 500

vert=(50, 220, 100)
speed = 1

ballon= Actor("ballon.png")
ballon.pos=(WIDTH / 2, 700)

joueur= Actor("joueur.png")
joueur.pos=(WIDTH / 2, 620)

def draw():
  screen.fill(vert)
  ballon.draw()
  joueur.draw()

def update():
  ballon.x = ballon.x + speed
    
pgzrun.go()