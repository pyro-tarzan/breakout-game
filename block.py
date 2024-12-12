from turtle import Turtle

class Block(Turtle):
    def __init__(self, x_pos: int, y_pos: int, color: int):
        super().__init__()
        self.shape("square")
        self.colors = ["red", "yellow", "lightgreen", "grey", "lightblue", "purple", "blue", "violet", "pink"]
        self.shapesize(1, 2.5, None)
        self.color(self.colors[color])
        self.penup()
        self.goto(x_pos, y_pos)
        