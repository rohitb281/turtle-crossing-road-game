from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_generate(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(310, random.randint(-260, 260))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
