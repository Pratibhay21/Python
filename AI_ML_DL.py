import turtle   #makes all turtle functionalities available to us
t=turtle.Turtle() #creates/returns a new turtle object

t.fillcolor("light green")  #fill color specified
t.penup() #to avoid the lines drawn during drawing(i.e pick pen up)
t.begin_fill()   #start filling color
t.circle(100)  #circle method with radius
t.end_fill()    #close ploygon and end filling color
t.goto(2,150)   #go to the position
t.color("maroon")   #change the turtle color to red
t.write("AI",font=("Arial",17,"bold"))  #to write a text in turtle screen


t.goto(10,20) #coordinates can be chosen timely when needed
t.fillcolor("pink")
t.penup()
t.begin_fill()
t.circle(60)
t.end_fill()
t.goto(2,90)
t.color("green")
t.write("ML",font=("Arial",15,"bold"))



t.goto(10,20)
t.fillcolor("yellow")
t.penup()
t.begin_fill()
t.circle(30)
t.end_fill()
t.goto(2,25)
t.color("maroon")
t.write("DL",font=("Arial",15,"bold"))

t.goto(110,100)  
t.color("red") 
t.write("AI-ML-DL Relationship",font=("Arial",15,"bold"))
t.hideturtle()    #to hide the arrowhead

