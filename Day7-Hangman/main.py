from hangman_art import stages, logo               # importing ASCII art and logo
from hangman_words import word_list                # importing word list
import random                                      # Random Module

chosen_word = random.choice(word_list)             # chosen word stored in variable      
correct_guesses = []                               # created list to store length of underscore(_)
chosen_word_list = []                              # created list to store list of chosen word
lives = 6                                          # defined number of lives
print(logo)                                        # printing logo

for i in chosen_word:                              # looped chosen_word 
    correct_guesses.append("_")                    # appended length of underscores in correct_guesses list
    chosen_word_list.append(i)                     # appened chosen_word elements to the chosen_word_list
print(correct_guesses)                             # Printed list of correct_guesses ["_", "_", "_"]


while  lives > 0:                                  # Run while loop until lives become 0
    guess = input("Guess The Letter :").lower()    # taken input from the user
    position = 0                                   # defined position for indexing to assign guess in the correct index
    
    if guess in correct_guesses:                   # checking if user has guessed same as previous letter
        print(f"You've already guessed {guess}")   # notifying user using print statement
        
    for letter in chosen_word:                     # Ran for loop with chosen_word and assigned every list to the variable letter
        if guess == letter:                        # Checking if the guess is equal to letter
            correct_guesses[position] = letter     # if above condition is true then modify correct_guesses list and assign letter to the positon index
        position += 1                              # incrementing the position by 1 to get correct index position
    
    if not guess in chosen_word_list:              # if guess element not in chosen_word_list then 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1                                 # decrease lives by 1
        if  lives == 0:                            # if lives become 0 then
            print("You lose!")                     # print You lose
            print("Game over!")                    # print game over
            
                               
    print(f"{' '.join(correct_guesses)}")          # printing correct_guesses
    print(stages[lives])                           # print the ASCII art by using lives as index position
    
    if chosen_word_list == correct_guesses:        # when chosen_word_list become same as correct_guesses then
        lives = 0                                  # assign 0 to lives variable to exit the loop
        print("You win!")                          # printing You win                      