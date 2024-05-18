class Character:
    #DECLARE private Name: STRING
    #DECLARE private XCoordinate, YCoordinate: INTEGER
    def __init__(self,Name,XCoordinate,YCoordinate):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

#DECLARE CharacterArray : ARRAY[0:9] OF Character
CharacterArray = []

try:
    CharactersFile = open("Characters.txt", "r")
    for i in range(10):
        read_name = CharactersFile.readline().strip()
        read_xCoordinate = int(CharactersFile.readline().strip())
        read_yCoordinate = int(CharactersFile.readline().strip())
        CharacterArray.append(Character(read_name,read_xCoordinate,read_yCoordinate))

    CharactersFile.close()
except FileNotFoundError:
    print("File not found")

found = False
while found == False:
    searchName = input("Enter a character's name to be searched: ")
    i=0
    while found == False and i<10:
        if CharacterArray[i].GetName().lower() == searchName.lower():
            found = True
        else:
            i+=1

    if found == False:
        print("Value not found!")
    

Move = input("Input A,W,S or D: ").lower()
while Move !='a' and Move != 'w' and Move != 's' and Move != 'd':
    Move = input("Error! Input A,W,S or D: ").lower()

if Move == 'a':
    CharacterArray[i].ChangePosition(-1,0)
elif Move == 'w':
    CharacterArray[i].ChangePosition(0,1)
elif Move == 's':
    CharacterArray[i].ChangePosition(0,-1)
elif Move=='d':
    CharacterArray[i].CHangePosition(1,0)

print(f"{CharacterArray[i].GetName()} has changed coordinates to X = {CharacterArray[i].GetX()} and Y = {CharacterArray[i].GetY()}")


