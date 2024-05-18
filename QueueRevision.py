#global variables
Head = -1
Tail = -1
Queue = [-1 for i in range(5)]

def Enqueue(val):
    global Head ,Tail,Queue
    #if queue is empty
    if (Tail == -1 and Head == -1):
        Head =0
        Tail =0
        Queue[Tail] = val
    #if queue is full
    elif ((Tail == Head - 1)or (Tail == 4 and Head == 0)):
        print("Full!")
    else:
        #if at the end of queue 
        if Tail == 4:
            Tail =0
        else:
            Tail += 1
        Queue[Tail] = val

def Dequeue():
    global Head ,Tail,Queue
    #if nothing
    if (Head == -1 and Tail == -1):
        print("Nothing!")
    elif Head == Tail:
        temp = Queue[Head]
        Head = -1 
        Tail = -1
        return temp
    else:
        temp = Queue[Head]
        if Head == 4:
            Head = 0
        else:
            Head += 1

def displayQueue():
    # Val1 VAl2 .. Val5
    # 0     1    .. 4
    #Head Tail
    for i in range(5):
        print(Queue[i],end = '\t')
    print()
    for j in range(5):
        print(j,end = '\t')
    print()
    print(f"Head: {Head}")
    print("Tail: "+str(Tail))

Enqueue(9)
Enqueue(39)
Enqueue(2)
Dequeue()
displayQueue()
