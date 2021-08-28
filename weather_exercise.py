# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem
import csv
from HashTable import *

with open('Resources/nyc_weather.csv', newline='') as file:
    reader = csv.DictReader(file)
    csv_tuple_list = []
    for row in reader:
        date = row['date']
        integer = int(row['temperature(F)'])
        csv_tuple = (date, integer)
        csv_tuple_list.append(csv_tuple)

print(csv_tuple_list)

t = HashTable()
for element in csv_tuple_list:
    key = element[0]
    value = element[1]
    t.set_item(key, value)

print(t.arr)



