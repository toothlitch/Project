from Tetris_Shape import Shape
from Control import Control
import turtle
import random

if __name__ == '__main__':
    tetris = Shape()
    tetris.setup()
    control = Control(tetris)
    turtle.mainloop()

