# import turtle
# import random
#
# # Set up the turtle
# screen = turtle.Screen()
# screen.bgcolor("white")
# my_turtle = turtle.Turtle()
# my_turtle.speed('fastest')
#
# # Function to pick a random color
# def random_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     return (R, G, B)
#
# # Function to draw a spirograph
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         my_turtle.color(random_color())
#         my_turtle.circle(100)  # Radius of each circle
#         my_turtle.setheading(my_turtle.heading() + size_of_gap)
#
# # Draw the spirograph
# draw_spirograph(5)  # Size of gap in degrees between each circle
#
# # Finish drawing
# screen.mainloop()

import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
