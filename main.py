import turtle
import pandas

data = pandas.read_csv("50_states.csv")
# print(data[data.state.str.lower() == "alabama"])

screen = turtle.Screen()
screen.title("Map Game")
image = "blank_states_img.gif"
screen.addshape(image)
t = turtle.Turtle()
t.shape(image)
text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.ht()

found_states = set()
lives = 10
while len(found_states) < 50 and lives > 0:
    answer_state = screen.textinput(title=f"{len(found_states)}/50 States, {lives} lives", prompt="Name another state")
    states = data[data.state.str.lower() == answer_state.lower()]
    if len(states == 1):
        state = states.state.item()
        if state not in found_states:
            x = int(states.x)
            y = int(states.y)
            text_turtle.goto(x, y)
            text_turtle.write(f"{state}", align="center", font=("Verdana", 10, "normal"))
            found_states.add(state)
    else:
        lives -= 1

data_dict = data.to_dict()
missed_states = []
for state in data_dict['state']:
    s = data_dict['state'][state]
    if s not in found_states:
        missed_states.append(s)

pandas.DataFrame(missed_states, columns=["Missed States"]).to_csv("missed_states.csv")

screen.exitonclick()
