from random import randint

def guessanumber():
    print("Hello! What is your name?")
    name = input("name:")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")


guessanumber()