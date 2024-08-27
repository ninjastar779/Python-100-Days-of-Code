loan = 1000
interest_rate = 0.05
years = 10
interest = 0
for i in range(1, years + 1):
    interest = loan * interest_rate
    loan = loan + interest
    print(f"Year: " + str(i) + " Interest: " + str(interest) + " Loan: " + str(loan))
print(f"You will have to pay ${round((loan - 1000), 2)} in interest")