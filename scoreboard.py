from turtle import Turtle
with open("high_scores.txt") as high:
    contents = high.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.update_scoreboard()
        self.goto(0, 250)
        self.hideturtle()
        self.pencolor("white")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", mode="w") as high_scores:
                high_scores.write(str(self.high_score))
            self.score = 0
            self.update_scoreboard()
