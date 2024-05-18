#DECLARE DataArray : [0:24] OF INTEGER
DataArray = []

try:
    FileName = "Data.txt"
    DataFile = open(FileName,"r")
    for x in DataFile:
        DataArray.append(int(x.strip()))
    
    DataFile.close()
except FileNotFoundError:
    print("File not found")


def printArray(DataArray):
    for x in DataArray:
        print(x,end=" ")

printArray(DataArray)
print()


def LinearSearch(DataArray, searchValue):
    count =0
    for x in DataArray:
        if x == searchValue:
            count+=1
    return count

searchValue = int(input("Input a whole number between 0 and 100 inclusive: "))
while searchValue<0 or searchValue>100:
    searchValue = int(input("Value out of range! Please input a whole number between 0 and 100 inclusive: "))

count = LinearSearch(DataArray,searchValue)
print(f"The number {searchValue} is found {count} times")

