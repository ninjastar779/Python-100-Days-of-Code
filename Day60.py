import datetime

today = datetime.date.today()

print("EVENTS COUNTDOWN")
print("-----------------")
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

event_date = datetime.date(year, month, day)

delta = event_date - today

delta = delta.days

if event_date < today:
    print(f"😭😭😭 You missed the event by {delta} days")
elif event_date == today:
    print("🥳🥳🥳🥳")
else:
    print(f"Coming soon in {delta} days")
