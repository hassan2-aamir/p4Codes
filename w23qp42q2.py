def IterativeCalculate(Number:int)->int:
    #DECLARE Total,ToFind:INTEGER
    ToFind = Number
    Total =0
    while Number !=0:
        if ToFind%Number ==0:
            Total+=Number
        Number-=1
    return Total

print(IterativeCalculate(10))

def RecursiveValue(Number:int,ToFind:int)->int:
    if Number==0:
        return 0
    else:
        if ToFind%Number==0:
            return Number+RecursiveValue(Number-1,ToFind)
        else:
            return RecursiveValue(Number-1,ToFind)
        
print("Recursive Output: ",RecursiveValue(50,50))