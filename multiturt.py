import turtle
import random

class Globals():
    turtles = []

class SmartTurtle():
    turtle
    size = 0

startT = turtle.Turtle()
s = startT.getscreen()
s.colormode(255)

def moveTurtles():
    s.ontimer(moveTurtles,700)
    for turt in Globals.turtles:
        turt.turtle.forward(turt.size)
        turt.turtle.right(91)



def handleClick(xPos,yPos):
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.speed(0)
    turt.pu()
    turt.goto(xPos,yPos)
    turt.pd()
    randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    turt.pencolor(randColor)
    t = SmartTurtle()
    t.turtle = turt
    randSpiralSize = random.randint(30,200)
    t.size = randSpiralSize
    Globals.turtles.append(t)
    
s.onclick(handleClick)

turtle.ontimer(moveTurtles)
s.mainloop()    

