#generate random number
#check whether number is right or wrong
#difficulty function
#main fun
#ask for input

import random
#constants

easy_turns = 10
hard_turns = 5

def check_answer(random_value , guess, turns):
    if guess < random_value:
        print("your guess is too low")
        return turns - 1
    elif guess > random_value:
        print("your guess is too high")
        return turns - 1
    else:
        print("you have guessed correctly!!")
        return

def difficulty(diff_selection):
    if diff_selection == 'easy':
        return easy_turns
    elif diff_selection == 'hard':
        return hard_turns


# main func
def game():
    random_value = random.randint(1,100)
    print("WELCOME!!")
    diff_selection = input("Enter your difficulty : (easy)/(hard) ").lower()
    turns = difficulty(diff_selection)


    guess = 0
    while guess != random_value:
        guess = int(input("Guess the number!, please enter your number : "))
        turns = check_answer(random_value , guess , turns)
        print(f"remaining turns are {turns}")
        if turns == 0 :
            print("You're out of turns! you lost")
            print(f"Correct answer was {random_value}")
            return


game()