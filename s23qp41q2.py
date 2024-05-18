class vehicle:
    #DECLARE private ID: STRING
    #DECLARE private MaxSpeed,CurrentSpeed,IncreaseAmount,HorizontalPosition :INTEGER

    def __init__(self,IDP,MaxSpeedP,IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self,CurrentSpeedP):
        self.__CurrentSpeed = CurrentSpeedP
    def SetHorizontalPosition(self,HorizontalPositionP):
        self.__HorizontalPosition=HorizontalPositionP

    def IncreaseSpeed(self):
        if self.__CurrentSpeed+self.__IncreaseAmount <= self.__MaxSpeed:
            self.SetCurrentSpeed(self.__CurrentSpeed+self.__IncreaseAmount)
            self.SetHorizontalPosition(self.__HorizontalPosition+self.__CurrentSpeed)

class Helicopter(vehicle):
    #DECLARE private VerticalPosition,VerticalChange,MaxHeight: INTEGER

    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP,VerticalChangeP,MaximumHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalChange = VerticalChangeP
        self.__MaxHeight= MaximumHeightP
        self.__VerticalPosition = 0

    def IncreaseSpeed(self):
        if self.__VerticalPosition + self.__VerticalChange <= self.__MaxHeight:
            self.__VerticalPosition += self.__VerticalChange
        super().IncreaseSpeed()

    def GetVerticalPosition(self):
        return self.__VerticalPosition
    

def getSpeedPosition(Vehicle):
    print("Vehicle horizontal speed: ",Vehicle.GetCurrentSpeed())
    print("Horizontal Position: ",Vehicle.GetHorizontalPosition())
    if type(Vehicle)== Helicopter:
        print("Vertical Position: ",Vehicle.GetVerticalPosition())


car = vehicle("Tiger",100,20)
helicopter1= Helicopter("Lion",350,40,3,100)

car.IncreaseSpeed()
car.IncreaseSpeed()

getSpeedPosition(car)

print()

helicopter1.IncreaseSpeed()
helicopter1.IncreaseSpeed()

getSpeedPosition(helicopter1)




