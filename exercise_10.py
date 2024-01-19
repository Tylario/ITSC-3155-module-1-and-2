userString = input("Enter a string: ")

i = -1
j = 0

outputArr = [[]]

for char in userString:
    i = i + 1
    
    if (i == 3):
        i = 0
        j = j + 1
        outputArr.append([])
    outputArr[j].append("")
    outputArr[j][i] = char
    
print(outputArr)
    