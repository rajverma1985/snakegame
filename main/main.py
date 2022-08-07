# create snake body 3 squares
# move the snake forward and direction changes
# control the snake(up, left, down , right)
# detect collision with food
# create a scoreboard
# detect collision with walls
# detect collision with tail
from turtle import Screen
import time
from snake.body import Snake

## code for the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()
