#DECLARE TheData: ARRAY[0:8] OF INTEGERS
TheData = [20,3,4,8,12,99,2,26,4]

def InsertionSort(TheData):
    for count in range(len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count-1
        while (NextValue>=0 and Inserted != 1):
            if(DataToInsert < TheData[NextValue]):
                TheData[NextValue+1]=TheData[NextValue]
                NextValue -=1
                TheData[NextValue+1]= DataToInsert
            else:
                Inserted = 1
InsertionSort(TheData)

print(TheData)