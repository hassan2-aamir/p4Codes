#DECLARE Queue: ARRAY[0:99] OF INTEGER
#DECLARE Head,Tail : INTEGER
global Queue,Head,Tail
Queue = [None for i in range(100)]
head = 0
tail = 0

def Enqueue(Val:int):
    global head,tail,Queue
    if (head == 0 and tail == 99)or(tail==head-1):
        print("Queue is full")
        return False
    else:
        Queue[tail]= Val

        if tail==99:
            tail=0
        else:
            tail+=1

        return True
    
successful = True
for i in range(1,21):
    successful=Enqueue(i)
    if successful == False:
        break

if successful:
    print("Successful")
else:
    print("Unsuccessful")


Total = 0
def RecursiveOutput(CurrentIndex:int):
    global Total
    if CurrentIndex == tail-1:
        return Total + Queue[CurrentIndex]
    else:
        return Total + Queue[CurrentIndex]+RecursiveOutput(CurrentIndex+1)


print("Sum = ",RecursiveOutput(head))
