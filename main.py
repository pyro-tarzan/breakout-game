from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Block
import time

WIDTH = 1200
HEIGHT = 700

def start_game():
    # INITIALIZE SCREEN
    screen.clear()
    screen.title("Breakout")
    screen.bgcolor("black")
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)

    breakout = Turtle()
    breakout.penup()
    breakout.color("white")
    breakout.goto(0, 300)
    breakout.write("Breakout", align="center", font=("Courier", 26, "normal"))
    breakout.hideturtle()

    controls = Turtle()
    controls.penup()
    controls.color("white")
    controls.goto(0, 270)
    controls.write("\"Left\" or \"a\" to move paddle left. \"Right\" or \"d\" to move paddle right.", align="center", font=("Courier", 16, "normal"))
    controls.hideturtle()

    paddle = Paddle(WIDTH, HEIGHT)
    ball = Ball(HEIGHT)

    BLOCK_WIDTH = 55  # Width of each block
    BLOCK_HEIGHT = 25  # Height of each block
    ROWS = 9  # Number of rows
    COLS = 21  # Number of columns
    START_Y = 250  # Starting y-position for blocks
    START_X = -WIDTH // 2 + (BLOCK_WIDTH // 2)  # Starting x-position for blocks

    # Create blocks
    blocks = []
    for row in range(ROWS):
        for col in range(COLS):
            x_pos = START_X + col * BLOCK_WIDTH
            y_pos = START_Y - row * BLOCK_HEIGHT
            block = Block(x_pos, y_pos, row)
            blocks.append(block)

    # LISTEN SCREEN WITH EVENT LISTENER
    screen.listen()
    screen.onkey(paddle.move_left, "Left")
    screen.onkey(paddle.move_left, "a")
    screen.onkey(paddle.move_right, "Right")
    screen.onkey(paddle.move_right, "d")

    def continue_game():
        game_over.clear()
        query.clear()
        start_game()

    def exit_game():
        screen.bye()

    def game_loop():
        # UPDATE THE ANIMATION
        is_game_on = True
        while is_game_on:
            time.sleep(0.05)
            screen.update()
            ball.move()

            if ball.ycor() + .25 > HEIGHT // 2:
                ball.bounce_y()
            
            if ball.xcor() + .25 > WIDTH // 2 or ball.xcor() - .25 < -WIDTH // 2:
                ball.bounce_x()

            if ball.ycor() - 10 < paddle.ycor() + 20: 
                if paddle.xcor() - 60 < ball.xcor() < paddle.xcor(): 
                    if not ball.bounced:
                        ball.bounce_y()
                        if ball.set_x > 0:
                            ball.set_x *= -1
                if paddle.xcor() < ball.xcor() < paddle.xcor() + 60:
                    if not ball.bounced:
                        ball.bounce_y()
                        if ball.set_x < 0:
                            ball.set_x *= -1
                    
            # Reset the bounce flag when the ball moves away from the paddle
            if ball.ycor() - 10 > paddle.ycor() + 20:
                ball.reset_bounce()

            for block in blocks[:]:
                if abs(ball.xcor() - block.xcor()) < 27.5 and abs(ball.ycor() - block.ycor()) < 12.5:
                    block.hideturtle()
                    blocks.remove(block)
                    ball.bounce_y()
                    break  # To avoid multiple collisions at once

            if ball.ycor() < -320:
                ball.stop()
                game_over.write("Game Over", align="center", font=("Courier", 24, "normal"))
                query.write("Press \"Y\" to continne the game or \"N\" to exit.", align="center", font=("Courier", 18, "normal"))

                screen.listen()
                screen.onkey(continue_game, "y")
                screen.onkey(exit_game, "n")
                is_game_on = False
        
    game_over = Turtle()
    game_over.penup()
    game_over.color("white")
    game_over.goto(0, -80)
    game_over.hideturtle()

    query = Turtle()
    query.penup()
    query.color("white")
    query.goto(0, -100)
    query.hideturtle()

    game_loop()

# MAIN
screen = Screen()

start_game()

screen.mainloop()
