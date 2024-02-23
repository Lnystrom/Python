from turtle import Turtle, Screen
from random import choice, randrange
#from turtle import * // Importa todas as classes dentro do módulo

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow

cores = ["purple", "black", "blue", "red", "green", "orange", "pink", "yellow"]
directions = [0, 90, 180, 270]


#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("square")
timmy_the_turtle.speed(6)

for walk in range (0,100):
    timmy_the_turtle.pensize(randrange(10))
    timmy_the_turtle.color(cores[(walk)%len(cores)])
    timmy_the_turtle.right(choice(directions))
    timmy_the_turtle.forward(40)

#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
