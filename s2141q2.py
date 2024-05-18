#DECLARE arrayData: ARRAY[0:9] OF INTEGER
arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(item):
    global arrayData
    i = 0
    while i < len(arrayData):
        if item == arrayData[i]:
            return True
        i+=1
    return False

searchItem = int(input("Enter integer to search: "))
found = linearSearch(searchItem)
if found:
    print("Value found in array!")
else:
    print("Value does not exist in array.")


def bubbleSort():
    global arrayData
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1-x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1]=temp

               