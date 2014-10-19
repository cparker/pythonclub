import turtle

def makeASquare():
  for count in range(0,4):
    turtle.forward(100)
    turtle.right(90)

def makeABetterSquare(size):
  for count in range(0,4):
    turtle.forward(size)
    turtle.right(90)

def squareWithStartPos(size,startX,startY):
  turtle.penup()
  turtle.goto(startX,startY)
  turtle.pendown()
  for count in range(0,4):
    turtle.forward(size)
    turtle.right(90)

squareWithStartPos(50,-100,-100)
squareWithStartPos(50,100,-100)
squareWithStartPos(50,-100,100)
squareWithStartPos(50,100,100)

input("press enter to exit.")

