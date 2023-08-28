# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#how to create a virtual envirionment: python -m venv C:\Users\apleu\Desktop\Python\Python\Day_16\venv ->  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process ->  
# venv\scripts\activate  -> pip install PrettyTable

from prettytable import PrettyTable

table = PrettyTable() #object created from this prettytable class
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) #called the method on object
table.add_column("Pokemon Type", ["Eletric", "Water", "Fire"])
table.align = "l" #atribute
table.border = True

print(table)