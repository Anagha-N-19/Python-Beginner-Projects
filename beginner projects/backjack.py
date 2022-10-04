logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
import os
import random

def dealcard():
    c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(c)
    return card
def calcscore(l):
    
    if sum(l) == 21 and len(l) == 2:
        return 0
    if 11 in l and sum(l) > 21:
        l.remove(11)
        l.append(1)
    return sum(l)
def compare(userscore, compscore):
    if userscore == compscore:
        return "Draw"
    elif compscore == 0:
        return "Lose, opponent has blackjack"
    elif userscore == 0:
        return "Win with blackjack"
    elif userscore > 21:
        return "You went over. You lose"
    elif userscore > compscore:
        return "You Win"
    else:
        return "You lose"
def playing():
    print(logo)
    userc = []
    comp = []
    g_over = False
    for _ in range(2):
        userc.append(int(dealcard()))
        comp.append(int(dealcard()))

    while not g_over:
        user_score = calcscore(userc)
        comp_score = calcscore(comp)
        print("user and comp scores are ",user_score,comp_score)
        print("The computer's first card is",comp[0])
        if user_score == 0 or comp_score > 21:
            g_over = True
        
        else:
            j = input("Do you want more cards?y or n ")
            if j == 'y' or j == "Y":
                userc.append(dealcard())
            else:
                g_over = True    
    while comp_score != 0 and comp_score < 17:
                comp.append(dealcard())
                comp_score = calcscore(comp)
    print("Your hand and score",userc,user_score)
    print("Computer's hand and score",comp,comp_score)
    print(compare(user_score,comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    playing()
