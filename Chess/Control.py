import turtle
from Screen import Screen
class Control:
    def __init__(self,screen):
        self.points = {6: 'King_W', -6: 'King_B', 5: 'Queen_W', -5: 'Queen_B', 4: 'Rook_W', -4: 'Rook_B', \
                  3: 'Bishop_W', -3: 'Bishop_B', 2: 'Knight_W', -2: 'Knight_B', 1: 'Pawn_W', -1: 'Pawn_B'}
        self.screen = screen
        self.field = [[4,2,3,5,6,3,2,4],[1,1,1,1,1,1,1,1]] + [[0 for _ in range(8)]for _ in range(4)] \
                     + [[-1,-1,-1,-1,-1,-1,-1,-1], [-4,-2,-3,-5,-6,-3,-2,-4]]
        self.cur_player = True
        self.selected = None
        self.print_field()
        turtle.onscreenclick(self.click)

    def print_field(self):
        print("\n-----------test-----------\n")
        for i in self.field:
            print(i)
    def is_checked(self):
        if self.cur_player == True:
            pass
        else:
            pass

    def click(self,a,b):
        #옮기려는 위치
        row =int((700-50-b)//75)
        col =int((a-50)//75)
        print(row,col)

        #백 차례
        if self.cur_player is True and self.field[row][col] > 0:
            self.selected = [row,col]
        elif self.cur_player is True and self.field[row][col] <= 0 and self.selected is not None:
            able = []
            x = self.selected[1]
            y = self.selected[0]
            #pawn
            if self.field[self.selected[0]][self.selected[1]] == 1:
                if y == 1:
                    for i in range(1,3):
                        if self.field[y+i][x] == 0:
                            able.append([y+i,x])
                else:
                    if self.field[y+1][x] == 0:
                        able.append([y+1,x])
                if x > 1 and self.field[y+1][x-1] < 0:
                    able.append([y+1, x-1])
                if x < 7 and self.field[y+1][x+1] < 0:
                    able.append([y+1, x+1])

            #knight
            if self.field[self.selected[0]][self.selected[1]] == 2:

                if 0 <= y-2 <= 7 and 0 <= x+1 <= 7:
                    if self.field[y-2][x+1] <= 0:
                        able.append([y-2, x+1])
                if 0 <= y-1 <= 7 and 0 <= x+2 <= 7:
                    if self.field[y-1][x+2] <= 0:
                        able.append([y-1, x+2])
                if 0 <= y+1 <= 7 and 0 <= x+2 <= 7:
                    if self.field[y+1][x+2] <= 0:
                        able.append([y+1, x+2])
                if 0 <= y+2 <= 7 and 0 <= x+1 <= 7:
                    if self.field[y+2][x+1] <= 0:
                        able.append([y+2, x+1])
                if 0 <= y+2 <= 7 and 0 <= x-1 <= 7:
                    if self.field[y+2][x-1] <= 0:
                        able.append([y+2, x-1])
                if 0 <= y+1 <= 7 and 0 <= x-2 <= 7:
                    if self.field[y+1][x-2] <= 0:
                        able.append([y+1, x-2])
                if 0 <= y-1 <= 7 and 0 <= x-2 <= 7:
                    if self.field[y-1][x-2] <= 0:
                        able.append([y-1, x-2])
                if 0 <= y-2 <= 7 and 0 <= x-1 <= 7:
                    if self.field[y-2][x-1] <= 0:
                        able.append([y-2, x-1])

            #bishop
            if self.field[self.selected[0]][self.selected[1]] == 3:

                block_1 = False
                x_count_1 = 0
                y_count_1 = 0
                while block_1 is False:
                    x_count_1 += 1
                    y_count_1 += 1
                    if 0 <= y-y_count_1 <= 7 and 0 <= x+x_count_1 <= 7:
                        if self.field[y-y_count_1][x+x_count_1] == 0:
                            able.append([y-y_count_1, x+x_count_1])
                        elif self.field[y-y_count_1][x+x_count_1] > 0:
                            block_1 = True
                        elif self.field[y-y_count_1][x+x_count_1] < 0:
                            able.append([y-y_count_1, x+x_count_1])
                            block_1 = True
                    else:
                        block_1 = True

                block_2 = False
                x_count_2 = 0
                y_count_2 = 0
                while block_2 is False:
                    x_count_2 += 1
                    y_count_2 += 1
                    if 0 <= y+y_count_2 <= 7 and 0 <= x+x_count_2 <= 7:
                        if self.field[y+y_count_2][x+x_count_2] == 0:
                            able.append([y+y_count_2, x+x_count_2])
                        elif self.field[y+y_count_2][x+x_count_2] > 0:
                            block_2 = True
                        elif self.field[y+y_count_2][x+x_count_2] < 0:
                            able.append([y+y_count_2, x+x_count_2])
                            block_2 = True
                    else:
                        block_2 = True

                block_3 = False
                x_count_3 = 0
                y_count_3 = 0
                while block_3 is False:
                    x_count_3 += 1
                    y_count_3 += 1
                    if 0 <= y + y_count_3 <= 7 and 0 <= x - x_count_3 <= 7:
                        if self.field[y + y_count_3][x - x_count_3] == 0:
                            able.append([y + y_count_3, x - x_count_3])
                        elif self.field[y + y_count_3][x - x_count_3] > 0:
                            block_3 = True
                        elif self.field[y + y_count_3][x - x_count_3] < 0:
                            able.append([y + y_count_3, x - x_count_3])
                            block_3 = True
                    else:
                        block_3 = True

                block_4 = False
                x_count_4 = 0
                y_count_4 = 0
                while block_4 is False:
                    x_count_4 += 1
                    y_count_4 += 1
                    if 0 <= y - y_count_4 <= 7 and 0 <= x - x_count_4 <= 7:
                        if self.field[y - y_count_4][x - x_count_4] == 0:
                            able.append([y - y_count_4, x - x_count_4])
                        elif self.field[y - y_count_4][x - x_count_4] > 0:
                            block_4 = True
                        elif self.field[y - y_count_4][x - x_count_4] < 0:
                            able.append([y - y_count_4, x - x_count_4])
                            block_4 = True
                    else:
                        block_4 = True

            #rook
            if self.field[self.selected[0]][self.selected[1]] == 4:

                block_5 = False
                y_count_5 = 0
                while block_5 is False:
                    y_count_5 += 1
                    if 0 <= y + y_count_5 <= 7:
                        if self.field[y + y_count_5][x] == 0:
                            able.append([y + y_count_5, x])
                        elif self.field[y + y_count_5][x] > 0:
                            block_5 = True
                        elif self.field[y + y_count_5][x] < 0:
                            able.append([y + y_count_5, x])
                            block_5 = True
                    else:
                        block_5 = True

                block_6 = False
                x_count_6 = 0
                while block_6 is False:
                    x_count_6 += 1
                    if 0 <= x + x_count_6 <= 7:
                        if self.field[y][x + x_count_6] == 0:
                            able.append([y, x + x_count_6])
                        elif self.field[y][x + x_count_6] > 0:
                            block_6 = True
                        elif self.field[y][x + x_count_6] < 0:
                            able.append([y, x + x_count_6])
                            block_6 = True
                    else:
                        block_6 = True

                block_7 = False
                y_count_7 = 0
                while block_7 is False:
                    y_count_7 += 1
                    if 0 <= y - y_count_7 <= 7:
                        if self.field[y - y_count_7][x] == 0:
                            able.append([y - y_count_7, x])
                        elif self.field[y - y_count_7][x] > 0:
                            block_7 = True
                        elif self.field[y - y_count_7][x] < 0:
                            able.append([y - y_count_7, x])
                            block_7 = True
                    else:
                        block_7 = True

                block_8 = False
                x_count_8 = 0
                while block_8 is False:
                    x_count_8 += 1
                    if 0 <= x - x_count_8 <= 7:
                        if self.field[y][x - x_count_8] == 0:
                            able.append([y, x - x_count_8])
                        elif self.field[y][x - x_count_8] > 0:
                            block_8 = True
                        elif self.field[y][x - x_count_8] < 0:
                            able.append([y, x - x_count_8])
                            block_8 = True
                    else:
                        block_8 = True

            #queen
            if self.field[self.selected[0]][self.selected[1]] == 5:

                block_1 = False
                x_count_1 = 0
                y_count_1 = 0
                while block_1 is False:
                    x_count_1 += 1
                    y_count_1 += 1
                    if 0 <= y - y_count_1 <= 7 and 0 <= x + x_count_1 <= 7:
                        if self.field[y - y_count_1][x + x_count_1] == 0:
                            able.append([y - y_count_1, x + x_count_1])
                        elif self.field[y - y_count_1][x + x_count_1] > 0:
                            block_1 = True
                        elif self.field[y - y_count_1][x + x_count_1] < 0:
                            able.append([y - y_count_1, x + x_count_1])
                            block_1 = True
                    else:
                        block_1 = True

                block_2 = False
                x_count_2 = 0
                y_count_2 = 0
                while block_2 is False:
                    x_count_2 += 1
                    y_count_2 += 1
                    if 0 <= y + y_count_2 <= 7 and 0 <= x + x_count_2 <= 7:
                        if self.field[y + y_count_2][x + x_count_2] == 0:
                            able.append([y + y_count_2, x + x_count_2])
                        elif self.field[y + y_count_2][x + x_count_2] > 0:
                            block_2 = True
                        elif self.field[y + y_count_2][x + x_count_2] < 0:
                            able.append([y + y_count_2, x + x_count_2])
                            block_2 = True
                    else:
                        block_2 = True

                block_3 = False
                x_count_3 = 0
                y_count_3 = 0
                while block_3 is False:
                    x_count_3 += 1
                    y_count_3 += 1
                    if 0 <= y + y_count_3 <= 7 and 0 <= x - x_count_3 <= 7:
                        if self.field[y + y_count_3][x - x_count_3] == 0:
                            able.append([y + y_count_3, x - x_count_3])
                        elif self.field[y + y_count_3][x - x_count_3] > 0:
                            block_3 = True
                        elif self.field[y + y_count_3][x - x_count_3] < 0:
                            able.append([y + y_count_3, x - x_count_3])
                            block_3 = True
                    else:
                        block_3 = True

                block_4 = False
                x_count_4 = 0
                y_count_4 = 0
                while block_4 is False:
                    x_count_4 += 1
                    y_count_4 += 1
                    if 0 <= y - y_count_4 <= 7 and 0 <= x - x_count_4 <= 7:
                        if self.field[y - y_count_4][x - x_count_4] == 0:
                            able.append([y - y_count_4, x - x_count_4])
                        elif self.field[y - y_count_4][x - x_count_4] > 0:
                            block_4 = True
                        elif self.field[y - y_count_4][x - x_count_4] < 0:
                            able.append([y - y_count_4, x - x_count_4])
                            block_4 = True
                    else:
                        block_4 = True

                block_5 = False
                y_count_5 = 0
                while block_5 is False:
                    y_count_5 += 1
                    if 0 <= y + y_count_5 <= 7:
                        if self.field[y + y_count_5][x] == 0:
                            able.append([y + y_count_5, x])
                        elif self.field[y + y_count_5][x] > 0:
                            block_5 = True
                        elif self.field[y + y_count_5][x] < 0:
                            able.append([y + y_count_5, x])
                            block_5 = True
                    else:
                        block_5 = True

                block_6 = False
                x_count_6 = 0
                while block_6 is False:
                    x_count_6 += 1
                    if 0 <= x + x_count_6 <= 7:
                        if self.field[y][x + x_count_6] == 0:
                            able.append([y, x + x_count_6])
                        elif self.field[y][x + x_count_6] > 0:
                            block_6 = True
                        elif self.field[y][x + x_count_6] < 0:
                            able.append([y, x + x_count_6])
                            block_6 = True
                    else:
                        block_6 = True

                block_7 = False
                y_count_7 = 0
                while block_7 is False:
                    y_count_7 += 1
                    if 0 <= y - y_count_7 <= 7:
                        if self.field[y - y_count_7][x] == 0:
                            able.append([y - y_count_7, x])
                        elif self.field[y - y_count_7][x] > 0:
                            block_7 = True
                        elif self.field[y - y_count_7][x] < 0:
                            able.append([y - y_count_7, x])
                            block_7 = True
                    else:
                        block_7 = True

                block_8 = False
                x_count_8 = 0
                while block_8 is False:
                    x_count_8 += 1
                    if 0 <= x - x_count_8 <= 7:
                        if self.field[y][x - x_count_8] == 0:
                            able.append([y, x - x_count_8])
                        elif self.field[y][x - x_count_8] > 0:
                            block_8 = True
                        elif self.field[y][x - x_count_8] < 0:
                            able.append([y, x - x_count_8])
                            block_8 = True
                    else:
                        block_8 = True

            #king
            if self.field[self.selected[0]][self.selected[1]] == 6:

                if 0 <= y-1 <= 7:
                    if self.field[y-1][x] <= 0:
                        able.append([y-1, x])
                if 0 <= y-1 <= 7 and 0 <= x+1 <= 7:
                    if self.field[y-1][x+1] <= 0:
                        able.append([y-1, x+1])
                if 0 <= x+1 <= 7:
                    if self.field[y][x+1] <= 0:
                        able.append([y, x+1])
                if 0 <= y+1 <= 7 and 0 <= x+1 <= 7:
                    if self.field[y+1][x+1] <= 0:
                        able.append([y+1, x+1])
                if 0 <= y+1 <= 7:
                    if self.field[y+1][x] <= 0:
                        able.append([y+1, x])
                if 0 <= y+1 <= 7 and 0 <= x-1 <= 7:
                    if self.field[y+1][x-1] <= 0:
                        able.append([y+1, x-2])
                if 0 <= x-1 <= 7:
                    if self.field[y][x-1] <= 0:
                        able.append([y, x-1])
                if 0 <= y-1 <= 7 and 0 <= x-1 <= 7:
                    if self.field[y-1][x-1] <= 0:
                        able.append([y-1, x-1])

            if [row,col] in able:
                self.field[row][col] = self.field[self.selected[0]][self.selected[1]]
                self.field[self.selected[0]][self.selected[1]] = 0
                self.screen.redraw(self.field)
                self.selected = None
                self.cur_player = False



        #흑 차례
        elif self.cur_player is False and self.field[row][col] < 0:
            self.selected = [row,col]
        elif self.cur_player is False and self.field[row][col] >= 0 and self.selected is not None:

            able = []
            x = self.selected[1]
            y = self.selected[0]

            # pawn
            if self.field[self.selected[0]][self.selected[1]] == -1:
                if y == 6:
                    for i in range(1, 3):
                        if self.field[y - i][x] == 0:
                            able.append([y - i, x])
                else:
                    if self.field[y - 1][x] == 0:
                        able.append([y - 1, x])
                if x > 1 and self.field[y - 1][x - 1] > 0:
                    able.append([y - 1, x - 1])
                if x < 7 and self.field[y - 1][x + 1] > 0:
                    able.append([y - 1, x + 1])

            # knight
            if self.field[self.selected[0]][self.selected[1]] == -2:
                if 0 <= y - 2 <= 7 and 0 <= x + 1 <= 7:
                    if self.field[y - 2][x + 1] >= 0:
                        able.append([y - 2, x + 1])
                if 0 <= y - 1 <= 7 and 0 <= x + 2 <= 7:
                    if self.field[y - 1][x + 2] >= 0:
                        able.append([y - 1, x + 2])
                if 0 <= y + 1 <= 7 and 0 <= x + 2 <= 7:
                    if self.field[y + 1][x + 2] >= 0:
                        able.append([y + 1, x + 2])
                if 0 <= y + 2 <= 7 and 0 <= x + 1 <= 7:
                    if self.field[y + 2][x + 1] >= 0:
                        able.append([y + 2, x + 1])
                if 0 <= y + 2 <= 7 and 0 <= x - 1 <= 7:
                    if self.field[y + 2][x - 1] >= 0:
                        able.append([y + 2, x - 1])
                if 0 <= y + 1 <= 7 and 0 <= x - 2 <= 7:
                    if self.field[y + 1][x - 2] >= 0:
                        able.append([y + 1, x - 2])
                if 0 <= y - 1 <= 7 and 0 <= x - 2 <= 7:
                    if self.field[y - 1][x - 2] >= 0:
                        able.append([y - 1, x - 2])
                if 0 <= y - 2 <= 7 and 0 <= x - 1 <= 7:
                    if self.field[y - 2][x - 1] >= 0:
                        able.append([y - 2, x - 1])


            # bishop
            if self.field[self.selected[0]][self.selected[1]] == -3:
                block_1 = False
                x_count_1 = 0
                y_count_1 = 0
                while block_1 is False:
                    x_count_1 += 1
                    y_count_1 += 1
                    if 0 <= y - y_count_1 <= 7 and 0 <= x + x_count_1 <= 7:
                        if self.field[y - y_count_1][x + x_count_1] == 0:
                            able.append([y - y_count_1, x + x_count_1])
                        elif self.field[y - y_count_1][x + x_count_1] < 0:
                            block_1 = True
                        elif self.field[y - y_count_1][x + x_count_1] > 0:
                            able.append([y - y_count_1, x + x_count_1])
                            block_1 = True
                    else:
                        block_1 = True

                block_2 = False
                x_count_2 = 0
                y_count_2 = 0
                while block_2 is False:
                    x_count_2 += 1
                    y_count_2 += 1
                    if 0 <= y + y_count_2 <= 7 and 0 <= x + x_count_2 <= 7:
                        if self.field[y + y_count_2][x + x_count_2] == 0:
                            able.append([y + y_count_2, x + x_count_2])
                        elif self.field[y + y_count_2][x + x_count_2] < 0:
                            block_2 = True
                        elif self.field[y + y_count_2][x + x_count_2] > 0:
                            able.append([y + y_count_2, x + x_count_2])
                            block_2 = True
                    else:
                        block_2 = True

                block_3 = False
                x_count_3 = 0
                y_count_3 = 0
                while block_3 is False:
                    x_count_3 += 1
                    y_count_3 += 1
                    if 0 <= y + y_count_3 <= 7 and 0 <= x - x_count_3 <= 7:
                        if self.field[y + y_count_3][x - x_count_3] == 0:
                            able.append([y + y_count_3, x - x_count_3])
                        elif self.field[y + y_count_3][x - x_count_3] < 0:
                            block_3 = True
                        elif self.field[y + y_count_3][x - x_count_3] > 0:
                            able.append([y + y_count_3, x - x_count_3])
                            block_3 = True
                    else:
                        block_3 = True

                block_4 = False
                x_count_4 = 0
                y_count_4 = 0
                while block_4 is False:
                    x_count_4 += 1
                    y_count_4 += 1
                    if 0 <= y - y_count_4 <= 7 and 0 <= x - x_count_4 <= 7:
                        if self.field[y - y_count_4][x - x_count_4] == 0:
                            able.append([y - y_count_4, x - x_count_4])
                        elif self.field[y - y_count_4][x - x_count_4] < 0:
                            block_4 = True
                        elif self.field[y - y_count_4][x - x_count_4] > 0:
                            able.append([y - y_count_4, x - x_count_4])
                            block_4 = True
                    else:
                        block_4 = True

            # rook
            if self.field[self.selected[0]][self.selected[1]] == -4:

                block_5 = False
                y_count_5 = 0
                while block_5 is False:
                    y_count_5 += 1
                    if 0 <= y + y_count_5 <= 7:
                        if self.field[y + y_count_5][x] == 0:
                            able.append([y + y_count_5, x])
                        elif self.field[y + y_count_5][x] < 0:
                            block_5 = True
                        elif self.field[y + y_count_5][x] > 0:
                            able.append([y + y_count_5, x])
                            block_5 = True
                    else:
                        block_5 = True

                block_6 = False
                x_count_6 = 0
                while block_6 is False:
                    x_count_6 += 1
                    if 0 <= x + x_count_6 <= 7:
                        if self.field[y][x + x_count_6] == 0:
                            able.append([y, x + x_count_6])
                        elif self.field[y][x + x_count_6] < 0:
                            block_6 = True
                        elif self.field[y][x + x_count_6] > 0:
                            able.append([y, x + x_count_6])
                            block_6 = True
                    else:
                        block_6 = True

                block_7 = False
                y_count_7 = 0
                while block_7 is False:
                    y_count_7 += 1
                    if 0 <= y - y_count_7 <= 7:
                        if self.field[y - y_count_7][x] == 0:
                            able.append([y - y_count_7, x])
                        elif self.field[y - y_count_7][x] < 0:
                            block_7 = True
                        elif self.field[y - y_count_7][x] > 0:
                            able.append([y - y_count_7, x])
                            block_7 = True
                    else:
                        block_7 = True

                block_8 = False
                x_count_8 = 0
                while block_8 is False:
                    x_count_8 += 1
                    if 0 <= x - x_count_8 <= 7:
                        if self.field[y][x - x_count_8] == 0:
                            able.append([y, x - x_count_8])
                        elif self.field[y][x - x_count_8] < 0:
                            block_8 = True
                        elif self.field[y][x - x_count_8] > 0:
                            able.append([y, x - x_count_8])
                            block_8 = True
                    else:
                        block_8 = True

            #queen
            if self.field[self.selected[0]][self.selected[1]] == -5:

                block_1 = False
                x_count_1 = 0
                y_count_1 = 0
                while block_1 is False:
                    x_count_1 += 1
                    y_count_1 += 1
                    if 0 <= y - y_count_1 <= 7 and 0 <= x + x_count_1 <= 7:
                        if self.field[y - y_count_1][x + x_count_1] == 0:
                            able.append([y - y_count_1, x + x_count_1])
                        elif self.field[y - y_count_1][x + x_count_1] < 0:
                            block_1 = True
                        elif self.field[y - y_count_1][x + x_count_1] > 0:
                            able.append([y - y_count_1, x + x_count_1])
                            block_1 = True
                    else:
                        block_1 = True

                block_2 = False
                x_count_2 = 0
                y_count_2 = 0
                while block_2 is False:
                    x_count_2 += 1
                    y_count_2 += 1
                    if 0 <= y + y_count_2 <= 7 and 0 <= x + x_count_2 <= 7:
                        if self.field[y + y_count_2][x + x_count_2] == 0:
                            able.append([y + y_count_2, x + x_count_2])
                        elif self.field[y + y_count_2][x + x_count_2] < 0:
                            block_2 = True
                        elif self.field[y + y_count_2][x + x_count_2] > 0:
                            able.append([y + y_count_2, x + x_count_2])
                            block_2 = True
                    else:
                        block_2 = True

                block_3 = False
                x_count_3 = 0
                y_count_3 = 0
                while block_3 is False:
                    x_count_3 += 1
                    y_count_3 += 1
                    if 0 <= y + y_count_3 <= 7 and 0 <= x - x_count_3 <= 7:
                        if self.field[y + y_count_3][x - x_count_3] == 0:
                            able.append([y + y_count_3, x - x_count_3])
                        elif self.field[y + y_count_3][x - x_count_3] < 0:
                            block_3 = True
                        elif self.field[y + y_count_3][x - x_count_3] > 0:
                            able.append([y + y_count_3, x - x_count_3])
                            block_3 = True
                    else:
                        block_3 = True

                block_4 = False
                x_count_4 = 0
                y_count_4 = 0
                while block_4 is False:
                    x_count_4 += 1
                    y_count_4 += 1
                    if 0 <= y - y_count_4 <= 7 and 0 <= x - x_count_4 <= 7:
                        if self.field[y - y_count_4][x - x_count_4] == 0:
                            able.append([y - y_count_4, x - x_count_4])
                        elif self.field[y - y_count_4][x - x_count_4] < 0:
                            block_4 = True
                        elif self.field[y - y_count_4][x - x_count_4] > 0:
                            able.append([y - y_count_4, x - x_count_4])
                            block_4 = True
                    else:
                        block_4 = True

                block_5 = False
                y_count_5 = 0
                while block_5 is False:
                    y_count_5 += 1
                    if 0 <= y + y_count_5 <= 7:
                        if self.field[y + y_count_5][x] == 0:
                            able.append([y + y_count_5, x])
                        elif self.field[y + y_count_5][x] < 0:
                            block_5 = True
                        elif self.field[y + y_count_5][x] > 0:
                            able.append([y + y_count_5, x])
                            block_5 = True
                    else:
                        block_5 = True

                block_6 = False
                x_count_6 = 0
                while block_6 is False:
                    x_count_6 += 1
                    if 0 <= x + x_count_6 <= 7:
                        if self.field[y][x + x_count_6] == 0:
                            able.append([y, x + x_count_6])
                        elif self.field[y][x + x_count_6] < 0:
                            block_6 = True
                        elif self.field[y][x + x_count_6] > 0:
                            able.append([y, x + x_count_6])
                            block_6 = True
                    else:
                        block_6 = True

                block_7 = False
                y_count_7 = 0
                while block_7 is False:
                    y_count_7 += 1
                    if 0 <= y - y_count_7 <= 7:
                        if self.field[y - y_count_7][x] == 0:
                            able.append([y - y_count_7, x])
                        elif self.field[y - y_count_7][x] < 0:
                            block_7 = True
                        elif self.field[y - y_count_7][x] > 0:
                            able.append([y - y_count_7, x])
                            block_7 = True
                    else:
                        block_7 = True

                block_8 = False
                x_count_8 = 0
                while block_8 is False:
                    x_count_8 += 1
                    if 0 <= x - x_count_8 <= 7:
                        if self.field[y][x - x_count_8] == 0:
                            able.append([y, x - x_count_8])
                        elif self.field[y][x - x_count_8] < 0:
                            block_8 = True
                        elif self.field[y][x - x_count_8] > 0:
                            able.append([y, x - x_count_8])
                            block_8 = True
                    else:
                        block_8 = True

            # king
            if self.field[self.selected[0]][self.selected[1]] == -6:
                if 0 <= y - 1 <= 7:
                    if self.field[y - 1][x] >= 0:
                        able.append([y - 1, x])
                if 0 <= y - 1 <= 7 and 0 <= x + 1 <= 7:
                    if self.field[y - 1][x + 1] >= 0:
                        able.append([y - 1, x + 1])
                if 0 <= x + 1 <= 7:
                    if self.field[y][x + 1] >= 0:
                        able.append([y, x + 1])
                if 0 <= y + 1 <= 7 and 0 <= x + 1 <= 7:
                    if self.field[y + 1][x + 1] >= 0:
                        able.append([y + 1, x + 1])
                if 0 <= y + 1 <= 7:
                    if self.field[y + 1][x] >= 0:
                        able.append([y + 1, x])
                if 0 <= y + 1 <= 7 and 0 <= x - 1 <= 7:
                    if self.field[y + 1][x - 1] >= 0:
                        able.append([y + 1, x - 2])
                if 0 <= x - 1 <= 7:
                    if self.field[y][x - 1] >= 0:
                        able.append([y, x - 1])
                if 0 <= y - 1 <= 7 and 0 <= x - 1 <= 7:
                    if self.field[y - 1][x - 1] >= 0:
                        able.append([y - 1, x - 1])

            if [row,col] in able:
                self.field[row][col] = self.field[self.selected[0]][self.selected[1]]
                self.field[self.selected[0]][self.selected[1]] = 0
                self.screen.redraw(self.field)
                self.selected = None
                self.cur_player = True


        #self.print_field()


        #안약에 흰색 차례인데 흰색의 말을 선택하면 그말로 선택
        #안약에 흰색 차례인데 비어진 공간을 선택하면 선택된 말을 놓고 다음 사람으로 턴 변경

