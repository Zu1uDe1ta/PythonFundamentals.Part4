print("Give me a number between 1 and 10!")
number = int(input())
from random import randrange
random_number = (randrange(1, 11))

def comparison(random_number, number):
    while True:
        if random_number > number:
            print("Too low")
            print("Give me a number between 1 and 10!")
        elif random_number < number:
            print("Too high")
            print("Give me a number between 1 and 10!")
        elif random_number == number:
            print("Awesome!")
        break
