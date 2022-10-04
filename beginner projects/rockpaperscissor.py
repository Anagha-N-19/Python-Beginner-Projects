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
l = [rock,paper,scissors]
print(rock,"\n",paper,"\n",scissors)
print("Rock Paper Scissor game")
i = int(input("Enter 0 for rock, 1 for paper and 2 for scissors "))
r = random.randint(0,2)
d = {"Rock":rock,"Paper":paper,"Scissors":scissors}

keys_list = list(d)
key = keys_list[r]
if i == r:
    print("computer chose",key)
    print(l[r])
    print("You Win")
elif i>2 or i<0:
    print("Enter only valid values")
else:
    print("Computer chose",key)
    print(l[r])
    print("You lose")
