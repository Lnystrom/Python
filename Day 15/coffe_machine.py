import menu
def beverage(bebida, lista_de_bebidas, moedas_entra):
    """This functions shows the drink, its cost and """
    #this section is related to money
    money_cost = lista_de_bebidas[bebida]["cost"]
    print(money_cost)
    money_client = moedas_entra["quarters"]*0.25 + moedas_entra["dimes"]*0.10 + moedas_entra["nickles"]*0.05 + moedas_entra["pennies"]*0.01
    print(money_client)
    if money_client == money_cost:
        print("There we go")
        global profit
        profit += money_cost
        return 1
    elif money_client > money_cost:
        troco = round(money_client - money_cost, 2)
        profit += money_cost
        print(f"There we go, here's your change {troco}")
        print(troco)
        return 1
    #this section is related to the machine resorces
    machine_resources["Water"] -= lista_de_bebidas[bebida]["ingredients"]["water"]
    machine_resources["Coffe"] -= lista_de_bebidas[bebida]["ingredients"]["coffee"]
    machine_resources["Milk"] -= lista_de_bebidas[bebida]["ingredients"]["milk"]
    for resource in machine_resources:
        if resource < lista_de_bebidas[bebida]["ingredients"][resource]:
            print(f"Sorry, we're out of {resource}")
   
    print(machine_resources)
    
profit = 0
moedas_cliente = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
}

machine_resources = {
    "Water": 500,
    "Milk": 250,
    "Coffe": 100,
    "Money": profit
}

RODANDO = True
while RODANDO is True:
    decision = input("What would you like? (espresso/latte/cappuccino/report/off) ")
    if decision == "off":
        RODANDO = False
    elif decision == "report":
        print(f" Water: {machine_resources['Water']}ml \n Milk:{machine_resources['Milk']}ml \n Coffee:{machine_resources['Coffe']}g \n Money:{machine_resources['Money']}")
    else:
        print("Please insert coins")
        for coin in moedas_cliente:
            moedas_cliente[coin] = int(input(f"How many {coin} do you want to insert? "))
        beverage(decision, menu.MENU, moedas_cliente)
        for coin in moedas_cliente:
            moedas_cliente[coin] = 0
