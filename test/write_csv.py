import csv

data = [
    ['Name', 'Alter'],
    ['Max', 25],
    ['Anna', 30],
    ['Peter', 35]
]

with open('dateiname.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)