from turtle import Turtle

FONT = ("Courier", 24, "normal")


# Creating class for scoreboard used to show level
class Scoreboard(Turtle):

    # Defining attributes of scoreboard
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.goto(x=-200, y=260)
        self.hideturtle()
        self.update_scoreboard()

    # Write on scoreboard
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    # Change text while leveling up
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    # Game over actions
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
