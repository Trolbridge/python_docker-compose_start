import subprocess
import sys
subprocess.run(["clear"])

# VARIABLES
# Statically typed python code
# https://betterdatascience.com/python-statically-typed/
age: int = 32
rating: float = 7.9
is_premium: bool = True
my_name: str = "DEN"
print("Hello", my_name, "World")

def sum_numbers(a: int, b: int) -> int:
    return a + b

print(sum_numbers(10, 5))

# Use double quotes \"
# escape characters: \\, \n, \t, \r, \b, \f, \v, \0, \00, \01, \02, \0, \03, \0, \\, \', ,\", 

print(repr('''Escape Characters: \\, \n, \t, \\", \', \01, \02, \03, \04, \05, ,\06, \07, \0'''))

print("max size of int", sys.maxsize)
print("max size of float", sys.float_info.max)
# floats are accurate to 15 digits

cn_1: complex = 5 + 6j

can_vote: bool = True

# Casting
print("Cast", type(int(rating)))
print("Cast", type(str(rating)))
print("Cast", type(chr(97))) # no chr types in python
print("Cast", type(ord('a'))) # casting char to unicode
print("Cast", type(float(2)))
