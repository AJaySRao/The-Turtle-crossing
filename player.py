from turtle import Turtle
INITIAL = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.reposition()
        self.setheading(90)

    def move(self):
        self.forward(10)

    def reposition(self):
        self.goto(INITIAL)
