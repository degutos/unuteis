### Functions

def pig_latin(word):
    '''
    :param word:
    :return: pig_word
    :description: this function check if starts with vowel and add ay if not add first letter + ay
    example apple -> appleay
            word -> wordway
    '''
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word + first_letter + 'ay'
    return pig_word

pig_word = pig_latin('word')
print(pig_word)


###################################################

# function with no specific number of arguments - *args
def myfunc(*args):
    print(args)
    for num in args:
        print(num)

myfunc(10,10,20,30,50)

##########################################################

def myfunc(word):
    '''Function returns a word with first letter as lowercase and second
    letter as uppercase and so on till the end
    '''
    index_count = 0
    myword = ''
    for letter in word:
        if index_count % 2 == 0:
            myword = myword + letter.lower()
        else:
            myword = myword + letter.upper()
        index_count += 1
    print(myword)
myfunc('acknowledge')

########################################################################

'''
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
'''

def lesser_two_evens(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            return num2
        else:
            return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2

num = lesser_two_evens(2,5)
print(num)


### Another way

def lesser_two_events_new(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)

num_new = lesser_two_events_new(7,5)
print(num_new)

###################################################################

def animal_crackers(animal1, animal2):
    '''
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    '''
    str1 = animal1[0]
    str2 = animal2[0]
    if str1 == str2:
        return True
    else:
        return False

ret=animal_crackers('cat','bird')
print(ret)

##############################################################################

def make_twenty(num1,num2):
    '''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
    if one of the integers is 20. If not, return False
    '''
    if num1 == 20 or num2 == 20:
        return True
    elif num1 + num2 == 20:
        return True
    else:
        return False

ret=make_twenty(21,1)
print(ret)

##############################################################################

def has_33(nums):
    '''This function receives a list of numbers and check if we find 3 and 3 next to each other '''
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


result = has_33([3,3,4,5,5,3,])
print(result)

