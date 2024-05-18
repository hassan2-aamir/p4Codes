def bubbleSort(array):
    for i in range(len(array)):
        sorted = True
        for j in range((len(array)-1)-i):
            if array[j][0]>array[j+1][0]:
                sorted = False
                for k in range(3):
                    temp = array[j][k]
                    array[j][k]=array[j+1][k]
                    array[j+1][k]=temp
        if sorted == True:
            break

    return array

testArray = [[1001,"Rochan",98],
             [1000,"Hassan",97],
             [1003,"Ali",50],
             [100,"Rohan",67]]

testArray = bubbleSort(testArray)

print(testArray)
    
