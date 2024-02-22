from turtle import Turtle, Screen
#from turtle import * // Importa todas as classes dentro do módulo

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow



#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("honeydew2")

#movimentação
for _ in range(30):
    timmy_the_turtle.forward(30)
    if _%2 == 0:
        timmy_the_turtle.pendown()
    else:
        timmy_the_turtle.penup()
   

#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
