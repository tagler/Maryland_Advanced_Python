# Generator function to read data line by line.
def pres_gen(filename):
    with open(filename,'r') as file:
        for each_line in file:
            each_line_split = each_line.replace('\n','').split(':')
            last_name = each_line_split[1]
            first_middle_name = each_line_split[2]
            yield (first_middle_name, last_name)

# Test Generator Expression 1.
gen_names_tuples = (each for each in pres_gen('presidents.txt'))
for each in gen_names_tuples:
    print(each)

# Test Generator Expression 2.
gen_names = (f'{each[0]} {each[1]}'.upper() for each in pres_gen('presidents.txt'))
for each in gen_names:
    print(each)
