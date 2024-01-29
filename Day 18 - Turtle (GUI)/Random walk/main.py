import turtle as t
import random

timmy = t.Turtle()
colors = ["red", "orange", "yellow", "green", "cyan", "purple", "gray", "medium aquamarine", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]
news = [0, 90, 180, 270]
timmy.pensize(15)

for i in range(200):
    timmy.forward(30)
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(news))
