# I/O with Basic Files
# mode='r' # to read file
# mode='w' # to write a file or create a file
# mode='a' # to append a new content to the end of the file
# mode='w+' # to create and read a file

myfile = open('myfile.txt')
# print(os.system('pwd'))

# printing file content
print(myfile.read())

# System can not read twice
print(f'Reading second time {myfile.read()}')

# Reseting cursor to read again the file
myfile.seek(0)

print(f'Reading again {myfile.read()}')

# Reseting cursor to file line 0
myfile.seek(0)

# Reding file line by line with method .readlines()
print(myfile.readlines())

myfile.seek(0)
print(myfile.readlines())


# Closing file after using it to avoid issues
myfile.close()

# Another way of working with files - not necessary to close file at the end
with open('myfile.txt') as myfile:
    content = myfile.read()
    print(f'New way {content}')

with open('my_new_file.txt',mode='r') as f:
    print(f.read())

# Appending a new line to file with mode=a. It will always add to the end of the file.
# Don't forget to add new line with \n
with open('my_new_file.txt',mode='a') as f:
    f.write('\nFOUR ON FOURTH')

# Reading file again with new line added
with open('my_new_file.txt',mode='r') as f:
    print(f.read())

# Creating a new file xyz.txt with mode=w
with open('xyz.txt',mode='w') as f:
    f.write('I created this file with the python!')

# Displaying new file content
with open('xyz.txt',mode='r') as f:
    print(f.read())




