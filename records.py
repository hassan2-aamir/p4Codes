from pickle import dump,load

class record:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

pickelFile = open("test.bin","wb")
count = 0
Hassan = record("Hassan",20)
count+=1
Rochan = record("Rochan",18)
count+=1

dump(count,pickelFile)
dump(Hassan,pickelFile)
dump(Rochan,pickelFile)

pickelFile.close()

pickelFile = open("test.bin","rb")
for i in range(load(pickelFile)):
    input = load(pickelFile)
    print(input.name,input.age)

pickelFile.close()

