import typing

# Type Hinting for input and output of function 
def grep(x: str, coll: typing.List[str]) -> str :
    '''returns only strings in list that contain x'''
    for each_string in coll:
        if x in each_string:
            yield each_string

# Test function.
for each in grep('o', ['apple','orange','pear']):
    print(each)

