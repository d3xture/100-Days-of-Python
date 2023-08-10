import random
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

end_of_game = False
words_list = ["mouse", "keyboard", "deodorant", "cabinet"]
chosen_word = random.choice(words_list)
length = len(chosen_word)
lives = 6

print(f"cheat {chosen_word}")

display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Enter a letter ").lower()

    for postion in range(len(chosen_word)):
        letter = chosen_word[postion]

        if letter == guess:
            display[postion] = letter 

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

