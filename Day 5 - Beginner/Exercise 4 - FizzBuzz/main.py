for i in range(1, 101):
    fb = ""
    if i % 3 == 0:
        fb += "Fizz"
    if i % 5 == 0:
        fb += "Buzz"
    if fb == "":
        print(i)
    else:
        print(fb)