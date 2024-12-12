from turtle import Screen, Turtle

WIDTH = 1200
HEIGHT = 700

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

class Paddle(Turtle):
    def __init__(self):
        super.__init__()
        self.color("white")
        self.shapesize(stretch_wid=.5, stretch_len=8)
        self.penup()
        self.goto(0, 40 - HEIGHT // 2)

    def move_left(self):
        if self.xcor() > -WIDTH // 2 + 80:
            self.setx(self.xcor() - 20)

    def move_right(self):
        if self.xcor() < WIDTH // 2 - 80:
            self.setx(self.xcor() + 20)
        
paddle = Paddle()

ball = Turtle("circle")
ball.color("white")
ball.shapesize(.5, .5, None)
ball.penup()
ball.goto(0, 52 - HEIGHT // 2)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_right, "d")

is_game_on = True
while is_game_on:
    screen.update()

screen.mainloop()
