import random

#emotess
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

# Conputer choosing emote
List = [rock, paper, scissors]
Comp= random.randint(0,2)

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

Answer = int(input(""))

print(List[Answer])
print(List[Comp])

if Answer == 0 and Comp == 2:
    print("You have won!!!")
elif Answer == 1 and Comp == 0:
    print("You have won")
elif Answer == 2 and Comp == 1:
    print("You have won")
elif Answer == Comp:
    print("DRWAAWWASDAWDWA")
else:
    print("You have lost")