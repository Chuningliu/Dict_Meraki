#  Find keys with duplicate values in the dictionary?


c= {'a':1, 'b':2, 'c':3, 'd':2}
# print("initial_dictionary", (a))
b= {}
for i, j in c.items():
    if j not in b:
        b[j] = [i]
    else:
        b[j].append(i)
print("final_dictionary",(b))




        
        
    




