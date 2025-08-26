from lib import *
import csv
dramas = []

def read_file(filename):
    with open(filename, "r") as file:
        lines = list(csv.reader(file))[1:]

        for line in lines:
            dramas.append(Drama(
                line[0],
                float(line[1]),
                [line[2]],
                float(line[3]),
                line[4],
                line[5],
                line[6],
                int(line[7]),
                int(line[8]),
                line[9],
            ))

def get_dramas_from_year(year) -> list:
    return [drama for drama in dramas if year == drama.year]

read_file("kdramaMini.txt")

print(dramas)

print (get_dramas_from_year(2017))

