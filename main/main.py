# create snake body 3 squares
# move the snake forward and direction changes
# control the snake(up, left, down , right)
# detect food with food
# create a scoreboard
# detect food with walls
# detect food with tail
from turtle import Screen
import time
from snake.body import Snake
from food.dot import Dot
from score.scoreboard import ScoreBoard

## code for the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
dot = Dot()
score = ScoreBoard()

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
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    elif snake.head.distance(dot) < 15:
        score.keep_score()
        dot.move()

screen.exitonclick()
