import subprocess
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
