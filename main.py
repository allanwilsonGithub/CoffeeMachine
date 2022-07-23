from data import resources, MENU

machine_power_on = True
money = 0


def check_available_resources(drink_option):
    """ Verifies that there are enough resources to make the chosen drink """
    for ingredient in MENU[drink_option]['ingredients']:
        if MENU[drink_option]['ingredients'][ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


def take_coins():
    """ Receives coins from customer and returns the dollar amount """
    quarters_inserted = int(input('Insert quarters: '))
    dimes_inserted = int(input('Insert dimes: '))
    nickels_inserted = int(input('Insert nickels: '))
    pennies_inserted = int(input('Insert pennies: '))
    amount_received = (quarters_inserted*0.25) + (dimes_inserted*0.10) + (nickels_inserted*0.05) + \
                      (pennies_inserted*0.01)
    return amount_received


def process_payment(drink):
    """ Checks that amount received is enough to purchase the drink """
    dollars_received = take_coins()
    if dollars_received >= MENU[drink]['cost']:
        purchase(dollars_received, MENU[drink]['cost'])
        return True
    else:
        print("Sorry, you didn't pay enough")
        return False


def purchase(amount_received, drink_cost):
    """ Adds the received money to the machines profit and returns change to customer """
    global money
    money += drink_cost
    change = round(amount_received - drink_cost, 2)
    print(f"You're change is: {change}")


def deliver_drink(product):
    """ Reduces the drink resources from machine's resources """
    for ingredient in MENU[product]['ingredients']:
        ingredient_amount = MENU[product]['ingredients'][ingredient]
        resources[ingredient] -= ingredient_amount


while machine_power_on:
    user_input = input('What would you like? (espresso/latte/cappuccino) ☕: ').lower()

    if user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif user_input == 'off':
        machine_power_on = False

    elif check_available_resources(user_input):
        if process_payment(user_input):
            deliver_drink(user_input)
            print(f"Here is your {user_input}. Enjoy!")
