NullPtr = -1

#global variables
StartPtr = NullPtr
FreePtr = 0
linkedList = [[-1,-1] for i in range(10)]
for i in range(9):
    linkedList[i][1] = i+1
linkedList[9][1] = NullPtr

def InsertItem(val):
    global StartPtr,NullPtr,FreePtr,linkedList
    #list is full?
    if FreePtr == NullPtr:
        print("Full!")
    else:
        #insert our item
        newPtr = FreePtr
        linkedList[newPtr][0] = val
        FreePtr = linkedList[newPtr][1]

        #Search for insertion
        SearchPtr = StartPtr
        PrePtr = NullPtr
        #search until end of list or insertion point found
        while SearchPtr != NullPtr and linkedList[SearchPtr][0] < val:
            PrePtr = SearchPtr
            SearchPtr = linkedList[SearchPtr][1]
        
        #if first value or value lesser than whole list
        if PrePtr == NullPtr:
            linkedList[newPtr][1] = StartPtr
            StartPtr = newPtr
        #if last value or value in between 
        else:
            linkedList[newPtr][1] = linkedList[PrePtr][1]
            linkedList[PrePtr][1] = newPtr

def searchNode(searchItem):
    global StartPtr,FreePtr,NullPtr,linkedList

    #flag
    found = False
    #starting point
    SearchPtr = StartPtr

    #loop until either we find or we reach the end
    while not (found or SearchPtr == NullPtr):
        #if equal
        if linkedList[SearchPtr][0] == searchItem:
            found = True
        #go to next ptr
        else:
            SearchPtr = linkedList[SearchPtr][1]
        
    #if value not found
    if not found:
        print("Value does not exist")
    else:
        print("Search item found at ", SearchPtr)

def deleteNode(searchItem):
    global StartPtr,FreePtr,linkedList,NullPtr
    #flag
    found = False
    #starting point
    SearchPtr = StartPtr

    #loop until either we find or we reach the end
    while not (found or SearchPtr == NullPtr):
        #if equal
        if linkedList[SearchPtr][0] == searchItem:
            found = True
        #if not found go to next ptr
        else:
            prePtr = SearchPtr
            SearchPtr = linkedList[SearchPtr][1]
        
    #if value not found
    if not found:
        print("Value does not exist")
    else:
        #if it's the first value
        if SearchPtr == StartPtr:
            StartPtr = linkedList[SearchPtr][1]
        #if it's in between or the end
        else:
            linkedList[prePtr][1] = linkedList[SearchPtr][1]

        #update the free list
        linkedList[SearchPtr][1] = FreePtr
        FreePtr = SearchPtr

def outputList():
    global StartPtr,FreePtr,linkedList,NullPtr
    #Starting point
    currentPtr = StartPtr
    #print headings
    print("Value\tPointer")
    #loop to print nodes
    #loop until end
    while not (currentPtr == NullPtr):
        print(linkedList[currentPtr][0],linkedList[currentPtr][1],sep="\t")
        currentPtr = linkedList[currentPtr][1]
    print("Start Ptr:",StartPtr)
    print("Free Ptr:",FreePtr)

InsertItem(2)
InsertItem(1)
InsertItem(4)

outputList()

searchNode(4)
deleteNode(2)

outputList()
print(linkedList)