from turtle import Turtle, Screen
import pandas as pd

score = 0
data = pd.read_csv('50_states.csv')

screen = Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
tim = Turtle(shape=image)
screen.tracer(0)
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f'{score}/{len(data["state"])}Guess the name.',
                                   prompt="What is another city's name?").title()
    if user_answer == "Exit":
        remaining_states_data = {
            'remaining_states': states
        }
        remaining_states_data = pd.DataFrame(remaining_states_data)
        remaining_states_data.to_csv('remaining_states_data.csv')
        break
    if user_answer in states:
        screen.update()
        score += 1
        print('yes')
        state_data = data[data['state'] == user_answer]
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_data['x']), int(state_data['y']))
        tim.write(state_data.state.item(), align='center', font=('Arial', 8, 'normal'))
        guessed_states.append(user_answer)
        states.remove(user_answer)
    else:
        pass
    if score >= 30:
        print("You've won")


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # It loops the screen even the code finishes the work.

# screen.exitonclick()
