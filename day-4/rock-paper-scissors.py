# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

#Write your code below this line 👇

choices = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_choice = int(player_choice)
cpu_choice = random.choice(choices)

print(choices[player_choice])
print(f"CPU CHOSE: {cpu_choice}")

if (player_choice == 1 and cpu_choice == rock) or (player_choice == 2 and cpu_choice == paper) or (player_choice == 0 and cpu_choice == scissors):
  print("YOU WIN")
elif (player_choice == 0 and cpu_choice == paper) or (player_choice == 1 and cpu_choice == scissors) or (player_choice == 2 and cpu_choice == rock):
  print("YOU LOSE")
else:
  print("DRAW")