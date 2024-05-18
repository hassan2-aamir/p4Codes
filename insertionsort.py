array = [2,3,4,1,5,6]

for i in range(1,len(array)):
    j=i-1
    temp = array[i]

    while temp<array[j] and j >=0:
        array[j+1]=array[j]
        j-=1

    array[j+1] = temp

for element in array:
    print(element,end = " ")