# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Cynthia'
age = 31

# Concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position: ONLY AVAIABLE IN PY 3.6+
# print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age}'.format(name="Berry", age="Blessed"))
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')

# String Methods

s = 'HEllo tHeRe worlD'

# Capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('worlD', 'everyone'))

# Count
sub = "H"
print(s.count(sub))

# Starts with
print(s.lower().startswith('hello'))

# Ends with
print(s.endswith('d'))
print(s.endswith('D'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())