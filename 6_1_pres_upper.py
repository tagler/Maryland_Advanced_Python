# Generator function to read data line by line.
def pres_gen(filename):
    with open(filename,'r') as file:
        for each_line in file:
            each_line_split = each_line.replace('\n','').split(':')
            last_name = each_line_split[1]
            first_middle_name = each_line_split[2]
            yield (first_middle_name, last_name)

# Test List Comprehension 1.
list_of_names_tuples = [each for each in pres_gen('presidents.txt')]
print(list_of_names_tuples)

# Test List Comprehension 2.
list_of_names = [f'{each[0]} {each[1]}'.upper() for each in pres_gen('presidents.txt')]
print(list_of_names)
for each_name in list_of_names:
    print(each_name)
