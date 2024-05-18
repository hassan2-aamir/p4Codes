#DECLARE Animals: ARRAY[0:9] OF STRING
Animals = ["horse","lion","rabbit","mouse","bird","deer","whale","elephant","kangaroo","tiger"]

def SortDescending():
    global Animals
    #DECLARE ArrayLength: INTEGER
    #DECLARE Temp: STRING

    ArrayLength = len(Animals)
    for x in range(ArrayLength):
        for y in range(ArrayLength -1 ):
            if Animals[y][0] < Animals[y+1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp



SortDescending()
for animal in Animals:
    print(animal)






