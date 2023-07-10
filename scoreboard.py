from turtle import Turtle
from typing import Tuple

ALINGMENT = "center"
FONT: tuple[str, int, str] = ('Arial', 20, 'normal')
with open("data.txt") as f:
    high_score = f.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0

        self.high_score = int(high_score)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align=ALINGMENT, arg=f"Score: {self.score} High Score: {self.high_score}", move=False, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def track_score(self):
        self.score += 1
        self.update_scoreboard()
