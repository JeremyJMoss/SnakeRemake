from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_scoreboard()
        self.goto(0, 250)
        self.hideturtle()
        self.pencolor("white")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 14, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! Final Score: {self.score}", align="center", font=("Courier", 20, "normal"))
