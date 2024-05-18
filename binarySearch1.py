def binarySearch(search_val, array):
    array.sort()
    lower = 0
    upper = len(array)-1
    found = False
    while lower <= upper and found == False:
        middle = int((upper+lower/2))
        if array[middle]== search_val:
            found = True
        elif search_val<array[middle]:
            upper = middle - 1
        elif search_val>array[middle]:
            lower = middle + 1

    return found

array = [1,2,3,4,5]
search_val = 0

print(binarySearch(search_val,array))