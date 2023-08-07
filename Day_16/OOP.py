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


x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"]) x.align["City name"] = "l" # Left align city names x.padding_width = 1
x.add_row(["Adelaide",1295, 1158259, 600.5])
x.add_row(["Brisbane",5905, 1857594, 1146.4]) 
x.add_row(["Darwin", 112, 120900, 1714.7])
print(x)