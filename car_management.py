import imp
from turtle import Turtle
COLORS = 


class Car(Turtle):
    def __init__(self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.cars = []

    def create_cars(self):

