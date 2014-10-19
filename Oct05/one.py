import turtle


def drawCircleAt(turtleX, turtleY, circleSize):
    turtle.penup()
    turtle.goto(turtleX,turtleY)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(circleSize)
    turtle.end_fill()


def drawSquare():
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)


drawSquare()
drawCircleAt(100,100,50)


turtle.exitonclick()