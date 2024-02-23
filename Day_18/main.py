from turtle import Turtle, Screen, colormode
import random
#from turtle import * // Importa todas as classes dentro do módulo

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow

directions = [0, 90, 180, 270]
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    arco_iris = (r, g, b)
    return arco_iris

#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("square")
timmy_the_turtle.speed(6)

for walk in range (0,100):
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.right(random.choice(directions))
    timmy_the_turtle.forward(40)

#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
