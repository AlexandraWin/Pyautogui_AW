import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    print ("Guess the number between 1 an 100!")
    guess = int(input())
    counter += 1

    if guess == number:
        print ("You Win!")
        print ("You Tried in " + str(counter) + " guesses.")
        break 
    elif guess > number:
        print ("Too High!")
    elif guess < number:
        print ("Too Low")

                
