from turtle import Turtle

# Positioning player
STARTING_POSITION = (0, -280)
# Player move speed
MOVE_DISTANCE = 15
# Y - coordinate for finish line
FINISH_LINE_Y = 280


# Creating class for player
class Player(Turtle):

    # Initializing attributes of a player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    # Define moving speed of a player
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Reset position of a player while leveling up
    def reset_position(self):
        self.goto(STARTING_POSITION)
