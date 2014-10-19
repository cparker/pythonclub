import turtle
import random
import math

class Globals():
  counter = 0


myT = turtle.Turtle()
myT.speed(8)
myT.color('black','red')
s = myT.getscreen()
s.colormode(255)

def goToPointer(mouseX,mouseY):
  Globals.counter += 1

  if (Globals.counter % 10 == 0):
    print(str(int(mouseX)) + "," + str(int(mouseY)))
    myT.goto(mouseX,mouseY)

def jumpTo(clickedX, clickedY):
  print("pu")
  myT.pu()
  myT.setx(clickedX)
  myT.sety(clickedY)
  print(str(int(clickedX)) + "," + str(int(clickedY)))
  myT.pd()
  print("pd")




myT.ondrag(goToPointer)
s.onclick(jumpTo)

s.mainloop()