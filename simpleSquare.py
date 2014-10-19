import turtle


def makeSquare(size=200):
  for count in range(0,4):
    turtle.forward(size)
    turtle.right(90)

makeSquare()
makeSquare(10)
makeSquare(10)

input("press enter")
