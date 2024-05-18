def LinearSearch(array, searchValue):
    count = 0
    for i in range(len(array)):
        if searchValue == array[i]:
            count +=1
    
    print("The number", searchValue,"is found", count, "times")

array = [1,9,8,7,8,9,7,8,9,9,10]
searchValue = int(input("input the search value between 0 and 100 inclusive:  "))

while(searchValue < 0 or searchValue > 100):
    searchValue = int(input("error! Please input a value between 0 and 100 inclusive: "))

LinearSearch(array,searchValue)

#prompt the user to input a whole number between 0 and 100 inclusive
#read and validate the input from the user
#call LinearSearch() with DataArray and the validated input value
#output the result in the format:
#The number 7 is found 2 times
    