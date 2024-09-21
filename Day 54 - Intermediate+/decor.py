import time


# Python decorator function
def delay_decorator(function):
    def wrapper_function():
        # do something before
        time.sleep(1)
        # call function
        function()
        # do something after

    return wrapper_function()


@delay_decorator
def say_hello():
    print("Hello!")


@delay_decorator
def say_greeting():
    print("How are you?")


@delay_decorator
def say_goodbye():
    print("Goodbye!")


say_hello()
say_greeting()
say_goodbye()

decorated_function = delay_decorator(say_goodbye)
decorated_function()
