from president import President

# New president object.
new_pres = President(1)

# Get attributes.
pres_last_name = getattr(new_pres, 'last_name')
pres_first_name = getattr(new_pres, 'first_name')
pres_party = getattr(new_pres, 'party')
print(f'{pres_first_name} {pres_last_name}, {pres_party}')
