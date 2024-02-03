import turtle as t
import random

game_over = True
screen = t.Screen()
screen.setup(800, 700)
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
user_bet = screen.textinput(title="Ghoray kachway", prompt="Enter color to bet")
y_directions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for i in range(0, 6):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-370, y=y_directions[i])
    all_turtles.append(new_turtle)

if user_bet:
    game_over = True

    while game_over:
        random_turtle = random.choice(all_turtles)
        if random_turtle.xcor() > 380:
            game_over = False
            winning_color = random_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        random_turtle.forward(random_distance)

screen.exitonclick()

