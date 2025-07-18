from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,-100)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)

    def create_new_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()