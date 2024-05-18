class node:
    #declare data:INTEGER
    #declare nextNode:INTEGER
    def __init__(self,data,nextNode):
        self.data = data
        self.nextNode = nextNode

#DECLARE linkedList : ARRAY[0:9] OF node
#DECLARE startPointer,emptyList : INTEGER
linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

def outputNodes(startPointer,array):
    print("Linked list data: ")
    currentPtr = startPointer
    while currentPtr != -1:
        print(array[currentPtr].data)
        currentPtr = array[currentPtr].nextNode
    


def addNode(linkedList,startPtr,freePtr):
    if freePtr == -1:
        return False,linkedList,startPtr,freePtr
    #data inserted
    dataToAdd = int(input("input data to add to linked List"))
    linkedList[freePtr].data = dataToAdd
    newPtr = freePtr
    freePtr = linkedList[freePtr].nextNode
    #update pointers
    searchPtr = startPtr
    prePtr = -1
    while searchPtr != -1:
        prePtr = searchPtr
        searchPtr = linkedList[searchPtr].nextNode
    
    if prePtr == -1:
        linkedList[newPtr].nextNode = startPtr
        startPtr = newPtr
    else:
        linkedList[newPtr].nextNode = -1
        linkedList[prePtr].nextNode = newPtr
    
    return True,linkedList,startPtr,freePtr


outputNodes(startPointer,linkedList)

isInserted,linkedList,startPointer,emptyList = addNode(linkedList,startPointer,emptyList)
if isInserted:
    print("Data added successfully")
else:
    print("List full")

outputNodes(startPointer,linkedList)
