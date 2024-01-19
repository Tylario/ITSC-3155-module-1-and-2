intList = []
for i in range(10):
    intList.append(int(input("Enter number " + str(i) + ": ")))

uniqueIntList = []
for val in intList:
    freq = 0;
    for compVal in intList:
        if val == compVal:
            freq = freq + 1
    if (freq == 1):
        uniqueIntList.append(val)
        
print("Original List: " + str(intList))
print("Nums that appear once: " + str(uniqueIntList))