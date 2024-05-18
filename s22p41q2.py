class balloon:
    #DECLARE private  health: INTEGER
    #DECLARE private colour, defenceItem : STRING
    
    def __init__(self,defenceItem,colour):
        self.__defenceItem = defenceItem
        self.__colour = colour
        self.__health = 100

    def getDefenceItem(self):
        return self.__defenceItem
    
    def ChangeHealth(self,x:int):
        self.__health += x
    
    def CheckHealth(self):
        if self.__health <=0:
            return True
        else:
            return False
        

defenceItem = input("Input the name of your defence item:  ")
colour = input("Input your balloon colour:  ")

Balloon1 = balloon(defenceItem,colour)

def Defend(Balloon1:balloon):
    Strength = int(input("Input the strength of the opponent:  "))
    Balloon1.ChangeHealth(-Strength)
    print("Balloon's defence item: ",Balloon1.getDefenceItem())
    HealthRemaining = Balloon1.CheckHealth()
    if not HealthRemaining:
        print("You are still in the game! keep fighting!")
    else:
        print("GAME OVER!")
    return Balloon1

Defend(Balloon1)
