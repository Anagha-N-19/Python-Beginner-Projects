print("Welcome to treasure Island.\n Your mission is to find the treasure.")
i1 = input("Left or Right ")
if i1!="Left":
    print("Fall into a hole.\nGane Over.")
else:
    i2 = input("Swim or Wait ")
    if i2!="Wait":
        print("attacked by trout.\nGame Over.")
    else:
        i3 = input("which Door? Red, Blue, Yellow? ")
        if i3=="Red":
            print("Burned by fire.\nGame Over")
        elif i3=="Blue":
            print("Eaten by beasts.\nGame Over")
        elif i3=="Yellow":
            print('You Win')
        else:
            print("Game Over.")
