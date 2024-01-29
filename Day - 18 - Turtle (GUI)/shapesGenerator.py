import turtle as t
import random

tim = t.Turtle()

colors = ["red", "orange", "yellow", "green", "cyan", "purple", "gray", "medium aquamarine", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    color_picker = random.choice(colors)
    tim.color(color_picker)
    draw_shape(i)

