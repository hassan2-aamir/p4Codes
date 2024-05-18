#DECLARE QueueArray: ARRAY[0:9] OF STRING
#DECLARE head,tail,numberOFItems: INTEGER

head = 0
tail = 0
numberOfItems = 0
QueueArray = ["" for i in range(10)]

def Enqueue(QueueArray, Head,Tail,NumberItems,DataToAdd):
    if NumberItems == 10:
        return False,QueueArray, Head,Tail,NumberItems
    
    QueueArray[Tail] = DataToAdd

    if Tail >= 9:
        Tail=0
    else:
        Tail += 1
    
    NumberItems += 1
    return True, QueueArray, Head,Tail,NumberItems

def Dequeue(QueueArray, Head,Tail,NumberItems):
    if NumberItems == 0:
        return "FALSE",QueueArray, Head,Tail,NumberItems

    returnVal = QueueArray[Head]

    if Head>=9:
        Head = 0
    else:
        Head+=1
    
    NumberItems-=1
    return returnVal,QueueArray, Head,Tail,NumberItems

for i in range(11):
    DataToAdd = input("Enter string to add to queue: ")
    successful,QueueArray,head,tail,numberOfItems = Enqueue(QueueArray,head,tail,numberOfItems,DataToAdd) 
    if successful:
        print("Data added successfully!")
    else:
        print("Data not added!")
    

for i in range(2):
    returnVal,QueueArray,head,tail,numberOfItems = Dequeue(QueueArray,head,tail,numberOfItems)
    print("Dequeue item",(i+1),':',returnVal)
