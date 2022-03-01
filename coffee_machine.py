"""
Espresso        Latte           Cappuccino
$1.50           $2.50           $3.00
50ml water      200ml water     250ml water
16g coffee      24g coffee      24g coffee
                150ml milk      100ml milk

Coffee machine starts out with:
300ml water
200ml milk
100g coffee

1. Print report
2. Check resources sufficient
3. Process coins
4. Check transaction successful?

"""
import time
from replit import clear
from menu import MENU, resources

money_in_machine = 0
machine_on = True


def report():
    """ Function that creates a report of the resources currently available in the machine. """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${money_in_machine}\n")


def refill():
    """ Function to refill resources in the machine. """
    add_water = int(input("How much water added?: "))
    resources["water"] += add_water
    add_milk = int(input("How much milk added?: "))
    resources["milk"] += add_milk
    add_coffee = int(input("How much coffee added?: "))
    resources["coffee"] += add_coffee


def drinks():
    """ Function that checks if there are enough resources in the machine, if there are then
    machine dispenses the selected drink and uses resources. If not enough resources then
    won't dispense that drink. """
    for drink in MENU.keys():
        if choice == drink:
            if resources["water"] < MENU[choice]["ingredients"]["water"]:
                print("Sorry, there is not enough {water}!")
            elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk!")
            elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
                print("Sorry, there is not enough coffee.")
            else:
                money()
                print(f"Here is your {choice}. Enjoy\n")
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                global money_in_machine
                money_in_machine += MENU[choice]["cost"]
                if drink == "latte" or drink == "cappuccino":
                    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                # print(MENU[selection]["ingredients"]["water"])


def money():
    """ Function that ask for payment in coins, check if enough paid. If enough then carries on making a drink,
    if overpaid, calculates and returns the change. If underpaid, cancels the drink and refunds any money paid."""
    print("Please insert coins.")
    quarters = float(input("How many quarters ($0.25)?: ")) * 0.25
    dimes = float(input("How many dimes ($0.10)?: ")) * 0.10
    nickles = float(input("How many nickles ($0.05)?: ")) * 0.05
    pennies = float(input("How many pennies ($0.01)?: ")) * 0.01
    money_paid = quarters + dimes + nickles + pennies
    change = money_paid - MENU[choice]["cost"]
    print(f"Total paid: {money_paid}")
    if money_paid >= MENU[choice]["cost"]:
        if change > 0:
            print(f"Change: ${change}")
        # return drinks()
    else:
        print(f"Not enough coins. Selection cancelled, ${money_paid} refunded.")


def machine_off():
    """ Function for exiting the while loop and shutting the machine down. """
    for timer in range(3, 0, -1):
        clear()
        print("Machine is shutting down...")
        print(timer)
        time.sleep(1)
        clear()
        print("The machine is off.")
        global machine_on
        machine_on = False


""" While loop to continuously ask user for drink until machine is shut down."""
while machine_on:
    choice = input("Select a drink: \n1. Espresso - $1.5\n2. Latte - $2.5\n3. Cappuccino - $3:\n")
    if choice == "report":
        report()
    elif choice == "refill":
        refill()
    elif choice == "off":
        machine_off()
    elif choice == "espresso" or "latte" or "cappuccino":
        drinks()
