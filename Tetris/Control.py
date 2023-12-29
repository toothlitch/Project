from Tetris_Shape import Shape
import random
import turtle

class Control:
    def __init__(self, shape):
        self.shape = shape
        self.shape_list = [shape.twoxtwo, shape.onexfour, shape.fourxone, shape.up, shape.down, shape.left, shape.right]
        self.next = random.randint(0, len(self.shape_list) - 1)
        self.next = 6
        self.cur = None
        self.cur_x = None
        self.cur_y = 12
        self.occupied = [[0, 0, 0, 0, 0, 0, 0, 0] for i in range(13)]
        self.find_x = lambda x: x * 50 + 25
        self.find_y = lambda x: x * 50 + 50
        turtle.onkeypress(self.down, "Down")
        turtle.onkeypress(self.right, "Right")
        turtle.onkeypress(self.left, "Left")
        turtle.onkeypress(self.turn, "Up")
        turtle.listen()
        self.spawn()


    def spawn(self):
        self.cur = self.next
        self.next = random.randint(0, len(self.shape_list) - 1)
        #self.next = 6
        self.shape.draw_next()
        self.shape_list[self.next](550, 400)
        self.cur_x = 3
        self.cur_y = 12
        self.shape_list[self.cur](self.find_x(self.cur_x), self.find_y(self.cur_y))
        self.fill()


    def fill(self):
        if self.cur == 0:
            for i in range(self.cur_x,self.cur_x+2):
                for j in range(self.cur_y,self.cur_y-2,-1):
                    self.occupied[j][i] = 1
        elif self.cur == 1:
            for i in range(self.cur_y, self.cur_y -4,-1):
                self.occupied[i][self.cur_x] = 2
        elif self.cur == 2:
            for i in range(self.cur_x, self.cur_x +4):
                self.occupied[self.cur_y][i] = 3
        elif self.cur == 3:
            self.occupied[self.cur_y][self.cur_x+1] = 4
            for i in range(3):
                self.occupied[self.cur_y-1][self.cur_x+i] = 4
        elif self.cur == 4:
            for i in range(3):
                self.occupied[self.cur_y][self.cur_x+i] = 5
            self.occupied[self.cur_y-1][self.cur_x + 1] = 5
        elif self.cur == 5:
            for i in range(3):
                self.occupied[self.cur_y - i][self.cur_x+1] = 6
            self.occupied[self.cur_y - 1][self.cur_x] = 6
        elif self.cur == 6:
            for i in range(3):
                self.occupied[self.cur_y - i][self.cur_x] = 7
            self.occupied[self.cur_y - 1][self.cur_x + 1] = 7



    def print_t(self):
        print("______________test___________________")
        for i in self.occupied[::-1]:
            print(i)

    def right(self):
        if self.cur == 0 and self.cur_x + 2 < 8 and \
                self.occupied[self.cur_y -1][self.cur_x + 2] == 0 and self.occupied[self.cur_y][self.cur_x + 2] == 0:
            self.occupied[self.cur_y][self.cur_x + 2] = 1
            self.occupied[self.cur_y - 1][self.cur_x + 2] = 1
            self.occupied[self.cur_y][self.cur_x] = 0
            self.occupied[self.cur_y - 1][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 1 and self.cur_x < 7 and \
                self.occupied[self.cur_y][self.cur_x + 1] == 0 and self.occupied[self.cur_y-1][self.cur_x + 1] == 0 \
                and self.occupied[self.cur_y-2][self.cur_x + 1] == 0 and self.occupied[self.cur_y-3][self.cur_x + 1] == 0:
            for i in range(4):
                self.occupied[self.cur_y - i][self.cur_x + 1] = 2
            for i in range(4):
                self.occupied[self.cur_y - i][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 2 and self.cur_x < 4 and \
                self.occupied[self.cur_y][self.cur_x + 4] == 0:
            for i in range(1,5):
                self.occupied[self.cur_y][self.cur_x + i] = 3
            self.occupied[self.cur_y][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 3 and self.cur_x <= 4 and self.occupied[self.cur_y][self.cur_x+2] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x+3] == 0:
            self.occupied[self.cur_y][self.cur_x+2] = 4
            self.occupied[self.cur_y][self.cur_x+1] = 0
            for i in range(1,4):
                self.occupied[self.cur_y-1][self.cur_x + i] = 4
            self.occupied[self.cur_y-1][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 4 and self.cur_x <= 4 and self.occupied[self.cur_y][self.cur_x+3] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x+2] == 0:
            self.occupied[self.cur_y-1][self.cur_x+2] = 5
            self.occupied[self.cur_y-1][self.cur_x+1] = 0
            for i in range(1,4):
                self.occupied[self.cur_y][self.cur_x + i] = 5
            self.occupied[self.cur_y][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 5 and self.cur_x + 2 <= 7 and self.occupied[self.cur_y][self.cur_x+2] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x+2] == 0 and self.occupied[self.cur_y-2][self.cur_x+2] == 0:
            self.occupied[self.cur_y-1][self.cur_x+1] = 6
            self.occupied[self.cur_y-1][self.cur_x] = 0
            for i in range(0,3):
                self.occupied[self.cur_y - i][self.cur_x + 2] = 6
            self.occupied[self.cur_y][self.cur_x+1] = 0
            self.occupied[self.cur_y-2][self.cur_x+1] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        if self.cur == 6 and self.cur_x + 2 <= 7 and self.occupied[self.cur_y][self.cur_x+1] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x+2] == 0 and self.occupied[self.cur_y-2][self.cur_x+1] == 0:
            self.occupied[self.cur_y-1][self.cur_x+2] = 7
            for i in range(0,3):
                self.occupied[self.cur_y - i][self.cur_x + 1] = 7
            for i in range(0,3):
                self.occupied[self.cur_y - i][self.cur_x] = 0
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        #if self.cur == 3 and self.cur_x

    def left(self):
        #정사각형
        if self.cur == 0 and self.cur_x >= 1 and \
                self.occupied[self.cur_y - 1][self.cur_x - 1] == 0 and self.occupied[self.cur_y][self.cur_x - 1] == 0:
            self.occupied[self.cur_y][self.cur_x - 1] = 1
            self.occupied[self.cur_y - 1][self.cur_x - 1] = 1
            self.occupied[self.cur_y][self.cur_x + 1] = 0
            self.occupied[self.cur_y - 1][self.cur_x + 1] = 0
            self.cur_x -= 1
            self.shape.redraw(self.occupied)

        #세로 길쭉
        if self.cur == 1 and self.cur_x > 0 and \
                self.occupied[self.cur_y][self.cur_x - 1] == 0 and self.occupied[self.cur_y-1][self.cur_x - 1] == 0 \
                and self.occupied[self.cur_y-2][self.cur_x - 1] == 0 and self.occupied[self.cur_y-3][self.cur_x - 1] == 0:
            for i in range(4):
                self.occupied[self.cur_y - i][self.cur_x - 1] = 2
            for i in range(4):
                self.occupied[self.cur_y - i][self.cur_x] = 0
            self.cur_x -= 1

            self.shape.redraw(self.occupied)

        if self.cur == 2 and self.cur_x > 0 and \
                self.occupied[self.cur_y][self.cur_x-1] == 0:
            for i in range(3, -2, -1):
                self.occupied[self.cur_y][self.cur_x + i] = 3
            self.occupied[self.cur_y][self.cur_x + 3] = 0
            self.cur_x -= 1

            self.shape.redraw(self.occupied)

        if self.cur == 3 and self.cur_x >= 1 and self.occupied[self.cur_y][self.cur_x] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x-1] == 0:
            self.occupied[self.cur_y][self.cur_x] = 4
            self.occupied[self.cur_y][self.cur_x+1] = 0
            self.occupied[self.cur_y-1][self.cur_x-1] = 4
            self.occupied[self.cur_y-1][self.cur_x+2] = 0
            self.cur_x -= 1
            self.shape.redraw(self.occupied)

        if self.cur == 4 and self.cur_x >= 1 and self.occupied[self.cur_y][self.cur_x-1] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x] == 0:
            self.occupied[self.cur_y][self.cur_x-1] = 5
            self.occupied[self.cur_y][self.cur_x+2] = 0
            self.occupied[self.cur_y-1][self.cur_x] = 5
            self.occupied[self.cur_y-1][self.cur_x+1] = 0
            self.cur_x -= 1
            self.shape.redraw(self.occupied)

        if self.cur == 5 and self.cur_x >= 1 and self.occupied[self.cur_y][self.cur_x] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x-1] == 0 and self.occupied[self.cur_y-2][self.cur_x] == 0:
            for i in range(3):
                self.occupied[self.cur_y-i][self.cur_x] = 6
            for i in range(3):
                self.occupied[self.cur_y-i][self.cur_x+1] = 0
            self.occupied[self.cur_y-1][self.cur_x-1] = 6
            self.cur_x -= 1
            self.shape.redraw(self.occupied)

        if self.cur == 6 and self.cur_x >= 1 and self.occupied[self.cur_y][self.cur_x-1] == 0 \
                and self.occupied[self.cur_y-1][self.cur_x-1] == 0 and self.occupied[self.cur_y-2][self.cur_x-1] == 0:
            for i in range(3):
                self.occupied[self.cur_y-i][self.cur_x-1] = 7
            self.occupied[self.cur_y][self.cur_x] = 0
            self.occupied[self.cur_y-2][self.cur_x] = 0
            self.occupied[self.cur_y-1][self.cur_x+1] = 0
            self.cur_x -= 1
            self.shape.redraw(self.occupied)

    def down(self):
        if self.cur == 0 and self.cur_y-2 > -1 and\
                self.occupied[self.cur_y-2][self.cur_x] == 0 and self.occupied[self.cur_y-2][self.cur_x + 1] == 0:
            self.occupied[self.cur_y - 2][self.cur_x] = 1
            self.occupied[self.cur_y - 2][self.cur_x + 1] = 1
            self.occupied[self.cur_y][self.cur_x] = 0
            self.occupied[self.cur_y][self.cur_x + 1] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 1 and self.cur_y-4 > -1 and self.occupied[self.cur_y-4][self.cur_x] == 0:
            for i in range(1,5):
                self.occupied[self.cur_y-i][self.cur_x] = 2
            self.occupied[self.cur_y][self.cur_x] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 2 and self.cur_y > 0 and self.occupied[self.cur_y - 1][self.cur_x] == 0\
            and self.occupied[self.cur_y - 1][self.cur_x+1] == 0 and self.occupied[self.cur_y - 1][self.cur_x+2] == 0\
                and self.occupied[self.cur_y - 1][self.cur_x+3] == 0:
            for i in range(4):
                self.occupied[self.cur_y-1][self.cur_x+i] = 3
            for i in range(4):
                self.occupied[self.cur_y][self.cur_x+i] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 3 and self.cur_y - 1 > 0 and self.occupied[self.cur_y - 2][self.cur_x] == 0 \
            and self.occupied[self.cur_y - 2][self.cur_x+1] == 0 and self.occupied[self.cur_y - 2][self.cur_x+2] == 0:
            for i in range(3):
                self.occupied[self.cur_y-2][self.cur_x+i] = 4
            for i in range(3):
                self.occupied[self.cur_y-1][self.cur_x+i] = 0
            self.occupied[self.cur_y-1][self.cur_x + 1] = 4
            self.occupied[self.cur_y][self.cur_x + 1] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 4 and self.cur_y - 1 > 0 and self.occupied[self.cur_y - 1][self.cur_x] == 0 \
            and self.occupied[self.cur_y - 2][self.cur_x+1] == 0 and self.occupied[self.cur_y - 1][self.cur_x+2] == 0:
            for i in range(3):
                self.occupied[self.cur_y-1][self.cur_x+i] = 5
            for i in range(3):
                self.occupied[self.cur_y][self.cur_x+i] = 0
            self.occupied[self.cur_y-2][self.cur_x + 1] = 5
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 5 and self.cur_y - 2 > 0 and self.occupied[self.cur_y - 2][self.cur_x] == 0 \
            and self.occupied[self.cur_y - 3][self.cur_x+1] == 0:
            self.occupied[self.cur_y-3][self.cur_x+1] = 6
            self.occupied[self.cur_y][self.cur_x+1] = 0
            self.occupied[self.cur_y-2][self.cur_x] = 6
            self.occupied[self.cur_y-1][self.cur_x] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        elif self.cur == 6 and self.cur_y - 2 > 0 and self.occupied[self.cur_y - 3][self.cur_x] == 0 \
            and self.occupied[self.cur_y - 2][self.cur_x+1] == 0:
            self.occupied[self.cur_y-3][self.cur_x] = 7
            self.occupied[self.cur_y][self.cur_x] = 0
            self.occupied[self.cur_y-2][self.cur_x+1] = 7
            self.occupied[self.cur_y-1][self.cur_x+1] = 0
            self.cur_y-=1
            #self.print_t()
            self.shape.redraw(self.occupied)

        else:
            self.clear()


    def turn(self):
        #세로 길쭉
        if self.cur == 1:
            for i in range(1, 4):
                self.occupied[self.cur_y - i][self.cur_x] = 0
            for i in range(4):
                self.occupied[self.cur_y][self.cur_x+i] = 3
            # self.print_t()
            self.cur = 2
            self.shape.redraw(self.occupied)

        elif self.cur == 2:
            for i in range(4):
                self.occupied[self.cur_y][self.cur_x + i] = 0
            for i in range(4):
                self.occupied[self.cur_y-i][self.cur_x] = 2
            self.cur = 1
            self.shape.redraw(self.occupied)

        elif self.cur == 3:
            self.occupied[self.cur_y ][self.cur_x+1] = 0
            self.occupied[self.cur_y - 1][self.cur_x] = 0
            for i in range(3):
                self.occupied[self.cur_y - i][self.cur_x + 1] = 7
            self.occupied[self.cur_y - 1][self.cur_x + 2] = 7
            self.cur = 6
            self.cur_x += 1
            self.shape.redraw(self.occupied)

        elif self.cur == 4:
            for i in range(3):
                self.occupied[self.cur_y + 1 - i][self.cur_x + 1] = 6
            self.occupied[self.cur_y][self.cur_x] = 6
            self.occupied[self.cur_y][self.cur_x + 2] = 0
            self.cur_y += 1
            self.cur = 5
            self.shape.redraw(self.occupied)


        elif self.cur == 5:
            for i in range(3):
                self.occupied[self.cur_y - 1][self.cur_x + i] = 4
            self.occupied[self.cur_y][self.cur_x + 1] = 4
            self.occupied[self.cur_y - 2][self.cur_x + 1] = 0
            self.cur = 3
            self.shape.redraw(self.occupied)


        elif self.cur == 6:
            for i in range(3):
                self.occupied[self.cur_y - 1][self.cur_x - 1 + i] = 5
            self.occupied[self.cur_y - 2][self.cur_x] = 5
            self.occupied[self.cur_y][self.cur_x] = 0
            self.cur_x -= 1
            self.cur_y -= 1
            self.cur = 4
            self.shape.redraw(self.occupied)

    def clear(self):

        for i in range(12, -1, -1):
            count, index = 0, -1
            check = False
            if 0 not in self.occupied[i]:
                check = True
                count += 1
                index = i
            if check:
                for h in range(8):
                    self.occupied[i][h] = 0
                for h in range(i+1,13):
                    for j in range(8):
                        self.occupied[h-1][j] = self.occupied[h][j]





        self.print_t()
        for i in range(8):
            if self.occupied[-1][i]!=0:
                end = turtle.Turtle()
                end.penup()
                end.hideturtle()
                end.color(([1,1,1]))
                end.goto(500,100)
                end.write("END" ,font=("arial",30,'normal'))
                return None
        self.spawn()

        '''
        self.shape_list = [shape.twoxtwo, shape.onexfour, shape.fourxone, shape.up , shape.down, shape.left, shape.right]
        self.lowest = [[-1, -1], [-3], [0,0,0,0], [-1, -1, -1], [0, -1, 0], [-1, -2], [-2,-1]]
        self.highest = [[2, 2], [4], [1, 1, 1, 1], [1, 2, 1], [2, 2, 2], [2, 3], [3, 2]]
        self.height = [2, 4, 1, 2, 2, 3, 3]
        self.width = [2, 1, 4, 3, 3, 2, 2]
        self.left_start = [175, 175, 175, 125, 125, 125, 175]
        self.right_start = [225, 175, 325, 225, 225, 175, 225]
        self.distance = [[0,1], [0,1], [0,3], [0,2], [0,2], [0,1],[0,1]]
        self.next = random.randint(0,len(self.shape_list)-1)
        self.cur = None
        self.cur_x = None
        self.cur_y = 650
        self.spawn()
        #self.shape_list[self.cur](self.cur_x,self.cur_y)
        self.ylimit = [0, 0, 0, 0, 0, 0, 0, 0]
        turtle.onkeypress(self.down, "Down")
        turtle.onkeypress(self.right, "Right")
        turtle.listen()

        self.occupied = []
        for i in range(13):
            if i % 2 == 0:
                self.occupied.append([-2, -1, -2, -1, -2, -1, -2, -1])
            else:
                self.occupied.append([-1, -2, -1, -2, -1, -2, -1, -2])

    def spawn(self):
        self.cur = self.next
        self.cur_x = self.left_start[self.cur]
        self.next =random.randint(0,len(self.shape_list)-1)
        self.shape.draw_next()
        self.shape_list[self.next](550, 400)
        self.cur_x = 175
        self.cur_y = 650
        self.shape_list[self.cur](self.cur_x,self.cur_y)

    def okay(self):
        for i in range(self.width[self.cur]):
            #print(self.cur_y + 50 * (self.lowest[self.cur][i] -1), self.ylimit[(self.cur_x - 25)//50 + i])
            if self.cur_y + 50 * (self.lowest[self.cur][i] -1) <= self.ylimit[(self.cur_x - 25)//50 + i]:
                return self.ylimit[(self.cur_x - 25)//50 + i], False
        return 0,True

    def down(self):
        h ,ans = self.okay()
        if ans:
            for y in range(self.height[self.cur]):
                color = "black"
                if ((self.cur_y - (y*50)) // 50) % 2 == 1:
                    color = "gray"
                for x in range(25, 400, 50):
                    print((650 - (self.cur_y - (y*50))) // 50,(x - 25) // 50)
                    if self.occupied[(650 - (self.cur_y - (y*50))) // 50][(x - 25) // 50] <0:
                        self.shape.square_s(x, (self.cur_y - (y*50)), color)
                    if color == 'black':
                        color = 'gray'
                    else:
                        color = 'black'

            self.cur_y -= 50
            self.shape_list[self.cur](self.cur_x, self.cur_y)

        else:
            for i in range(self.width[self.cur]):
                self.ylimit[(self.cur_x - 25)//50 + i] = 50 * (self.highest[self.cur][i]) + h
            print(self.ylimit)
            self.fill()
            self.spawn()

    def okay_right(self):
        for i in range(self.height[self.cur]):
            print(self.right_start[self.cur])
            if self.cur_x + 50*self.distance[self.cur][1] >= 375 or \
                    self.occupied[(650 - (self.cur_y - 50)) // 50 - 1 + i][(self.right_start[self.cur] - 25) // 50 + 1] >= 0:
                return False
        return True

    def right(self):
        if self.okay_right():
            for y in range(self.height[self.cur]):
                color = "black"
                if ((self.cur_y - (y * 50)) // 50) % 2 == 1:
                    color = "gray"
                for x in range(25, 400, 50):
                    if self.occupied[(650 - (self.cur_y - 50)) // 50][(x - 25) // 50] < 0:
                        self.shape.square_s(x, (self.cur_y - (y * 50)), color)
                    if color == 'black':
                        color = 'gray'
                    else:
                        color = 'black'

            self.cur_x += 50
            self.shape_list[self.cur](self.cur_x, self.cur_y)
        print(self.cur_x)

    def fill(self):
        if self.cur == 0:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y-50))//50 -1][(self.cur_x - 25)//50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y-50))//50][(self.cur_x - 25)//50] = self.cur
            self.occupied[(650 - (self.cur_y-50))//50][(self.cur_x - 25)//50 + 1] = self.cur

        if self.cur == 1:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 + 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 + 2][(self.cur_x - 25) // 50] = self.cur

        if self.cur == 2:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 2] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 3] = self.cur

        if self.cur == 3:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50 + 2] = self.cur

        if self.cur == 4:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 2] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50 + 1] = self.cur

        if self.cur == 5:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 + 1][(self.cur_x - 25) // 50 + 1] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50] = self.cur

        if self.cur == 6:
            self.occupied[(650 - (self.cur_y - 50)) // 50 - 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50 + 1][(self.cur_x - 25) // 50] = self.cur
            self.occupied[(650 - (self.cur_y - 50)) // 50][(self.cur_x - 25) // 50 + 1] = self.cur

        for i in range(13):
            print(self.occupied[i])
        print()
        '''
