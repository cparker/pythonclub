import turtle
import random
import math

class Globals():
  lineCounter = 1

def sun():
  myT = turtle.Turtle()
  myT.speed(10)
  myT.color('red', 'yellow')
  myT.begin_fill()
  s = myT.getscreen()
  s.colormode(255)

  while True:
    myT.forward(200)
    myT.left(170)

    if abs(myT.pos()) < 1:
      break

  myT.end_fill()
  turtle.done()

def follow():
  myT = turtle.Turtle()
  myT.speed(8)
  myT.color('black','red')
  s = myT.getscreen()
  s.colormode(255)

  myT.begin_fill()
  def goToPointer(mouseX,mouseY):

    if Globals.lineCounter % 5 == 0:
      print("trying to fill")
      myT.end_fill()
      myT.begin_fill()
      randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
      myT.fillcolor(randColor)

    xPos = myT.xcor()
    yPos = myT.ycor()
    deltaX = mouseX - xPos
    deltaY = mouseY - yPos
    angleInDegrees = math.degrees(math.atan2(deltaY,deltaX))
    print(Globals.lineCounter)
    myT.setheading(angleInDegrees)
    dist = math.sqrt(deltaX**2 + deltaY**2)
    myT.forward(dist)
    Globals.lineCounter += 1

  s.onclick(goToPointer)
  s.mainloop()



def colorTornado():
  myTurtle = turtle.Turtle()
  myTurtle.speed(0)

  colors = ["red","blue","green"]
  penSizes = [1,2,3,4,5]

  for count in range(1,25):
    myTurtle.pencolor(colors[count % 3])
    myTurtle.pensize( penSizes[count % 5] )
    myTurtle.circle(count * 5)



def wander():
  myT = turtle.Turtle()
  myT.speed(0)
  s = myT.getscreen()
  s.colormode(255)
  s.bgcolor( (200,200,200) )

  randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

  myT.penup()
  for count in range(1,150):
    randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    myT.color(randColor)
    yMax = int(s.window_height()/2)
    yMin = int(-yMax)
    xMax = int(s.window_width()/2)
    xMin = int(-xMax)
    myT.setx(random.randint(xMin,xMax))
    myT.sety(random.randint(yMin,yMax))
    myT.begin_fill()
    myT.circle(10)
    myT.end_fill()

colorTornado()
wander()
sun()
follow()
