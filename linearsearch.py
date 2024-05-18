found = False

numbers = [1,2,9,10,8,7]
number = int(input("Enter a search number:  "))

for i in range(len(numbers)):
    if numbers[i] == number:
        print("The element is found at index ", i)
        found = True

if found == False:
    print("search element not in list")
    

