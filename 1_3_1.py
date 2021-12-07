#import commands
import turtle as trtl
import random as rand
class Er(Exception):
  pass
#variables-------------------
active_fruit = trtl.Turtle()
active_fruit.hideturtle()
active_fruit.penup()
while True:
  try:
    difficulty = int(input("Choose between difficulty 1, 2, or 3: ")
    if difficulty == 1:
      difficulty = 1
      active_fruit.speed(1)
    elif difficulty == 2:
      difficulty = 2
      active_fruit.speed(5)
    elif difficulty == 3:
      difficulty = 3
      active_fruit.speed(0)
    else:
      raise Er(Exception)
    break
  except Er:
    print("please only choose between said aforementioned difficulties")
fruitz = ["apple.gif","banana.gif","cherry.gif","orange.gif","pear.gif"]
score = 0
#turtle configuration------------
wn = trtl.Screen()
wn.setup(width=600,height=350)
wn.bgpic("fruit_ninja.gif")
for x in fruitz:
  wn.addshape(x)
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-180,170)
counter = trtl.Turtle()
counter.hideturtle()
counter.color("white")
font_setup = ("Arial", 12, "normal")
timer = 3
counter_interval = 1000   #1000 represents 1 second
timer_up = False
# Game start
'''
game_start = False
start = trtl.Turtle()
start.shape("triangle")
start.shapesize(5, 10, 0)
start.color("white")
def start_game(x, y):
  global game_start
  game_start = True
  start.hideturtle()
start.onclick(start_game)
while not(game_start):
  fruits.hideturtle()
  fruits.showturtle()
'''
#Timer------------------------------
counter.penup()
counter.goto(210, 135)
counter.pendown()
#functions--------------------------
def draw_fruit():
  random_fruit = rand.randint(0,4)
  active_fruit.shape(fruitz[random_fruit])
  active_fruit.showturtle()
  fruit_drop()
def random_location():
  randomx = rand.randint(-150,150)
  active_fruit.hideturtle()
  active_fruit.goto(randomx, 400)
  draw_fruit()
 def fruit_drop():
  ycor = active_fruit.ycor()
  speed = 2
  while ycor > -200:
    active_fruit.sety(ycor-speed*difficulty)
    speed*2 = speed
  random_location()
'''
def start_game():
'''
def update_score():
  global score 
  score += 1
  print(score)
  score_writer.clear()
  score_writer.write(score, font=font_setup) 
def fruits_clicked():
  if timer_up == False:
    update_score()
    random_location()
  else:
    active_fruit.hideturtle()
    active_fruit.clear()
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#Events----------------------------
active_fruit.onclick(fruits_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()







 



