import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# Create a screen with specific width and height
screen = Screen()
screen.setup(width=600, height=600)
# Automatic screen updates off
screen.tracer(0)

# Creating objects
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# Listening for key press
screen.listen()
screen.onkey(player.move, "Up")

# Running the game
game_is_on = True
while game_is_on:
    # Screen update and add cars
    time.sleep(0.05)
    screen.update()
    car_manager.add_car()
    car_manager.move_cars()

    # Detects distance between player and car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Level up if player reaches finish line
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

# Wait for the user to close the window
screen.exitonclick()
