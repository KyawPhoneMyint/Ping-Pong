from turtle import Screen,Turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pingpong")
screen.listen()
screen.tracer(0)
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_on=True
scoreboard = ScoreBoard()
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    scoreboard.update()

    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_paddle()

    if ball.xcor()>380:
        ball.go_home()
        scoreboard.increase_l_score()

    if ball.xcor()<-380:
        ball.go_home()
        scoreboard.increase_r_score()

screen.exitonclick()