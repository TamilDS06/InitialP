import random

words = ['tamil', 'enaaglish', 'maths']
word = random.choice(words)
underscore = ['_' for i in range(0, len(word))]
print(underscore)
lives = 6
while '_' in underscore:
    letter = input("Guess a letter").lower()
    if letter in word:
        for i in range(0,len(word)):
            if word[i] == letter:
                # print("Right\n")
                underscore[i] = letter
                print(underscore)
    else:
        # print("Wrong\n")
        lives -= 1
        print(f'Your lives reduced to {lives} you have lost {6 - lives}')
        pass
    if lives == 0:
        print("You have lost..Try again")
        break
if '_' not in underscore:
    print("You've won")