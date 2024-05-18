#declare theData: Array[0:8] of integer

theData = [20,3,4,8,12,99,4,26,4]

FirstElement = 1
def InsertionSort(theData):
    global FirstElement
    for count in range(FirstElement,len(theData)):
        DataToInsert = theData[count]
        inserted = 0
        nextValue = count-1
        while(nextValue>= 0 and inserted != 1):
            if DataToInsert<theData[nextValue]:
                theData[nextValue+1]=theData[nextValue]
                nextValue -= 1
                theData[nextValue+1]= DataToInsert
            else:
                inserted = 1
    return theData
    
def printArray(theData):
    for element in theData:
        print(element,end=" ")

    print()

print("Before sorting: ", end="")
printArray(theData)    
theData = InsertionSort(theData)
print("After sorting: ", end="")
printArray(theData)

def binarySearch():
    global theData
    searchNumber = int(input("Enter number to search: "))
    lower = 0
    upper = len(theData) -1
    found = False
    while lower<=upper and found == False:
        middle = (lower+upper)//2
        if searchNumber == theData[middle]:
            print("found")
            return True
        elif searchNumber < theData[middle]:
            upper = middle -1
        else:
            lower = middle +1
    
    print("not found")
    return found

binarySearch()
binarySearch()