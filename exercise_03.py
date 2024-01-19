def cubePrint(numberGreaterThanOne):
    i = 0
    while (i <= numberGreaterThanOne):
        i = i + 1
        print(i * i * i)
        
n = int(input("Enter an integer greater than 1: "))
cubePrint(5)