# Exercise 1-2

# Read data line by line and store value in dictionary.
states = {}
with open('presidents.txt','r') as file:
    for each_line in file:
        each_line_split = each_line.replace('\n','').split(':')
        state = each_line_split[6]
        try:
            states[state] = states[state] + 1
        except:
            states[state] = 1

# Order states.
states_sorted_order = sorted(states)

# Print Results.
for each_state in states_sorted_order:
    print( f'{each_state}: {states[each_state]}')

