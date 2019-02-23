import turtle


class Rectangle(object):
    """
    Rectangle object.

    Args:
        x (int): x coordinate of bottom left corner
        y (int): y coordinate of bottom left corner
        height (int): height
        width (int): width

    Attributes:
        x (int): x coordinate of the bottom left corner
        y (int): y coordinate of the bottom left corner
        height (int): height
        width (int): width
        bottom_left (tupple): bottom left edge coordinates
        bottom_right (tuple): bottom right edge coordinates
        top_left (tuple): top left edge coordinates
        top_right (tuple): top right edge coordinates
    """
    def __init__(self, x=0, y=0, height=0, width=0):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.bottom_left = (self.x, self.y)
        self.bottom_right = None
        self.top_left = None
        self.top_right = None

    def setpos(self, x, y):
        """
        Set pen position in arbitrary position

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        turtle.setheading(0)
        turtle.penup()
        turtle.setpos(x, y)
        turtle.pendown()

    def color(self, color="black"):
        """ Set pen color for drawing
        
        Args:
            color (str): color string.
        """
        self.color = color
        turtle.color(color)
            
    def draw(self):
        """ Draw a rectangle """
        self.setpos(self.x, self.y)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        
        self.bottom_right = (self.x + self.width, self.y)
        self.top_left = (self.x, self.y + self.height)
        self.top_right = (self.x + self.width, self.y + self.height)

    def draw_right(self, angle):
        """
        Draw a rectangle rotated right

        Args:
            angle (int): angle of rotation
        """
        self.setpos(self.x, self.y)
        turtle.forward(self.width)
        x, y = map(int, turtle.pos())
        self.bottom_right = (x, y)
        
        turtle.left(90 - angle)
        turtle.forward(self.height)
        x, y = map(int, turtle.pos())
        self.top_right = (x, y)

        turtle.left(90 + angle)
        turtle.forward(self.width)
        x, y = map(int, turtle.pos())
        self.top_left = (x, y)
        
        turtle.left(90 - angle)
        turtle.forward(self.height)

    def corners(self):
        """ Returns a list of four edges of a rectangle """
        return [self.bottom_left, self.bottom_right,
                self.top_left, self.top_right]

    def erase(self, p1, p2):
        """
        Erase line from p1 to p2.

        Args:
            p1 (tupple): point (x, y)
            p2 (tupple): point (x, y)
            bgcolor (str): background color name string
        """
        x, y = turtle.pos()
        color = turtle.color()[0]
        heading = turtle.heading()

        x1, y1 = p1
        x2, y2 = p2

        turtle.penup()
        turtle.setpos(x1, y1)
        turtle.pendown()
        turtle.color(turtle.bgcolor())
        turtle.setheading(turtle.towards(x2, y2))
        turtle.forward(turtle.distance(x2, y2))

        turtle.penup()
        turtle.setpos(x, y)
        turtle.color(color)
        turtle.pendown()
