class Card:
    #DECLARE private Number:INTGER
    #DECLARE private Colour:STRING
    def __init__(self,NumberP,ColourP):
        self.__Number=NumberP
        self.__Colour=ColourP

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

#DECLARE CardArray : ARRAY[0:30] OF Card
CardArray=[None for i in range(30)]

try:
    Filename="CardValues.txt"
    File=open(Filename,'r')
    for x in range(30):
        CardNumber=int(File.readline())
        CardColour=File.readline()
        CardArray[x]=Card(CardNumber,CardColour)
    File.close()
except FileNotFoundError:
    print("File could not be found")

ChosenCardsIndexes = []
def ChooseCard():
    global ChosenCardsIndexes
    searchIndex = int(input("Enter the index of the card that you want between 1 and 30: "))
    while (searchIndex <1 or searchIndex >30) or searchIndex in ChosenCardsIndexes:
        searchIndex = int(input("Wrong input. Please Enter the index of the card that you want between 1 and 30:  "))
    else:
        ChosenCardsIndexes.append(searchIndex)
        return searchIndex


#DECLARE Player1 : ARRAY[0:3] OF Card
Player1 = []

for i in range(4):
    Player1.append(CardArray[ChooseCard()])

for j in range(4):
    print("Card ",j+1, "Number: ", Player1[j].GetNumber())
    print("Card ",j+1, "Colour: ",Player1[j].GetColour())

    
