array = [2,5,7,9,4,5,6,3]


for i in range(len(array)):
    sorted = True
    for j in range(len(array)-1-i):
        if array[j]> array[j+1]:
            temp = array[j]
            array[j]= array[j+1]
            array[j+1]= temp
            sorted = False

    if sorted:
        break

print("Sorted array: ")
for k in range(len(array)):
    print(array[k],end = ',')

#print(printingVariable, sep = " ",end = "\n")
    