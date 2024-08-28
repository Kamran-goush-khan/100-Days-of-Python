alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

instruct = "yes"

while instruct == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(original_text, shift_number, encode_or_decode) :
        message = ""
        if encode_or_decode == "decode" :
            shift_number *= -1
        for letter in original_text:
            if letter in alphabet :
                index_of_letter = alphabet.index(letter)
                number = (index_of_letter + shift_number) % 26
                message += alphabet[number]
            else :
                message += letter

        print(f"Here is the {encode_or_decode}d message result : {message}")

    caesar(text, shift, direction)
    instruct = input("Type 'yes' if you want to go again. otherwise, type 'no'\n").lower()
