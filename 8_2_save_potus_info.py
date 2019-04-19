from collections import namedtuple
import pickle

# Namedtuple object constructor. 
President = namedtuple('President', ['lastname', 
                                     'firstname', 
                                     'birthplace', 
                                     'birthdate', 
                                     'party'])

# Read data.
data = []
with open('presidents.txt','r') as file: 
    for each_line in file:
        each_line_split = each_line.strip().split(':') 
        each_president = President(each_line_split[1], 
                                   each_line_split[2], 
                                   each_line_split[6], 
                                   each_line_split[3], 
                                   each_line_split[9])
        data.append(each_president)
print(data)

# Export data.
pickle.dump(data, open('pres_data.pkl','wb'))


