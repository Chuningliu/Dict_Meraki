# Write a program to print 'exists' if entered key already exists
# in the dictionary and print 'not exists' if the entered key does not exist.

dict1={"name":"Raju","marks":56}
name=input("Enter the name:-")
if name in dict1 :
    print(name,"Exists")
else:
    print(name,"Not exist")
    



