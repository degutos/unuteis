### Map, Filter and Lambda


# main function
def square(num):
    return num**2


# Interacting with a List in a normal way using looping
my_nums = [1, 2, 3, 4, 5]


result_list = []  # creating a list to receive the return
for x in my_nums:
    result = square(x)
    result_list.append(result)

print(result_list)

# This example will print out the return value without list
for x in my_nums:
    print(square(x))

##### Map ######

# map with list
my_list = list(map(square,my_nums))
print(my_list)

# map with item
for item in map(square,my_nums):
    print(item)


# Another example with Map

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'


names = ['Andy', 'Eve', 'Sally']

mylist = list(map(splicer,names))
print(mylist)


### Filter ###

# Filter is used when you need interact with all items in a list but return only True or False

def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

#  using filter function
my_list = list(filter(check_even, mynums))
print(my_list)

# interacting with for and filter function
for n in filter(check_even, mynums):
    print(n)


### Lambda ###

# Lambda is to used only once, not like function which can be used and called many times

square = lambda num: num ** 2

print(square(6))


# using lambda with map function
mylist = list(map(lambda num: num ** 2, mynums))
print(mylist)

# using lambda with filter function
mylist = list(filter(lambda num: num % 2 == 0, mynums))
print(mylist)

###############################
# Another lambda example
# Lets return first letter for each name

names = ['Andy', 'Eve', 'Sally']

my_list = list(map(lambda name: name[0], names))

print(my_list)

