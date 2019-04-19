from president import President

@property
def full_name(self):
    return f'{self.first_name} {self.last_name}'

# Set Attribute.
setattr(President, 'full_name', full_name)

# Test Attribute. 
first_pres = President(1)
print(first_pres.full_name)
