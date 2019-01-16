# Nested Statement and scope

# LEGB Rule:
# Local (def ir lambda)
# Enclosing (function inside a function)
# Global
# Built-in Python


# Global variable
x = 25

def printer():
    # Local variable
    x = 50
    return x

# printing global variable
print(f'Printing global x {x}')

# printing local variable
print(f'Printing local x {printer()}')

# printing global variable again
print(f'printing global variable again {x}')

# reassigning global variable from local variable
x=printer()

# printing global variable
print(f'reassigning global variable from local variable {x}')

############################################

# another example
# This example has no local variable but it will look for Enclose variable (inside greet() function)
# If we comment the enclose variable it will print global variable 'THIS IS GLOBAL'

# global variable
name = 'THIS IS GLOBAL'

def greet():
    # enclosing
    name = 'Sammy'
    def hello():
        print('Hello ' + name)
    hello()


greet()

############################################
# using global statement to within function
print('############')
x = 50

def func():
    global x
    # print global
    print(x)

    # reassign x on a global variable
    x = 'NEW VALUE'
    print(x)


func()

# printing the global variable
print(x)



