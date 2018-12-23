# Tuples are very similar to lists although I can not re-assign value to a tuple
# Not able to reassign values like my_tuple[0] = 'NEW_VALUE'

# Checking the difference between Tuples and List
tup = (1,2,3)
lis = [1,2,3]
print(type(tup))
print(type(lis))

# Checking how many objects the tuple has
print(len(tup))

my_tuple = ('zero',1,2,3,4,5) # tuples can manage different types
print(my_tuple) # printing tuples
print(my_tuple[0]) # printing tuple position 0
print(my_tuple[-1]) # printing last position with -1

# Counting how many times a value 'a' appears on a tuple
my_tuple = ('a','a','b','c')
print(my_tuple.count('a'))

# Checking what index specific word has
print(my_tuple.index('b')) # will return the position of specific word






