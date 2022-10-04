logo = """
 _____________________
|  _________________  |
| | Anagha's  Calc  | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
import os
#os.system('cls')
print(logo)
def addition(a,b):
    return a + b
def subtr(a,b):
    return a - b
def mult(a,b):
    return a*b
def divis(a,b):
    return a / b
k = 'n'
while k == 'N' or k ==  'n':
    a = float(input("Enter first number "))
    k = "y"
    d = {
        "+": addition,
        "-": subtr,
        "*": mult,
        "/": divis
        }
    for i in d:
        print(i,end=' ')
    print()
    op = input("Pick an operation ")
    b = float(input("Enter second number "))
    function = d[op]
    s = function(a,b)

    print(f"{a} {op} {b} = {s}")
    k = input(f"Enter y to continue with {s} and n to do new calculation ")
    while k == 'Y' or k == "y":
        op = input("Pick an operation ")
        b = float(input("Enter second number "))
        function = d[op]
        s1 = s
        s = function(s,b)
        print(f"{s1} {op} {b} = {s}")
        k = input(f"Enter y to continue with {s} and n to do new calculation ")

    os.system('cls')