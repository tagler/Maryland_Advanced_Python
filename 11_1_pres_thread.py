import multiprocessing
import multiprocessing.dummy
from datetime import datetime
import time

# Generator function to read data line by line.
def pres_gen(filename):
    with open(filename,'r') as file:
        for each_line in file:
            each_line_split = each_line.replace('\n','').split(':')
            last_name = each_line_split[1]
            birth_date = each_line_split[3]
            inauguration_date = each_line_split[7]
            yield (last_name, birth_date, inauguration_date)

# List Comprehension of data. 
list_of_names_tuples = [each for each in pres_gen('presidents.txt')]*10000

# Function to calculate age in years at inauguration.
def age_at_inauguration(each_pres_tuple):
    birth_date = datetime.strptime(each_pres_tuple[1], '%Y-%m-%d')
    inauguration_date = datetime.strptime(each_pres_tuple[2], '%Y-%m-%d')
    return inauguration_date.year - birth_date.year

# Single processing.
start = time.time()
results = []
for each in list_of_names_tuples:
    results.append(age_at_inauguration(each))
print(time.time()-start)

# Multi-processing.
start_p = time.time()
pool_p = multiprocessing.Pool()
results_p = pool_p.map(age_at_inauguration, list_of_names_tuples)
print(time.time()-start_p)

# Multi-threading.
start_t = time.time()
pool_t = multiprocessing.dummy.Pool()
results_t = pool_t.map(age_at_inauguration, list_of_names_tuples)
print(time.time()-start_t)

