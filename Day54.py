import csv

with open("Day54Totals.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = list(reader)

total = 0
for row in data:
    total += float(row[0]) * int(row[1])

print(f"Total: {total}")