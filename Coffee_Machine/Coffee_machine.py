from data import MENU, resources

profit = 0


def is_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def get_coins():
    """Returns the total calculated from coins inserted."""
    print("Please enter the coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total_coins = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_coins


def is_transaction_successfully(payment_, cost_of_drink):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment_ > cost_of_drink:
        change = round(payment_ - cost_of_drink, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(user_choice_, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {user_choice_} ☕️. Enjoy!")


wanna_continue = True
while wanna_continue:
    report = f"water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}g." \
             f"\nMoney: ${round(profit, 2)}."
    user_choice = input("What would you like?? (espresso/latte/cappuccino):")
    if user_choice == "off":
        break
    elif user_choice == "report":
        print(report)
    else:
        drink = MENU[user_choice]
        if is_sufficient(drink['ingredients']):
            payment = get_coins()
            if is_transaction_successfully(payment, drink['cost']):
                make_coffe(user_choice, drink['ingredients'])
