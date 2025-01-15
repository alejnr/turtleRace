from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a colour:")
turtleColours = ["red", "orange", "yellow", "green", "blue", "violet"]
y_Positions = [-70, -40, -10, 20, 50, 80]

for _ in range(0,6):
    tim = Turtle("turtle")
    tim.color(turtleColours[_])
    tim.penup()
    tim.goto(x=-230, y=y_Positions[_])

Screen().exitonclick()
