from turtle import Screen
from player import Player
import time


s = Screen()
s.screensize(600, 500)
s.tracer(0)

p = Player()
s.listen()
s.onkey(p.move, 'w')

game = True

while game:
    time.sleep(0.1)
    s.update()


s.exitonclick()