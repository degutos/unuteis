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


#############################################

# Another way of doing the above exercise
# function that checks whether a number is in a given range

def ran_check2(num, low, high):
    if num in range(low, high+1):
        print(f'The number {num} is between your range from {low} to {high}')
    else:
        print(f'The number {num} is not between your range from {low} to {high}')



ran_check2(11,1,10)

####################################

# If we want return just boolean for the above exercise
def ran_check_bol(num, low, high):
    return num in range(low, high + 1)

print((ran_check_bol(1,1,10)))


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

message = 'This is a simple Test'
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


##############################################################

# Function palindrome, receives a string and return if it's palindrome or not.
# example of palindrome: helleh, madam, nurses run

def palindrome(s):
    if s.replace(" ","") == s[::-1].replace(" ",""):
        return True
    else:
        return False


print(palindrome('nurses run'))

##############################################################

# Pangrams are words or sentences containing every letter of the alphbet at least once.
# For example: The quick brown fox jumps over the lazy dog
# We need `import string` modules

def inspangram(str1, aphabet=string.ascii_lowercase):
    str1 = str1.replace(" ","")
    str1 = str1.lower()
    if aphabet in str1:
        print('Truee')



inspangram('The quick brown fox jumps over the lazy dog')