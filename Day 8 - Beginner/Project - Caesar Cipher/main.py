import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        letter_pos = alphabet.index(letter)
        new_pos = letter_pos + shift_amount
        end_text += alphabet[new_pos]
    print(f"The {cipher_direction}d text is {end_text}")


print(art.logo)
do_work = True
while do_work:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(text, shift, direction)

    try_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if try_again == 'no':
        do_work = False
    elif try_again == 'yes':
        do_work = True
    else:
        print("Unknown command - stopping process")
        do_work = False
