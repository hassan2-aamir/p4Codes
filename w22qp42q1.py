#DECLARE Jobs : ARRAY[0:99][0:1] OF INTEGER
#DECLARE NumberOfJobs : INTEGER
global Jobs, NumberOfJobs
def Initialise():
    global Jobs, NumberOfJobs
    Jobs = [[-1 for col in range(2)] for row in range(10)]
    NumberOfJobs = 0

def AddJob(JNo,JPriority):
    global Jobs, NumberOfJobs
    if NumberOfJobs == 10:
        print("Not Added ")
    else:
        Jobs[NumberOfJobs][0] = JNo
        Jobs[NumberOfJobs][1] = JPriority
        NumberOfJobs += 1
        print("Added")

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

def InsertionSort():
    global Jobs,NumberOfJobs
    for i in range(1,NumberOfJobs):
        sortedIndex = i-1
        UnsortedJNo = Jobs[i][0]
        UnsortedJPriority = Jobs[i][1]
        while sortedIndex >= 0 and UnsortedJPriority < Jobs[sortedIndex][1]:
            Jobs[sortedIndex+1][0]=Jobs[sortedIndex][0]
            Jobs[sortedIndex+1][1]=Jobs[sortedIndex][1]
            sortedIndex -= 1

        Jobs[sortedIndex+1][0] = UnsortedJNo
        Jobs[sortedIndex+1][1] = UnsortedJPriority  


def printArray():
    global Jobs, NumberOfJobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

InsertionSort()
printArray()






    