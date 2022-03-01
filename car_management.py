
from turtle import Turtle
import random
COLORS = ["red", 'blue', 'green', 'yellow', 'pink', 'black', 'orange', 'purple']
SPEED = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = SPEED

    def create(self):
        if random.randint(1, 8) == 5:
            car = Turtle('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            y = random.randint(-210, 210)
            car.goto(300, y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5

