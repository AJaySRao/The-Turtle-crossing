from turtle import Screen
from player import Player
import time
from car_management import CarManager
from scoreboard import ScoreBoard


s = Screen()
s.screensize(600, 600)
s.tracer(0)

p = Player()
s.listen()
s.onkey(p.move, 'w')

cars = CarManager()
score = ScoreBoard()

game = True

while game:
    time.sleep(0.1)
    s.update()
    cars.create()
    cars.move()

    # Player & Car collision
    for car in cars.cars:
        if car.distance(p) <= 25:
            score.game_over()
            game = False

    #Player reaches the other side
    if p.ycor() >= 280:
        score.refresh_level()
        cars.level_up()
        p.reposition()


s.exitonclick()