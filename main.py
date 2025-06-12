import turtle as turtle_module
import os
import time
from snake import Snake_class
from food import Food
from Scorecard import Scorecard
from collision import Collision

os.environ['TCL_LIBRARY'] = r"C:\Users\archi\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"

screen = turtle_module.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
blocks = []
snake1 = Snake_class()
food = Food()
scorecard = Scorecard()
screen.listen()
screen.onkey(snake1.move_up,    "w")
screen.onkey(snake1.move_down,  "s")
screen.onkey(snake1.move_left,  "a")
screen.onkey(snake1.move_right, "d")
game_is_on = True

while game_is_on:
    screen.update()
    snake1.move_snake()
    for i in range(3,len(snake1.blocks)):
        if snake1.blocks[0].distance(snake1.blocks[i]) <20:
            col = Collision()
            game_is_on = False

    if snake1.blocks[0].distance(food) <15: #(SO BASICALLY THE DISTANCE FROM CENTER OF THE SQUARE TO THE OUTWARD EDGE(FACING THE FOOD) IS 10/2 AND THE RADIUS OF FOOD IS 10/2 = 5 HENCE 10+5 = 15 , IF THE DISTANCE IS 15 OR LESSER THAN 15 THEN COLLISION HAS OCCURED WOOO)
        food.refresh_on_collision()
        snake1.add_block()
        scorecard.increase()


    time.sleep(0.1)
    if snake1.blocks[0].xcor() > 300 or snake1.blocks[0].xcor() < -300 or snake1.blocks[0].ycor() > 300 or  snake1.blocks[0].ycor() < -300:

        col2 = Collision()
        game_is_on = False


screen.exitonclick()