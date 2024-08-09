#Tip Calculator
bill = float(input("What was the total bill?: "))
tip = float(input("How much tip would you like to give?: "))
people = int(input("How many people are you splitting the bill with?: "))

tip_value = (tip / 100) * bill
total_bill = bill + tip_value
each_person_pays = total_bill / people

print("Each person should pay: $" + str(round(each_person_pays, 2)))
