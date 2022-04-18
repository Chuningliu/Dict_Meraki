# Write a program remove the first key value pair from a nested dictionary.
# Output :-
# Dic= {1: 'NAVGURUKUL',2: 'IN',3:{ 'B' : 'To','C' : 'DHARAMSALA'}}
 
a= {1: 'NAVGURUKUL',2: 'IN',3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
for i in a:
        del a[3]['A']
        break
print(a)



                
                
                
        
