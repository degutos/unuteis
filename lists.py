# Working with Lists and Formatting String

# Creating a simple list
my_list = [1,2,3]

# Here we have 03 ways of using print with variables
print('This is the content of my_list variable: {}' .format(my_list))
print('This is another way of doing the same: {l}' .format(l=my_list))
print(f'This is a different and new way: {my_list}')

# Printing specific position - starting from position 0
print('This is the 2nd position: {}' .format(my_list[1]))

# Printing the last position with [-1]
print('This is the last position: {}' .format(my_list[-1]))

# Counting how many itens there are in a list with function len()
print('There are {} item in the list'.format(len(my_list)))

# List also accept different types
my_diverse = ['STRING', 100, 99.9]

my_list = ['one','two','three','four']

# Printing from specific position to the end
print('Printing from position 2 to the end: {}'.format(my_list[1:]))

# Printing from position 2 and 3. For this we need represent 3 is the 4th item and it doesn't count on display and it will show till 3rd
print('Printing from position 2 to 3: {}'.format(my_list[1:3]))

# Concatenating another list
another_list = ['five','six']
print(f'Concatenating two lists: {my_list + another_list}')
print(f'Showing my list {my_list}')
print(f'Showing another_list {another_list}') # we still have both list

# Concatenating two lists and new list
new_list = my_list + another_list
print('Showing new list concatenated: {}'.format(new_list))

# Replacing one value on the list at position 0
new_list[0] = 'ONE'
print(new_list)

# Adding a new item to the end of the list with method .append()
new_list.append('seven')
print(new_list)

# Adding a new item to specific position with method .insert()
new_list.insert(0,'zero')
print(new_list)

# Deleting a item from the list with .pop()
new_list.pop()
print(new_list)

# Deleting a item from specific position on the list
new_list.pop(0)
print(new_list)

# Sorting a list with .sort(). This will change the list order in first place, you will lose the original sequence
new_list = ['a','m','x','e',]
new_list.sort()
print(new_list)

# Sorting reverse
new_list.reverse()
print(new_list)


