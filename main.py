from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  #to turn off animation
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

#keys for moving right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#keys for moving left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    #detect collision with top and bottom wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        #needs to bounce
        pong_ball.bounce_y()

    #detect collision with the paddles
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 330 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -330:
        pong_ball.bounce_x()


    #detect when a paddle misses
    elif pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    elif pong_ball.xcor() < - 380:
        pong_ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
