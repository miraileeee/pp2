import random
def guess_game():

    name = input("Hello! What is your name?")
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    input("Take a guess.")
    num = random.randrange(1, 20)
    guess_times = 0
    while True:
        guess = int(input())
        guess_times += 1
        if guess > num:
            print("Your guess is too high")
        elif guess < num:
            print("Your guess is too low")
        else: 
            print("Good job, " + name + "! You guessed my number in " + str(guess_times) + " guesses.")
guess_game()