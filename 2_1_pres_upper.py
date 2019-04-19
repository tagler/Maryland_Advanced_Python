# Exercise 2-1

# Read filename and parse last names.
last_names = []
with open('presidents.txt','r') as file:
    for each_line in file:
        each_line_split = each_line.split(':')
        last_names.append(each_line_split[1])

# List comprehension to uppercase letters.
last_names_upper = [each_last_name.upper() for each_last_name in last_names]

# Print out names.
for each_last_name in last_names_upper:
    print(each_last_name)
