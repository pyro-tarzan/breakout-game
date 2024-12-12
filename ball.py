from turtle import Turtle

class Ball(Turtle):
    def __init__(self, height: int):
        super().__init__()
        self.height = height
        self.shape("circle")
        self.color("white")
        self.shapesize(.5, .5, None)
        self.penup()
        self.goto(0, 60 - height // 2)
        self.set_x = 10
        self.set_y = 10
        self.bounced = False

    def move(self):
        new_x = self.xcor() + self.set_x
        new_y = self.ycor() + self.set_y
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.set_y *= -1
        self.bounced = True
    
    def bounce_x(self):
        self.set_x *= -1

    def stop(self):
        self.setx(self.set_x)
        self.sety(self.set_y)

    def reset_bounce(self):
        self.bounced = False