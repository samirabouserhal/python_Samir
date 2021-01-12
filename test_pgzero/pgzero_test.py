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
  global speed, height_gain

  if (ballon.x < 0 or ballon.x > WIDTH):
    speed= -speed
  
  if (ballon.y < 0 or ballon.y > HEIGHT):
    height_gain= -height_gain

  ballon.x += speed
  ballon.y += height_gain
    
pgzrun.go()