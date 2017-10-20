def binarySearch(myItem, myList):
    found = False
    bottom = 0
    top = len(myList) - 1 #We use -1 to stay in loop range

    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found

if __name__ == "__main__":
    numberList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    #numberList = [1, 2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                #21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    item = 5
    isItFound = binarySearch(item, numberList)
    if isItFound:
        print("Your number is in list!")
    else:
        print("The number you entered does not belong to the list")
            