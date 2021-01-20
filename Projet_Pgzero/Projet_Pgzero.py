import pgzrun
import random

WIDTH= 700
HEIGHT= 500

score= 0

l_target_speed_x=2
l_target_speed_y=1

m_target_speed_x=3
m_target_speed_y=2

s_target_speed_x=5
s_target_speed_y=4

l_target = Actor("l_target.png",anchor=("center", "top"))
#l_target.pos= (200,200)

m_target = Actor("m_target.png")
#m_target.pos =(WIDTH/2,HEIGHT/2)

s_target= Actor("s_target.png")
#s_target.pos= (100,100) 



def draw():
  screen.fill("orange")
  screen.draw.text("Score : ", +str(score), (10,10), fontsize= 30)
  l_target.draw()
  m_target.draw()
  s_target.draw()
 


def update():
  global l_target_speed_x, l_target_speed_y, m_target_speed_x, m_target_speed_y, s_target_speed_x, s_target_speed_y

  l_target.x= l_target.x + l_target_speed_x
  if l_target.x < 0 or l_target.x > WIDTH:
    l_target_speed_x=-l_target_speed_x
  l_target.y= l_target.y + l_target_speed_y
  if l_target.y < 200 or l_target.y > HEIGHT:
    l_target_speed_y=-l_target_speed_y

  m_target.x = m_target.x + m_target_speed_x
  if m_target.x < 0 or m_target.x > WIDTH:
    m_target_speed_x= -m_target_speed_x
  m_target.y = m_target.y + m_target_speed_y
  if m_target.y < 200 or m_target.y > HEIGHT:
    m_target_speed_y= -m_target_speed_y

  s_target.x = s_target.x + s_target_speed_x
  if s_target.x < 0 or s_target.x > WIDTH:
    s_target_speed_x= -s_target_speed_x
  s_target.y = s_target.y + s_target_speed_y
  if s_target.y < 200 or s_target.y > HEIGHT:
    s_target_speed_y= -s_target_speed_y

pgzrun.go()