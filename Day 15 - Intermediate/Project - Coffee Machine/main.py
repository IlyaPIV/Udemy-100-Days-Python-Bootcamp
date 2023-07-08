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

money_profit = 0


def print_report():
    print(f"> Water: {resources['water']}")
    print(f"> Milk: {resources['milk']}")
    print(f"> Coffee: {resources['coffee']}")
    print(f"> Money: {money_profit}")


def resources_ok(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, not enough {item} in machine")
            return False
    return True


def processing_money():
    """Returns total summ of inserted coins"""
    print("Please insert coins:")
    total = int(input(">> How many quarters?: ")) * 0.25
    total += int(input(">> How many dimes?: ")) * 0.1
    total += int(input(">> How many nickles?: ")) * 0.05
    total += int(input(">> How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money >= drink_cost:
        global money_profit
        money_profit += drink_cost
        change = round(money - drink_cost, 2)
        if change > 0:
            print(f"Here is {change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def prepare_drink(drink_name, drink_ingredients):
    print(f"Here is your {drink_name} ☕︎")
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


def working_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso / latte / cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "status":
            print_report()
        else:
            drink = MENU[choice]
            if resources_ok(drink["ingredients"]):
                inserted_money = processing_money()
                if is_transaction_successful(inserted_money, drink["cost"]):
                    prepare_drink(choice, drink["ingredients"])


working_machine()
