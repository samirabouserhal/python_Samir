import pgzrun


WIDTH= 700
HEIGHT= 500

speed=2

l_target = Actor("l_target.png")
l_target.pos=(WIDTH/2, HEIGHT/2)

m_target = Actor("m_target.png")
m_target.pos=(50,50)

s_target = Actor("s_target.png")
s_target.pos=(100,100)


def draw():
  screen.fill("white")
  l_target.draw()
  m_target.draw()
  s_target.draw()

def update():
  global speed
  l_target.y= l_target.y + speed
  if l_target.y < 0 or l_target.y > WIDTH:
    speed=-speed
pgzrun.go()