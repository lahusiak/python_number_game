import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    # limit to 5 guesses
    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
             print("{} is not a number!".format(guess))
        else:
            # compare quess to secret number
            # print hit/miss
            if guess == secret_num:
                print("You got it!")
                break
            # print "too low" or "too high"
            elif guess < secret_num:
                print("My number is higher than {}!".format(guess))
            else:
                print("My number is lower than {}!".format(guess))
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}.".format(secret_num))
    play_again = input("Would you like to play again? Y/n ")
    if play_again.lower() != 'n':
        game()


game()

# error if input is not an integer
