from turtle import Turtle
INITIAL = (0, -250)
END = (0, 250)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(stretch_len=1.1, stretch_wid=1.1)
        self.penup()
        self.goto(INITIAL)
        self.setheading(90)

    def move(self):
        y = self.ycor()
        self.sety(y+10)