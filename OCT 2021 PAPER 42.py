"""
def Unknown(X,Y):
    if X<Y:
        print(str(X+Y))
        return(Unknown(X+1,Y)*2)
    elif X==Y:
        return 1
    else:
        print(str(X+Y))
        return (Unknown(X-1,Y)//2)

print("10 and 15")
print(str(Unknown(10,15)))
print("10 and 10")
print(str(Unknown(10,10)))
print("15 and 10")
print(str(Unknown(15,10)))
"""
"""

def IterativeUnknown(X,Y):
    Total=0
    while X!=Y:
        print(str(X+Y))
        if X<Y:
            X+=1
            Total=Total*2
        else:
            X-=1
            Total=int(Total/2)
    return Total


print("10 and 15")
print(str(IterativeUnknown(10,15)))
print("10 and 10")
print(str(IterativeUnknown(10,10)))
print("15 and 10")
print(str(IterativeUnknown(15,10)))
"""
"""
class Picture:
    def __init__(self,DescriptionP,WidthP,HeightP,FrameColourP):
        #DECLARE Description:STRING 
        #DECLARE Width:INTEGER
        #DECLARE Height: INTEGER
        #DECLARE FrameColour: STRING
        self.__Description=DescriptionP
        self.__Width=WidthP
        self.__Height=HeightP
        self.__FrameColour=FrameColourP

def GetDescription(self):
    return self.__Description
def GetHeight(self):
    return self.__Height
def GetWidth(self):
    return self.__Width
def GetColour(self):
    return self.__FrameColour

def SetDescription(self,DescriptionP):
    return self.__Description==DescriptionP

PictureArray=[]
for i in range(100):
    PictureArray.append(Picture("",0,0,""))

def ReadData(PictureArray):
    FileName="Pictures.txt"
    Index=0
    try:
        File=open(FileName,'r')
        Description=(File.readline()).strip().lower()
        while Description!="":
            Height=int((File.readline()).strip())
            Width=int((File.readline()).strip())
            FrameColour=(File.readline()).strip().lower()
            PictureArray[Index]=Picture(Description,Height,Width,FrameColour)
            Description=(File.readline()).strip().lower()
            Index+=1
        File.close()
    except FileNotFoundError:
        print("File is not found")

NumberPictures,PictureArray=ReadData(PictureArray)

FrameColour=input("Enter the colour of the picture: ")
MaxHeight=int(input("Enter the maximum height of the picture: "))
MaxWidth=int(input("Enter the maximum width of the picture: "))
for x in range(NumberPictures):
    if PictureArray[x].GetColour()==FrameColour:
        if PictureArray[x].GetWidth()<=MaxWidth:
            if PictureArray[x].GetHeight()<=MaxHeight:
                print(PictureArray[x].GetDescription(),"", str(PictureArray[x].GetHeight()),"",str(PictureArray[x].GetWidth()))
    
"""
"""
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

for y in range(10):
    ArrayNodes,RootPointer,FreeNode=AddNode(ArrayNodes,RootPointer,FreeNode)
    
PrintAll(ArrayNodes)
"""

def InOrder(ArrayNodes,RootNode):
    if ArrayNodes[RootNode][0]!=-1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][0])
    print(ArrayNodes[RootNode][1])
    if ArrayNodes[RootNode][2]!=-1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][2])

for z in range(10):
    ArrayNodes
