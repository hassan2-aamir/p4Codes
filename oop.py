class Employee:
    __name =""
    __age = -1
    __salary = -1
    def __init__(self,name,age,salary):
        self.__name= name
        self.__salary = salary
        self.__age = age
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def getAnnualSalary(self):
        return self.__salary * 12
    



e1 = Employee("Rochan",18,50000)
print(e1.getName())
e1.setName("Hassan")
print("Annual Salary: ",e1.getAnnualSalary())