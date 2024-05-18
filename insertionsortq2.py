#DECLARE playerNames: ARRAY [0:10] OF STRING
#DECLARE playerScores : ARRAY[0:10] OF INTEGER

playerNames = ["HAS","ROC","ALI","MIH","FYI","ABC","DEE","DEF","AHM","IBR",""]
playerScores = [1000,999,888,777,666,555,444,333,222,111,0]

def OutputHighScores():
    for i in range(10):
        print(playerNames[i],playerScores[i],sep="  ")


OutputHighScores()       

playerNames[10] = input("Input 3 letter initials for your name:  ")
while(len(playerNames[10])!=3):
    playerNames[10] = input("Error! Please input 3 letter initials for your name:  ")

playerScores[10] = int(input("Input the score that you achieved between 1 and 100000:  "))
while(playerScores[10]<1 or playerScores[10]>100000 ):
    playerScores[10] = int(input("Error! Please input the score that you achieved between 1 and 100000:  "))

def changeTopTen(playerName,playerScore):
    i=10
    j=i-1
    tempScore = playerScores[i]
    tempName = playerNames[i]
    while(tempScore>playerScores[j] and j>=0):
        playerScores[j+1] = playerScores[j]
        playerNames[j+1] = playerNames[j]
        j-=1

    playerNames[j+1] = tempName
    playerScores[j+1] = tempScore

changeTopTen(playerNames[10],playerScores[10])
print()
OutputHighScores()        