Tail = -1
Head = -1
Queue = [-1 for i in range(3)]

def Enqueue(Val:int):
    
    if Tail == -1 and Head == -1:
        Tail=0
        Head =0
        Queue[Tail] = Val
    elif ((Tail == Head -1)or(Tail == len(Queue)-1 and Head == 0)):
        print("Queue is full")
    else:
        if Tail == len(Queue)-1:
            Tail = 0
        else:
            Tail+= 1
        Queue[Tail] = Val

def Dequeue():
    global Head,Tail,Queue
    if Head==-1 and Tail==-1:
        print("Nothing in queue")
    elif Head == Tail:
        Queue[Head] = -1
        Head = -1
        Tail = -1
    else:
        Queue[Head] = -1
        if Tail == len(Queue)-1:
            Head = 0
        else:
            Head+= 1
        

Enqueue(10)
print(Queue, Head,Tail)
Enqueue(90)
print(Queue, Head,Tail)
Enqueue(12)
print(Queue, Head,Tail)
