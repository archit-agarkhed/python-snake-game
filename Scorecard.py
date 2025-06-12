from turtle import Turtle
class Scorecard(Turtle):
    def __init__(self):
        self.counter = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-20,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.counter}", align="center", font=("Arial", 24, "bold"))

    def increase(self):
        self.counter += 1
        self.update_score()

