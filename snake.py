from turtle import Turtle

STARTING_POSITONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
        This class represents a snake in a turtle graphics game.

        Attributes:
            color (str): Color of the snake segments.
            shape (str): Shape of the snake segments.

        Methods:
            create_turtle_obj(x, y): Create a turtle object with the specified coordinates.
            create_snake(): Create and return a list of turtle segments to form the snake.
            move(): Move the snake by updating the positions of its segments.

        """

    def __init__(self, color="white", shape="square"):
        """
                Initializes a new instance of the Snake class.

                Args:

                    color (str, optional): Color of the snake segments.
                    shape (str, optional): Shape of the snake segments.

                """

        self.color = color
        self.shape = shape
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_turtle_obj(self, position):
        """
                Creates a turtle object with the specified coordinates.

                Args:
                    x (int): X-coordinate for the turtle object.
                    y (int): Y-coordinate for the turtle object.

                Returns:
                    Turtle: The created turtle object.

                """
        name = Turtle(self.shape)
        name.penup()
        name.goto(position)
        name.color(self.color)
        return name

    def create_snake(self):
        """
                Creates and returns a list of turtle segments to form the snake.

                Returns:
                    list: The list of turtle segments.

                """

        for position in STARTING_POSITONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = self.create_turtle_obj(position)

        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000) # it will disappear
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(position=self.segments[-1].position()) # adding new segment to last segment position

    def move(self):
        """
               Moves the snake by updating the positions of its segments.

               The segments are moved from the tail to the head, where each segment takes the position
               of the segment ahead of it. Finally, the head segment is moved forward.

               """

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Change the snake's heading to "up" (north) if it's currently moving horizontally.

        The snake can only change its direction vertically when its current heading is either 0 (east) or 180 (west).
        """
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        """
        Change the snake's heading to "down" (south) if it's currently moving horizontally.

        The snake can only change its direction vertically when its current heading is either 0 (east) or 180 (west).
        """
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        """
        Change the snake's heading to "left" (west) if it's currently moving vertically.

        The snake can only change its direction horizontally when its current heading is either 90 (north) or 270 (south).
        """
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        """
        Change the snake's heading to "right" (east) if it's currently moving vertically.

        The snake can only change its direction horizontally when its current heading is either 90 (north) or 270 (south).
        """
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
