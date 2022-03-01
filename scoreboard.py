from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level : {self.level}", align='center', font=('Retro Gaming', 18, 'normal'))

    def refresh_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"G A M E  O V E R", align='center', font=('Retro Gaming', 25, 'normal'))
