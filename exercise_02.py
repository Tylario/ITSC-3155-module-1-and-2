def matchingSuffix(string1, string2):
    if (len(string1) > len(string2)):
        longerStringLength = len(string1)
        shorterStringLength = len(string2)
        if (string1[-1 * shorterStringLength:] == string2):
            return True
        return False
    else:
        longerStringLength = len(string2)
        shorterStringLength = len(string1)
        if (string2[-1 * shorterStringLength:] == string1):
            return True
        return False
        
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
    
print(matchingSuffix(string1, string2))