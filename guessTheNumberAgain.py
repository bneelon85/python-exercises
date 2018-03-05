import random

secretNumber = random.randint(1,10)
#count = 0

#print("I am thinking of a number between 1 and 10...")
#print("You have 5 guesses left.")
#guess = int(input("What's the number? "))
again = 'Y'

while(again.upper() == 'Y'):
    count = 0
    print("I am thinking of a number between 1 and 10...")
    print("You have 5 guesses left.")
    guess = int(input("What's the number? "))
    while(count <5):
        if(count == 4):
            print("You ran out of guesses.")
            break
        elif(guess<secretNumber):
            count += 1
            print(guess,"is too low.")
            print("You have",5-count,"guesses left.")
            guess = int(input("What's the number? "))
        elif(guess > secretNumber):
            count += 1
            print(guess,"is too high.")
            print("You have",5-count,"guesses left.")
            guess = int(input("What's the number? "))
        elif(guess == secretNumber):
            print("You Win!")
            break
    again = input("Do you want to play again?(Y or N)? ")
print("Bye!")
