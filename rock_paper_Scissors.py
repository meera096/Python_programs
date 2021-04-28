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

choice=int(input('enter your choice of weapon 0 for Rock ,1 for paper , 2 for scissors\n'))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

print('Computer chose:')
r=random.randint(0,2)
if r == 0:
  print(rock)
elif r == 1:
  print(paper)
else:
  print(scissors)

if choice != r:
  if choice == 0 and r == 1:
    print('You lose.Computer won')
  elif choice == 1 and r == 2:
    print('You lose.Computer won')
  else:
    print('You Win.Computer lost')
else:
  print('You are tied')
  
