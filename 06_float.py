

x = float(input("Enter x:"))
y = float(input("Enter y:"))

print(x+y)

#--------------------------------------------

x = float(input("Enter x:"))
y = float(input("Enter y:"))

z = round(x+y)

print(z)

"""
if x = 1.234 & y = 1.234  --> x+y = 2
"""
# -------------------------------------------

x = float(input("Enter x:"))
y = float(input("Enter y:"))

z = round((x+y),2)

print(z)

"""
x = 1.150 , y = 1.156  --> x+y = 2.31
"""

#----------------------------------------------
x = int(input("Enter x:"))
y = int(input("Enter y:"))

z = x+y

print(f"{z:,}")

"""
x=999, y=1  --> z=1,000 --------> US based system
The , tells Python: “Insert commas as thousands separators.”

, is called format specifier
"""
#----------------------------------------------------

x = int(input("Enter x:"))
y = int(input("Enter y:"))

z = x/y   # / is float division --> notice x and y are int

print(f"{z}")

"""
2/3 --> 0.6666666666666666

"""


#----------------------------------------------------

x = int(input("Enter x:"))
y = int(input("Enter y:"))

z = round(x/y,2)

print(f"{z}")

"""
2/3 --> 0.67

/ --> float division(True division)
// --> integer division (Floor division)
"""

#----------------------------------------

x = float(input("Enter x:"))
y = float(input("Enter y:"))

z = x/y

print(f"{z:.2f}")

"""
2/3 --> 0.67
.2f → means fixed-point notation(f) with 2 digits after the decimal (format specifier)
"""

#---------------------------------------------

x = float(input("Enter x:"))
y = float(input("Enter y:"))

z = x/y

print(f"{z:.3f}")

"""
2/3 --> 0.667
"""

#-------------------------------------------


