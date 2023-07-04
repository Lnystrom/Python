alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            index = alphabet.index(letter)
            new_index = index + shift
            if new_index >len(alphabet):
                new_index = new_index%len(alphabet)
            cipher_text += alphabet[new_index]
        print(f"The encoded text is {cipher_text}")
    
    elif direction == "decode":
        cipher_text = ""
        for letter in text:
            index = alphabet.index(letter)
            new_index = index - shift
            cipher_text += alphabet[new_index]
        print(f"The decoded text is {cipher_text}")

finished = False
while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    question = input("Do you want to do it again? 'Yes' or 'No'")
    if question.lower() == "no":
        finished = True
    else:
        caeser(text, shift, direction)   
