'''
Truth Table Calculator

by trustnoedo
'''


def AND(x, y):
    if x == "T":
        if y == "T":
            return "T"
        else:
            return "F"
    elif x == "F":
        if y == "T":
            return "F"
        else:
            return "F"


def OR(x, y):
    if x == "F":
        if y == "F":
            return "F"
        else:
            return "T"
    else:
        return"T"


def implies(x, y):
    if x == "T":
        if y == "T":
            return "T"
        else:
            return "F"
    else:
        return "T"


# Body

print()
print("Hi! This is a truth table calculator.")
print("Insert T or F")
print()




# Inputs
# -------- first line--------
x1 = input("x one: ")
y1 = input("y one: ")
# -------- second line--------
x2 = input("x two: ")
y2 = input("y two: ")
# -------- third line--------
x3 = input("x three: ")
y3 = input("y three: ")
# -------- fourth line--------
x4 = input("x four: ")
y4 = input("y four: ")

# Initial table
print()
print("x" + " | " + "y")
print()
print(x1 + " | " + y1)
print(x2 + " | " + y2)
print(x3 + " | " + y3)
print(x4 + " | " + y4)
print()

choice = int(input("Choose:\n"
                   "1. And\n"
                   "2. Or\n"
                   "3. Implies\n"
                   "\n"))

if choice == 1:
    print()
    print("x" + " | " + "y" + " | " + "x and y")
    print("----------------")
    print(x1 + " | " + y1 + " | " + AND(x1, y1))
    print(x2 + " | " + y2 + " | " + AND(x2, y2))
    print(x3 + " | " + y3 + " | " + AND(x3, y3))
    print(x4 + " | " + y4 + " | " + AND(x4, y4))

elif choice == 2:
    print()
    print("x" + " | " + "y" + " | " + "x or y")
    print("----------------")
    print(x1 + " | " + y1 + " | " + OR(x1, y1))
    print(x2 + " | " + y2 + " | " + OR(x2, y2))
    print(x3 + " | " + y3 + " | " + OR(x3, y3))
    print(x4 + " | " + y4 + " | " + OR(x4, y4))

else:
    print()
    print("x" + " | " + "y" + " | " + "x implies y")
    print("----------------")
    print(x1 + " | " + y1 + " | " + implies(x1, y1))
    print(x2 + " | " + y2 + " | " + implies(x2, y2))
    print(x3 + " | " + y3 + " | " + implies(x3, y3))
    print(x4 + " | " + y4 + " | " + implies(x4, y4))
