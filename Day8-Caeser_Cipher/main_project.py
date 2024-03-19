alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(plain_text, shift_amount, direction):
    """Encrypt or decrypt text message using caesar cipher technique

    Args:
        text (str): enter a text message to encode or decode
        shift (int): enter shift number
        direction (str): 'encode' to encrypt, 'decode' to decrypt
    """
    result_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = (position + shift_amount) % 26
            elif direction == 'decode':
                new_position = (position - shift_amount) % 26
            result_text += alphabet[new_position]
        else:
            result_text += char 
    return f"The {direction} text is :{result_text}"

from art import logo
print(logo)

should_continue = True
while should_continue:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction in ['encode', 'decode']:
        print(caesar_cipher(text, shift, direction))
    else:
        print("Enter valid input as 'encode' or 'decode'.")
    
    result = input("Type 'yes' if you want to continue again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")        