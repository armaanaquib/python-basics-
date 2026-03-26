

def hello():
    print("Hello")

name = input("Enter name:")
hello()
print(name)

#-------------------------------------------------

def hello(to):
    print(f"Hello, {to}")

name = input("Enter name:")
hello(name)

#--------------------------------------------------

def hello(to="world"):          # default parameter --> parameter(variable) with its own value
    print(f"Hello, {to}")

name = input("Enter name:")

# passing name variable as an argument --> default parameter wont act
hello(name)          # name acts as a value for the parameter(variable)

# without argument --> result-> default parameter acts
hello()


"""
Hello, armaan
Hello, world
"""


#------------------------------------------------------

def main():
    name = input("Enter name:")
    hello(name)
    hello()


def hello(to="world"):
    print(f"Hello, {to}")


main()

#------------------------------------------------------

def main():
    x = int(input("What's x"))
    print(f"square of x is {square(x)}")
          
def square(num):
    return num**2


main()

#----------------------------------------------

