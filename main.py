from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a colour:")
turtleColours = ["red", "orange", "yellow", "green", "blue", "violet"]
y_Positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for _ in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(turtleColours[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_Positions[_])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The winning colour is {winning_colour}.")
            else:
                print(f"You've lost! The winning colour is {winning_colour}.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

Screen().exitonclick()
