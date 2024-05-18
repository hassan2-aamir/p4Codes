class FieldObject:
    pass

class Box:
    __Size = ""
    __Contents = []
    __Lock= ""
    __Strength = -1
    def __init__(self,Size,item,Lock):
        self.__Size = Size
        self.__Contents += item
        self.__Lock = Lock
        self.__Strength = 100

    
    def Unlock(self,Code):
        if Code == self.__Lock:
            return True
        else:
            self.__Strength -= 1
            if self.__Strength<1:
                return True
            else:
                return False

def LoadGame():
    try:
        myFile = open("Progress.txt","r")
        GameData = ""
        for i in myFile:
            GameData+= i
    except FileNotFoundError:
        print("File not found!")


    