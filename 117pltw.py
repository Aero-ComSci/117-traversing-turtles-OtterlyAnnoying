#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#adjusts the previous for loop to make it able to iterate through the turtle_colors list as well
for s in range(len(turtle_shapes)):
  t = trtl.Turtle(shape=turtle_shapes[s])
  t.penup()
  my_turtles.append(t)
  t.color(turtle_colors[s])

#sets the start of the program at the center of the screen (0,0)  
startx = 0
starty = 0
startDir = 0
#creates a for loop that for each of the turtles in the list, goes to the set coordinates in lines 17-18, then moves 50 units after turning right 45 degrees
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.left(startDir)     
  t.forward(50)
  startDir += 45

#changes the start coordinates such that the next iteration starts at different coordinates	
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()