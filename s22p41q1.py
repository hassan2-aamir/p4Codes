#DECLARE highScoreArray: ARRAY[0:10] OF INTEGER
#DECLARE highScoreNameArray : ARRAY[0:10] OF STRING

highScoreArray = [-1 for i in range(11)]
highScoreNameArray = ["" for j in range(11)]

def ReadHighScores():
    global highScoreArray,highScoreNameArray
    File = open("HighScore.txt","r")
    for i in range(10):
        highScoreNameArray[i] = File.readline().strip()
        highScoreArray[i] = int(File.readline().strip())
    
    File.close()

def OutputHighScores():
    global highScoreArray,highScoreNameArray
    print("PlayerName\tScore")
    for i in range(10):
        print(f"{highScoreNameArray[i]}\t\t{highScoreArray[i]}")

newName = input("Enter a 3 character player name:  ")
while len(newName) != 3:
    newName = input("Error! Please Enter a 3 character player name:  ")

newScore = int(input("Enter your score between 1 and 100000:  "))
while newScore < 1 or newScore>100000:
    newScore = int(input("Error! Please Enter your score between 1 and 100000:  "))



def updateArray(newName,newScore):
    global highScoreArray,highScoreNameArray
    highScoreArray[10] = newScore
    highScoreNameArray[10] = newName
    unSorted = 10
    unSortedScore = highScoreArray[10]
    unSortedName = highScoreNameArray[10]
    i = unSorted -1
    while i > 0 and unSortedScore > highScoreArray[i]:
        highScoreArray[i+1] = highScoreArray[i]
        highScoreNameArray[i+1] = highScoreNameArray[i]
        i-=1

    highScoreArray[i+1] = unSortedScore
    highScoreNameArray[i+1] = unSortedName


ReadHighScores()
OutputHighScores()
print()
updateArray(newName,newScore)
OutputHighScores()

def writeTopTen():
    global highScoreArray,highScoreNameArray
    File = open("NewHighScore.txt","w")
    for i in range(10):
        File.write(highScoreNameArray[i]+'\n')
        File.write(str(highScoreArray[i])+'\n')
    File.close()

writeTopTen()
