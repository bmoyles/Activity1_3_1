#import commands
import turtle as trtl
import random as rand
import leaderboard as lb
#variables-------------------
fruits = ["apple.gif","banana.gif","cherry.gif","orange.gif","pear.gif"]
turtles = []
score = 0
#turtle configuration------------
wn = trtl.Screen()
wn.setup(width=600,height=350)
wn.bgpic("fruit_ninja.gif")
for x in fruits:
  wn.addshape(x)
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.goto(-180,170)
counter = trtl.Turtle()
counter.hideturtle()
counter.color("white")
font_setup = ("Arial", 15, "normal")
timer = 3
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#Timer------------------------------
counter.penup()
counter.goto(175, 150)
counter.pendown()
#functions---------------------------
def move_turtle(turtle,xx,yy):
  turtle.penup()
  turtle.goto(xx,yy)
  turtle.pendown()
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
wn.ontimer(countdown, counter_interval)


wn = trtl.Screen()
wn.mainloop()







 



