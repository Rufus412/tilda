from lib import *
import csv
drama1 = Drama("k1", 12, ["peter", "oskar"],
               12, "kdrama", "peter",
               "oskar", 2012, 12, "kanal 12")

drama2 = Drama("k2", 11, ["peter", "oskar"],
               12, "kdrama", "peter",
               "oskar", 2012, 12, "kanal 12")

print (str(drama1))
print (str(drama2))

print (repr(drama1))

drama1.add_episode(78, ["lisa", "peter"])

print (repr(drama1))

print ( drama1 < drama2)