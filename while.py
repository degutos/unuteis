# While loop

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1

x = 0
while x < 5:
    print(x)
    x += 1
else:
    print('Not less than 5')

########################### pass, breaks and continue ########################

### pass = does anything just pass
### breaks = breaks the current loop
### continue = goes to the top of the closest enclosing loop

x = [1,2,3]

for item in x:
    # comment
    pass # pass does anything and avoid error if your for statement has no code inside it

print('End of code')


