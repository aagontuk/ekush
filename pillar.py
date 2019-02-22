from shapes import Rectangle


class Pillar(object):
    """
    Pillar object.

    A pillar is a complex shape composed
    of three rectangle. 2 columns and a beam. Example:

        2
     ________
     |______|
   1 | |  | | 3
     | |  | |
     | |  | |

    Args:
        x (int): x coordinate of the bottom left corner
                of the first pillar

        y (int): y coordinate of the bottom left corner
                of the first pillar

        height (int): height of the pillar

        width (int): width of the pillar

        thickness (int): Thickness of the pillar columns and beams
    """
    def __init__(self, x, y, height, width, thickness):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.thickness = thickness
        self.col1 = None
        self.beam2 = None
        self.col2 = None

    def draw(self):
        """ Draw pillar """
        self.col1 = Rectangle(self.x, self.y, self.height, self.thickness)
        self.col1.draw()

        x, y = self.col1.top_left
        self.beam1 = Rectangle(x, y, self.thickness, self.width)
        self.beam1.draw()

        x, y = self.col1.bottom_left
        x = x + self.width - self.thickness
        self.col2 = Rectangle(x, y, self.height, self.thickness)
        self.col2.draw()

    def far_left(self):
        """ Returns bottom left coordinate of the left column """
        return self.x, self.y

    def far_right(self):
        """ Returns bottom right coordinate of the right column """
        return self.col2.bottom_right

    def prettify(self):
        """
        Erase common section between left column and beam.
        And between right column and beam.
        """
        x1, y1 = self.beam1.bottom_left
        x2, y2 = x1 + self.thickness, y1
        self.beam1.erase((x1+1, y1), (x2 -1, y2))
        
        x1, y1 = self.beam1.bottom_right
        x2, y2 = x1 - self.thickness, y1
        self.beam1.erase((x2+1, y2), (x1 -1, y1))
