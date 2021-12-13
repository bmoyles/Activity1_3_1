#Imports/Classes
import turtle as trtl
import random as rand
import highscore as hs

class Er(Exception):
  pass

#Variables - - - - - - - - - - - - - - - - - - -

while True:
  try:
    difficulty = int(input("Choose between difficulty 1(easy), 2(normal), or 3(hard): "))

    if difficulty == 1:
      fruit_dis = 10
      fruit_speed = 2

    elif difficulty == 2:
      fruit_dis = 10
      fruit_speed = 7

    elif difficulty == 3:
      fruit_dis = 15
      fruit_speed = 10

    else:
      raise Er(Exception)
    break

  except Er:
    print("please only choose between said aforementioned difficulties")
  
  except ValueError:
    print("please only choose between said aforementioned difficulties")

fruitz = ["apple.gif","cherry.gif","orange.gif","pear.gif","banana.gif"]

score = 0

font_setup = ("Arial", 15, "normal")

timer = 30

counter_interval = 1000   #1000 represents 1 second

score_file = "LB.txt"

timer_up = False

game_start = False

#Turtle Configuration - - - - - - - - - -

active_fruit = trtl.Turtle()
active_fruit.hideturtle()
active_fruit.penup()

wn = trtl.Screen()
wn.setup(width=1500,height=800)
wn.bgpic("fruit_ninja.gif")
wn.addshape("game_start.gif")
for x in fruitz:
  wn.addshape(x)

start_game = trtl.Turtle()
start_game.pu()
start_game.speed(8)
start_game.hideturtle()
start_game.shape("game_start.gif")

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-700,350)
score_writer.pd()
score_writer.color("white")

counter = trtl.Turtle()
counter.hideturtle()
counter.color("white")
counter.penup()
counter.goto(600,350)
counter.pendown()

#Functions - - - - - - - - - - - - - -
def manage_highscore():
  global score
  hs.score_evaluation(score_file,score,score_writer)


def random_location():
  try:
    randomx = rand.randint(-500,500)
    active_fruit.hideturtle()
    active_fruit.speed(fruit_speed)
    active_fruit.goto(randomx, 400)
    random_fruit = rand.randint(0,4)
    active_fruit.shape(fruitz[random_fruit])
  except trtl.Terminator:
      print("yo shit broke")
      pass


def fruit_drop():
  global timer_up
  ycor = int(active_fruit.ycor())
  active_fruit.showturtle()
  active_fruit.speed(fruit_speed)
  while ycor > -400:
    if timer_up == True:
      active_fruit.hideturtle()
      break

    ycor = int(active_fruit.ycor()) - fruit_dis
    active_fruit.sety(ycor)

    if ycor <= -400:
      update_score(False)
      random_location()
      wn.update()
      fruit_drop()



def update_score(scored_point):
  global score
  if scored_point == True:
    score += 1
  else:
    score -= 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)


def fruits_clicked(x,y):
  active_fruit.hideturtle()
  update_score(True)
  random_location()
  fruit_drop()


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_highscore()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown,counter_interval)


def start_click(x,y):
  global game_start
  start_game.hideturtle()
  start_game.goto(0,-1000)
  random_location()
  countdown()
  score_writer.write(score, font=font_setup)
  game_start = True
  active_fruit.onclick(fruits_clicked)
  fruit_drop()


def gamestart_anim():
  start_game.showturtle()

  while game_start == False:
    start_game.circle(20)

#Events -------------------

start_game.onclick(start_click)

gamestart_anim()

wn.mainloop()