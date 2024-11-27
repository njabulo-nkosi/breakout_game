import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from gameboard import GameBoard
from scoreboard import ScoreBoard

DEFAULT_POS = (0, -300)

screen = Screen()
screen.title('BreakOut')
screen.bgcolor('black')
screen.setup(width=800, height=650)
screen.tracer(0)

paddle = Paddle(DEFAULT_POS)
ball = Ball()
gameboard = GameBoard()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.right_movement, 'Right')
screen.onkey(paddle.left_movement, 'Left')

game_on = True
PADDLE_Y_THRESHOLD = -270
PADDLE_WIDTH = 6 * 20
PADDLE_BUFFER = 5
while game_on:
    time.sleep(0.05)
    screen.update()

    ball.move_()

    # Paddle boundaries
    if paddle.xcor() > 350 or paddle.xcor() < -350:
        scoreboard.out_of_play()
        game_on = False

    # Ball boundary
    if ball.ycor() < -310:
        scoreboard.game_over()
        game_on = False

    # B)all rebound
    if ball.ycor() > 310:
        ball.rebound_y()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.rebound_x()

    # collision between ball and paddle
    # if ball.ycor() < -270 and (ball.xcor() - paddle.xcor()) < 50:
    #     print(f"Ball Y: {ball.ycor()}, Paddle X: {paddle.xcor()}, Ball X: {ball.xcor()}")
    #     ball.rebound_y()
    if (
            PADDLE_Y_THRESHOLD - PADDLE_BUFFER <= ball.ycor() <= PADDLE_Y_THRESHOLD + PADDLE_BUFFER
            and paddle.xcor() - (PADDLE_WIDTH / 2) <= ball.xcor() <= paddle.xcor() + (PADDLE_WIDTH / 2)
    ):
        ball.rebound_y()

    # Detect collision with bricks
    if gameboard.collision(ball):
        ball.rebound_y()
        scoreboard.update_score()
        print(len(gameboard.bricks))

    # Win cond
    if len(gameboard.bricks) == 0 and scoreboard.score == 60:
        scoreboard.win()
        game_on = False


screen.exitonclick()
