from turtle import Turtle

STYLE = ('Courier', 50, 'bold')
POSITION = (0, 250)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        self.goto(POSITION)
        self.write(arg=f'Score: {self.score}', font=STYLE, align='center')

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.increase_score()
        self.clear()
        self.write(arg=f'Score: {self.score}', font=STYLE, align='center')

    def out_of_play(self):
        self.goto(x=0, y=0)
        self.write('OUT OF PLAY.', align='center', font=STYLE)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write('GAME OVER.', align='center', font=STYLE)

    def win(self):
        self.goto(x=0, y=0)
        self.write('YOU WIN.', align='center', font=STYLE)
