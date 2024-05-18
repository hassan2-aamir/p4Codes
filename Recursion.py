#print list from 1 to 10
def RecursivePrint(i,j):
    if i ==j:
        print(i)
    else:
        
        RecursivePrint(i+1,j)
        print(i)
        
    

#print Table of 2 till 20

#print factorial
def RecursiveFactorial(i):
    #base case
    if i ==0 or i==1:
        return 1
    #general case
    elif i>1:
        return i*RecursiveFactorial(i-1)
    else:
        print("Do not enter a negative value")
        return
    
def IterativeFactorial(i):
    answer = 1
    for j in range(i,0,-1):
        answer *= j

    print(answer)

def Fibonnaci(i):
    if i ==1 or i ==0:
        return i
    else:
        return Fibonnaci(i-1) + Fibonnaci(i-2)

def IterativeFibonnaci(i):
    n1 = 1
    n2 = 1
    for j in range(i-2):
        temp = n2
        n2 += n1
        n1 = temp
    return n2

array = [1,2,4,6,7,8,10]
def recursiveBinarySearch(array,searchItem,Lower,Upper):
    
    if Upper>=Lower:
        Middle = (Upper+Lower)//2
        if array[Middle] == searchItem:
            print("Value at index: ",Middle)
            return
        elif searchItem < array[Middle]:
            recursiveBinarySearch(array,searchItem,Lower,Middle-1)
        elif searchItem > array[Middle]:
            recursiveBinarySearch(array,searchItem,Middle+1,Upper)
    else:
        print("Value not in list")

recursiveBinarySearch(array,3,0,len(array)-1)
