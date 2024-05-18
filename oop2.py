class Person:
    firstname=""
    lastname=""
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def setfirstName(self,firstname):
        self.firstname = firstname
    def setLastName(self,lastname):
        self.lastname=lastname
    def getName(self):
        return self.firstName + ' '+ self.lastname

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    def getName(self):
        return self.firstname + ' ' + Person.lastname
    
x = Student("Hassan","Aamir")
print(x.getName())