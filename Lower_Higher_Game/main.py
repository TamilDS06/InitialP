from Game_Data import data
from Art import logo, vs
import random

print(logo)

def check_(A,B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.\n{vs}\nAgainst B: {B['name']}, a {B['description']}, from {B['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B'")
    if A['follower_count'] > B['follower_count'] and user_choice == 'A':
        return True
    elif B['follower_count'] > A['follower_count'] and user_choice == 'B':
        return True
    else:
        return False

wanna_continue = True 
while wanna_continue:
    score = 0
    A = random.choice(data)
    B = random.choice(data)

    while True:
        if check_(A,B):
            score += 1
            print(f'You are right. Your score is {score}')
            A = B
            B = random.choice(data)
            continue
        else:
            wanna_continue = input(f"You've lost the game.Your final score {score}. Do you want to continue? Type 'Y' or 'N'.")
            if wanna_continue.lower() == "y":
                wanna_continue = True
                break
            else:
                wanna_continue = False
                break

