from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_movement = 10
        self.y_movement = 10
        self.ball_speed = 0.1

    def move_(self):
        refresh_x = self.xcor() + self.x_movement
        refresh_y = self.ycor() + self.y_movement
        self.goto(refresh_x, refresh_y)

    def refresh(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.rebound_x()

    def rebound_x(self):
        self.x_movement *= -1
        self.ball_speed *= 0.9

    def rebound_y(self):
        self.y_movement *= -1
