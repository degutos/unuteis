# Functions homework and exercices

# write a function that computes the volume of a sphere given its radius

import string


def vol(rad):
    v = (4 / 3) * 3.14 * (rad * rad * rad)
    return v


rad = vol(6)

print(rad)


#########################################

# function that checks whether a number is in a given range


def ran_check(num, low, high):
    list_range = []
    for x in range(low, high + 1):
        list_range.append(x)
    print(list_range)
    if num in list_range:
        return True
    else:
        return False


boo_result = ran_check(1, 1, 20)

print(boo_result)


####################################################

# Function that accepts a string and calculate number of upper case and lowe case letters
# sample: 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Uppercase: 4
# Lowercase: 33

def uplow(s):
    # s = s.replace(" ","") # function to remove all spaces - not necessary here
    # removing all special character including spaces with this func
    s = ''.join(filter(str.isalnum, s))
    # setting up new variables and assigning 0 value
    uppercase = 0
    lowercase = 0
    #
    for x in range(len(s)):

        if s[x].isupper():
            print(f'upper {s[x]}')
            uppercase += 1
        else:
            print(f'lower {s[x]}')
            lowercase += 1
    return uppercase, lowercase


uppercase, lowercase = uplow('Hello Mr. Rogers, how are you this fine Tuesday?')

print(uppercase)
print(lowercase)

###################################

# another way of sum uppercase and lowercase

message = input("Type word: ")
print("Capital Letters: ", sum(1 for c in message if c.isupper()))
print("Lower case Letters: ", sum(1 for c in message if c.islower()))

#######################################

# Function that takes a list and returns a new list with unique elements
# Sample List: [1,1,1,1,2.2.2,3,3,3,3,3,4,5]
# Return List: [1,2,3,4,5]


def unique_list(l):
    # set eleminites all duplicated number, allow only unique values
    l=set(l)
    # convert set into list
    my_list = list(l)
    print(my_list)


unique_list([1,1,1,1,2,2,2,2,2,3,3,3,4,5])


###########################################################

# Function multiply all numbers in a list

def multiply(numbers):
    acum=1
    for x in numbers:
        acum=acum*x
    print(acum)

multiply([2,2,3,2])