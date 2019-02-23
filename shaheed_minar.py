#!/usr/bin/python

import turtle
from shapes import Rectangle
from pillar import Pillar


def mainPillar(x, y, bottom_height, top_height, width, thickness):
    # Draw bottom column 1
    col1 = Rectangle(x, y, bottom_height, thickness)
    col1.draw()

    # Draw bottom column 2
    x, y = col1.bottom_right
    col2 = Rectangle(x + width, y, bottom_height, thickness)
    col2.draw()
    
    # Draw rods inside col1 and col2
    roddist = width / 3
    x, y = col1.bottom_right
    draw_rods(x, y, bottom_height, roddist)
   
    # Draw bottom column 3
    x, y = col2.bottom_right
    col3 = Rectangle(x + width, y, bottom_height, thickness)
    col3.draw()
    
    # Draw rods inside col2 and col3
    x, y = col2.bottom_right
    draw_rods(x, y, bottom_height, roddist)

    x1, y1 = col1.top_left
    x2, y2 = col3.top_left

    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(turtle.distance(x2, y2))

    # Draw top column 1
    x, y = col1.top_left
    col4 = Rectangle(x, y, top_height, thickness)
    col4.draw_right(30)
    
    # Draw top column 2
    x, y = col2.top_left
    col5 = Rectangle(x, y, top_height, thickness)
    col5.draw_right(30)

    # Draw rods inside col4 and col5
    x, y = col4.bottom_right
    draw_rods(x, y, top_height, roddist, -30)
    
    # Draw top column 3
    x, y = col2.top_left
    x, y = col3.top_left
    col6 = Rectangle(x, y, top_height, thickness)
    col6.draw_right(30)
    
    # Draw rods inside col5 and col6
    x, y = col5.bottom_right
    draw_rods(x, y, top_height, roddist, -30)

    x, y = col4.top_left
    
    beam1 = Rectangle(x, y+1, thickness, width * 2 + 30)
    beam1.draw_right(30)
    
    # Remove intersection of coloumn 4 and beam 1
    x, y = beam1.bottom_left
    print((x, y))
    beam1.erase((x + 1, y), (x + thickness - 1, y))
   
    # Remove intersection of coloumn 5 and beam 1 
    x, y = col5.top_left
    print((x, y))
    beam1.erase((x + 1, y + 1), (x + thickness + 2, y))

    # Remove intersection of coloumn 5 and beam 1 
    x, y = col6.top_left
    print((x, y))
    beam1.erase((x + 1, y + 1), (x + thickness + 2, y))

    return col3.bottom_right

# Draws rods inside the pillars
def draw_rods(x, y, height, roddist, angle=0):
    turtle.penup()
    turtle.setpos(x + roddist, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(90+angle)
    turtle.forward(height)
    
    turtle.penup()
    turtle.setpos(x + (2 * roddist), y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(90+angle)
    turtle.forward(height)


if __name__ == "__main__":
    turtle.hideturtle()
    turtle.bgcolor("black")
    turtle.color("green")

    start_x = -280
    start_y = -150
    height = 100
    width = 60
    thickness = 10
    roddist = width / 3

    # Draw first small pillar
    p1 = Pillar(start_x, start_y, height, width, thickness)
    p1.draw()
    p1.prettify()
    draw_rods(start_x, start_y, height, roddist)
    
    # Draw second small pillar
    x, y = p1.far_right()
    
    p2 = Pillar(x + 20, y, height * 2, width, thickness)
    p2.draw()
    p2.prettify()

    # Draw rods inside second pillar
    x, y = p2.far_left()
    draw_rods(x, y, height * 2, roddist)

    # Draw main pillar
    x, y = p2.far_right()

    x, y = mainPillar(x + 20, y, height * 3, height, width + 20, thickness)
   
    # Draw third small pillar
    p3 = Pillar(x + 20, y, height * 2, width, thickness)
    p3.draw()
    p3.prettify()

    # Draw rods inside third pillar
    x, y = p3.far_left()
    draw_rods(x, y, height * 2, roddist)

    # Draw fourth small pillar
    x, y = p3.far_right()
    
    p4 = Pillar(x + 20, y, height, width, 10)
    p4.draw()
    p4.prettify()

    # Draw rods inside fourth small pillar
    x, y = p4.far_left()
    draw_rods(x, y, height, roddist)

    turtle.penup()
    turtle.setheading(0)
    turtle.setpos(-350, -150)
    turtle.pendown()
    turtle.forward(turtle.distance(350, -150))

    x = raw_input()
