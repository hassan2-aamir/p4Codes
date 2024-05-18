class Vehicle():
    
    def Move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):

    def Move(self):
        print("Sail")

x = [Vehicle(), Car(), Boat()]
for i in x:
    i.Move()