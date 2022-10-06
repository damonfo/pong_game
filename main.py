

# Create another paddle
# Create the ball and make it move


# Detect when paddle misses
# keep score


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


# Create the screen
turtle = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle

screen.exitonclick()