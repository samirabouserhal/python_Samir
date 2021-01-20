import pgzrun
import random

WIDTH= 700
HEIGHT= 500

l_target_speed_x=2
l_target_speed_y=1

m_target_speed_x=3
m_target_speed_y=2

s_target_speed_x=4
s_target_speed_y=3

l_target = Actor("l_target.png")
l_target.pos= (200,200)

m_target = Actor("m_target.png")
m_target.pos =(WIDTH/2,HEIGHT/2)

s_target= Actor("s_target.png")
s_target.pos= (100,100) 



def draw():
  screen.fill("orange")
  l_target.draw()
  m_target.draw()
  s_target.draw()
 


def update():
  global l_target_speed_x, l_target_speed_y, m_target_speed_x, m_target_speed_y, s_target_speed_x, s_target_speed_y

  l_target.x= l_target.x + l_target_speed_x
  if l_target.x < 0 or l_target.x > WIDTH:
    l_target_speed_x=-l_target_speed_x
  l_target.y= l_target.y + l_target_speed_y
  if l_target.y < 0 or l_target.y > HEIGHT:
    l_target_speed_y=-l_target_speed_y

  m_target.x = m_target.x + m_target_speed_x


pgzrun.go()