import turtle
import sys

myT = turtle.Turtle()

turtFile = open(sys.argv[1])

for line in turtFile:
    if line[0] == "#":
        continue
    elif "pu" in line:
        myT.pu()

    elif "pd" in line:
        myT.pd()

    else:
        points = line.split(",")
        xPoint = int(points[0])
        yPoint = int(points[1])
        myT.goto(xPoint,yPoint)


input("Any key to exit.")

