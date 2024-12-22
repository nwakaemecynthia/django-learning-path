# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 


# Simple tuple
fruit_tuple_basic = ('Apple', 'Orange', 'Mango')

# Using constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# Get length of tuple
print(len(fruit_tuple_2))

# You cant delete inidivual item in a tuple but you can delete the whole tuple
del fruit_tuple_2

 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

# Check if in set
print('Apple' in fruit_set)
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

print(fruit_set)

# Delete set
del fruit_set