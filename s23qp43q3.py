class Employee:
    #DECLARE private HourlyPay:REAL
    #DECLARE private EmployeeNumber:STRING
    #DECLARE private JobTitle:STRING
    #DECLARE private PayYear2022:ARRAY[0:51] OF REAL 
    def __init__(self,PayP,EmpNumP,JobP):
        self.__HourlyPay=PayP
        self.__EmployeeNumber=EmpNumP
        self.__JobTitle=JobP
        self.__PayYear2022=[]
        for x in range(52):
            self.__PayYear2022.append(0.00)
        
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self,WeekNumber,Hours):
        self.__PayYear2022[WeekNumber-1]=Hours*self.__HourlyPay

    def GetTotalPay(self):
        TotalPay=0
        for x in range(52):
            TotalPay=TotalPay+self.__PayYear2022[x]
        return TotalPay


class Manager(Employee):
    #DECLARE private BonusValue:REAL

    def __init__(self,PayP,EmpNumP,JobP,BonusValP):
        super().__init__(PayP,EmpNumP,JobP)
        self.__BonusValue=BonusValP
    

    def SetPay(self,WeekNumber,Hours):
        Hours=Hours*(1+self.__BonusValue/100)
        super().SetPay(WeekNumber,Hours)




EmployeeArray=[]



Pay=0.00
ID=""
Bonus=0.00
Title=""
Bonus=""

try:
    File=open("Employees.txt",'r')
    for x in range(8):
        Pay=float(File.readline().strip())
        ID=File.readline().strip()
        Bonus_or_Title =File.readline().strip()

        
        if Bonus_or_Title[0].isnumeric():
            Title=File.readline().strip()
            EmployeeArray.append(Manager(Pay,ID,Title,float(Bonus_or_Title)))
        else:
            EmployeeArray.append(Employee(Pay,ID,Bonus_or_Title))

    File.close()
except FileNotFoundError:
    print("File is not found")


def EnterHours():
    global EmployeeArray

    try:
        File=open("HoursWeek1.txt",'r')
        EmpID=" "

        for x in range(8):
            EmpID=File.readline().strip()
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber()==EmpID:
                    EmployeeArray[y].SetPay(1,float(File.readline().strip()))
                    break


    except FileNotFoundError:
        print("File could not be found")


EnterHours()
for z in range(8):
    print(EmployeeArray[z].GetEmployeeNumber()," ",EmployeeArray[z].GetTotalPay())






























