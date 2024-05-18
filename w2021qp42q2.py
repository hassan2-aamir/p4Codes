class Picture:
    def __init__(self,DescriptionP,WidthP,HeightP,FrameColourP):
        #DECLARE private Description:STRING 
        #DECLARE private Width:INTEGER
        #DECLARE private Height: INTEGER
        #DECLARE private FrameColour: STRING
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
    
    return Index, PictureArray


NumberPictures,PictureArray = ReadData(PictureArray)

FrameColour=input("Enter the colour of the picture: ")
MaxHeight=int(input("Enter the maximum height of the picture: "))
MaxWidth=int(input("Enter the maximum width of the picture: "))
for x in range(NumberPictures):
    if PictureArray[x].GetColour()==FrameColour:
        if PictureArray[x].GetWidth()<=MaxWidth:
            if PictureArray[x].GetHeight()<=MaxHeight:
                print(PictureArray[x].GetDescription(),"", str(PictureArray[x].GetHeight()),"",str(PictureArray[x].GetWidth()))