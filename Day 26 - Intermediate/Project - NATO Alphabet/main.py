import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alpha_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index, row) in alpha_data_frame.iterrows()}
print(alpha_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter your name: ")
code = [alpha_dict[char.upper()] for char in input_word]
print(code)
