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


class Score(Turtle):
    def __init__(self, score: int):
        super().__init__()
        self.score = score
        self.score_display()
    
    def score_display(self):
        self.penup()
        self.color("white")
        self.goto(550, 300)
        self.write(f"Score: {self.score}", align="right", font=("Courier", 16, "bold"))
        self.hideturtle()