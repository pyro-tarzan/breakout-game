from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=.5, stretch_len=8)
        self.penup()
        self.goto(0, 40 - height // 2)

    def move_left(self):
        if self.xcor() > -self.width // 2 + 80:
            self.setx(self.xcor() - 20)

    def move_right(self):
        if self.xcor() < self.width // 2 - 80:
            self.setx(self.xcor() + 20)