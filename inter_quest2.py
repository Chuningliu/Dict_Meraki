# Method 1: Displaying result by iterating through values. 

dict ={}
dict1 = {1: ["Ningmeih", 21, 'Data Structures'],
     2: ["Mathiudim", 20, 'Machine Learning'],
     3: ["Silas", 21, 'OOPS with java'],
     }
print ("{:<11} {:<11} {:<11}".format('NAME', 'AGE', 'COURSE'))
for key, value in dict1.items():
    name, age, course = value
    print ("{:<11} {:<11} {:<11}".format(name, age, course))
    























# Method 2: Displaying by using matrix format 
 
# dict1 = {}
# dict1 = {(0, 0): 'Mathiu', (0, 1): 21, (0, 2): 'Data structures',
#          (1, 0): 'Ningss', (1, 1): 20, (1, 2): 'Machine Learning',
#          (2, 0): 'Silass', (2, 1):21, (2, 2): 'OOPS with Java'
# }
# print(" NAME ", " AGE ", "  COURSE " )
# for i in range(3):
#     for j in range(3):
#         print(dict1[(i, j)], end ='   ')
#     print()  
    
    
# Method 3: Displaying by using zip format 
 
# dict1 = {}
# dict1 = {'NAME':['Silas', 'Ragang', 'Ningmei'],
#          'AGE':[21, 20, 21],
#          'COURSE':['Data Structures', 'Machine Learning', 'OOPS with Java']}
# for each_row in zip(*([i] + (j)
#                       for i, j in dict1.items())):
#      print(*each_row, " ")
