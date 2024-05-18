arrayScores = [["",-1]for i in range(11)]


def ReadHighScores():
    global arrayScores
    try:
        MyFile = open("HighScore.txt","r")
    
        for i in range(10):
            arrayScores[i][0] = MyFile.readline().strip()
            arrayScores[i][1] = MyFile.readline().strip()
            


        MyFile.close()
    except FileNotFoundError:
        print("File not found!")

def OutputHighScores():
    global arrayScores
    print("PlayerName\tScore")
    for i in range(10):
        print(f"{arrayScores[i][0]}\t\t{arrayScores[i][1]}")


ReadHighScores()
OutputHighScores()