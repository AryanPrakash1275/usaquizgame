import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("USA Game of Guess")
usa_map = "blank_states_img.gif"
screen.bgpic(usa_map)

parsed_state_csv = pandas.read_csv("50_states.csv")
states_array = parsed_state_csv.columns[0]
state_x_cord = parsed_state_csv.columns[1]
state_y_cord = parsed_state_csv.columns[2]
parsed_state_csv[states_array] = parsed_state_csv[states_array].astype(str).str.lower()

score = 0

game_on = True
while game_on:
    answer = screen.textinput(title="Guess the state", prompt="Enter a state's name.")
    print(answer)
    if answer == 'exit':
        game_on = False
    if answer in parsed_state_csv[states_array].values:
        print("Yes")
        row = parsed_state_csv[parsed_state_csv[states_array] == answer]
        x = row[state_x_cord].values[0]
        y = row[state_y_cord].values[0]
        turtle.penup()
        turtle.goto(int(x), int(y))
        turtle.pendown()
        turtle.dot(10, "red")
        score += 1
    if len(states_array) == score:
        game_on = False
        print("You Win")
    print(score)
turtle.mainloop()
