import turtle as turtle_module
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake_class:
    def __init__(self):
        self.blocks = []
        self.create_snake()

    def create_snake(self):
        x = -10
        for i in range(3):
            timmy = turtle_module.Turtle()
            timmy.shape("square")
            timmy.color("red")
            timmy.penup()
            timmy.goto(x, -10)
            x = x - 20
            self.blocks.append(timmy)

    def move_snake(self):
        for i in range(len(self.blocks) - 1, 0, -1):  # we are going in a reverse order remember that
            x_cor = self.blocks[i - 1].xcor()
            y_cor = self.blocks[i - 1].ycor()
            self.blocks[i].goto(x_cor, y_cor)
        self.blocks[0].forward(20)

    def move_up(self):
        if self.blocks[0].heading()!=DOWN:
            self.blocks[0].setheading(90)

    def move_down(self):
        if self.blocks[0].heading()!=UP:
            self.blocks[0].setheading(270)

    def move_left(self):
        if self.blocks[0].heading()!=RIGHT:
            self.blocks[0].setheading(180)

    def move_right(self):
        if self.blocks[0].heading()!=LEFT:
            self.blocks[0].setheading(0)

    def add_block(self):
        new_block = self.blocks[-1]
        timmy2 = turtle_module.Turtle()
        timmy2.shape("square")
        timmy2.color("red")
        timmy2.penup()
        timmy2.goto(new_block.xcor() , new_block.ycor())
        self.blocks.append(timmy2)





