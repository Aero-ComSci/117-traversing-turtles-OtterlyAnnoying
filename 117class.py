import turtle as trtl

class TurtleTarget:

    def __init__(self):

        self.turtles = [] #creates a empty list that will be filled with turtles
        self.colors = ["red", "blue", "green", "orange", "purple", "gold"] #creates a list of colors for each turtle
        
        self.shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"] #creates a list of shapes for each turtle

        
        #making new turtles, one for every color and shape
        for i in range(len(self.colors)):
            t = trtl.Turtle(shape=self.shapes[i])
            t.color(self.colors[i])
            t.penup()
            self.turtles.append(t)

    def __str__(self): #uses step6 of the PLTW instructions
        new_list = ["dog", "cat", "mouse", "bird", "monkey"]
        string = ''
        for animal in new_list: 
            string += " "+animal
        print(str(new_list))
    
    def draw_turtles(self):
        #sets up starting coordinates and direction
        startx = 0
        starty = 0
        startDir = 0

        for t in self.turtles:
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


x = TurtleTarget()
x.draw_turtles()
print(str(str(x)))