import pgzrun

WIDTH= 700
HEIGHT= 500

score= 0

lives= 3

time_played= 0

game=True

l_target_speed_x=-2
l_target_speed_y=1

m_target_speed_x=3
m_target_speed_y=-2

s_target_speed_x=-3
s_target_speed_y=2

l_target = Actor("l_target.png")
l_target.pos=(WIDTH/2, HEIGHT/2)

m_target = Actor("m_target.png")
m_target.pos=(WIDTH/2, HEIGHT/2)

s_target= Actor("s_target.png")
s_target.pos=(WIDTH/2, HEIGHT/2) 



def game():
  screen.fill("white")
  screen.draw.text("Score: " +str(score), (10,10), color= "black")
  screen.draw.text("Vie: " +str(lives), (10,30), color="black")
  screen.draw.text("Temps: " +str(time_played), (600, 10), color="black")
  l_target.draw()
  m_target.draw()
  s_target.draw()
 

def game_over():
  screen.fill("black")
  screen.draw.text("Game over", (300,150))
  screen.draw.text("Score: "+ str(score), (300,200))
  screen.draw.text("Temps: " +str(time_played), (300,250))


def draw():
  if lives:
    game()
  else:
    game_over()


def on_mouse_down(pos):
  global score, lives
  if l_target.collidepoint(pos):
      if lives >=1:
        score += 1

  elif m_target.collidepoint(pos):
    if lives>=1:
      score += 2

  elif s_target.collidepoint(pos):
    if lives >=1:
      score += 3  
      
  else: 
    if lives>=1:
      lives -=1


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
    
  if lives == 0:
    game=False


def update_timer():
  global time_played, game
  if lives>=1:
    time_played += 1

clock.schedule_interval(update_timer, 1.0)

pgzrun.go()