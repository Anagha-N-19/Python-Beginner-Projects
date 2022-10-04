logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
k = "Yes"
d = {}
while(k == "Yes" or k == "yes"):

    name = input("Your name is: ")
    bid = int(input("Your bid is Rs."))
    k = input("Are there more bidders? ")
    d[name] = bid
    if k == "yes" or k == "Yes":
        os.system('cls')
os.system('cls')
r = max(d, key = d.get)
print("The highest bid is by",r,"for the amount",d[r])