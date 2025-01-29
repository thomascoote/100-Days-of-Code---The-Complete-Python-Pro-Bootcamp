import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount):

    original_text = text
    shift_amount = shift

    if direction == "1":
     # Takes each letter in the input phrase, checks if it's alphanumeric, then shifts by the "Shift" amount.

        for letter in text:
            if letter.isalnum():
                letter = alphabet.index(letter) + shift
                if letter > len(alphabet) -1:
                    letter %= len(alphabet)
                list.append(new_word, alphabet[letter])
            else:
                list.append(new_word, letter)

        encrypted_word = "".join(new_word)
        print(encrypted_word)

    else:
        for letter in text:
            if letter.isalnum():
                letter = alphabet.index(letter) - shift
                if letter > len(alphabet) -1:
                    letter %= len(alphabet)
                list.append(new_word, alphabet[letter])
            else:
                list.append(new_word, letter)

        decrypted_word = "".join(new_word)
        print(decrypted_word)

new_word = []


run_program = True

while run_program:

    direction = input("Type 1 to encode or 2 to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift)

    run_again = input("Would you like to run the program again? Y/N?")

    if run_again.lower() == "y":
        run_program = True
        new_word = []

    else:
        run_program = False