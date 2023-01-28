import subprocess
subprocess.run(["clear"])

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