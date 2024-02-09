# Day 20  : Programming is not about memorising
# Topics  : Animation and Coordinates
# Project : Python: A Snake Game


######################################## Code ############################################
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("white")
screen.title("Python: A Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
