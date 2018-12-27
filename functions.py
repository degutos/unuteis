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