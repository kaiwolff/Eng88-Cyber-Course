# Magic number Game!
Timing:

40-60 Minutes

## Summary
This is a sequel to your previous Magic Number Program, Welcome to the MAGIC NUMBER GAME!

This time we'll increase complexity up a notch to use other things such as:

libraries
control flow
conditions
while loops
Read the user stories.

Task
The following are the user stories

### User story 1 - As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.



I use the command ```target = random.randint(1, range)``` to generate a random number, having imported the ```random``` library at the beginning of the program. (I will show the full code block in the relevant user story later. To enable repeat guesses, the guess-taking process and most other functionality is embedded in a while loop. Before the while loop, I initialise some variables, which I will discuss during the relevant user story.


Now, I want to take user input as a guess, and check whether the input is in a usable format. The below code block achieves this by calling a fucntion called ```positive integer```, which returns True if the number is a positive integer:

```
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
   ```
The function positive_integer was used later for the range as well, which is why I packaged it as below:

```
def positive_integer(var):
    #check that an input is a positive integer. Return true if it is, otherwise return False
    if var.isdigit() and int(var) >= 1:
        return True
    else:
        return False
```
### 2 - As a user, I should get feedback if my number is too high or too low so I can adjust my guess.



### 3 - as a user I should only be able to guess 3 times before a new number is generated
As these stories tie in the same code block as the previous user story, I have included the relevant code below. The if statements are similar to how they would be for User Story 1, except that I am adding the contingencies for too low or too high guesses. The variables guess_counter and overall_guesse go up once the guess has been evaluated. overall_guesses and win_counter are used in later user stories.

```
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
```

For User Story 3, I added a check to see if the number of guesses had reached or exceeded 3:
```
    if guess_counter >= 3
        print(f"Bad Luck, unfortunately you are out of guesses. The number was {target}")
        game_over = True
        loss_counter += 1
```
### 4 - as a user, I should be able to keep playing until I respond with exit
To address this, I added a code block at the end of the loop that occurs if the game_over condition is true (triggered either by the correct guess being made, or by the maximum number of guesses being reached):

```
    if game_over == True:
        play_again = input("Type exit to quit, or anything else to continue: ")
        if "exit" in play_again.lower():
            break
        else:
            new_game = true
```
Setting the variable new_game to True triggers a code block at the beginning of the while loop, creating a new guessable number. I will show this block as part of user story 7

### 5 - as a user, I should be able to use exit in a sentence and still terminate the program

I completed this user story by usign the ```in``` command. An example of this is my guess-taking prompt, which is followed by the statement:

```    
if "exit" in guess:
        break
```
the ```break``` statement causes the while loop to quit, terminating the program
### extra 6 - as a user, when I terminate the program I should get a message thanking me for playing and the number of times I guesses and number of times I found the number.

To address this story, I added some counters, which are initialised before the while loop begins:

```

overall_guesses = 0
win_counter = 0
loss_counter = 0
range = 10
new_game = True
```
The counters iterate with every guess, win, or loss, but are not reset inside the while loop like the guess_counter variable. This means they will keep track throughout the whole program run. After the while loop is terminated, the following statement shows the final score:

```
print(f"Thank you for playing!\nYou guessed a total of {overall_guesses} times, with {win_counter} wins and {loss_counter} losses.")
```

### Extra 7 - as a user, I should be asked the highest number that can be used to generate a random number

This user story gives me an excuse to show a code block at the beginning of my while loop:

```
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

```

The variable new_game is set to True before the while loop is initiated, and set back to true every time the user chooses to continue playing. I reused the ```positive_integer``` function here to force the user to input a proper range. I also gave the user the option to exit here.

# self five
Acceptance Criteria
random number is generated by random library
all core 5 user stories should be done
program should not break when given strings
program should use while loop