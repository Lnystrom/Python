import random
import art

baralho = [11,2,3,4,5,6,7,8,9,10,10,10,10]
j1 = []
j2 = []
rodando = True
Game_Over = False

def sorteador(mao, sorteios):
    """função que sorteia as cartas de cada jogador"""
    for _ in range(sorteios):
        mao.append(random.choice(baralho))

def calculador(mao):
    """função que calcula quantos pontos cada jogador possui e dizer quem é 
    o ganhador, se teve blackjack ou algo do tipo"""
    if sum(mao) == 21 and len(mao) == 2:
        return 0 #blackjack
    if 11 in mao and sum(mao)>21:
        mao.append(1)
        mao.remove(11)
    return sum(mao)

def comparador(p_jogador, p_computador):
    """Function that compares the scores and tell us what is the winner"""
    if p_jogador > 21 and p_computador > 21:
        return "You went over. You lose 😤"
    elif p_jogador == p_computador:
        return "Draw"
    elif p_computador == 0:
        return "Lose, opponent has Blackjack"
    elif p_jogador== 0:
        return "Win with a Blackjack"
    elif p_jogador>21:
        return "You went over. You lose"
    elif p_computador>21:
        return "Opponent went over. You win"
    elif p_jogador > p_computador:
        return "You win"
    else:
        return "you lose"
    
while rodando == True:
    start = input("Do you wanna start a blackjack game? 'y' or 'n': ")
    if start == "y":
        print(art.logo)
    else:
        print("oh, yes, you want to")
        print(art.logo)

    sorteador(j1, 2)
    sorteador(j2, 2)
    print(f"Your deck is: {j1}, Your total is: {calculador(j1)}")
    print(f"The first card of the oponent is [{j2[0]}]")

    while Game_Over != True:
        if calculador(j1)==0 or calculador(j2)==0 or calculador(j1)>21 or calculador(j2)>21:
            Game_Over = True
            print(comparador(calculador(j1), calculador(j2)))
        answer = input("Wanna take another card? 'y' or 'n': ")
        if answer == "y":
            sorteador(j1, 1)
            print(f"Your deck is {j1} and your total is: {calculador(j1)}")
        else:
            while calculador(j2)<17:
                sorteador(j2,1)
            print(comparador(calculador(j1),calculador(j2)))
            print(f"The opponent deck is: {j2}, its score was: {calculador(j2)}")
            Game_Over = True

    again = input("Want to start a new game? 'y' or 'n': ")
    if again == "y":
        print("\n" * 100)
        j1 = []
        j2 = []
        Game_Over = False
    elif again == "n":
        rodando = False
