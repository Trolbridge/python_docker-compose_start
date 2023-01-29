import subprocess

# FUNCTIONS
def clear():
    subprocess.run(["clear"])

clear()

def print_menu():
    print("1. Create a new folder")
    print("2. Create a new file")
    print("3. Open a file")
    print("4. Open a folder")

#print_menu()

# print
# https://docs.python.org/3/library/functions.html?highlight=print#print
# https://docs.python.org/3/library/functions.html#print

# return values
# variables
# pseudocode
# input accepts a string
# str = string
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *objects = can take any number of objects
# sep = separator
# end = default value


# https://docs.python.org/3/library/functions.html?highlight=input#input
def input1():
    name: str = input("what name? ")
    return print('hi', name, end='')

#input1()

# https://docs.python.org/3/library/string.html#formatspec
def formatstring(name="DEN"):
    print(f'hi {name} ', ) # format string
    print(int(input("x?")) + int(input("y?")))
    print(f"{int(input('x?')):,.2f}") # add commas to big numbers with format string
    return
    
# formatstring()


# string methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
def test_string_methods():
    print(f'hi {(input("Name? ").capitalize())} ', ) # format string
    print(f'hi {(input("Name? ").title())} ', ) # format string

# test_string_methods()
    

# Functions
def hello(to='world'): # default to 'world' called without argument
    print(f'hello {to}')

# hello(input("what's your name? "))

# scope
# return
# https://docs.python.org/3/library/functions.html?highlight=return#return
def hello_world():
    return print('hello world')

# hello_world() 

def test_return():
    x = int(input("What number to square? "))
    print(f'{x} squared is {x*x}')
    print(f'{x} squared is {squared(x)}')

def squared(n):
    # return n*n
    # return n ** 2
    return pow(n, 2)

test_return()
    


