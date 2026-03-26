

# Ask user for their name
name = input("What's your name? ")

# print hello
print("hello,")

#Print inputted name
print(name)


"""
hello,
armaan aquib
"""

#----------------------------------------------

name = input("What's your name? ")
print("hello,",end="-")
print(name)

"""
hello,-armaan aquib
"""


#---------------------------------------------
# Ask user for ther name
name = input("What's your name? ")
print("hello, "+name)       #concatenation

# Print User's name
print("hello,",name)       # two arguments



"""
hello, name
hello, armaan aquib
hello, armaan aquib
"""

#------------------------------------------------------------------------

name = input("What's your name? ")
print("hello","to the world",name,sep="-")

"""
hello-to the world-armaan
"""

#------------------------------------------------------------------------

#FORMATTED STRING

name = input("What's your name? ")
print(f"hello, {name}")


"""
hello, armaan aquib
"""

#--------------------------------------------------------------------
#.strip()-->  will remove any whitespace from the left and right of the user’s input. 
# .tilte() -->  it would title case the user’s name.
# 
name = input("What's your name? ").strip().title()
print(f"Hello, {name}")



"""
Hello, Armaan Aquib
"""
#------------------------------------------------------------------------------

name = input("What's your name? ").strip().capitalize()
print(f"Hello, {name}")

"""
Hello, Armaan aquib
"""

#-----------------------------------------------------------------------------






