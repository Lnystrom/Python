import art
import random

def sort_number():
    lucky_number = random.randint(1,100)
    return lucky_number

def introduction(numero_da_sorte):
    print(art.logo)
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
    print(f"Psss, the correct answer is {numero_da_sorte}")
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficult

def game(dificuldade, resposta):
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
        elif chute != resposta:
            lives -= 1
            if chute > resposta:
                print(f"Too high \n Guess again.")
            elif chute < resposta:
                print(f"Too low \n Guess again.")

numero_sorteado = sort_number()
dificuldade = introduction(numero_sorteado)
game(dificuldade, numero_sorteado)
