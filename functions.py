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
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

pig_word = pig_latin('word')
print(pig_word)


###################################################

# Find out if the word dog is in a string

def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

result = dog_check('the dog run away')

print(result)

print(dog_check('Dogs runs'))

##########################

# better way to compare the above if statement in one line
print('dog' in 'dog ran away')

##########################

# function with the above better way

def dog_check_better(mystring):
    return 'dog' in mystring.lower()


print(dog_check_better('dog ran away'))


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

def animal_crackers2(animal):
    '''
    Animal crackers 2 do the same above but receving two words in a single string
    '''
    animallist = animal.lower().split()
    print(animallist)
    return animallist[0][0] == animallist[1][0]


ret = animal_crackers2('Andre anna')
print(ret)


###################################################################

def make_twenty(num1,num2):
    '''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or
    if one of the integers is 20. If not, return False
    '''
    return num1 == 20 or num2 == 20 or num1 + num2 == 20


ret=make_twenty(10,10)
print(ret)

##############################################################################

def has_33(nums):
    '''This function receives a list of numbers and check if we find 3 and 3 next to each other '''
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            # if nums[i:i+2] == [3,3]: # This is another way of doing the same above
            return True
    return False


result = has_33([3,3,2,4,5,5,3])
print(result)



##########################################################################

# Function skyline
# Function receives a word and returns first caracter lower and second caracter as upper case and so on

#def my_func(word):

##########################################################################

def macdonald(word):
    '''
    This function receives a word and Captalize the first and the fourth letter
    '''
    firsthalf = word[:3]
    secondhalf = word[3:]
    print(firsthalf)
    return firsthalf.capitalize() + secondhalf.capitalize()


ret = macdonald('macdonald')
print(ret)

##########################################################################

def master_yoda(text):
    '''
    This function receives a phrase and return it reversed. Example: I am home -> home am I
    '''
    textlist = text.split()
    reverse_phrase = textlist[::-1]
    # using function join to join list in one string again
    return ' '.join(reverse_phrase)



ret = master_yoda('I am home')
print(ret)



###################################################################


# Function paper doll:
# This function receives a word and repeat 03 times every letter. Example:
# paper_doll('Hello') -> 'HHHeeellllllooo'

def paper_doll(word):
    new_word = ''
    for letter in word:
        new_word += letter*3
    return new_word


ret = paper_doll('Hello')
print(ret)


#####################################################################

# Function BlackJack
# Function receives 03 integers between 1 and 11. If their sum is less than or equal to 21, return
# their sum. If sum exceeds 21 and there is an eleven, reduce total sum by 10. Finally,
# if the sum exceeds 21 return 'BUST'


def blackjack(my_list):
    my_sum = sum(my_list)
    if my_sum > 21:
        if 11 in my_list:
            my_sum = my_sum - 10
        if my_sum > 21:
            return 'BUST'
        else:
            return my_sum
    else:
        return my_sum

ret = blackjack([10,5,11])
print(ret)

# Another way
def blackjack2(my_list):
    my_sum = sum(my_list)
    if my_sum > 21 and 11 in my_list:
        my_sum = my_sum - 10
    elif my_sum > 21:
        return 'BUST'
    return my_sum

ret = blackjack2([10,10,1])
print(ret)


