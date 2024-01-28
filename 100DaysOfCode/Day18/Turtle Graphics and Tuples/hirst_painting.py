# import colorgram
#
# rgb_colors = []
# colours = colorgram.extract('image.jpg', 30)
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors = [(138, 78, 52), (49, 26, 23), (41, 78, 183), (226, 237, 248), (196, 158, 118), (80, 234, 202), (66, 200, 226), (237, 169, 164), (240, 16, 16), (174, 178, 231), (224, 19, 119), (27, 40, 156), (81, 80, 213), (238, 227, 5), (248, 236, 31), (63, 233, 242), (222, 248, 240), (225, 138, 205), (238, 156, 218), (19, 150, 23), (222, 78, 50), (11, 226, 238), (6, 245, 223), (10, 79, 111), (239, 41, 154), (249, 223, 239), (18, 20, 44), (39, 213, 68), (195, 15, 11)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()