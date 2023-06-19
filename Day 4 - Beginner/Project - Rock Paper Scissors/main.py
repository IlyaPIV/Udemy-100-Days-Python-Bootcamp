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
import random

ppl_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
comp_choise = random.randint(0, 2)

if ppl_choise == 0:
    print(rock)
elif ppl_choise == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
if comp_choise == 0:
    print(rock)
elif comp_choise == 1:
    print(paper)
else:
    print(scissors)

if (comp_choise == ppl_choise + 1) or (comp_choise == ppl_choise - 2):
    print("You lose")
elif (ppl_choise == comp_choise + 1) or (ppl_choise == comp_choise - 2):
    print("You win")
else:
    print("Draw")