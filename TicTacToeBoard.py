#!/use/bin/env python
"""
    This is a graphical display for a tic-tac-toe game using turtle

    My Notes:
        Need to draw 4 lines... center of board
        Need an API where you pass in a list of x, o and it displays

"""
__author__ = 'cparker'

import turtle, math


class TicTacToeBoard:
    oSymbolRadius = 75
    oSymbolPenSize = 25

    xSymbolSize = oSymbolRadius * 2
    xSymbolPenSize = oSymbolPenSize

    boardPenSize = 4
    boardPenColor = 'black'

    oColor = 'blue'
    xColor = 'green'

    winLineSize = 20
    winLineColor = 'red'

    textDisplayHeight = 50


    def __init__(self):
        print("initializing board")
        self.board = turtle.Turtle()
        screen = self.board.getscreen()
        self.w = turtle.window_width()
        self.h = turtle.window_height()  # room for display
        self.boardHeight = self.h - self.textDisplayHeight

        # make the symbol sizes relative to the board width
        self.oSymbolRadius = math.floor(0.09 * self.w)

        screen.setworldcoordinates(0, 0, turtle.window_width(), turtle.window_height())
        self.board.hideturtle()
        self.board.speed(0)
        self.board.pensize(3)
        self.board.pencolor("blue")
        turtle.speed(0)
        turtle.title("Tic Tac Toe")

        self.drawBoard()

    def drawBoard(self):
        thirdWidth = math.floor(self.w / 3)
        thirdHeight = math.floor(self.boardHeight / 3)


        def drawVert(x):
            self.board.penup()
            self.board.hideturtle()
            self.board.goto(x, self.textDisplayHeight)
            self.board.pendown()
            self.board.goto(x, self.h)

        def drawHoriz(y):
            self.board.penup()
            self.board.hideturtle()
            self.board.goto(0, y + self.textDisplayHeight)
            self.board.pendown()
            self.board.goto(self.w, y + self.textDisplayHeight)

        self.board.pensize(self.boardPenSize)
        self.board.pencolor(self.boardPenColor)
        drawVert(thirdWidth)
        drawVert(thirdWidth * 2)
        drawHoriz(thirdHeight)
        drawHoriz(thirdHeight * 2)


    def getCordFromBoardPos(self, pos):
        centerFormulas = {
            "0": lambda w, h: (math.floor(w / 6) * 1, math.floor(h / 6) * 5 + self.textDisplayHeight),
            "1": lambda w, h: (math.floor(w / 6) * 3, math.floor(h / 6) * 5 + self.textDisplayHeight),
            "2": lambda w, h: (math.floor(w / 6) * 5, math.floor(h / 6) * 5 + self.textDisplayHeight),
            "3": lambda w, h: (math.floor(w / 6) * 1, math.floor(h / 6) * 3 + self.textDisplayHeight),
            "4": lambda w, h: (math.floor(w / 6) * 3, math.floor(h / 6) * 3 + self.textDisplayHeight),
            "5": lambda w, h: (math.floor(w / 6) * 5, math.floor(h / 6) * 3 + self.textDisplayHeight),
            "6": lambda w, h: (math.floor(w / 6) * 1, math.floor(h / 6) * 1 + self.textDisplayHeight),
            "7": lambda w, h: (math.floor(w / 6) * 3, math.floor(h / 6) * 1 + self.textDisplayHeight),
            "8": lambda w, h: (math.floor(w / 6) * 5, math.floor(h / 6) * 1 + self.textDisplayHeight)
        }

        return centerFormulas[str(pos)](self.w, self.boardHeight)


    def drawSymbol(self, symbol, boardPos):
        """
        :param symbol: x or y
        :param boardPos: 0-8, 0 is top left, 1 is top middle, ...
        :return:
        """


        def drawX():
            self.board.penup()
            xy = self.getCordFromBoardPos(boardPos)
            lineOneStartX = xy[0] - self.xSymbolSize / 2
            lineOneStartY = xy[1] - self.xSymbolSize / 2

            lineTwoStartX = xy[0] + self.xSymbolSize / 2
            lineTwoStartY = xy[1] - self.xSymbolSize / 2

            symbolLength = self.xSymbolSize / math.sin(math.radians(45))

            # first line
            self.board.goto(lineOneStartX, lineOneStartY)
            self.board.setheading(45)
            self.board.pendown()
            self.board.pencolor(self.xColor)
            self.board.pensize(self.xSymbolPenSize)
            self.board.forward(symbolLength)
            self.board.penup()

            # second line
            self.board.goto(lineTwoStartX, lineTwoStartY)
            self.board.pendown()
            self.board.setheading(135)
            self.board.forward(symbolLength)
            self.board.penup()


        def drawO():
            self.board.setheading(0)
            self.board.penup()
            xy = self.getCordFromBoardPos(boardPos)
            yAdjusted = xy[1] - self.oSymbolRadius
            self.board.goto(xy[0], yAdjusted)
            self.board.pendown()
            self.board.pencolor(self.oColor)
            self.board.pensize(self.oSymbolPenSize)
            self.board.circle(self.oSymbolRadius)

        if symbol.lower() == 'x':
            drawX()
        elif symbol.lower() == 'o':
            drawO()


    def drawWinLine(self, startBoardPos, endBoardPos):
        startXY = self.getCordFromBoardPos(startBoardPos)
        endXY = self.getCordFromBoardPos(endBoardPos)
        self.board.penup()
        self.board.goto(startXY[0], startXY[1])
        self.board.pendown()
        self.board.pensize(self.winLineSize)
        self.board.pencolor(self.winLineColor)
        self.board.goto(endXY[0], endXY[1])

    def drawMessage(self, msg):
        self.board.pencolor('black')
        self.board.penup()
        self.board.goto(0, 0)
        self.board.write(msg, font=("Tahoma", 20, "normal"))
        self.board.penup()

    def clearSymbol(self, boardPos):
        squareCenter = self.getCordFromBoardPos(boardPos)
        startX = squareCenter[0] - self.xSymbolSize / 1.5
        startY = squareCenter[1] - self.xSymbolSize / 1.5
        self.board.penup()
        self.board.goto(startX, startY)
        self.board.pendown()
        self.board.pensize(1)
        self.board.pencolor('white')
        self.board.fillcolor('white')
        self.board.begin_fill()

        self.board.setheading(90)
        for n in range(1, 5):
            self.board.forward(self.xSymbolSize * 1.4)
            self.board.right(90)

        self.board.end_fill()


    def wait(self):
        self.board.getscreen().exitonclick()

    def drawSymbols(self, symbols):
        for index, s in enumerate(symbols):
            self.drawSymbol(s, index)

    def redrawSymbols(self, symbols):
        self.clearAllSymbols()
        self.drawSymbols(symbols)

    def clearAllSymbols(self):
        for n in range(0, 9):
            self.clearSymbol(n)


if __name__ == '__main__':
    print("test mode")
    t = TicTacToeBoard()
    t.drawMessage('Welcome to Tic Tac Toe!')

    symbols = []
    for n in range(0, 9):
        if n % 2 == 0:
            symbols.append('x')
        else:
            symbols.append('o')

    t.redrawSymbols(symbols)

    t.drawWinLine(0, 2)
    t.drawWinLine(0, 8)
    t.drawWinLine(6, 2)
    t.drawWinLine(6, 8)

    t.wait()


