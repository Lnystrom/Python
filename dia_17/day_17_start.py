class User:
    # def __init__(self): #called evertytime that a new object from this class is created
    #     print('new user is being created')
    # #pass #initializing objects
    
    # # def __init__(self, seats): (objeto, parâmetros)
    # #     self.seats = seats

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User('Nystrom', '2826') #criou user, from a user class, incializando com os values
user_2 = User('Luigi', '3274')

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)

#atributos = o que o objeto tem
#methods = o que o objeto faz, quando uma função é associada à um objeto

# class Car:
#     def enter_race_mode():
#         self.seats = 2

# my_car.enter_race_mode