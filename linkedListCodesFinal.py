startPtr = -1
freePtr = 0
linkedList = [[-1,-1] for i in range(5)]
for i in range(5):
    linkedList[i][1] = i+1
linkedList[4][1] = -1

def insertList(val):
    global startPtr,freePtr,linkedList
    #list is full?
    if freePtr == -1:
        print("Full!")
    else:
        #insert our item
        newPtr = freePtr
        linkedList[newPtr][0] = val
        freePtr = linkedList[newPtr][1]

        #Search for insertion
        SearchPtr = startPtr
        PrePtr = -1
        #search until end of list or insertion point found
        while SearchPtr != -1 and linkedList[SearchPtr][0] < val:
            PrePtr = SearchPtr
            SearchPtr = linkedList[SearchPtr][1]
        
        #if first value or value lesser than whole list
        if PrePtr == -1:
            linkedList[newPtr][1] = startPtr
            startPtr = newPtr
        #if last value or value in between 
        else:
            linkedList[newPtr][1] = linkedList[PrePtr][1]
            linkedList[PrePtr][1] = newPtr


def searchList(num:int):
    global startPtr, freePtr,linkedList

    thisPtr = startPtr
    while thisPtr != -1 and num != linkedList[thisPtr][0]:
        thisPtr = linkedList[thisPtr][1]

    print("Value found at", thisPtr)


def deleteList(num:int):
    global startPtr, freePtr,linkedList

    thisPtr = startPtr
    prePtr = -1
    while thisPtr != -1 and linkedList[thisPtr][0] != num:
        prePtr=thisPtr
        thisPtr = linkedList[thisPtr][1]

    if thisPtr != -1:
        if prePtr == -1:
            startPtr = linkedList[thisPtr][1] 
        else:
            linkedList[prePtr][1] = linkedList[thisPtr][1]
        
        linkedList[thisPtr][1] = freePtr
        freePtr = thisPtr
    else:
        print("Value not found for deletion or list is empty!")


insertList(3)
insertList(5)


print(linkedList)
print(startPtr)
print(freePtr)


