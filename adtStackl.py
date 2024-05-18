TOS = -1
Stack = [-1 for i in range(10)]

def Push(Val):
    global TOS, Stack
    if TOS == len(Stack) - 1:
        print("No space in Stack")
    else:
        TOS += 1
        Stack[TOS] = Val
    

def Pop():
    global TOS, Stack
    if TOS == -1:
        print("Stack is empty")
    else:
        Stack[TOS] = -1
        TOS -= 1

Push(10)
Push(7)
Pop()

def displayStack():
    for i in range(9,-1,-1):
        print(i, Stack[i])
        
    print("TOS: ",TOS)


displayStack()