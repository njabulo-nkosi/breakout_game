import random
from turtle import Turtle

COLORS = ["#FFB200", "#EB5B00", "#D91656", "#640D5F"]
BRICK_WIDTH = 40
BRICK_HEIGHT = 10
START_X = -380
START_Y = 100
COLUMNS = 15
ROWS = 4
GAP_BTW_BRICKS = 15


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = START_X + (col * (BRICK_WIDTH + GAP_BTW_BRICKS))
                y = START_Y + (row * (BRICK_HEIGHT + 30))
                color = COLORS[row % len(COLORS)]
                self.add_bricks((x, y), color)

    def add_bricks(self, position, color):
        brick = Turtle()
        brick.shape('square')
        brick.color(color)
        brick.penup()
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.goto(position)
        self.bricks.append(brick)
        self.hideturtle()

    def collision(self, ball):
        bricks_to_remove = []
        collision = False
        for brick in self.bricks:
            if ball.distance(brick) < 20:
                self.explosion(brick)
                brick.clear()
                brick.hideturtle()
                bricks_to_remove.append(brick)
                collision = True

        for brick in bricks_to_remove:
            self.bricks.remove(brick)

        return collision

    def explosion(self, brick):
        explosion = Turtle()
        explosion.hideturtle()
        explosion.penup()
        explosion.goto(brick.position())
        explosion.color(random.choice(COLORS))
        explosion.write("BOOM!", align="center", font=("Arial", 16, "bold"))

        def clear_explosion():
            explosion.clear()
            explosion.hideturtle()

        explosion.getscreen().ontimer(clear_explosion, 100)
