#   leaderboard.py
# The leaderboard module to be used in a122 solution.

# set the levels of scoring

# load leaderboard from file
def score_evaluation(file_name,player_score,turtle_object):
  player_score = str(player_score)
  font_setup = ("Arial", 15, "normal")
  highscore_file = open(file_name, "r")  # need to create the file ahead of time in same folder
  # use a for loop to iterate through the content of the file, one line at a time
  for line in highscore_file:
    high_score = line
  if int(player_score) > int(high_score):
    turtle_object.clear()
    turtle_object.write("Congratulations! You beat the high score!", font=font_setup)
    turtle_object.penup()
    turtle_object.sety(0)
    turtle_object.pendown()
    turtle_object.write("New high score is: "+player_score, font=font_setup)
    highscore_file = open(file_name, "w")
    highscore_file.write(player_score)
  else:
    turtle_object.clear()
    turtle_object.write("Sorry, you didn't beat the high score. Maybe next time!", font=font_setup)
    turtle_object.penup()
    turtle_object.sety(0)
    turtle_object.pendown()
    turtle_object.write("Your score was: "+player_score+". you need "+(high_score-player_score+1)+" to beat the high score of "+high_score, font=font_setup)
  highscore_file.close()
 
# update leaderboard by evaluating if player score is greater than high score
'''
def update_leaderboard(file_name,playr_score):
  global high_score,player_score
  player_score = player_score.append(playr_score)
  # store the latest highscore
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  if player_score > high_score:
    leaderboard_file.write(player_score)
  else:
    leaderboard_file.write(high_score)
  leaderboard_file.close()
 
 
# draw leaderboard and display a message to player
def draw_leaderboard(turtle_object):
  global high_score,player_score
  high_score = int(high_score)
  player_score = int(player_score)
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  # Display message about player beating/not beating the high score
  if (player_score > high_score):
    turtle_object.write("Congratulations! You beat the high score!", font=font_setup)
  else:
    turtle_object.write("Sorry, you didn't beat the high score. Maybe next time!", font=font_setup)
 
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.sety(0)
  turtle_object.pendown()
 
  if (player_score > high_score):
    turtle_object.write("New high score is: "+high_score, font=font_setup)
  else:
    turtle_object.write("Your score was: "+player_score+". you need "+(high_score-player_score+1)+" to beat the high score of "+high_score, font=font_setup)
'''