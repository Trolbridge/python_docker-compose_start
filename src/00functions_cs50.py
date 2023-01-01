import subprocess

# FUNCTIONS
def clear():
    subprocess.run(["clear"])

def print_menu():
    clear()
    print("1. Create a new folder")
    print("2. Create a new file")
    print("3. Open a file")
    print("4. Open a folder")

print_menu()

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



name: str = input("what name? ")
print('hi', name, end='')
print(f'hi {name} ', )

# string methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
