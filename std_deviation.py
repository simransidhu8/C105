from typing import ClassVar


import csv
import math
with open("data.csv", newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# finding mean
def mean(data) :
    n= len(data)
    total = 0
    for i in data:
        total = total + float(i)
    
    mean = total/n
    return mean

# subtracting mean and squaring the difference
squared_list= []
for number in data:
    x = int(number) - mean(data)
    x = x**2
    squared_list.append(x)

# sum of squares of differences
sum = 0
for d in squared_list:
    sum = sum + d

# divide the sum of number of values in the data set
result = sum/(len(data) - 1)

# square root of result 
std_deviation = math.sqrt(result)
print(std_deviation)