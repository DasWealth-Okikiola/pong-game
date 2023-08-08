from turtle import Turtle


class Dots(Turtle):

    def __init__(self):
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.shape("square")
        self.shapesize(1)
        self.penup()
        self.goto(x=0, y=-280)
        self.pendown()
        self.draw()
        self.house()


    def draw(self):
        # Crates a middle dotted lines that serves as border
        for _ in range(12):
            self.pendown()
            self.dot(size=8)
            x = self.xcor()
            y = self.ycor() + 40
            self.penup()
            self.goto(x=x, y=y)

    def house(self):
        self.penup()
        self.goto(0, -2)
        self.color("brown")
        self.pendown()
        self.circle(12)