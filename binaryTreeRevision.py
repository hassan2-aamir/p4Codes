NullPtr = -1
class node:
    leftPtr= NullPtr
    Value = NullPtr
    rightPtr = NullPtr

RootPtr = NullPtr
binaryTree = [node() for i in range(10)]
freePtr = 0
for i in range(9):
    binaryTree[i].rightPtr = i+1
binaryTree[9].rightPtr=NullPtr

def InsertTree(Val):
    global NullPtr, RootPtr, freePtr, binaryTree

    # If tree is full
    if freePtr == NullPtr:
        print("tree is full")
    else:
        # Insert value
        # NewNodePtr
        newNodePtr = freePtr
        # Update free ptr
        freePtr = binaryTree[newNodePtr].rightPtr
        # Insert the item
        binaryTree[newNodePtr].Value = Val
        binaryTree[newNodePtr].rightPtr = NullPtr
        binaryTree[newNodePtr].leftPtr = NullPtr

        # Find insertion point and update the pointers
        # If at first
        if RootPtr == NullPtr:
            RootPtr = newNodePtr
        else:
            # Start searching for location
            # SearchPtr
            searchPtr = RootPtr
            # Loop until we find an empty end
            inserted = False
            while not inserted:
                # Update the searchPtr or insert value
                # If value lesser than current node value
                if Val < binaryTree[searchPtr].Value:
                    if binaryTree[searchPtr].leftPtr == NullPtr:
                        binaryTree[searchPtr].leftPtr = newNodePtr
                        inserted = True
                    # Update searchPtr
                    else:
                        searchPtr = binaryTree[searchPtr].leftPtr
                else:
                    if binaryTree[searchPtr].rightPtr == NullPtr:
                        binaryTree[searchPtr].rightPtr = newNodePtr
                        inserted = True
                    else:
                        searchPtr = binaryTree[searchPtr].rightPtr

# Testing the insertion
InsertTree(10)
InsertTree(2)
InsertTree(12)
InsertTree(7)
InsertTree(15)

# Print the tree structure
for i in range(10):
    print(binaryTree[i].leftPtr, binaryTree[i].Value, binaryTree[i].rightPtr, sep='\t')

print("RootPtr:", RootPtr)
print("freePtr:", freePtr)

def SearchTree(searchItem):
    global RootPtr,NullPtr,freePtr,binaryTree
    #define searching index
    searchPtr = RootPtr

    #loop to find value
    #until we reach end
    while searchPtr != NullPtr:
        #if lesser
        if searchItem < binaryTree[searchPtr].Value:
            #move left
            searchPtr = binaryTree[searchPtr].leftPtr
        #if greater 
        elif searchItem > binaryTree[searchPtr].Value:
            #move right
            searchPtr=binaryTree[searchPtr].rightPtr
        #if equal
        else:
            return searchPtr
    
    return searchPtr

#inOrder
def inOrder(RootPtr):
    global NullPtr,binaryTree

    if binaryTree[RootPtr].Value == NullPtr:
        return
    
    #left
    inOrder(binaryTree[RootPtr].leftPtr)
    #print current value
    print(binaryTree[RootPtr].Value)
    #right
    inOrder(binaryTree[RootPtr].rightPtr)

def postOrder(RootPtr):
    global NullPtr,binaryTree
    if binaryTree[RootPtr].Value == NullPtr:
        return
    
    #left
    postOrder(binaryTree[RootPtr].leftPtr)
    #right
    postOrder(binaryTree[RootPtr].rightPtr)
    #print current value
    print(binaryTree[RootPtr].Value)