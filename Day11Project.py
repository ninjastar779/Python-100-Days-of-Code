secondsInMinute = 60
minutesInHour = 60
hoursInDay = 24
DaysInYear = 365
year = int(input("Enter the year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    DaysInYear = 366

print(str(year) + " has " + str(DaysInYear*hoursInDay*minutesInHour*secondsInMinute) + " seconds")
