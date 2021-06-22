#firstly - will need random for the number to be guessed

import random

def positive_integer(var):
    #check that an input is a positive integer. Return true if it is, otherwise return False
    if var.isdigit() and int(var) >= 1:
        return True
    else:
        return False

#initialise game variables
overall_guesses = 0
win_counter = 0
loss_counter = 0
range = 10
new_game = True


while True:

    #if the game is new or the user asked for another game, set up a new random number
    #Thanks to new_game, this block should skip if the user inputs unsuitable content for the guess
    if new_game:
        # generate a random integer in a pre-set range.
        range = input("What's the highest number you would like? Please input an integer, or type exit to quit: ")
        if "exit" in range:
            break
        elif positive_integer(range) == True:
            range = int(range)
        else:
            print("input not recognised, please input a positive integer for the range")
            continue

        print("Generating new number")
        target = random.randint(1, range)
        # reset guess_counter, game_over, and new_game
        guess_counter = 0
        game_over = False
        new_game = False

    #take input and give option to quit.
    guess = input("\nPlease input your guess, as an integer. Type 'exit' to quit the game: ")

    #check guess formatting.
    if "exit" in guess:
        break
    elif positive_integer(guess):
        # convert guess to integer once for better readability
        guess = int(guess)

    else:
        print("input not recognised, please input a positive integer for the guess")
        continue

    #compare to target. tell whether too high and iterate guess counter. For bonus, iterate overall counters.
    if guess == target:
        print("Congratulations, you nailed it!")
        overall_guesses += 1
        win_counter += 1
        game_over = True

    elif guess > target:
        print("Too high")
        guess_counter += 1
        overall_guesses +=1

    elif guess < target:
        print("Too low")
        guess_counter += 1
        overall_guesses += 1

    #check number of guesses
    if guess_counter >= 3:
        print(f"Bad Luck, unfortunately you are out of guesses. The number was {target}")
        game_over = True
        loss_counter += 1

    #Check if user wants to quit if game is over
    if game_over == True:
        play_again = input("Type exit to quit, or anything else to continue: ")
        if "exit" in play_again.lower():
            break
        else:
            new_game = true

print(f"Thank you for playing!\nYou guessed a total of {overall_guesses} times, with {win_counter} wins and {loss_counter} losses.")