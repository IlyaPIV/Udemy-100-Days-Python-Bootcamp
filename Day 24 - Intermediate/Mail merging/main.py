PLACEHOLDER = "[name]"

with open("./Input/starting_letter.txt") as letter_file:
    letter_lines = letter_file.readlines()


with open("./Input/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    cleared_name = name.strip()
    with open(f"./Output/ReadyToSend/{cleared_name}.txt", mode="w") as letter:
        for line in letter_lines:
            new_line = line.replace(PLACEHOLDER, cleared_name)
            letter.write(new_line)
