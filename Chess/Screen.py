import turtle
class Screen:
    def __init__(self):
        turtle.setup(700,700)
        turtle.setworldcoordinates(0, 0, 700, 700)
        turtle.tracer(False)
        self.draw = turtle.Turtle()
        self.draw.hideturtle()
        turtle.bgcolor([78/255,45/255,28/255])
        self.draw.penup()
        self.draw.goto(25,25)
        self.draw.color([232/255, 195/255, 151/255])
        self.draw.begin_fill()
        for _ in range(4):
            self.draw.forward(650)
            self.draw.left(90)
        self.draw.end_fill()
        val = 65
        val2 = 8
        self.draw.color([78 / 255, 45 / 255, 28 / 255])
        for i in range(85,86+ (75*7),75):
            self.draw.goto(i,650)
            self.draw.write(chr(val),font=("Arial",15,"bold"))
            self.draw.goto(30, i-10)
            self.draw.write(str(val2), font=("Arial", 15, "bold"))
            val += 1
            val2 -= 1
        self.names_B = ["Rook_B", "Knight_B", "Bishop_B", "Queen_B", "King_B", "Bishop_B", "Knight_B", "Rook_B", "Pawn_B"]
        self.names_W = ["Rook_W", "Knight_W", "Bishop_W", "Queen_W", "King_W", "Bishop_W", "Knight_W", "Rook_W", "Pawn_W"]

        for name1,name2 in zip(self.names_W,self.names_B):
            turtle.addshape("images/" + name1 + ".gif")
            turtle.addshape("images/" + name2 + ".gif")

        self.s= turtle.Turtle()
        self.s.penup()
        self.s.goto(87.5,87.5)
        turtle.tracer(True)

    def board(self):
        x,y = 50,50
        turtle.tracer(False)
        self.draw.goto(x, y)
        self.draw.color([78/255, 45/255, 28/255])
        for i in range(8):
            if i%2 == 0:
                x = 50
                for j in range(4):
                    self.draw.goto(x,y)
                    self.draw.begin_fill()
                    for h in range(4):
                        self.draw.forward(75)
                        self.draw.left(90)
                    self.draw.end_fill()
                    x += 150

            else:
                x = 125
                for j in range(4):
                    self.draw.goto(x,y)
                    self.draw.begin_fill()
                    for h in range(4):
                        self.draw.forward(75)
                        self.draw.left(90)
                    self.draw.end_fill()
                    x += 150

            y += 75

        self.draw.penup()
        self.draw.goto(50, 50)
        self.draw.pendown()
        for i in range(4):
            self.draw.forward(600)
            self.draw.left(90)

        self.s.hideturtle()

        for i in range(8):
            self.s.shape("images/"+self.names_B[i]+".gif")
            self.s.stamp()
            self.s.goto(self.s.xcor()+75, self.s.ycor())

        self.s.goto(self.s.xcor(), self.s.ycor() + 75)

        for i in range(8):
            self.s.shape("images/"+self.names_B[8]+".gif")
            self.s.goto(self.s.xcor() - 75, self.s.ycor())
            self.s.stamp()

        self.s.goto(self.s.xcor(), self.s.ycor() + 450)

        for i in range(8):
            self.s.shape("images/"+self.names_W[i]+".gif")
            self.s.stamp()
            self.s.goto(self.s.xcor()+75, self.s.ycor())

        self.s.goto(self.s.xcor(), self.s.ycor() - 75)

        for i in range(8):
            self.s.shape("images/"+self.names_W[8]+".gif")
            self.s.goto(self.s.xcor() - 75, self.s.ycor())
            self.s.stamp()


        turtle.tracer(True)

    def redraw(self,field):
        print("test")
        points = {6: 'King_W', -6: 'King_B', 5: 'Queen_W', -5: 'Queen_B', 4: 'Rook_W', -4: 'Rook_B', \
                       3: 'Bishop_W', -3: 'Bishop_B', 2: 'Knight_W', -2: 'Knight_B', 1: 'Pawn_W', -1: 'Pawn_B'}

        self.s.clear()
        turtle.tracer(False)
        self.s.goto(87.5,87.5)
        for j in range(7,-1,-1):
            for i in range(8):
                if field[j][i] != 0:
                    self.s.shape("images/"+points[field[j][i]]+".gif")
                    self.s.stamp()
                self.s.goto(self.s.xcor() + 75, self.s.ycor())
            self.s.goto(87.5, self.s.ycor()+75)
        turtle.tracer(True)
