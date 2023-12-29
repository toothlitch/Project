import turtle
class Shape:
    def __init__(self,title="Tetris"):
        turtle.title(title)
        turtle.setup(800,750)
        turtle.setworldcoordinates(0,0,800,750)
        turtle.bgcolor("black")
        self.t = turtle.Turtle()

    def setup(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(22,47)
        self.t.pendown()
        turtle.tracer(False)
        self.t.color("green")
        self.t.pensize(3)
        self.t.forward(406)
        self.t.left(90)
        self.t.forward(656)
        self.t.left(90)
        self.t.forward(406)
        self.t.left(90)
        self.t.forward(656)
        self.t.left(90)
        '''
        for y in range(50, 700, 50):
            if (y//50) % 2 == 0:
                color = "black"
            else:
                color = 'gray'
            for x in range(25, 400, 50):
                self.square_s(x,y,color)
                if color == 'black':
                    color = 'gray'
                else:
                    color = 'black'
           
        '''
        self.draw_next()
        turtle.tracer(True)
        self.t.speed(0)
        turtle.tracer(False)

    def draw_next(self):
        self.t.penup()
        self.t.color("green")
        self.t.goto(475, 500)
        self.t.pendown()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(300)
            self.t.right(90)
        self.t.color("black")
        self.t.end_fill()

    def square_s(self,x,y,color = "gray"):
        self.t.penup()
        self.t.goto(x,y)
        self.t.color(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(50)
            self.t.left(90)
        self.t.end_fill()

    def twoxtwo(self, x, y):
        for i in range(2):
            for j in range(2):
                self.square_s(x + (50 * j), y - (50 * i), "blue")

    def onexfour(self, x, y):
        for i in range(4):
            self.square_s(x, y - 50*i, "yellow")

    def fourxone(self, x, y):
        for i in range(4):
            self.square_s(x + 50*i, y, "orange")

    def up(self, x, y):
        self.square_s(x+50, y, "red")
        for i in range(3):
            self.square_s(x + 50*i, y - 50, "red")

    def down(self, x, y):
        for i in range(3):
            self.square_s(x + 50*i, y, "green")
        self.square_s(x + 50, y - 50, "green")

    def left(self, x, y):
        for i in range(3):
            self.square_s(x + 50, y - 50*i, "violet")
        self.square_s(x, y - 50, "violet")

    def right(self, x, y):
        for i in range(3):
            self.square_s(x, y - 50*i, "purple")
        self.square_s(x + 50, y - 50, "purple")



    def redraw(self,occupied):
        colors = ["blue","yellow","orange","red","green","violet", "purple"]
        self.t.goto(22, 47)
        self.t.pendown()
        turtle.tracer(False)
        self.t.color("green")
        self.t.pensize(3)
        self.t.begin_fill()
        self.t.forward(406)
        self.t.left(90)
        self.t.forward(656)
        self.t.left(90)
        self.t.forward(406)
        self.t.left(90)
        self.t.forward(656)
        self.t.left(90)
        self.t.color("black")
        self.t.end_fill()
        row = lambda x: x * 50 + 50
        col = lambda x: x * 50 + 25
        for r in range(13):
            for c in range(8):
                if occupied[r][c] != 0:
                    self.square_s(col(c),row(r),colors[occupied[r][c]-1])
        turtle.tracer(True)
        turtle.tracer(False)


