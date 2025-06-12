from turtle import Turtle
class Collision(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

