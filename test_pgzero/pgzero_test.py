import pgzrun

WIDTH= 700
HEIGHT= 500

vert=(50, 220, 100)

ballon= Actor("ballon.png")
ballon.pos=(WIDTH / 2, HEIGHT / 2)

joueur= Actor("joueur.png")
joueur.pos=(WIDTH / 2, HEIGHT / 2)

def draw():
  screen.fill(vert)
  ballon.draw()
  joueur.draw()
    
pgzrun.go()