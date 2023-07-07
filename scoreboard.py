from turtle import Turtle
from typing import Tuple

ALINGMENT = "center"
FONT: tuple[str, int, str] = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(align=ALINGMENT, arg=f"Score: {self.score}", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALINGMENT, font=FONT)

    def track_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
