import turtle
import random
# extract colours
# import colorgram
#
# colors = colorgram.extract("image.jpg", 300)
# rgb_colour = []
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_colour.append(new_color)
# print(rgb_colour)
timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(235, 243, 239), (194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15), (168, 208, 178), (14, 88, 104), (162, 203, 212), (220, 179, 173), (236, 204, 13)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(15, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = turtle.Screen()
screen.exitonclick()



























