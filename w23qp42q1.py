#DECLARE StackVowel: ARRAY[0:99] OF CHAR
#DECLARE StackConsonant: ARRAY[0:99] OF CHAR
global StackVowel,StackConsonant
StackVowel=[None for i in range(100)]
StackConsonant=[None for i in range(100)]

#DECLARE VowelTop, ConsotantTop: INTEGER
global VowelTop,ConsonantTop
VowelTop = 0
ConsonantTop =0

def PushData(letter):
    global StackConsonant,StackVowel,VowelTop,ConsonantTop
    if letter == 'a' or letter =='e' or letter =='i' or letter =='o' or letter =='u':
        if VowelTop ==100:
            print("Vowel Stack is full")
        else:
            StackVowel[VowelTop] = letter
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack is full")
        else:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop+=1

def ReadData():
    global StackConsonant,StackVowel,VowelTop,ConsonantTop
    try:
        File = open("StackData.txt","r")
        for x in File:
            PushData(x.strip())
        File.close()
    except FileNotFoundError:
        print("File not found") 

def PopVowel():
    global VowelTop,StackVowel
    if VowelTop==0:
        return "No Data"
    else:
        VowelTop-=1
        return StackVowel[VowelTop]
    
def PopConsonant():
    global ConsonantTop,StackConsonant
    if ConsonantTop==0:
        return "No Data"
    else:
        ConsonantTop-=1
        return StackConsonant[ConsonantTop]   

returnVals = []
ReadData()   
count =0
while count <5:
    letterChoice = input("Do you want to input a vowel or consonant: ").lower()
    while letterChoice != "vowel" and letterChoice != "consonant":
        letterChoice = input("Please check your input spelling and try again. Do you want to input a vowel or consonant: ").lower()
    
    if letterChoice =="vowel":
        val = PopVowel()
        if val == "No data":
            print("Vowel stack empty")
        else:
            returnVals.append(val)
            count+= 1
    else:
        val = PopConsonant()
        if val == "No data":
            print("Consonant stack empty")
        else:
            returnVals.append(val)
            count+= 1

for val in returnVals:
    print(val,end="")
