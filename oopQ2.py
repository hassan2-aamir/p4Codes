class Character:
    #DECLARE Name: STRING
    #DECLARE XCoordinate : INTEGER
    #DECLARE YCoordinate : INTEGER
    def __init__(self,NameP,XCoordinateP,YCoordinateP):
        self.__Name = NameP
        self.__XCoordinate = XCoordinateP
        self.__YCoordinate = YCoordinateP
    
    def getName(self):
        return self.__Name
    def getXCoordinate(self):
        return self.__XCoordinate
    def getYCoordinate(self):
        return self.__YCoordinate
    
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

#DECLARE characters : ARRAY[0:9] OF Character
characters=[]
fileName=" "
fileX=0
fileY=0
myFile = open("Characters.txt","r")
while fileName != "":
    fileName = myFile.readline().strip()
    if fileName != "":
        fileX = int(myFile.readline().strip())
        fileY = int(myFile.readline().strip())
        addCharacter = Character(fileName,fileX,fileY)
        characters.append(addCharacter)

found = False
while not found:
    searchName = input("Enter a character's name that exists to search: ")
    for i in range(len(characters)):
        if characters[i].getName().lower() == searchName.lower():
            index = i
            found = True
            break

move = input("Enter direction: ")
while move != 'A' != 'W' != 'S' != 'D':
    move = input("Wrong key! Enter direction again: ")

if move == 'A':
    characters[i].ChangePosition(-1,0)
elif move == 'W':
    characters[i].ChangePosition(0,1)
elif move == 'S':
    characters[i].ChangePosition(0,-1)
elif move == 'D':
    characters[i].ChangePosition(1,0)

print(characters[i].getName(), "has changed coordinates to X =",characters[i].getXCoordinate(),"and Y =", characters[i].getYCoordinate())

