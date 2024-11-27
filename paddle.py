from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.start_pos = start_pos
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.setposition(self.start_pos)

    def right_movement(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def left_movement(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())
