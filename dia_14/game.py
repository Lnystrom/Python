import random
import art
import lista


def sorteador(banco_de_dados):
    """It'll sort one contestant"""
    lucky_number = random.randint(1,100)
    lucky_contestant = banco_de_dados[lucky_number]
    lucky_visits = lucky_contestant['visits']
    lucky_domain = lucky_contestant['domain']

    lucky_list = [lucky_number, lucky_domain, lucky_visits]
    return lucky_list

def comparador(site_1, site_2):
    """It'll tell what score is higher"""
    if site_1[0] < site_2[0]:
        return 0
    else:
        return 1

print(art.logo)

points = 0
rodando = True

while rodando is True:
    first_competitor = sorteador(lista.website_data)
    second_competitor = sorteador(lista.website_data)
    chute = input(f"Who is the most acessed site? \n A: {first_competitor[1]} or B: {second_competitor[1]}: ")
    chute = chute.lower()

    if comparador(first_competitor, second_competitor) == 0 and chute == "a":
        print("You got it")
        print(f"{first_competitor[1]} with {first_competitor[2]} views is more acessed is more acessed than {second_competitor[1]} with {second_competitor[2]} views")
        points += 1
        second_competitor = first_competitor
        print(f"you have {points} points")

    elif comparador(first_competitor, second_competitor) == 1 and chute == "b":
        print("You got it")
        print(f"{second_competitor[1]} with {second_competitor[2]} views is more acessed is more acessed than {first_competitor[1]} with {first_competitor[2]} views")
        points += 1
        print(f"you have {points} points")

    else:
        print(f"you have {points} points")
        print("you lost the game")
        rodando = False
        break
