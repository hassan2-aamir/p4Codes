ArrayNodes=[]
for x in range(20):
    ArrayNodes.append([-1,-1,-1])

ArrayNodes=[[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]
FreeNodes=6
RootPointer=0
def SearchValue(Root,ValueToFind):
    if Root==-1:
        return -1
    elif ArrayNodes[Root][1]==ValueToFind:
        return Root
    elif ArrayNodes[Root][1]==-1:
        return -1
    if ArrayNodes[Root][1]>ValueToFind:
        return SearchValue(ArrayNodes[Root][0],ValueToFind)
    if ArrayNodes[Root][1]<ValueToFind:
        return SearchValue(ArrayNodes[Root][2],ValueToFind)


def PostOrder(RootNode):
    if RootNode[0]!=-1:
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2]!=-1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(RootNode[1])

ReturnVal=SearchValue(RootPointer,15)
if ReturnVal==-1:
    print("Not found")
else:
    print("Found at ",ReturnVal)
PostOrder(ArrayNodes[RootPointer])
