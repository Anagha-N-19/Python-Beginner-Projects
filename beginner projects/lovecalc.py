print("Welcome to love calculator")
n1 = input("Nmae 1 ")
n2 = input("Name 2 ")
n1 = n1.lower()
n2 = n2.lower()
n = n1 + n2
c1=0
c2=0
s1 = "true"
s2 = "love"
for i in n:
    if i in s1:
        c1+=1
for i in n:
    if i in s2:
        c2+=1   

r = c1*10 + c2
if r<10 or r>90:
    print(f"Your score is {r}, you go together like coke and mentos.")
if r>40 and r<50:
    print(f"Your score is {r}, you are alright together.")  
elif (r>=10 and r<=40) or (r>=50 and r<=90):
    print(f"Your score is {r}.")