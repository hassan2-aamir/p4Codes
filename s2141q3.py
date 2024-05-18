class TreasureChest:
    #PRIVATE question : STRING
    #PRIVATE answer,points : INTEGER

    def __init__(self,question,answer,points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self,answer):
        if self.__answer == answer:
            return True
        return False

    def getPoints(self,attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points//2
        elif attempts == 3 or 4:
            return self.__points//4
        else:
            return 0
        


#arrayTreasure: ARRAY[0:9] OF TreasureChest
arrayTreasure = []
def readData():

    global arrayTreasure
    try:
        treasureFile = open("C:\\Users\\hp\\Documents\\TreasureChestData.txt","r")
        EndOfFile = False
        while not EndOfFile:
            q = treasureFile.readline().strip()
            if q != "":
                a = int(treasureFile.readline().strip())
                p = int(treasureFile.readline().strip())
                arrayTreasure.append(TreasureChest(q,a,p))
            else:
                EndOfFile = True
    except FileNotFoundError:
        print("No such file exists") 

readData()
Qno = int(input("enter a question number between 1 and 5: "))
Answer = int(input(arrayTreasure[Qno-1].getQuestion()+ " = "))
isCorrect = arrayTreasure[Qno-1].checkAnswer(Answer)
attempts = 1
while not isCorrect:
    print("Wrong! Try again")
    Answer = int(input(arrayTreasure[Qno-1].getQuestion()+ " = "))
    isCorrect = arrayTreasure[Qno-1].checkAnswer(Answer)         
    attempts += 1

print("Points acheived: ",arrayTreasure[Qno-1].getPoints(attempts))

