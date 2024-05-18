#DECLARE ArrayNodes : ARRAY [0:19][0:2] OF INTEGER
NullPointer = -1

RootPointer = NullPointer
FreeNode = 0



ArrayNodes = [[NullPointer,None,NullPointer]for i in range(20)]
def AddNode(ArrayNodes,RootPointer:int,FreeNode:int):
    NodeData = int(input("Enter the data: "))
    if FreeNode == -1:
        print("Tree is  full")
    else:
        ArrayNodes[FreeNode][0] = NullPointer
        ArrayNodes[FreeNode][1]= NodeData
        ArrayNodes[FreeNode][2] =NullPointer

        if RootPointer != NullPointer:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == NullPointer:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                if NodeData > ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][2] == NullPointer:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
                

        else:
            RootPointer = 0 
        
        FreeNode += 1 

    return ArrayNodes, RootPointer, FreeNode

def printAll():
    global NullPointer,RootPointer,FreeNode,ArrayNodes
    print("Left Pointer","Data","Right Pointer",sep="  ")
    for i in range(20):
        print(f"    {ArrayNodes[i][0]}{(' '*(9-len(str(ArrayNodes[i][0]))))}{ArrayNodes[i][1]}{(' '*(7-len(str(ArrayNodes[i][1]))))}{ArrayNodes[i][2]}")
    
for i in range(10):
    ArrayNodes,RootPointer,FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)
printAll()

def inOrder(ArrayNodes,RootPointer):
    global NullPointer
    if ArrayNodes[RootPointer][1]==None:
        return
    inOrder(ArrayNodes,ArrayNodes[RootPointer][0])
    print(ArrayNodes[RootPointer][1])
    inOrder(ArrayNodes,ArrayNodes[RootPointer][2])

print("\n\n")    
inOrder(ArrayNodes,RootPointer)

