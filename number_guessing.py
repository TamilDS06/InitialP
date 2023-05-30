import random

def guess(user_number):
    if user_number == number:
        print("You won it")
        return True
    elif user_number < number:
        print("Too low")
        return False
    elif user_number > number:
        print("Too high")
        return False
    pass

def process(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        attempts -= 1
        if guess(user_number):
            break
        else:
            process(attempts)

print("Welcome to the number guessing game:!\nI'm thinking of a number between 1 to 100.")
continue_ = True
while continue_:
    level = input("choose a difficulty. Type 'easy' or 'hard':")
    number = random.randint(1,100)

    if level == 'easy':
        # attempts = 10
        # while attempts != 0:
        #     print(f"You have {attempts} attempts remaining to guess the number.")
        #     user_number = int(input("Make a guess: "))
        #     attempts -= 1
        #     if guess(user_number):
        #         break
        #     else:
        #         continue
        process(10)
        wanna_continue = input("You lost!!! Wanna play again? type 'yes' or 'no'")
        if wanna_continue == 'yes':
            pass
        else:
            continue_ = False

    elif level == 'hard':
        # attempts = 5
        # while attempts != 0:
        #     print(f"You have {attempts} attempts remaining to guess the number.")
        #     user_number = int(input("Make a guess: "))
        #     attempts -= 1
        #     if guess(user_number):
        #         break
        #     else:
        #         continue
        process(5)
        wanna_continue = input("You lost!!! Wanna play again? type 'yes' or 'no'")
        if wanna_continue == 'yes':
            pass
        else:
            continue_ = False
