# Exercise 2-3

# Generator function to read data line by line. 
def pres_gen(filename):
    with open(filename,'r') as file:
        for each_line in file:
            each_line_split = each_line.replace('\n','').split(':')
            last_name = each_line_split[1].upper()
            first_middle_name = each_line_split[2].upper()
            yield f'{last_name} {first_middle_name}'

# Test generator
filename = 'presidents.txt'
for each_pres in pres_gen(filename):
    print(each_pres)




