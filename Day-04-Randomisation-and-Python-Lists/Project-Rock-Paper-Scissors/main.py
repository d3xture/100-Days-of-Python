import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

options = ["rock", "paper", "scissors"]
game_images = [rock, paper, scissors]

user_choice = input("Enter your choice: (rock, paper, scissors) ").lower()
print("You Chose")
print(game_images[options.index(user_choice)])

computer_choice = random.choice(options)
print("Computer Chose")
print(game_images[options.index(computer_choice)])

if user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose!")

elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")

elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")

else:
    print("It's a draw!")
