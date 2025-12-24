from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2,stretch_len=6)
        self.setheading(90)
        self.penup()
        self.goto(x,y)
        self.speed(5)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)