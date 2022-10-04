print("Welcome to Tip calculator")
total = float(input("What was the total bill? $"))
tipperc = int(input("What percent tip would you like to give? 10, 12 or 15? "))
no = int(input("How many people to split the bill? "))
new_total = total * (1+(tipperc/100))
each_person = new_total / no
k = "{:.2f}".format(each_person)
#or k = round(each_person,2)
print("Each person should pay :$"+str(k))