rowNum = int(input("Enter a row num from 1 to 5: "))
colNum = int(input("Enter a col num from 1 to 5: "))

currentRow = ""
for y in range(5):
    print(currentRow)
    currentRow = ""
    for x in range(5):
            if (x == colNum - 1 and y == rowNum - 1):
                currentRow = currentRow + "1 "
            else:
                currentRow = currentRow + "0 "
print(currentRow)