from data import MENU, resources


def get_coins():
    print("Please enter the coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total_coins = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_coins


wanna_continue = True
while wanna_continue:
    report = f"water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}"
    user_choice = input("What would you like?? (espresso/latte/cappuccino):")
    if user_choice == "report":
        print(report)
    elif user_choice == "espresso":
        if resources['water'] >= MENU["espresso"]["ingredients"]["water"] and \
                resources['coffee'] >= MENU["espresso"]["ingredients"]["coffee"]:
            total_coins_ = get_coins()
            if total_coins_ >= MENU["espresso"]["cost"]:
                print("Here is your espresso. Enjoy!!!")
                resources['water'] = resources['water'] - MENU["espresso"]["ingredients"]["water"]
                resources['coffee'] = resources['coffee'] - MENU["espresso"]["ingredients"]["coffee"]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['coffee'] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif resources['water'] < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
    elif user_choice == "latte":
        if resources['water'] >= MENU["latte"]["ingredients"]["water"] \
                and resources['coffee'] >= MENU["latte"]["ingredients"]["coffee"] and \
                resources['milk'] >= MENU["latte"]["ingredients"]["milk"]:
            total_coins_ = get_coins()
            if total_coins_ >= MENU["latte"]["cost"]:
                print("Here is your espresso. Enjoy!!!")
                resources['water'] = resources['water'] - MENU["latte"]["ingredients"]["water"]
                resources['coffee'] = resources['coffee'] - MENU["latte"]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU["latte"]["ingredients"]["milk"]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['coffee'] < MENU["latte"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif resources['water'] < MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif resources['milk'] < MENU["latte"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
    elif user_choice == "cappuccino":
        if resources['water'] >= MENU["cappuccino"]["ingredients"]["water"] \
                and resources['coffee'] >= MENU["cappuccino"]["ingredients"]["coffee"] \
                and resources['milk'] >= MENU["cappuccino"]["ingredients"]["milk"]:
            total_coins_ = get_coins()
            if total_coins_ >= MENU["cappuccino"]["cost"]:
                print("Here is your espresso. Enjoy!!!")
                resources['water'] = resources['water'] - MENU["cappuccino"]["ingredients"]["water"]
                resources['coffee'] = resources['coffee'] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU["cappuccino"]["ingredients"]["milk"]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['coffee'] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif resources['water'] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
            elif resources['milk'] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
    elif user_choice == "off":
        break
    continue