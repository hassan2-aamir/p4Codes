#global variables
TOS = -1
Stack = [-1 for i in range(10)]

def Push(val):
    #global variables
    global TOS, Stack

    #If stack is full
    if TOS == len(Stack)-1:
        print("Stack is full")
    else:
        TOS+= 1
        Stack[TOS] = val


def Pop():
    global TOS,Stack
    #if stack is empty
    if TOS == -1:
        print("Stack is empty")
    else:
        temp = Stack[TOS]
        TOS -= 1
        return temp
    
def displayStack():
    global Stack,TOS
    # index Val 
    # TOS 
    print("Index",'\t',"Val")
    for i in range(TOS,-1,-1):
        print(i,'\t',Stack[i])

    print("TOS: ",TOS)


Push(99)
Push(9)
Push(7)
H = Pop()
displayStack()