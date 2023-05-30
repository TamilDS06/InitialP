import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def total(list_cards):
    total = 0
    for i in list_cards:
        total += i
    return total


def check_ace(cards):
  if 11 in cards:
      total_ = total(cards)
      if total_ >= 21:
          for i in range(0,len(cards)):
            try:
                cards[cards.index(11)] = 1
            except ValueError:
                pass
            total_ = total(cards)
      else:
          return total_
  else:
      total_ = total(cards)
  return total_

def win_lose(user_total, computer_total):
    if user_total > 21 and computer_total < 21:
            print("Computer wins!, You lose!!")
            return False
    elif computer_total > 21 and user_total < 21:
            print("you win!, computer loses!")
            return False
    else:
        return True
def check_to_continue(deck, user_cards, computer_cards):
    user_total, computer_total = check_ace(user_cards) ,check_ace(computer_cards)
    print(f'Your score {user_total}')
    result = False
    # computer_card = 0
    print(f"Your cards {user_cards}")
    # print(f'Current card of the computer is {computer_cards[computer_card]}')
    result = win_lose(user_total, computer_total)
    if result:
        should_continue = input("Type 'y' to take a card or type 'n' to stand!!!")
        if should_continue == 'y':
            # computer_card += 1
            user_cards.append(random.choice(deck))
            # check_to_continue(deck, user_cards, computer_cards, computer_card)
            user_total = check_ace(user_cards)
            result = win_lose(user_total,computer_total)
            user_total = check_ace(user_cards)
            if user_total == computer_total:
                print("Match draw")
                return False
            elif user_total < computer_total:
                    print('You win')
                    return False
            else:
                print("you lose")
                return False
            
        else:
            # computer_card += 1
            print(f'Current card of the computer is {computer_cards[0]}')
            # computer_cards.append(random.choice(deck))
            # computer_total = check_ace(computer_cards)
            if computer_total < 17:
                computer_cards.append(random.choice(deck))
                # check_to_continue(deck, user_cards, computer_cards, computer_card)
                # print("Computer wins!")
                user_total, computer_total = check_ace(user_cards), check_ace(computer_cards)
                win_lose(user_total,computer_total)
                if user_total == computer_total:
                    print("Match draw")
                    return False
                elif user_total < computer_total:
                    print('You win')
                    return False
                else:
                    print("you lose")
                    return False
            else:
                # check_to_continue(deck, user_cards, computer_cards, computer_card)
                win_lose(check_ace(user_cards),check_ace(computer_cards))
                if user_total == computer_total:
                    print("Match draw")
                    return False
                elif user_total > computer_total:
                    print('computer wins')
                    return False
                else:
                    print("computer loses")
                    return False
    return False

    
def pick_user_computer_cards():
    user_cards = [random.choice(deck) for i in range(0, 2)]
    # user_cards = [1, 1]
    computer_cards = [random.choice(deck) for i in range(0, 2)]
    # computer_cards = [2,2]
    return user_cards, computer_cards


want_continue = True
play_again = False
computer_card = 0
while want_continue or play_again:
    user_cards, computer_cards = pick_user_computer_cards()
    if 10 in computer_cards and 11 in computer_cards:
        print("Computer wins with BlackJack")
        want_continue = False
    elif 10 in user_cards and 11 in user_cards:
        print("You win with BlackJack")
        want_continue = False
    else:
        want_continue = check_to_continue(deck, user_cards, computer_cards)
        if not want_continue:
            play_again = input("Type 'y' if you want to play again or type 'n' if you want to exit.")
            if play_again == 'y':
                play_again = True
            else:
                play_again = False
        