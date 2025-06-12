from turtle import Turtle
from snake import Snake_class
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5 , stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.x = random.randint(-280,280)
        self.y = random.randint(-280 , 280)
        self.goto(self.x , self.y)
    def refresh_on_collision(self):
        self.x = random.randint(-280,280)
        self.y = random.randint(-280,280)
        self.goto(self.x , self.y)


        
