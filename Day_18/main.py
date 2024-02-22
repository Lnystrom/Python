from turtle import Turtle, Screen

#para saber como usa deve-se pesquisar a documentação da API
#é uma boa ideia utilizar StackOverflow
#aparência
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("honeydew2")

#movimentação
timmy_the_turtle.forward(300)
timmy_the_turtle.right()

#isso deve ocorrer depois de criar a tartaruga
screen = Screen()
screen.exitonclick() #função
