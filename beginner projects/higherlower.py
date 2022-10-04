import random
from higherlowerdata import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

def randgener():
    r = {}
    r = random.choice(data)
    return r

def playing(k,n1,score):
    print(k['name'])
    c = randgener()
    while c['name'] == k['name']:
        c = randgener()
    n2 = c['follower_count']
    print(c['name'])
    i = input("A or B ") #A for n1
    if n1 > n2:
        m = n1
        d = k
    else:
        m = n2
        d = c
    if i == "A" and m == n1:
        score+=1
        playing(d,m,score)
    elif i == "B" and m == n1:
        print("You lose")
        print(k['name'],"was",n1,c['name'],"was",n2)
        print("Score =",score)
        return
    elif i == "A" and m == n2:
        print("You lose")
        print(k['name'],"was",n1,c['name'],"was",n2)
        print("Score =",score)
        return
    else:
        score+=1
        playing(d,m,score)
###########
print(logo)
while input("Do you want to play?y or n ") == "y":
    k = randgener()
    score = 0
    n1 = (k['follower_count'])
    #print(k)
    playing(k,n1,score)