print("Welcome to Python Pizza Deliveries!")
s = input("What size pizza do you want? S, M, or L ")
p = input("Do you want pepperoni? Y or N ")
c = input("Do you want extra cheese? Y or N ")
pr = 0
if s == "S":
    pr=15
    if p=="Y":
        pr+=2
elif s == "M":
    pr=20
    if p=="Y":
        pr+=3
elif s=="L":
    pr=25
    if p=="Y":
        pr+=3
if c=="Y":
    pr+=1
print(f"Your final bill is: ${pr}.")
