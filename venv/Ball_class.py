from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x=x, y=y)
     
    def bounce_yaxis(self):
        # bounce down from up direction
        self.move_y *= -1

    def bounce_xaxis(self):
        # bounces on paddle
        self.move_x *= -1
        # increase the speed
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_xaxis()
        self.ball_speed = 0.1





