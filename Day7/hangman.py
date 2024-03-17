stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random                                     
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = ""
display = []
chosen_word_list = []
lives = 7

for i in chosen_word:
    display.append("_")
    chosen_word_list.append(i)
print(display)


while not guess == 'exit':
    guess = input("Guess The Letter :").lower()
    position = 0
    for letter in chosen_word:
        if guess == letter:
            display[position] = letter
        elif lives == 0:
            guess == 'exit'
            print("You lose.")
        else:
            lives -= 1
            print(stages[lives])
        position += 1     
           
    print(display)
    
    
    if chosen_word_list == display:
        guess = 'exit'
        print("You win.")
    
    
    print(lives)