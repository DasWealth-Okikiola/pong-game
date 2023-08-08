from turtle import Turtle


class Score(Turtle):
    def __init__(self, color):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 80, "normal"))

        self.goto(0, 200)
        self.write(" : ", align="center", font=("courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 80, "normal"))

    def score_left(self):
        self.left_score += 1
        self.update_screen()

    def score_right(self):
        self.right_score += 1
        self.update_screen()