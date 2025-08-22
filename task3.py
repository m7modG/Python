fruits = ["apple","orange","banana","pineapple","grapes"]

print("the fruits list : ",fruits)
print("first one : ",fruits[0])
print("last one : ",fruits[-1])

fruits[1]="mango"
print("after editing to mango : ",fruits)

fruits.insert(2,"watermelon")
print("after inserting watermelon : ",fruits)

check_fruit = input("Enter a fruit name to check :")
print("is it in the list ? ",check in fruits)

fruits.sort()
print("the fruits sorted !",fruits)