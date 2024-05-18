#DECLARE Head,Tail,NumberOfItems : INTEGER
#DECLARE QueueArray : ARRAY[0:9] OF STRING

Head = 0
Tail = 0
NumberOfItems = 0
QueueArray = ["" for i in range(10)]

def Enqueue(QueueArray, Head,Tail,NumberOfItems,DataToAdd):
    if NumberOfItems == len(QueueArray):
        return False,QueueArray,Head,Tail,NumberOfItems
    QueueArray[Tail] = DataToAdd
    if Tail >= 9:
        Tail = 0
    else:
        Tail+=1
    
    NumberOfItems += 1
    return True,QueueArray,Head,Tail,NumberOfItems

def Dequeue(QueueArray, Head,Tail,NumberOfItems):
    if NumberOfItems == 0:
        return "FALSE",QueueArray,Head,Tail,NumberOfItems
    ReturnVal = QueueArray[Head]
    QueueArray[Head] = ""
    if Head >= 9:
        Head = 0
    else:
        Head += 1
    NumberOfItems -= 1
    return ReturnVal,QueueArray,Head,Tail,NumberOfItems 

for i in range(11):
    DataToAdd = input("Input string to add to queue: ")
    Successful,QueueArray,Head,Tail,NumberOfItems=Enqueue(QueueArray,Head,Tail,NumberOfItems,DataToAdd)
    if Successful:
        print("Data added successfully")
    else:
        print("The queue is full")

for j in range(2):
    ReturnVal,QueueArray, Head,Tail,NumberOfItems=Dequeue(QueueArray, Head,Tail,NumberOfItems)
    print("Return Value: ", ReturnVal)

