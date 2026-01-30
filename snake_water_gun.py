# Snake Water Gun Game
# Author: Sunil
# Description: A simple CLI-based Snake Water Gun game using Python
# Date: 27 Jan 2026

'''
 1 for Snake
-1 for Water
 0 for Gun
'''

import random

computer = random.choice([-1, 1, 0])

print("Enter your choice:")
print("1 for Snake")
print("-1 for Water")
print("0 for Gun")

you = int(input("Enter your choice: "))

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")

elif computer == -1 and you == 1:
    print("You win!")

elif computer == 1 and you == -1:
    print("You lose!")

elif computer == 0 and you == 1:
    print("You lose!")

elif computer == 1 and you == 0:
    print("You win!")

elif computer == -1 and you == 0:
    print("You lose!")

elif computer == 0 and you == -1:
    print("You win!")

else:
    print("Something went wrong!")
