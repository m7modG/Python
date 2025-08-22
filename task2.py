username = input("plz Enter u'r name : ")
password = input("Enter u'r pass : ")
le =len(password)
username=username.lower()
username=username.replace(" ","_")

print("\nu'r name is : ",username)
print("the password is : ",password)
print("password lenght : ", le)

print("\ncheck :\nis the password length is >= 8 ?",le>=8,"\n")
print("is the username equal admin ?",username=="admin","\n")
print("is tha password equal 1234",password=="1234","\n")
print("is the username = admin && password = 1234 ?",username=="admin" and password=="1234","\n")

print(f"welcome {username} u'r password has {le} character !")