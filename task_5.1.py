dict1 = {'Alice':85,'George':67,'Tony':89,'Sylver':78,'Brandon':66,'Lara':92,'Tom':88,'Steve':95}
# Here the value displays the name of the students and keys represents their marks
name = str(input("Enter the student name : "))
if name in dict1:
    key = dict1[name]
    print(name,"'s marks :",key)

else:
    print("Student not found")


