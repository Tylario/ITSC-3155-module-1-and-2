n = int(input("Enter a number: "))

numberList = []
sum = 0

for i in range(n):
    newInt = int(input("Enter a number " + str(i) + ": "))
    sum = sum + newInt
    numberList.append(newInt)

print("List: " + str(numberList))

average = sum / n

print("Average: " + str(average))