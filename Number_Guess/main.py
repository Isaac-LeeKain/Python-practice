import os
import random

from art import logo


# TODO:Create times fuction according to level
def level_times(level):
    return 10 if level == "easy" else 5


# TODO:Create check fuction
def check_number(guess, result):
    if result - guess > 0:
        print("Too low.\n")
        return False
    elif result - guess < 0:
        print("Too high.\n")
        return False
    else:
        print(f"You win. The right number is {result}.\n")
        return True


os.system("cls")
print(logo)
print("Guess a number between 1 and 100.")
# TODO:random a result and store it in a variable
result_numner = random.randint(1, 100)

# TODO:choose a level, give it to a level variable
level = input("choose a level, easy or hard\n").lower()
times = level_times(level)

# TODO:while loop with level variable times, input a variable
while times > 0:
    print(f"You have {times} attempts remaining to guess the number.\n")
    guess_number = int(input("Make a guess: "))
    # TODO:check variable is equal to result or not
    if flag := check_number(guess=guess_number, result=result_numner):
        break
    times -= 1
    if times == 0:
        print(f"You lose.The right number is {result_numner}.\n")
