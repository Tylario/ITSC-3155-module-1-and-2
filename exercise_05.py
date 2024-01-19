list1 = []

for i in range(5):
    newInt = int(input("Enter a number for the first list: "))
    list1.append(newInt)

list2 = []

for i in range(5):
    newInt = int(input("Enter a number for the second list: "))
    list2.append(newInt)

print("List 1: " + str(list1))
print("List 2: " + str(list2))

commonList = []

for value in list1:
    for value2 in list2:
        if value == value2:
            commonList.append(value)

print("Common List: " + str(commonList))