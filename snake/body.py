from turtle import Turtle

START_POS = [(0, 0), (-15, 0), (-30, 0)]
MOVE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def add_seg(self, pos):
        snake_seg = Turtle("square")
        snake_seg.color("white")
        snake_seg.shapesize(.75, .75)
        snake_seg.penup()
        snake_seg.goto(pos)
        self.segments.append(snake_seg)

    def extend_seg(self):
        # extending the snake and adding the turtle object at the end of the segments index.
        self.add_seg(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
