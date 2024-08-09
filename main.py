# import colorgram
import turtle as turtle_module
import random

# rgb_color = []
# colors = colorgram.extract('image2.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
turtle_module.colormode(255)
time = turtle_module.Turtle()
time.speed("fastest")
time.penup()
time.hideturtle()
colors_list = [(226, 229, 235), (243, 237, 222), (242, 233, 239), (231, 241, 236), (191, 165, 116), (139, 166, 189),
               (59, 101, 137),(138, 90, 53), (13, 23, 53), (221, 206, 125), (60, 23, 12), (181, 146, 165),
               (178, 152, 47), (142, 176, 150), (74, 116,82), (61, 15, 26), (124, 80, 101), (16, 38, 25), (127, 32, 18),
               (25, 52, 124), (178, 188, 215), (110, 34, 48), (162,106, 135), (98, 149, 102), (96, 122, 172),
               (209, 180, 195), (171, 106, 95), (172, 205, 181), (77, 148, 163), (26, 89,64)]

time.setheading(255)
time.forward(300)
time.setheading(0)
number_of_dots = 100

for doc_count in range(1, number_of_dots + 1):
    time.dot(20, random.choice(colors_list))
    time.forward(50)

    if doc_count % 10 == 0:
        time.setheading(90)
        time.forward(50)
        time.setheading(180)
        time.forward(500)
        time.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
