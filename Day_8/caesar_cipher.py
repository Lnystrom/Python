alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


finished = False
while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encypt(text,shift):
        """Function created to encrypt a code"""
        cipher_text = ""
        for letter in text:
            index = alphabet.index(letter)
            new_index = index + shift
            if new_index >len(alphabet):
                new_index = new_index%len(alphabet)
            cipher_text += alphabet[new_index]
        print(f"The encoded text is {cipher_text}")

    def decrypt(text, shift):
        """Function created to decrypt a code"""
        cipher_text = ""
        for letter in text:
            index = alphabet.index(letter)
            new_index = index - shift
            if new_index <0:
                addition = len(alphabet) - new_index
                new_index =  addition -1
                print(new_index)
            cipher_text += alphabet[new_index]
        print(f"The decoded text is {cipher_text}")

    if direction == "encode":
        encypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    question = input("Do you want to do it again? 'Yes' or 'No'")
    if question.lower() == "no":
        finished = True
        
