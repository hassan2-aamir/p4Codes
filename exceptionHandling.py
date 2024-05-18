try:
    MyFile = open("Hello.txt","r")
    MyFile.close()
except FileNotFoundError:
    print("No such file!")

print("hi")