#### here some useful tips

### Generating numbers

# printing from 0 to 10
for num in range(0,11):
    print(num)

# printing from 0 to 10 only even
for num in range(0,11,2):
    print(num)

# generating a list of range
print(list(range(0,11)))

### Inumerators

# normal way

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}' .format(index_count,letter))
    index_count += 1


# another way

index_count = 0

word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

# enumarating - this will generate a tuple with index and value
word = 'abcde'

for item in enumerate(word):
    print(item)

# enumarate with each variable

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

### Zip function - concatenate two list into one tuples

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

# zip into a list
print(list(zip(mylist1,mylist2)))

# cool way of checking if 'a' is in a phrase
print('a' in 'a world')


# checking dictionaries
d = {'mykey': 345}
print(345 in d.values())
print('mykey' in d.keys())


### working with random and shuffle

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

# random integer
from random import randint
print(randint(1,100))


### input

# interact with user
x = input('Enter with a number: ')
print(x)
print(type(x))
x= int(x)
print(type(x))


############################
### comprehensions

# normal way
mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist)

# working on a different way
mylist = []
mylist = [letter for letter in mystring]

print(mylist)

mylist2 = [x for x in 'myword']
print(mylist2)

# printing even numbers
mylist = [num for num in range(0,11) if num % 2 == 0]
print(mylist) # printing only even

### converting celcius to fahrenheit
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# another way
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)



