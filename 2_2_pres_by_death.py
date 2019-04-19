# Exercise 2-2

from datetime import datetime

# Read filename and parse data.
pres_data = []
with open('presidents.txt','r') as file:
    for each_line in file:
        each_line_split = each_line.replace('\n','').split(':')
        last_name = each_line_split[1]
        first_name = each_line_split[2].split(' ')[0]
        dob =  each_line_split[3]
        party = each_line_split[-1]
        pres_data.append((last_name, first_name, dob, party))

# Sort data by date of birth.
pres_data_sorted = sorted(pres_data, key= lambda x : datetime.strptime(x[2], '%Y-%m-%d'))

# Print results.
for each in pres_data_sorted:
    print(f'Name: {each[1]} {each[0]}; DOB: {each[2]}, Party: {each[3]}')


