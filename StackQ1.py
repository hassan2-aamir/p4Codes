#DECLARE StackData : ARRAY[0:9] OF INTEGER
#DECLARE StackPointer : INTEGER

StackPointer = 0
StackData = [-1 for i in range(10)]

def displayStack():
    global StackData, StackData
    for i in range(9,-1,-1):
        print(i, StackData[i],sep="  ")
    print("\nTOS: ", StackPointer)

def Push(Val:int):
    global StackData, StackPointer
    Successful = False
    if StackPointer != len(StackData):
        StackData[StackPointer]=Val
        StackPointer +=1
        Successful = True

    return Successful

for i in range(10):
    Val = int(input("Input value to add to the stack:  "))
    Successful = Push(Val)
    if Successful:
        print("The value was successfully added.")
    else:
        print("The stack is full")

displayStack()

def Pop():
    global StackPointer,StackData
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        return StackData[StackPointer]

Pop()

Push(10)

displayStack()
