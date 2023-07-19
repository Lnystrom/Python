import random
import art


def sort_number():
    """Function that sorts a number"""
    lucky_number = random.randint(1,100)
    return lucky_number

def introduction(numero_da_sorte):
    """Function that displays the game interface and chooses the difficulty"""
    print(art.logo)
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
    print(f"Psss, the correct answer is {numero_da_sorte}")
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficult

def game(dificuldade, resposta):
    """Calls the game"""
    if dificuldade == "easy":
        lives = 10
    elif dificuldade == "hard":
        lives = 5
    game_over = False
    while game_over is False:
        print(f"you have {lives} attempts remaining to guess the number.")
        chute = int(input("Make a guess: "))
        if chute == resposta:
            print(f"You got it! The answer was {resposta}")
            game_over = True
        elif chute != resposta:
            lives -= 1
            if chute > resposta:
                print("Too high \n Guess again.")
            elif chute < resposta:
                print("Too low \n Guess again.")


jogando = True
while jogando is True:
    numero_sorteado = sort_number()
    nivel = introduction(numero_sorteado)
    game(nivel, numero_sorteado)
    de_novo = input("Wanna play again? 'y' or 'n': ")
    if de_novo == "y":
        jogando = True
    else:
        jogando = False
        