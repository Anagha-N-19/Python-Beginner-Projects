import random
import hangmanpics
import hangmanwords

#from hangmanwords import w

w = hangmanwords.w
k = random.choice(w)
n = len(k)
print(hangmanpics.logo)
lives = 6

d = []
for _ in range(n):
    d += "_"

flag = False

while not flag:
  guess = input("Guess a letter: ").lower()
      
  for i in range(n):
    if k[i] == guess:
      print("Right choice")
      d[i] = k[i]

  if guess not in k:
    lives -= 1
    if lives == 0:
      flag = True
      print("You lose.")
      print("The right answer was",k)

  if flag == False:
    print(f"{' '.join(d)}")
  
  if "_" not in d:
    flag = True
    print("You win.")
  
  print(hangmanpics.stages[lives])