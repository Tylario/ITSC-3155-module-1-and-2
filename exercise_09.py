strList = []
for i in range(5):
    strList.append(input("Enter a word: "))
    
strOutput = ""
for i in range(5):
    strOutput = strOutput + strList[i] + " "
    
print("Words: " + str(strList))
print("One string: " + strOutput)