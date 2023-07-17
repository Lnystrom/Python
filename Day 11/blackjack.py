import random

baralho = [11,2,3,4,5,6,7,8,9,10,10,10,10]
j1 = []
j2 = []
rodando = True
Game_Over = False
resultado = 0

def sorteador(mao_jogador, sorteios):
    """função que sorteia as cartas de cada jogador"""
    for i in range(sorteios):
        mao_jogador.append(random.choice(baralho))

def comparador(mao_jogador, mao_computador):
    """função que calcula quantos pontos cada jogador possui e dizer quem é 
    o ganhador, se teve blackjack ou algo do tipo"""
    jogador_blackjack = False
    computador_blackjack = False

    p_jogador = 0
    p_computador = 0

    p_jogador = sum(mao_jogador)
    p_computador = sum(mao_computador)

    if 11 in mao_jogador and p_jogador>21:
        mao_jogador.append(1)
        mao_jogador.remove(11)
        p_jogador = sum(mao_jogador)
    if 11 in mao_computador and p_computador>21:
        mao_computador.append(1)
        mao_computador.remove(11)
        p_computador = sum(mao_computador)
    if mao_jogador == [11,10] or mao_jogador == [10,11]:
        jogador_blackjack = True
    elif mao_computador == [11,10] or mao_computador == [10,11]:
        computador_blackjack = True
    if computador_blackjack is True or (computador_blackjack is True and jogador_blackjack is True) or p_jogador>21:
        return 0
    elif jogador_blackjack is True or p_computador>21:
        return 1
    elif p_jogador>21 and p_computador>21:
        return 2

while rodando == True:
    start = input("Do you wanna start a blackjack game? 'y' or 'n': ")
    if start == "y":
        print("logo")
    else:
        print("oh, yes, you want to")
        print("logo")

    sorteador(j1, 2)
    sorteador(j2, 2)
    print(f"Your deck is: {j1}")
    print(f"The first card of the oponent is [{j2[0]}]")

    while Game_Over != True:
        answer = input("Wanna take another card? 'y' or 'n': ")
        if answer == "y":
            sorteador(j1, 1)
            print(f"Your deck is {j1} and your total is: {sum(j1)}")
            while sum(j2)<17:
                sorteador(j2, 1)
            resultado = comparador(j1,j2)
            if resultado == 0:
                print("The dealer wins")
                Game_Over = True
            if resultado == 1:
                print("The player wins")
                Game_Over = True
            if resultado == 2:
                print("Draw")
                Game_Over = True
        elif answer == "n":
            while sum(j2)<17:
                sorteador(j2, 1)
            resultado = comparador(j1,j2)
            if resultado == 0:
                print("The dealer wins")
                Game_Over = True
            if resultado == 1:
                print("The player wins")
                Game_Over = True
            if resultado == 2:
                print("Draw")
                Game_Over = True

    again = input("Want to start a new game? 'y' or 'n': ")
    if again == "y":
        print("\n" * 100)
        j1 = []
        j2 = []
        Game_Over = False
        resultado = 0
    elif again == "n":
        rodando = False
