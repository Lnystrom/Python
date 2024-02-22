from turtle import Turtle, Screen

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow



#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("honeydew2")

#movimentação
for _ in range(4):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(90)

#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
