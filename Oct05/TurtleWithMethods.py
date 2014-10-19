import turtle


def drawCircleAt(size, x, y):
    turtle.color('red')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(size)


def drawSquareAt(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)


def drawTriangleAt(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)


drawTriangleAt(-100,-100)
drawTriangleAt(-100,-200)

drawSquareAt(50, 100)
drawSquareAt(100, 50)
drawSquareAt(50, 50)

drawCircleAt(20, 100, 100)
drawCircleAt(20, 100, 200)
drawCircleAt(20, 200, 200)

turtle.exitonclick()
