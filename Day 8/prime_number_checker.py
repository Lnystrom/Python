def prime_checker(number):
    """Function that is made to check if a number is prime or not"""
    if (number%2 == 0) or  (number%3 == 0) or  (number%5 == 0) or  (number%7 == 0):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
