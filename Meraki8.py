# Take input of name and marks of 10 students and store to a dictionary.
# a={'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}


d={} 
for i in range(10):
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks of the students:"))
    d[name]=marks
print(d)














































# while True  :
#     num=input("Enter the serial no. of student  or \nEnter Q for quit: ")
#     if num=="Q" or num=="q":
#         break
#     else :
#         name=input("enter the name of student: ")
#         marks=int(input("enter the marks of student: "))
#         d={name,marks}
# print(d)