
from art import logo


# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(n1, n2, op):
    function = operations[op]
    result = function(n1, n2)
    print(f"{n1} {op} {n2} = {result}")
    return result


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    while True:
        for key in operations:
            print(key)
        operation_choice = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        num1 = calculate(num1, num2, operation_choice)
        if not input(f"Type 'y' to continue calculating with {num1}, or type 'n' to exit: ") == 'y':
            break


calculator()
