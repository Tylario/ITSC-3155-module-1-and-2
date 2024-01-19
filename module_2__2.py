inputVar = input("Enter a string: ");
lowerCase = ""
upperCase = ""

for char in inputVar:
    if (char.islower()):
        lowerCase = lowerCase + char
    else:
        if (char != ' '):
            upperCase = upperCase + char

print(lowerCase + upperCase)
