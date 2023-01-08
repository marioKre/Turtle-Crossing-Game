from turtle import Turtle
import random

# Set up colors of the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Moving speed of cars on first level
STARTING_MOVE_DISTANCE = 5
# Moving speed increment for higher levels
MOVE_INCREMENT = 10


# Creating a class for moving cars
class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Car spawn with 1/6 chance, coloring and positioning the cars
    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_len=2)
            new_car.setheading(180)
            new_car.goto(x=300, y=random.choice(range(-250, 250)))
            self.cars.append(new_car)

    # Move every spawned car with starting speed
    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    # Speed up cars by leveling up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
