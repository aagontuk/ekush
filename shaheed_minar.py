#!/usr/bin/python

import turtle
from shapes import Rectangle
from pillar import Pillar


def mainPillar(x, y, bottom_height, top_height, thickness):
    col1 = Rectangle(x, y, bottom_height, thickness)
    col1.draw()

    x, y = col1.bottom_right
    col2 = Rectangle(x + 80, y, bottom_height, thickness)
    col2.draw()
    
    x, y = col2.bottom_right
    col3 = Rectangle(x + 80, y, bottom_height, thickness)
    col3.draw()

    x1, y1 = col1.top_left
    x2, y2 = col3.top_left

    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(turtle.distance(x2, y2))

    x, y = col1.top_left
    col4 = Rectangle(x, y, top_height, thickness)
    col4.draw_right(30)
    
    x, y = col2.top_left
    col5 = Rectangle(x, y, top_height, thickness)
    col5.draw_right(30)
    
    x, y = col3.top_left
    col6 = Rectangle(x, y, top_height, thickness)
    col6.draw_right(30)

    x1, y1 = col4.top_right
    x2, y2 = col6.top_left
    
    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(turtle.distance(x2, y2))

    return col3.bottom_right


if __name__ == "__main__":
    turtle.hideturtle()
    turtle.color("green")

    p1 = Pillar(-280, -150, 100, 60, 10)
    p1.draw()
    p1.prettify()

    x, y = p1.far_right()
    
    p2 = Pillar(x + 20, y, 200, 60, 10)
    p2.draw()
    p2.prettify()

    x, y = p2.far_right()

    x, y = mainPillar(x + 20, y, 300, 100, 10)
    
    p3 = Pillar(x + 20, y, 200, 60, 10)
    p3.draw()
    p3.prettify()

    x, y = p3.far_right()
    
    p4 = Pillar(x + 20, y, 100, 60, 10)
    p4.draw()
    p4.prettify()

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(-350, -150)
    turtle.pendown()
    turtle.forward(turtle.distance(350, -150))

    x = raw_input()
