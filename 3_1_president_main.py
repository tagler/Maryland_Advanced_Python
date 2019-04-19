# Exercise 3-1

from president import President

# Tests President object class. 
for term in 1, 26, 39, 45:
    p = President(term) 
    print("{} {} was born at {}, {} on {}".format(p.first_name, 
                                                  p.last_name,
                                                  p.birth_place,
                                                  p.birth_state, 
                                                  p.birth_date))
    print()
