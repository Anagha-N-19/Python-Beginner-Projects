#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?\n")) 
s = int(input(f"How many symbols would you like?\n"))
n = int(input(f"How many numbers would you like?\n"))
l1=""
s1=""
n1=""
for i in range(0,l):
    rl = random.randint(0,len(letters)-1)
    l1 = l1 + str(letters[rl])
for i in range(0,s):
    rl = random.randint(0,len(symbols)-1)
    s1 = s1 + str(symbols[rl])
for i in range(0,n):
    rl = random.randint(0,len(numbers)-1)
    n1 = n1 + str(numbers[rl])
l1 = l1+s1+n1
word = list(l1)
random.shuffle(word)
s=""
for i in word:
    s+=i
print(s)
 

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P