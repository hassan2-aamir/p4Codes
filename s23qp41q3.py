#DECLARE Animal: ARRAY[0:19] OF STRING
#DECLARE Colour : ARRAY[0:9] OF STRING
#DECLARE AnimalTopPointer,ColourTopPointer : INTEGER

Animal = [None for i in range(20)]
Colour= [None for i in range(10)]

AnimalTopPointer =0
ColourTopPointer=0

def PushAnimal(DataToPush:str):
    global Animal,AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer += 1
        return True
    
def PopAnimal()->str:
    global Animal,AnimalTopPointer
    #DECLARE ReturnData : STRING
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer-1]
        AnimalTopPointer -= 1
        return ReturnData
    

def ReadData():
    global Animal,AnimalTopPointer,Colour,ColourTopPointer
    try:
        FileName="AnimalData.txt"
        File = open(FileName,"r")
        for x in File:
            PushAnimal(x.strip())

        File.close()
    except FileNotFoundError:
        print("File does not exist")

    try:
        FileName="ColourData.txt"
        File = open(FileName,"r")
        for x in File:
            PushColour(x.strip())

        File.close()
    except FileNotFoundError:
        print("File does not exist")


def PushColour(DataToPush:str):
    global Colour,ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer]=DataToPush
        ColourTopPointer += 1
        return True
    
def PopColour()->str:
    global Colour,ColourTopPointer
    #DECLARE ReturnData : STRING
    if ColourTopPointer==0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer-1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    global Animal,AnimalTopPointer,Colour,ColourTopPointer
    Animal1 = PopAnimal()
    Colour1 = PopColour()

    if Colour1 == "":
        print("No Colour")
        PushAnimal(Animal1)
    elif Animal1 == "":
        print("No Animal")
        PushColour(Colour1)
    else:
        print(f"{Colour1} {Animal1}")


ReadData()
for i in range(4):
    OutputItem()

    