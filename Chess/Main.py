import turtle
from Control import Control
from Screen import Screen
if __name__ == '__main__':
    screen = Screen()
    screen.board()
    control = Control(screen)

    turtle.mainloop()
