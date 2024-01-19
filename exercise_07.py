intList = []
userInput = input("Enter a number or QUIT to quit: ")
while (userInput != "QUIT"):
    intList.append(int(userInput))
    userInput = input("Enter a number or QUIT to quit: ")

print("All nums: " + str(intList))

evenNumbers = [];

for value in intList:
    if (value % 2 == 0):
        evenNumbers.append(value)

print("Even nums: " + str(evenNumbers))