with open("my_file.txt", mode="a") as file:  # mode="w" - writing / mode="a" - append / mode="r" (default) - reading
    file.write("\n\nNew text line.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
