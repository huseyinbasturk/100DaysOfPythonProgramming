# import turtle
# import random
#
# # Set up the turtle
# screen = turtle.Screen()
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
# # Function for random walk
# def random_walk(steps, step_size):
#     for _ in range(steps):
#         my_turtle.color(random_color())
#         my_turtle.forward(step_size)
#         turn_angle = random.choice([0, 90, 180, 270])  # Randomly choose one of the four cardinal directions
#         my_turtle.right(turn_angle)
#
# # Perform the random walk
# random_walk(200, 20)  # 200 steps, each of size 20
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
    random_color = (r, g, b)
    return random_color

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
   # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
