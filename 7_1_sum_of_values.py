from functools import reduce
import operator

# Read data.
data = []
with open('float_values.txt','r') as file:
    for each_value in file:
        data.append(float(each_value.strip()))

# Find sum of data.
sum_value = reduce(operator.add, data)
print(sum_value) 
