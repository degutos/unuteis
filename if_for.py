# If and For stuffs

#################################################
#### IF statement ###############################


# Working with if and else for boolean
hungry = True
# hungry = False

if hungry:
    print('Feed me!')
else:
    print('I am not hungry')



# Working if elif and else

loc = 'Bank'

if loc == 'Auto Shop':
    print('You are in a Auto Shop')
elif loc == 'Bank':
    print('You are in a bank')
elif loc == 'Store':
    print('You are in a Store')
else:
    print('Location not found')

#################################################
#### FOR statement ###############################



mylist = [1,2,3,4,5,6,7,8,9,10]

# simple for
for num in mylist:
    print(num)

# printing for and checking even and odd numbers
for num in mylist:
    # check if num is even
    if num % 2 == 0:
        print(f'The number {num} is even')
    else:
        print(f'The number {num} is odd')


# Working with sum list and accumulating value
list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)


# working with underscor variable when you don't need a variable
for _ in 'Hello World':
    print('Cool')


##############################################


# working with tuples and list
tup = (1,2,3,4)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]

for tup in mylist:
    print(tup)

# accessing indivuduals objects
for (a,b) in mylist:
    print(a)
    print(b)


##############################################
# working with dictionary

d = {'k1':10,'k2':20,'k3':30}

# showing default option when using for statement in dictionaries. It will show only the key
for item in d:
    print(item) # shows only the 'key'

# showing the value
for key,value in d.items():
    print(value)

# or
for value in d.values():
    print(value)
    