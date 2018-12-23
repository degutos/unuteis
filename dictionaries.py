# This is examples of dictionaries
# Example:
# {'key1':'value1','key2':'value2'}

# Creating a dictionary and printing out
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])
print(my_dict['key2'])


# Creating new dictionary with prices
prices_lookup = {'apple':2.99,'oranges':1.99,'milk':3.99}
print(prices_lookup['apple'])
print(prices_lookup['milk'])

# Creating a Dictionary with a list inside
d = {'key1':['a','b','c']}
print(d) # printing dictionary
print((d['key1'])) # printing only key1 which is a list
print(d['key1'][2]) # printing only letter c on my list

# Printing only one letter inside the list and using method upper() to convert the letter
print(d['key1'][2].upper())


# Adding new key to a dictionary
d = {'k1':100,'k2':200}
print(d)
d['k3'] = 300
print(d)
d['k4'] = 400
print(d)

# Replacing a new value
d['k1'] = 'NEW VALUE'
print(d)

# Show only dictionary keys
print(d.keys())

# Show only values
print(d.values())

# Show all items - keys and values
print(d.items())
print()

