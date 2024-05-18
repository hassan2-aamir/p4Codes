#writing a file
MyFile = open("practice.txt","w")
MyFile.write("hi\n")
MyFile.write("hello\n")
MyFile.write("bye\n")
MyFile.close()

#appending file 
MyFile = open("practice.txt","a")
MyFile.write("hi\n")
MyFile.write("hello\n")
MyFile.write("bye\n")
MyFile.close()

#reading a file 
MyFile = open("practice.txt","r")
String = "hello"
while(String != ""):
    String = MyFile.readline().strip()
    print(String)
MyFile.close()