# Import Random Module that will be used for using the random function
from random import Random, random

# Define number guesser method that accepts no parameters


def guessTheNum():
    # Print out a welcome statement and lower and upper bounds of the guess
    print('Welcome to Guess The Number! \nI am thinking of a number between 1 and 30. \nCan you guess what it is?')
    # Initlize a variable that is set equal to the random number that the user has to try to guess
    answer = Random.randint(1, 30)
    # Asks the user to enter a number and initilize a variable that is equal to the user input
    # If guess is too high, ask them to enter another guess
    # If guess is too low, ask them to enter another guess
    # If the user input and the random number are the same then print a statement saying they got it right


guessTheNum()
