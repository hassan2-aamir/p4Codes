FirstName=""
LastName=""
Name=input("Enter your first and last name: ")
for i in range(len(Name)):
    if Name[i]==" ":
        FirstName=Name[:i]
        LastName=Name[-i+1:]

print(FirstName)
print(LastName)