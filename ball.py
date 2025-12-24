from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.xmove=10
        self.ymove=10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed=0.1
        self.shapesize(stretch_wid=0.8,stretch_len=0.8)

    def move(self):
        new_x = self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove*=-1

    def bounce_paddle(self):
        self.xmove*=-1
        self.move_speed *= 0.9

    def go_home(self):
        self.home()
        self.move_speed=0.1