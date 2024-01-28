from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# My Solution
# num_sides = 3
# while num_sides < 10:
#     for _ in range(num_sides):
#         angle = 360 /num_sides
#         tim.forward(100)
#         tim.right(angle)
#     num_sides +=1


import turtle as t
import random



########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)






















screen = Screen()
screen.exitonclick()