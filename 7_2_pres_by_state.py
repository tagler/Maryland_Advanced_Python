from collections import Counter
from itertools import groupby

# Read data.
data = []
with open('presidents.txt','r') as file: 
    for each_line in file: 
        data.append(each_line)

# Extract states.
states = list(map(lambda x: x.strip().split(':')[6], data))

# Count most frequent values via Counter.
freq = Counter(states)
print(freq)

# Count values via groupby()
for state, items in groupby(sorted(states)):
    print(state, len(list(items)))





