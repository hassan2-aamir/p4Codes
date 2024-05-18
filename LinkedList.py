NullPtr = -1

StartPtr = NullPtr
FreePtr = 0
NodeVal = [-1 for i in range(10)]
NodePtr = [-1 for i in range(10)]

for i in range(9):
    NodePtr[i] = i+1

NodePtr[9] = NullPtr

def InsertItem(NewItem):
    global StartPtr,FreePtr,NodePtr,NodeVal
    #list full
    if FreePtr == NullPtr:
        print("List full")
    else:
        #insert the new value
        newPtr = FreePtr
        NodeVal[newPtr] = NewItem
        FreePtr = NodePtr[newPtr]
        #find the insertion point
        ThisPtr = StartPtr
        PrePtr = NullPtr
        while ThisPtr != NullPtr and NodeVal[ThisPtr] < NewItem:
            PrePtr = ThisPtr
            ThisPtr = NodePtr[ThisPtr]
        
        if PrePtr == NullPtr:
            NodePtr[newPtr] = StartPtr
            StartPtr = newPtr
        else:
            NodePtr[newPtr] = NodePtr[PrePtr]
            NodePtr[PrePtr] = newPtr

def printList():
    global StartPtr,FreePtr,NodePtr,NodeVal
    for i in range(10):
        print(NodeVal[i],NodePtr[i],sep = "  ")
    print("\n","Start Ptr: ",StartPtr,"\n","Free Ptr: ",FreePtr)

def findNode(DataItem: int):
    global StartPtr,FreePtr,NodeVal,NodePtr
    CurrentPtr = StartPtr
    while CurrentPtr != NullPtr and NodeVal[CurrentPtr] != DataItem:
        CurrentPtr = NodePtr[CurrentPtr]

    return CurrentPtr

def deleteItem(DataItem:int):
    global StartPtr,FreePtr,NodeVal,NodePtr
    ThisPtr = StartPtr
    while ThisPtr != NullPtr and NodeVal[ThisPtr] != DataItem:
        prePtr = ThisPtr
        ThisPtr = NodePtr[ThisPtr]

    if ThisPtr == NullPtr:
        print("Element does not exist or linked list is empty")
    else:
        if ThisPtr == StartPtr:
            StartPtr = NodePtr[ThisPtr]
        else:
            NodePtr[prePtr] = NodePtr[ThisPtr]

        NodePtr[ThisPtr] = FreePtr
        FreePtr = ThisPtr

def outputNodes():
    global StartPtr,NodeVal,NodePtr
    CurrentPtr = StartPtr
    print("Values\tPointers")
    while CurrentPtr != NullPtr:
        print(NodeVal[CurrentPtr],NodePtr[CurrentPtr],sep = "\t")
        CurrentPtr = NodePtr[CurrentPtr]




