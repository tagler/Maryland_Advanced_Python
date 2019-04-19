from collections import namedtuple
import pickle

# Namedtuple object constructor. 
President = namedtuple('President', ['lastname', 
                                     'firstname', 
                                     'birthplace', 
                                     'birthdate', 
                                     'party'])

# Import data.
data_input = pickle.load(open('pres_data.pkl','rb'))

# Display data.
for each_president in data_input:
    print(f'{each_president.firstname} {each_president.lastname}, {each_president.party}')

