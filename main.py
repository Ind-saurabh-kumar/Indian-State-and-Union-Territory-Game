import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States and Union Territory Game")
image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)



data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

# Code to plot in images(.gif format)
# def get_mouse_click_corr(x, y):
#     print(f"{x},{y}")
#
#
# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()


while len(guessed_states) < 31:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 States and Union Territory correct",
                                    prompt="What's another state's name ?").title()

    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()

        t.color("Red")
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state,False,"left",font=("Arial",12, "normal"))

screen.exitonclick()

