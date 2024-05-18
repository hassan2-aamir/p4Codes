ArrayNodes=[[0 for x in range(3)]for y in range(20)] #2D array of string
RootPointer=-1 #integer
FreeNode=0 #integer
def AddNode(ArrayNodes,RootPointer,FreeNode):
    NodeData=int(input("Enter data you want to put in the binary trees: "))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            Placed=False
            CurrentNode=RootPointer
            while Placed==False:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2]==-1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode+=1
    else:
        print("Tree is full")

    return ArrayNodes,RootPointer,FreeNode


def PrintAll(ArrayNodes):
    for x in range(20):
        print(ArrayNodes[x][0],"",ArrayNodes[x][1],"",ArrayNodes[x][2])

#for y in range(10):
 #   ArrayNodes,RootPointer,FreeNode=AddNode(ArrayNodes,RootPointer,FreeNode)
    
#PrintAll(ArrayNodes)

def InOrder(ArrayNodes,RootNode):
    if ArrayNodes[RootNode][0]!=-1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][0])
    print(ArrayNodes[RootNode][1])
    if ArrayNodes[RootNode][2]!=-1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][2])

for y in range(10):
    ArrayNodes,RootPointer,FreeNode=AddNode(ArrayNodes,RootPointer,FreeNode)
    
InOrder(ArrayNodes,RootPointer)