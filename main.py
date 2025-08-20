name = input("plz Enter u'r name :")
nots =input("Enter u'r nots :\n")

with open("nots.txt","w") as file:
    file.write("NAME : "+name+"\n\n")
    file.write(nots)
    
with open("nots.txt","r") as file:
        print(file.read())