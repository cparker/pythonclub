import turtle

pointsFile = open('turtle-points.txt')

for point in pointsFile:
  # a point is like x,y
  points = point.split(",")
  xPoint = points[0]
  yPoint = points[1]
  turtle.goto(int(xPoint),int(yPoint))

input('press enter ')
  
