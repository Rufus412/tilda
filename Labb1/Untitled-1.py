import csv

with ('kdramaMini.txt', 'r') as file:
    lines = csv.reader(file)
    for row in lines:
        print(', '.join(row))