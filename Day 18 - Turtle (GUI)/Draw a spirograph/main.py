import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fastest")


for _ in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)


screen.exitonclick()
