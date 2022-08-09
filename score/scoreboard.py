from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score={self.score}", False, font=('Courier', 20, 'normal'), align="center")

    def keep_score(self):
        self.score += 1
        self.clear()
        self.update_score()
