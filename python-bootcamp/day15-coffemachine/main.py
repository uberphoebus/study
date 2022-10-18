
# program requirements
# TODO: 1. print report.
# TODO: 2. check resources sufficient
# TODO: 3. process coins
# TODO: 4. check transaction successful
# TODO: 5. make coffee

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.0
is_machine_on = True

def check_resources(prompt):
    
    machine_status = True
    if resources['water'] < MENU[prompt]['ingredients']['water']:
        print("Sorry there is not enough water.")
        machine_status = False
    if prompt != 'espresso':
        if resources['milk'] < MENU[prompt]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            machine_status = False
    if resources['coffee'] < MENU[prompt]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        machine_status = False
    
    return machine_status

def process_coins(prompt):

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    return total_coins

def check_transaction(prompt, total_coins):
    global money
    successul_transaction = False

    cost = MENU[prompt]['cost']
    refund = total_coins - cost
    if refund < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        money += cost
        print(f"Here is ${refund:.2f} in change.")
        successul_transaction = True
    return successul_transaction

def make_coffee(prompt):
    global resources
    if prompt != 'espresso':
        resources['milk'] -= MENU[prompt]['ingredients']['milk']
    resources['water'] -= MENU[prompt]['ingredients']['water']
    resources['coffee'] -= MENU[prompt]['ingredients']['coffee']
    print(f"Here is your {prompt} ☕️. Enjoy!")

def main():
    global is_machine_on
    while is_machine_on:

        prompt = input("What would you like? (espresso/latte/cappuccino): ")

        if prompt == "off":
            print("Machine is off.")
            is_machine_on = False
            break

        elif prompt == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")

        else:
            checked = check_resources(prompt)
            if checked:
                total_coins = process_coins(prompt)
                successul_transaction = check_transaction(prompt, total_coins)
                if successul_transaction:
                    make_coffee(prompt)
                else:
                    continue
            else:
                continue

main()