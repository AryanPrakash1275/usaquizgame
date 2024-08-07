import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("USA Game of Guess")
image = "blank_states_img.gif"
screen.bgpic(image)

data_states = pandas.read_csv("50_states.csv")
ans_check_column = data_states.columns[0]
x_cord= data_states.columns[1]
y_cord = data_states.columns[2]
data_states[ans_check_column] = data_states[ans_check_column].astype(str).str.lower()

score = 0

game_on = True
while game_on:
    answer = screen.textinput(title="Guess the state", prompt="Enter a state's name.")
    print(answer)
    if answer == 'exit':
        game_on = False
    if answer in data_states[ans_check_column].values:
        print("Yes")
        row = data_states[data_states[ans_check_column] == answer]
        x = row[x_cord].values[0]
        y = row[y_cord].values[0]
        turtle.penup()
        turtle.goto(int(x), int(y))
        turtle.pendown()
        turtle.dot(10, "red")
        score += 1
    print(score)
turtle.mainloop()
