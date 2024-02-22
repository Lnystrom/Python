from turtle import Turtle, Screen
from random import choice
#from turtle import * // Importa todas as classes dentro do módulo

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow

cores = ["purple", "black", "blue", "red", "green", "orange", "pink", "yellow"]


#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")


#movimentação
for side in range(3, 50):
    timmy_the_turtle.color(cores[(side - 3)%len(cores)])
    for walks in range(side):
        timmy_the_turtle.forward(25)
        timmy_the_turtle.right(360/side)
        


#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
