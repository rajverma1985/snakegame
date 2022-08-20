from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score={self.score} | High Score={self.high_score}", False, font=('Courier', 20, 'normal'),
                   align="center")

    def keep_score(self):
        self.score += 1
        self.h_score()
        self.update_score()

    def h_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def game_over(self):
        self.score = 0
        self.update_score()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, font=('Courier', 20, 'bold'), align="center")

    def restart(self):
        self.goto(-220, 280)
        self.write(f"RESTART GAME", False, font=('Courier', 20, 'bold'), align="center")

    def exit(self):
        self.goto(250, 280)
        self.write(f"EXIT", False, font=('Courier', 20, 'bold'), align="center")



