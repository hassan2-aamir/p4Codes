NullPtr = -1
TreeNode = [[-1,"",-1]for i in range(10)]
RootPtr = NullPtr
FreePtr = 0

for i in range(9):
    TreeNode[i][2] = i+1
TreeNode[9][2] = NullPtr

def printTree():
    global FreePtr,RootPtr,TreeNode
    for i in range(10):
        print(TreeNode[i])
    print("Free pointer: ",FreePtr)
    print("Root pointer: ",RootPtr)


def InsertTree(newItem:str):
    global RootPtr,FreePtr,NullPtr,TreeNode
    #if tree empty
    if FreePtr == NullPtr:
        print("Tree is full")
    else: #if tree is not empty
    #insert value
        NewNodePtr = FreePtr
        FreePtr = TreeNode[NewNodePtr][2]
        TreeNode[NewNodePtr][1] = newItem
    #update ptrs
        TreeNode[NewNodePtr][0] = NullPtr
        TreeNode[NewNodePtr][2] = NullPtr
    #if not first element
    if RootPtr != NullPtr:    
        #use a loop to search insertion point
            thisPtr = RootPtr
            while thisPtr != NullPtr:
                #update prePtr before updating search pointer
                prePtr = thisPtr
                #update this ptr to our next node

                #if lesser
                if newItem < TreeNode[thisPtr][1]:
                    #update flag
                    turnedLeft = True
                    #update thisPtr accordingly
                    thisPtr = TreeNode[thisPtr][0]
                #if greater
                else:
                    #update flag
                    turnedLeft = False
                    #update thisPtr accordingly
                    thisPtr = TreeNode[thisPtr][2]
            #we have reached insertion point
            #if last action was going to left
            if turnedLeft:
                #update leftPtr of previous node
                TreeNode[prePtr][0] = NewNodePtr
            #if last action was going to right
            else:
                #update rightPtr of previous node
                TreeNode[prePtr][2] = NewNodePtr
    #if first element
    else:
        #update rootPtr
        RootPtr = NewNodePtr

InsertTree("Hassan")
InsertTree("Rochan")
InsertTree("Ali")
InsertTree("Ahmed")
InsertTree("Zara")
InsertTree("Anab")
InsertTree("Noor")
InsertTree("Muhammad")
printTree()

def SearchTree(SearchItem:str):
    global RootPtr,NullPtr,TreeNode
    #initialise search ptr to strating point
    thisPtr = RootPtr
    #Start loop
    #run loop until end or value found
    while thisPtr != NullPtr and SearchItem != TreeNode[thisPtr][1]:
        #update thisPtr to next node
        #if lesser
        if SearchItem < TreeNode[thisPtr][1]:
            #move left
            thisPtr = TreeNode[thisPtr][0]
        #if greater
        else:
            #move right
            thisPtr = TreeNode[thisPtr][2]
    #return location. -1 if tree was empty or searchItem was not in tree
    return thisPtr

