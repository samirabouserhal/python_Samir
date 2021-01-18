import pgzrun


WIDTH= 700
HEIGHT= 500


l_target = Actor("target.jpg")
l_target.pos=(10,10)

m_target = Actor("half-sized_target.jpg")
m_target.pos=(50,50)

def draw():
  screen.fill("white")
  l_target.draw()
  m_target.draw()


pgzrun.go()