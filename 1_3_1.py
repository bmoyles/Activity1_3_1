#import commands
import turtle as trtl
import random as rand
#classes an exception so i can retrieve only the input i ask for (shown below)
class Er(Exception):
  pass
#variables-------------------
#the while true statement loops user input until specified input is met
while True:
  try:
    difficulty = int(input("Choose between difficulty 1, 2, or 3: "))
    if difficulty == 1:
      fruit_dis = 10
      fruit_speed = 1
    elif difficulty == 2:
      fruit_dis = 25
      fruit_speed = 5
    elif difficulty == 3:
      fruit_dis = 40
      fruit_speed = 0
    #heres where we used the classed exception
    else:
      raise Er(Exception)
    break
  #heres where we used the classed exception
  except Er:
    print("please only choose between said aforementioned difficulties")
  except ValueError:
    print("please only choose between said aforementioned difficulties")
#created a list to store all fruit images 
fruitz = ["apple.gif","cherry.gif","orange.gif","pear.gif","banana.gif"]
#variable that represents starting score
score = 0
font_setup = ("Arial", 15, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
game_start = False
#turtle configuration---------------------------
#creating and placing turtles on plain 
active_fruit = trtl.Turtle()
active_fruit.hideturtle()
active_fruit.penup()
wn = trtl.Screen()
wn.setup(width=1500,height=800)
wn.bgpic("fruit_ninja.gif")
wn.addshape("game_start.gif")
#i used a for loop here so i didn't have to type wn.addshape(shape) a bunch of times
for x in fruitz:
  wn.addshape(x)
start_game = trtl.Turtle()
start_game.pu()
start_game.speed(10)
start_game.hideturtle()
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
#functions--------------------------
#selects a random fruit shape from the list using the random import, and makes the main turtle that shape
def draw_fruit():
    random_fruit = rand.randint(0,4)
    active_fruit.shape(fruitz[random_fruit])
#moves main turtle to a random location on the x axis at the top of the screen to be dropped
def random_location():
  randomx = rand.randint(-500,500)
  active_fruit.hideturtle()
  active_fruit.speed(fruit_speed)
  active_fruit.goto(randomx, 400)
#function that drops the fruit
def fruit_drop():
  global timer_up
  ycor = active_fruit.ycor()
  #and if statement to only continue the movement IF the timer is not out
  if timer_up == False:
    active_fruit.showturtle()
    #while loop that moves the main turtle down on its Y axis until specified placement is met
    while ycor > -400:
      #evaluates if the timer is still not up
      if timer_up == True:
        active_fruit.hideturtle()
        break
      active_fruit.speed(fruit_speed)
      ycor = active_fruit.ycor()
      active_fruit.sety(ycor-fruit_dis)
    #IF the fruit is not clicked by the time the turtle reaches specified placement, you will lose one point, and the turtle will reset
    if ycor <= -400:
      global score
      score -= 1
      score_writer.clear()
      score_writer.write(score, font=font_setup)
      random_location()
      draw_fruit()
      fruit_drop()
#retrieves global score and updates score on screen to match
def update_score():
  global score 
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup) 
#the function that dictates what happens when the fruit is clicked
def fruits_clicked(x,y):
  global timer_up
  #evaluates if time is up or not
  if timer_up == False:
    active_fruit.hideturtle()
    update_score()
    random_location()
    draw_fruit()
    fruit_drop()
  else:
    active_fruit.hideturtle()
#retrieves the time, and adjusts it according to how long you have been playing
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
#dictates what will happen when user clicks the start button
def start_click(x,y):
  global game_start
  game_start = True
  start_game.hideturtle()
  start_game.goto(0,-1000)
#the animation for the start button. This loops until the start button is clicked, and then will break, continuing into the actual game
def gamestart_anim():
  global game_start
  while game_start == False:
    start_game.circle(20)
#Events----------------------------
start_game.shape("game_start.gif")
start_game.showturtle()
#will run start_click() function when the start game turtle is clicked
start_game.onclick(start_click)
gamestart_anim()
#begins timer countdown
wn.ontimer(countdown, counter_interval)
#begins fruit dropping and clicking 
random_location()
draw_fruit()
active_fruit.onclick(fruits_clicked)
fruit_drop()
#write down initial starting score of 0
score_writer.write(score, font=font_setup)
#loops so the program does not close upon event completion 
wn.mainloop()