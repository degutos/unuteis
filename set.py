# set is unorder not repetable value

myset = set() # creating variable and setting as set
myset.add(1)  # adding value to a set
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset) # we can not add same value again. Set doesn't allow us to add twice

# Creating a list with repeted numbers and set them to get not repeted value
mylist = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]

print(set(mylist)) # will not show same number twice

