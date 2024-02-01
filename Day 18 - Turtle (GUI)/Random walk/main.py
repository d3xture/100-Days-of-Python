import turtle as t
import random

colors = [
    "#6495ED", "#4169E1", "#1E90FF", "#00BFFF", "#87CEEB",  # Blue shades
    "#4682B4", "#5F9EA0", "#20B2AA", "#00CED1", "#48D1CC",  # More Blue shades
    "#7FFFD4", "#B0E0E6", "#ADD8E6", "#87CEFA", "#87CEEB",  # Even more Blue shades
    "#F08080", "#CD5C5C", "#DC143C", "#FF4500", "#FF6347",  # Red and Orange shades
    "#FFA07A", "#FA8072", "#E9967A", "#FF7F50", "#FF6347",  # More Red and Orange shades
    "#20B2AA", "#008B8B", "#008080", "#66CDAA", "#00FA9A",  # Green and Aqua shades
    "#00FF7F", "#3CB371", "#2E8B57", "#2E8B57", "#008000",  # More Green shades
    "#556B2F", "#6B8E23", "#808000", "#BDB76B", "#EEE8AA",  # Yellow and Olive shades
    "#F0E68C", "#FFD700", "#DAA520", "#B8860B", "#FF8C00",  # More Yellow shades
    "#CD853F", "#A0522D", "#8B4513", "#A52A2A", "#800000"   # Brown and Maroon shades
]

news = [0, 90, 180, 270]
timmy = t.Turtle()
screen = t.Screen()
timmy.pensize(15)

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(news))

screen.exitonclick()
