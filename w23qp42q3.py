class Character:
    #DECLARE private CharacterName: STRING
    #DECLARE private DateOfBirth:DATE
    #DECLARE private Intelligence:REAL
    #DECLARE private Speed:INTEGER

    def __init__(self,CharacterNameP,DateOfBirthP,IntelligenceP,SpeedP):
        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfBirthP
        self.__Intelligence = IntelligenceP
        self.__Speed = SpeedP

    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    
    def SetIntelligence(self,Intelligence):
        self.__Intelligence = Intelligence
    

    def Learn(self):
        self.__Intelligence *= 1.1
    
    def ReturnAge(self):
        return 2023 - int(self.__DateOfBirth[-4:])
    
FirstCharacter = Character("Royal","1/1/2019",70,30) 

FirstCharacter.Learn()
print(FirstCharacter.GetName(),"is",FirstCharacter.ReturnAge(),"years old and has an intelligence of",FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    #DECLARE Element:String
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP,ElementP):
        super().__init__(CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP)
        self.__Element = ElementP

    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)

FirstMagic = MagicCharacter("Light","3/3/2018",75,22,"fire")
FirstMagic.Learn()
print(FirstMagic.GetName(),"is",FirstMagic.ReturnAge(),"years old and has an intelligence of",FirstMagic.GetIntelligence())

