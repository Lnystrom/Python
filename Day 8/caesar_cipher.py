import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
def caeser(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = index + shift
                if new_index >len(alphabet):
                    new_index = new_index%len(alphabet)
                cipher_text += alphabet[new_index]
            else:
                cipher_text+=char    
        print(f"The encoded text is {cipher_text}")
    
    elif direction == "decode":
        cipher_text = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = index - shift%len(alphabet)
                cipher_text += alphabet[new_index]
            else:
                cipher_text+=char 
        print(f"The decoded text is {cipher_text}")

finished = False
while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    question = input("Do you want to do it again? 'Yes' or 'No'")
    if question.lower() == "no":
        print("Goodbye!")
        finished = True
    else:
        caeser(text, shift, direction)   
