from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_choice(machine_menu):
    items = machine_menu.get_items()
    return input(f"What would you like? ({items}): ")


def print_report(drink_maker, money_receiver):
    drink_maker.report()
    money_receiver.report()


def working_machine():
    is_on = True
    machine_menu = Menu()
    drink_maker = CoffeeMaker()
    money_receiver = MoneyMachine()
    while is_on:
        choice = make_choice(machine_menu)
        if choice == "off":
            is_on = False
        elif choice == "status":
            print_report(drink_maker, money_receiver)
        else:
            drink = machine_menu.find_drink(choice)
            if drink_maker.is_resource_sufficient(drink):
                if money_receiver.make_payment(drink.cost):
                    drink_maker.make_coffee(drink)


working_machine()
