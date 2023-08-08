from turtle import  Screen
from paddle_class import Paddle
from Ball_class import Ball
import time
from score import Score
from design import Dots

# Importing the screen and defining it's functionalities
screen = Screen()
screen.title("The Pong Game | o |")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-350, 0), "yellow")
right_paddle = Paddle((350, 0), "blue")
ball = Ball()
score = Score("green")
dots = Dots()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "a")

Game_on = True
while Game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_yaxis()
    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_xaxis()

    elif ball.xcor() > 380:
        ball.reset()
        score.score_left()

    # Detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() > -330:
        ball.bounce_xaxis()

    elif ball.xcor() < -380:
        ball.reset()
        score.score_right()

screen.exitonclick()
