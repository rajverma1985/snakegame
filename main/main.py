from turtle import Screen
import time
from snake.body import Snake
from food.dot import Dot
from score.scoreboard import ScoreBoard

# code for the screen
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


def run_game():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            game_on = False
            score.game_over()
        elif snake.head.distance(dot) < 15:
            dot.move()
            snake.extend_seg()
            score.keep_score()
        # collision detection with tail
        for segs in snake.segments[1:]:
            if snake.head.distance(segs) < 8:
                game_on = False
                score.game_over()
    screen.exitonclick()


if __name__ == '__main__':
    run_game()
