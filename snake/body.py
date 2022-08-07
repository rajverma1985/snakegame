from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            snake_seg = Turtle("square")
            snake_seg.color("white")
            snake_seg.penup()
            snake_seg.goto(pos)
            self.segments.append(snake_seg)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.segments[0].setheading(0)




