array = [1,6,9,4,7,2]
array.sort()
print("Sorted array: ", array)

search = int(input("Input the value to search: "))
found = False

lower = 0

upper = len(array)-1

while lower<=upper and found == False:
    middle = int((lower+upper)/2)

    if array[middle] == search:
        print("In the sorted list, element is at ",middle)
        found = True
    
    elif search < array[middle]:
        upper = middle-1
        
    elif search > array[middle]:
        lower =middle+1




if found == False:
    print("Element not in list")
